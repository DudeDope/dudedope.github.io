const fs = require("fs");
const path = require("path");
const { PurgeCSS } = require("purgecss");
const config = require(path.resolve("purgecss.config.js"));

(async () => {
  const outputDirectory = path.resolve(config.output);
  const results = await new PurgeCSS().purge(config);

  fs.mkdirSync(outputDirectory, { recursive: true });
  for (const result of results) {
    if (!result.file) throw new Error("PurgeCSS did not identify the source stylesheet");
    fs.writeFileSync(path.join(outputDirectory, path.basename(result.file)), result.css, "utf8");
  }

  console.log(`Purged ${results.length} production stylesheet(s).`);
})().catch((error) => {
  console.error(`Production CSS purge failed: ${error.message}`);
  process.exitCode = 1;
});
