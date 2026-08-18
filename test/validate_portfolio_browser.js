const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const baseUrl = process.env.PORTFOLIO_URL || "http://127.0.0.1:4001/al-folio/";
const widths = [375, 768, 1024, 1440];
const mathRoutes = [
  "notes/sample-surveys/formula-sheet/",
  "notes/sample-surveys/lecture-03-design-based-estimation/",
  "notes/design-and-analysis-of-algorithms/formula-sheet/",
  "notes/design-and-analysis-of-algorithms/lecture-05-deterministic-linear-selection/",
];
const contentRoutes = [
  "about/",
  "research/",
  "research/em-convergence/",
  "research/battery-life/",
  "research/battery-dispatch/",
  "research/medical-vlm/",
  "publications/",
  "projects/",
  "projects/biostat-policyopt/",
  "projects/nonlinear-mlp/",
  "projects/stein-shrinkage/",
  "projects/copula-air-pollution/",
  "projects/sequential-testing/",
  "projects/audio-denoising/",
  "projects/football-probability/",
  "notes/",
  "notes/sample-surveys/",
  "notes/sample-surveys/formula-sheet/",
  "notes/sample-surveys/lecture-01-foundations-and-representativeness/",
  "notes/sample-surveys/lecture-02-finite-population-and-srs/",
  "notes/sample-surveys/lecture-03-design-based-estimation/",
  "notes/sample-surveys/lecture-04-confidence-intervals-and-sample-size/",
  "notes/design-and-analysis-of-algorithms/",
  "notes/design-and-analysis-of-algorithms/formula-sheet/",
  "notes/design-and-analysis-of-algorithms/lecture-01-algorithmic-foundations/",
  "notes/design-and-analysis-of-algorithms/lecture-02-minimum-enclosing-circles/",
  "notes/design-and-analysis-of-algorithms/lecture-03-divide-and-conquer-recurrences/",
  "notes/design-and-analysis-of-algorithms/lecture-04-simultaneous-minimum-maximum/",
  "notes/design-and-analysis-of-algorithms/lecture-05-deterministic-linear-selection/",
  "notes/design-and-analysis-of-algorithms/lecture-06-binary-search-rotated-arrays/",
  "notes/design-and-analysis-of-algorithms/lecture-07-binary-search-trees/",
  "notes/design-and-analysis-of-algorithms/lecture-08-height-balanced-search-trees/",
  "notes/design-and-analysis-of-algorithms/lecture-09-consolidated-algorithm-review/",
  "cv/",
];
const projectArtifacts = [
  { route: "projects/audio-denoising/", images: 2 },
  { route: "projects/copula-air-pollution/", images: 2 },
  { route: "projects/football-probability/", images: 1 },
  { route: "projects/sequential-testing/", images: 1 },
];
const screenshotDirectory = path.resolve("output/playwright");
let browser;

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

