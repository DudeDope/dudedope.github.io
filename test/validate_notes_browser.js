const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const baseUrl = process.env.PORTFOLIO_URL || "http://127.0.0.1:4000/al-folio/";
const requireMathJax = process.env.REQUIRE_MATHJAX === "1";
const screenshotDirectory = path.resolve("output/playwright/note-audit");
const notesRoot = path.resolve("_pages/notes");
const viewportWidths = [375, 768, 1024, 1440];
let browser;

function markdownFiles(directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const absolutePath = path.join(directory, entry.name);
    return entry.isDirectory() ? markdownFiles(absolutePath) : entry.name.endsWith(".md") ? [absolutePath] : [];
  });
}

function sourceTableCount(source) {
  const lines = source.split(/\r?\n/);
  return lines.filter((line, index) => {
    const current = line.trim();
    const next = lines[index + 1]?.trim() || "";
    return current.startsWith("|") && current.endsWith("|") && /^\|[\s:|-]+\|$/.test(next);
  }).length;
}

const pages = markdownFiles(notesRoot)
  .map((file) => {
    const source = fs.readFileSync(file, "utf8");
    const permalink = source.match(/^permalink:\s*(\S+)\s*$/m)?.[1];
    if (!permalink) throw new Error(`${file} has no permalink`);
    return { file, permalink, tableCount: sourceTableCount(source) };
  })
  .sort((left, right) => left.permalink.localeCompare(right.permalink));

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

