const fs = require("fs");
const path = require("path");

const notesRoot = path.resolve("_pages/notes");
const expectedPageCount = 25;
const issues = [];

function markdownFiles(directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const absolutePath = path.join(directory, entry.name);
    return entry.isDirectory() ? markdownFiles(absolutePath) : entry.name.endsWith(".md") ? [absolutePath] : [];
  });
}

function report(file, line, message) {
  issues.push(`${path.relative(process.cwd(), file)}:${line}: ${message}`);
}

function pipeCount(line) {
  return [...line].filter((character, index) => character === "|" && line[index - 1] !== "\\").length;
}

const files = markdownFiles(notesRoot);

if (files.length !== expectedPageCount) {
  issues.push(`Expected ${expectedPageCount} note pages, found ${files.length}.`);
}

for (const file of files) {
  const source = fs.readFileSync(file, "utf8");
  const lines = source.split(/\r?\n/);
  const requiresStrictInlineMath = /parametric-inference[\\/]lecture-0[12]-/.test(file);
  let displayDelimiterCount = 0;
  let fenceCount = 0;

  lines.forEach((line, index) => {
    const lineNumber = index + 1;
    const unquoted = line.replace(/^\s*>\s?/, "").trim();

    if (line.includes("$$")) {
      displayDelimiterCount += (line.match(/\$\$/g) || []).length;
      if (unquoted !== "$$") {
        report(file, lineNumber, "display-math delimiter must be on its own line");
      }
    }

    if (/^\s*```/.test(unquoted)) fenceCount += 1;
    if (file.includes(`${path.sep}sample-surveys${path.sep}`) && /^\s*>\s*\*\*(?:Slide question|Question|Answer)\.\*\*/i.test(line)) {
      report(file, lineNumber, "Sample Surveys question/answer content must not be boxed as a blockquote");
    }
    if (/^layout:\s+(note|notes-index)\s*$/.test(line)) report(file, lineNumber, "unsupported note layout");
    if (/\]\([^)]*\.md(?:[#?][^)]*)?\)/.test(line)) report(file, lineNumber, "public link still targets a Markdown source file");
    if (/\\[{}]/.test(line)) report(file, lineNumber, "fragile escaped brace; use a named TeX delimiter");
    if (/\\[A-Za-z]+\*|\*\{|[A-Za-z]\*[A-Za-z]|\$\$\\_|\$\$\*/.test(line)) {
      report(file, lineNumber, "possible Markdown-damaged TeX token");
    }

    const dollarInlineExpressions = [...line.matchAll(/(?<!\$)\$(?!\$)([^$]+?)(?<!\$)\$(?!\$)/g)];
    const parenthesizedInlineExpressions = [...line.matchAll(/\\\\\((.+?)\\\\\)/g)];
    const inlineExpressions = [...dollarInlineExpressions, ...parenthesizedInlineExpressions];
    if (requiresStrictInlineMath && dollarInlineExpressions.length > 0) {
      report(file, lineNumber, "dollar-delimited inline math is fragile; use escaped MathJax parenthesis delimiters");
    }
    for (const expression of inlineExpressions) {
      if (expression[1].includes("|")) report(file, lineNumber, "raw vertical bar inside inline math can become a Markdown table");
      if (requiresStrictInlineMath && expression[1].includes("*")) {
        report(file, lineNumber, "raw asterisk inside inline math can be parsed as Markdown; use a named TeX symbol");
      }
    }
    if (requiresStrictInlineMath && /\\\*/.test(line)) report(file, lineNumber, "stray escaped asterisk in prose");
  });

  if (displayDelimiterCount % 2 !== 0) report(file, 1, "unbalanced display-math delimiters");
  if (fenceCount % 2 !== 0) report(file, 1, "unbalanced fenced code block");
  if (requiresStrictInlineMath) {
    const inlineOpenCount = (source.match(/\\\\\(/g) || []).length;
    const inlineCloseCount = (source.match(/\\\\\)/g) || []).length;
    if (inlineOpenCount !== inlineCloseCount) {
      report(file, 1, `unbalanced inline-math delimiters (${inlineOpenCount} open, ${inlineCloseCount} close)`);
    }
  }

  const beginCount = (source.match(/\\begin\{/g) || []).length;
  const endCount = (source.match(/\\end\{/g) || []).length;
  if (beginCount !== endCount) report(file, 1, `unbalanced TeX environments (${beginCount} begin, ${endCount} end)`);

  for (let index = 0; index < lines.length; index += 1) {
    const line = lines[index].trim();
    const nextLine = lines[index + 1]?.trim() || "";
    if (!line.startsWith("|") || !line.endsWith("|") || !/^\|[\s:|-]+\|$/.test(nextLine)) continue;

    const columns = pipeCount(line);
    let cursor = index + 1;
    while (cursor < lines.length) {
      const row = lines[cursor].trim();
      if (!row.startsWith("|") || !row.endsWith("|")) break;
      if (pipeCount(row) !== columns) report(file, cursor + 1, "Markdown table row has an inconsistent column count");
      cursor += 1;
    }
    index = cursor - 1;
  }
}

if (issues.length > 0) {
  console.error(`Note-source validation failed with ${issues.length} issue(s):\n${issues.join("\n")}`);
  process.exitCode = 1;
} else {
  console.log(`Note-source validation passed for ${files.length} pages.`);
}