(async () => {
  fs.mkdirSync(screenshotDirectory, { recursive: true });

  browser = await chromium.launch();
  const context = await browser.newContext({ colorScheme: "dark" });
  const page = await context.newPage();
  const pageErrors = [];
  page.on("pageerror", (error) => pageErrors.push(error.message));

  for (const width of widths) {
    await page.setViewportSize({ width, height: 900 });
    await page.goto(baseUrl, { waitUntil: "domcontentloaded" });
    await page.waitForLoadState("networkidle");

    const measurements = await page.evaluate(() => ({
      bodyWidth: document.body.scrollWidth,
      documentWidth: document.documentElement.scrollWidth,
      headingCount: document.querySelectorAll("h1").length,
      theme: document.documentElement.dataset.theme,
      footerBaseFontSize: getComputedStyle(document.querySelector("footer .container")).fontSize,
      footerContent: getComputedStyle(document.querySelector("footer .container"), "::after").content.replace(/^['"]|['"]$/g, ""),
      footerAttributionLinks: document.querySelectorAll('footer a[href*="alshedivat/al-folio"]').length,
      publicationsNavLinks: document.querySelectorAll('.navbar a[href$="/publications/"]').length,
      courseNotesSectionPresent: Boolean(document.querySelector("#notes-status")),
      selectedProjectTitles: [...document.querySelector("#selected-projects").closest("section").querySelectorAll("h3")].map((heading) =>
        heading.textContent.trim()
      ),
    }));
    assert(measurements.bodyWidth <= width, `${width}px: body overflows at ${measurements.bodyWidth}px`);
    assert(measurements.documentWidth <= width, `${width}px: document overflows at ${measurements.documentWidth}px`);
    assert(measurements.headingCount === 1, `${width}px: expected one h1, found ${measurements.headingCount}`);
    assert(measurements.theme === "dark", `${width}px: dark system preference was not applied`);
    assert(measurements.footerBaseFontSize === "0px", `${width}px: default footer text is still visible`);
    assert(/^Last updated: \w+ \d{2}, \d{4}\.$/.test(measurements.footerContent), `${width}px: footer date is missing or malformed`);
    assert(measurements.footerAttributionLinks === 0, `${width}px: al-folio attribution link is still present`);
    assert(measurements.publicationsNavLinks === 0, `${width}px: Publications is still present in the main navigation`);
    assert(!measurements.courseNotesSectionPresent, `${width}px: Course notes still compete for space on the landing page`);
    assert(
      JSON.stringify(measurements.selectedProjectTitles) ===
        JSON.stringify([
          "BioStat-PO: Policy Selection for Causal Survival Analysis",
          "Nonlinear-MLP: Controlled Studies of Neural-Network Nonlinearity",
          "Bivariate Copula Modelling of Extreme Air-Pollution Events",
        ]),
      `${width}px: unexpected selected-project order: ${measurements.selectedProjectTitles.join(" | ")}`
    );

    await page.screenshot({
      path: path.join(screenshotDirectory, `portfolio-${width}-dark.png`),
      fullPage: true,
    });
  }

  await page.setViewportSize({ width: 375, height: 900 });
  await page.goto(baseUrl, { waitUntil: "domcontentloaded" });
  const mobileToggle = page.locator(".navbar-toggler-main");
  assert(await mobileToggle.isVisible(), "375px: mobile navigation toggle is not visible");
  await mobileToggle.click();
  await page.locator("#navbarNav.show").waitFor();
  assert((await mobileToggle.getAttribute("aria-expanded")) === "true", "375px: mobile navigation did not expose expanded state");
  assert(await page.getByRole("link", { name: "Research", exact: true }).isVisible(), "375px: expanded navigation links are not visible");

  await page.setViewportSize({ width: 1024, height: 900 });
  await page.goto(baseUrl, { waitUntil: "domcontentloaded" });
  await page.keyboard.press("Control+K");
  await page.waitForFunction(() => document.querySelector("ninja-keys")?.visible === true);
  await page.keyboard.press("Escape");
  await page.waitForFunction(() => document.querySelector("ninja-keys")?.visible === false);

  await page.evaluate(() => localStorage.setItem("theme", "light"));
  await page.reload({ waitUntil: "domcontentloaded" });
  assert((await page.locator("html").getAttribute("data-theme")) === "light", "Stored light theme was not restored");
  await page.screenshot({
    path: path.join(screenshotDirectory, "portfolio-1024-light.png"),
    fullPage: true,
  });

  await page.evaluate(() => localStorage.setItem("theme", "dark"));
  await page.reload({ waitUntil: "domcontentloaded" });
  assert((await page.locator("html").getAttribute("data-theme")) === "dark", "Stored dark theme was not restored");

  await page.keyboard.press("Tab");
  const focusedTag = await page.evaluate(() => document.activeElement?.tagName);
  assert(focusedTag && focusedTag !== "BODY", "Keyboard navigation did not move focus");

  for (const width of [375, 1440]) {
    await page.setViewportSize({ width, height: 900 });
    for (const route of contentRoutes) {
      await page.goto(new URL(route, baseUrl).href, { waitUntil: "domcontentloaded" });
      const measurements = await page.evaluate(() => ({
        bodyWidth: document.body.scrollWidth,
        documentWidth: document.documentElement.scrollWidth,
        headingCount: document.querySelectorAll("h1").length,
        overflowingElements: [...document.querySelectorAll("body *")]
          .filter((element) => element.getBoundingClientRect().right > document.documentElement.clientWidth + 1)
          .slice(0, 5)
          .map((element) => ({
            tag: element.tagName,
            className: element.className,
            right: Math.round(element.getBoundingClientRect().right),
            width: Math.round(element.getBoundingClientRect().width),
          })),
      }));
      assert(
        measurements.bodyWidth <= width,
        `${route} at ${width}px: body overflows at ${measurements.bodyWidth}px; ${JSON.stringify(measurements.overflowingElements)}`
      );
      assert(measurements.documentWidth <= width, `${route} at ${width}px: document overflows at ${measurements.documentWidth}px`);
      assert(measurements.headingCount === 1, `${route} at ${width}px: expected one h1, found ${measurements.headingCount}`);
    }
  }

  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto(new URL("about/", baseUrl).href, { waitUntil: "domcontentloaded" });
  const aboutText = await page.locator("body").innerText();
  for (const expected of ["All India Rank 90", "Indian National Mathematical Olympiad merit list", "All India Rank 1,034", "top-1,000 candidate"]) {
    assert(aboutText.includes(expected), `About page is missing verified academic highlight: ${expected}`);
  }

  await page.goto(new URL("research/", baseUrl).href, { waitUntil: "domcontentloaded" });
  assert(await page.locator("#publication-status").isVisible(), "Research page is missing the publication-status note");

  for (const project of projectArtifacts) {
    await page.goto(new URL(project.route, baseUrl).href, { waitUntil: "networkidle" });
    const artifacts = await page.evaluate(() => ({
      images: [...document.querySelectorAll('img[src*="/assets/img/projects/"]')].map((image) => ({
        complete: image.complete,
        naturalWidth: image.naturalWidth,
      })),
      pdfs: [...document.querySelectorAll('a[href*="/assets/pdf/projects/"]')].map((link) => link.getAttribute("href")),
    }));
    assert(
      artifacts.images.length === project.images,
      `${project.route}: expected ${project.images} project images, found ${artifacts.images.length}`
    );
    assert(
      artifacts.images.every((image) => image.complete && image.naturalWidth > 0),
      `${project.route}: one or more project images failed to load`
    );
    assert(artifacts.pdfs.length === 0, `${project.route}: an unsanitised source report is linked publicly`);
  }

  for (const width of [375, 1440]) {
    await page.setViewportSize({ width, height: 900 });
    for (const route of mathRoutes) {
      await page.goto(new URL(route, baseUrl).href, { waitUntil: "networkidle" });
      const mathRuntimeAvailable = await page.evaluate(() => Boolean(window.MathJax?.startup?.promise));
      if (mathRuntimeAvailable) {
        await page.evaluate(async () => window.MathJax.startup.promise);
      }
      const mathMeasurements = await page.evaluate(() => ({
        bodyWidth: document.body.scrollWidth,
        documentWidth: document.documentElement.scrollWidth,
        renderedMath: document.querySelectorAll("mjx-container").length,
        mathErrors: document.querySelectorAll("mjx-merror").length,
        mathScriptConfigured: Boolean(document.querySelector('script[src*="mathjax@"]')),
        mathSetupConfigured: Boolean(document.querySelector('script[src*="assets/al_math/js/mathjax-setup.js"]')),
      }));
      assert(mathMeasurements.bodyWidth <= width, `${route} at ${width}px after MathJax: body overflows at ${mathMeasurements.bodyWidth}px`);
      assert(
        mathMeasurements.documentWidth <= width,
        `${route} at ${width}px after MathJax: document overflows at ${mathMeasurements.documentWidth}px`
      );
      assert(mathMeasurements.mathScriptConfigured, `${route}: MathJax runtime script is not configured`);
      assert(mathMeasurements.mathSetupConfigured, `${route}: local MathJax setup script is not configured`);
      if (mathRuntimeAvailable) {
        assert(mathMeasurements.renderedMath > 0, `${route}: MathJax did not render any mathematics`);
        assert(mathMeasurements.mathErrors === 0, `${route}: MathJax reported ${mathMeasurements.mathErrors} errors`);
      }
    }
  }

  await page.setViewportSize({ width: 1440, height: 900 });
  for (const route of [
    "about/",
    "research/",
    "research/em-convergence/",
    "projects/copula-air-pollution/",
    "notes/sample-surveys/lecture-03-design-based-estimation/",
    "notes/design-and-analysis-of-algorithms/lecture-05-deterministic-linear-selection/",
    "cv/",
  ]) {
    await page.goto(new URL(route, baseUrl).href, { waitUntil: "networkidle" });
    await page.screenshot({
      path: path.join(screenshotDirectory, `${route.replaceAll("/", "-").replace(/-$/, "")}-1440-dark.png`),
      fullPage: true,
    });
  }

  assert(pageErrors.length === 0, `Browser page errors: ${pageErrors.join("; ")}`);

  await browser.close();
  browser = undefined;
  console.log(`Browser validation passed at ${widths.join(", ")}px; ${contentRoutes.length} content routes also pass at 375px and 1440px.`);
})().catch((error) => {
  Promise.resolve(browser?.close()).finally(() => {
    console.error(`Browser validation failed: ${error.message}`);
    process.exitCode = 1;
  });
});