(async () => {
  fs.mkdirSync(screenshotDirectory, { recursive: true });
  browser = await chromium.launch();
  const context = await browser.newContext({ colorScheme: "dark" });
  const page = await context.newPage();
  const pageErrors = [];
  page.on("pageerror", (error) => pageErrors.push(error.message));

  for (const width of viewportWidths) {
    await page.setViewportSize({ width, height: 900 });

    for (const note of pages) {
      const url = new URL(note.permalink.replace(/^\//, ""), baseUrl).href;
      await page.goto(url, { waitUntil: "networkidle" });

      const mathRuntimeAvailable = await page.evaluate(() => Boolean(window.MathJax?.startup?.promise));
      if (requireMathJax) assert(mathRuntimeAvailable, `${note.permalink}: MathJax runtime did not load`);
      if (mathRuntimeAvailable) await page.evaluate(async () => window.MathJax.startup.promise);

      const measurements = await page.evaluate(() => {
        const noteBody = document.querySelector(".aa-course-note");
        const tables = [...document.querySelectorAll(".aa-course-note table")];
        const displayMath = [...document.querySelectorAll('.aa-course-note mjx-container[display="true"]')];
        const treeWalker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        const rawMathFragments = [];
        let textNode;
        while ((textNode = treeWalker.nextNode())) {
          if (["SCRIPT", "STYLE", "CODE", "PRE"].includes(textNode.parentElement?.tagName)) continue;
          if (/\$\$|\\begin\{|\\end\{/.test(textNode.textContent)) rawMathFragments.push(textNode.textContent.trim().slice(0, 100));
        }

        return {
          bodyWidth: document.body.scrollWidth,
          documentWidth: document.documentElement.scrollWidth,
          headingCount: document.querySelectorAll("h1").length,
          mathErrors: [...document.querySelectorAll("mjx-merror")].map((error) => error.textContent.trim()),
          rawMathFragments,
          tableCount: tables.length,
          tablesInsideQuotes: tables.filter((table) => table.closest("blockquote")).length,
          malformedTables: tables.filter((table) => {
            const rowSizes = [...table.rows].map((row) => row.cells.length);
            return new Set(rowSizes).size > 1 || rowSizes.some((size) => size < 2);
          }).length,
          rawMathInsideTables: tables.filter((table) => /\$\$|\\begin\{/.test(table.textContent)).length,
          mixedDisplayParagraphs: displayMath.filter((math) => {
            if (math.parentElement?.tagName !== "P") return false;
            return [...math.parentElement.childNodes].some((node) => node !== math && node.textContent.trim() !== "");
          }).length,
          displayMathOutsideReadingColumn: displayMath.filter((math) => {
            if (!noteBody) return true;
            const mathRect = math.getBoundingClientRect();
            const noteRect = noteBody.getBoundingClientRect();
            return mathRect.left < noteRect.left - 1 || mathRect.right > noteRect.right + 1;
          }).length,
          boxedQuestionAnswers: [...document.querySelectorAll(".aa-course-note blockquote strong")].filter((label) =>
            /^(?:slide question|question|answer)\./i.test(label.textContent.trim())
          ).length,
          formalStatementsOutsideBoxes: [...document.querySelectorAll(".aa-course-note strong")].filter((label) => {
            if (!/^(?:definition|theorem|lemma)\s+\d/i.test(label.textContent.trim())) return false;
            return !label.closest(".definition, .theorem, .lemma");
          }).length,
        };
      });

      assert(measurements.bodyWidth <= width, `${note.permalink} at ${width}px: body overflows at ${measurements.bodyWidth}px`);
      assert(measurements.documentWidth <= width, `${note.permalink} at ${width}px: document overflows at ${measurements.documentWidth}px`);
      assert(measurements.headingCount === 1, `${note.permalink}: expected one h1, found ${measurements.headingCount}`);
      assert(
        measurements.tableCount === note.tableCount,
        `${note.permalink}: expected ${note.tableCount} table(s), rendered ${measurements.tableCount}`
      );
      assert(measurements.tablesInsideQuotes === 0, `${note.permalink}: a formula or answer was parsed as a table inside a blockquote`);
      assert(measurements.malformedTables === 0, `${note.permalink}: rendered table has inconsistent columns`);
      assert(measurements.rawMathInsideTables === 0, `${note.permalink}: unprocessed math appeared inside a table`);
      assert(measurements.rawMathFragments.length === 0, `${note.permalink}: unprocessed TeX remains visible`);
      assert(measurements.mixedDisplayParagraphs === 0, `${note.permalink}: display math is mixed into a prose paragraph`);
      assert(measurements.displayMathOutsideReadingColumn === 0, `${note.permalink}: display math escapes the reading column`);
      if (note.permalink.startsWith("/notes/sample-surveys/lecture-")) {
        assert(measurements.boxedQuestionAnswers === 0, `${note.permalink}: a question or answer is still boxed`);
        assert(
          measurements.formalStatementsOutsideBoxes === 0,
          `${note.permalink}: a definition, theorem, or lemma is outside its formal statement box`
        );
      }
      if (mathRuntimeAvailable)
        assert(measurements.mathErrors.length === 0, `${note.permalink}: MathJax errors: ${measurements.mathErrors.join("; ")}`);
    }
  }

  for (const permalink of [
    "/notes/sample-surveys/lecture-02-finite-population-and-srs/",
    "/notes/sample-surveys/lecture-03-design-based-estimation/",
    "/notes/design-and-analysis-of-algorithms/formula-sheet/",
    "/notes/design-and-analysis-of-algorithms/lecture-05-deterministic-linear-selection/",
  ]) {
    await page.setViewportSize({ width: 1440, height: 900 });
    const url = new URL(permalink.replace(/^\//, ""), baseUrl).href;
    await page.goto(url, { waitUntil: "networkidle" });
    if (await page.evaluate(() => Boolean(window.MathJax?.startup?.promise))) {
      await page.evaluate(async () => window.MathJax.startup.promise);
    }
    await page.screenshot({
      path: path.join(screenshotDirectory, `${permalink.split("/").filter(Boolean).join("-")}.png`),
      fullPage: true,
    });
  }

  assert(pageErrors.length === 0, `Browser page errors: ${pageErrors.join("; ")}`);
  await browser.close();
  browser = undefined;
  console.log(`Note browser validation passed for ${pages.length} pages at ${viewportWidths.join(", ")}px.`);
})().catch((error) => {
  Promise.resolve(browser?.close()).finally(() => {
    console.error(`Note browser validation failed: ${error.message}`);
    process.exitCode = 1;
  });
});
