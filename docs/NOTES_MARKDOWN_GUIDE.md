# Website-ready notes Markdown guide

This is the authoritative content and formatting guide for files under `_pages/notes/`. Follow it whenever a lecture, course index, or formula sheet is created or edited.

The site renders Markdown with Jekyll, Kramdown's GFM input, and MathJax 3. Notes also use the local `aa-course-note` reading layout and formal-statement callouts defined in `assets/css/main.scss`.

## 1. File organization

Use one folder per course:

```text
_pages/notes/<course-slug>/
|-- course-contents.md
|-- formula-sheet.md
|-- lecture-01-short-descriptive-slug.md
|-- lecture-02-short-descriptive-slug.md
`-- ...
```

Rules:

- Use lowercase, hyphen-separated folder names and filenames.
- Give lecture numbers two digits so files sort correctly.
- Keep one lecture per file. Do not combine a course into one very large Markdown file.
- Add every new lecture to `course-contents.md` and update `formula-sheet.md` when it introduces reusable notation or formulae.
- Use public site URLs in links, never links ending in `.md`.

## 2. Required lecture front matter

Copy this block and replace every placeholder. Keep dates quoted and use `YYYY-MM-DD`.

```yaml
---
layout: page
title: "Lecture 3: Full Descriptive Lecture Title"
short_title: "Short lecture title"
course: "Full Course Name"
lecture: 3
instructor: "Professor's Public Name"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "A specific one-sentence summary of the definitions, methods, and results developed in this lecture."
topics:
  - "first topic"
  - "second topic"
  - "third topic"
previous: "lecture-02-previous-slug"
next: "lecture-04-next-slug"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-13"
status: "complete"
math: true
permalink: /notes/course-slug/lecture-03-short-descriptive-slug/
course_slug: course-slug
note_kind: lecture
course_order: 3
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---
```

Use `previous: null` for the first lecture and `next: null` for the latest lecture when no next page exists. Update the adjacent lecture's navigation whenever a lecture is inserted or renamed.

The `description` should describe the material, not say only "notes from Lecture 3." Aim for one accurate sentence. Do not claim coverage that the page does not contain.

For `course-contents.md` and `formula-sheet.md`, retain `layout: page`, `course`, `course_slug`, `note_kind`, `math: true`, a permanent URL, and the same TOC configuration. Omit lecture-only fields when they have no meaning.

## 3. Standard lecture structure

Use this order unless the subject genuinely needs a different progression:

```markdown
<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Fall 2026 [Course Name] lectures of Prof. [Name] at the Indian Statistical Institute, Kolkata. Additional exposition and any remaining errors are the responsibility of the note author.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/course-slug/lecture-02-previous-slug/' | relative_url }}) · [Course contents]({{ '/notes/course-slug/' | relative_url }}) · [Formula sheet]({{ '/notes/course-slug/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/course-slug/lecture-04-next-slug/' | relative_url }})
</nav>

## Learning objectives

- State one observable learning outcome.
- Derive or prove one central result.
- Apply the result in a worked example.

## 1. First main section

Introduce notation and motivation before using it.

## 2. Second main section

Develop the principal argument in a logical order.

### Worked Example 3.1 — Descriptive name

**Problem.**

State the problem completely.

**Solution.**

Show the reasoning, not only the answer.

**Final result.**

State the conclusion and its interpretation.

## Questions answered in this lecture

**Question.**

Write the question as ordinary content.

**Answer.**

Give the answer as ordinary content, without a surrounding box.

## Lecture summary

Summarize the main definitions, results, and limitations in one compact paragraph.

## References and further reading

- Identify the lecture/source notes honestly.
- List books, papers, or documentation actually used.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/course-slug/lecture-02-previous-slug/' | relative_url }}) · [Course contents]({{ '/notes/course-slug/' | relative_url }}) · [Formula sheet]({{ '/notes/course-slug/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/course-slug/lecture-04-next-slug/' | relative_url }})
</nav>

</div>
```

The page layout creates the page's only H1 from `title`. Start the body at `##`; do not add a `#` heading inside the Markdown body.

## 4. Formal statements and callouts

Definitions, theorems, lemmas, and propositions must use the site's formal boxes. Leave a blank line after the opening tag and before the closing tag so Kramdown parses the contents.

```markdown
<div class="definition" markdown="1">

**Definition 3.1 — Sufficient statistic.**
A statistic \\(T\\) is sufficient for \\(\theta\\) if the conditional distribution of the sample given \\(T\\) does not depend on \\(\theta\\).

</div>
```

```markdown
<div class="theorem" markdown="1">

**Theorem 3.2 — Factorisation criterion.**
State all assumptions before the conclusion.

$$
f_{\theta}(x)=g_{\theta}(T(x))h(x).
$$

</div>
```

Available classes are:

- `.definition`
- `.theorem`
- `.lemma`
- `.proposition`
- `.example`
- `.remark`
- `.proof`
- `.warning`
- `.intuition`

Use boxes selectively. Definitions and named formal results should be boxed; routine derivations and ordinary prose should not. Proofs may remain as normal content beginning with `**Proof.**`. End a proof with `\\(\square\\)` when appropriate.

Questions and answers must never be placed in blockquotes or formal boxes. Keep `**Question.**` and `**Answer.**` as plain content. This prevents slide-derived material from dominating the page.

Use a normal blockquote only for a short attribution, convention, or genuinely important takeaway:

```markdown
> **Key point.** Unbiasedness is a restriction on an estimator's expectation, not a guarantee of small variance.
```

## 5. MathJax rules

Every page containing mathematics must set `math: true`.

### Inline mathematics

Use escaped MathJax parentheses in the Markdown source:

```markdown
The estimator \\(T\_{n}\\) is unbiased for \\(\theta\\).
```

Do not use single-dollar inline math such as `$T_n$`. Dollar delimiters interact with Markdown emphasis, currency, tables, and copied source more easily. Do not put spaces immediately inside the delimiters.

### Display mathematics

Put each `$$` delimiter on a line by itself, with a blank line before and after the display:

```markdown
The mean squared error decomposes as

$$
\operatorname{MSE}_{\theta}(T)
=\operatorname{Var}_{\theta}(T)
+\operatorname{Bias}_{\theta}(T)^2.
$$

For an unbiased estimator, the second term is zero.
```

Never write prose and `$$` on the same line. Never place a display equation inside a Markdown table, and avoid placing one inside a list item or blockquote.

For multi-line derivations, use one display with an `aligned` environment:

```markdown
$$
\begin{aligned}
R(\theta,T)
&=\operatorname{E}_{\theta}\!\left[(T-\theta)^2\right] \\
&=\operatorname{Var}_{\theta}(T)
  +\operatorname{Bias}_{\theta}(T)^2.
\end{aligned}
$$
```

Keep `\begin{...}` and `\end{...}` balanced. Do not paste complete LaTeX documents, theorem environments, `\documentclass`, `\usepackage`, `\label`, or `\ref` into Markdown.

### Markdown-safe TeX

Use explicit TeX commands for characters that Markdown can misread:

- For absolute values and cardinalities, use `\lvert x\rvert` and `\lvert A\rvert`; avoid raw vertical bars.
- For norms, use `\lVert x\rVert`; avoid doubled raw vertical bars.
- For a conditional separator, use `X\mid Y`; avoid a raw vertical bar.
- For set braces, use `\lbrace x:x>0\rbrace`; avoid `\{x:x>0\}`.
- For a starred estimator, use `T^{\star}` or `T^{\ast}`; avoid `T*` and `T^*`.
- For words inside equations, use `\text{for every }n`; avoid bare prose in math.

Brace subscripts and superscripts when they contain more than one character: use `X_{ij}`, `n^{-1}`, and `\theta_{0}`. Use `\operatorname{Var}`, `\operatorname{Cov}`, `\operatorname{E}`, `\Pr`, `\mathbb{R}`, and `\mathbf{x}` consistently rather than imitating them with italic prose.

Do not use raw vertical bars in inline math, especially on lines near tables. Do not use raw `*` inside math; use `\ast`, `\star`, or `\cdot` according to meaning.

For very wide expressions, break the equation with `aligned`, define intermediate quantities, or split it into multiple displays. A correct equation that overflows on mobile is not website-ready.

## 6. Markdown and layout rules

- Leave one blank line around headings, lists, code fences, equations, HTML wrappers, and blockquotes.
- Use `##` for numbered main sections and `###` for subsections. Do not skip heading levels.
- Keep paragraphs focused. Introduce every symbol before it appears in a theorem or derivation.
- Use fenced code blocks with a language identifier such as `python`, `r`, `cpp`, `text`, or `yaml`.
- Use Markdown tables only for genuinely tabular comparisons. Keep every row's column count identical.
- Use inline math only in tables; move long derivations below the table.
- Do not use raw HTML for spacing, font sizes, colors, or manual positioning.
- Do not add new CSS classes for a single note. Reuse the classes listed in this guide.

A Liquid filter contains a pipe, which can split a Markdown table. Assign the URL before the table, then use the variable inside it:

```text
{% assign lecture_url = '/notes/course-slug/lecture-01-topic/' | relative_url %}

| Lecture | Topic |
| --- | --- |
| [Lecture 1]({{ lecture_url }}) | Foundations |
```

For ordinary internal links and images, make the path deployment-safe with `relative_url`:

```markdown
[See the formula sheet]({{ '/notes/course-slug/formula-sheet/' | relative_url }}).

![A descriptive explanation of the diagram]({{ '/assets/img/notes/course-slug/descriptive-file.webp' | relative_url }})
```

Every image needs meaningful alt text. Use a descriptive lowercase filename and compress large images before committing them.

## 7. Content and academic standards

- Preserve the mathematical meaning of the source; never silently replace an assumption, estimator, algorithm, or conclusion.
- State assumptions before a theorem, method, or approximation.
- Distinguish a definition, theorem, heuristic, example, and personal explanation.
- Expand skipped algebra when it is necessary to understand the result, but do not pad the page with repetitive prose.
- Use consistent notation across a lecture and the cumulative formula sheet.
- Attribute professors and source material accurately. Keep the notes explicitly unofficial.
- Never invent a citation, proof attribution, empirical result, or publication status.
- If a statement is uncertain, mark it for verification rather than presenting it as settled fact.

## 8. Final readiness checklist

Before publishing a note, verify:

- [ ] The filename, permalink, lecture number, `previous`, and `next` values agree.
- [ ] `course-contents.md` and, when relevant, `formula-sheet.md` are updated.
- [ ] There is exactly one H1, supplied automatically by the page layout.
- [ ] Every formal definition, theorem, lemma, and proposition uses the correct box.
- [ ] Questions and answers are ordinary unboxed content.
- [ ] Inline math uses `\\(...\\)` in the Markdown source and every display delimiter is on its own line.
- [ ] No raw math bars, fragile escaped braces, raw math asterisks, or unbalanced environments remain.
- [ ] No display equation is inside a table or mixed into a prose paragraph.
- [ ] Tables have consistent columns and fit or scroll on a 375-pixel-wide screen.
- [ ] Links target public URLs rather than `.md` files, and images have alt text.
- [ ] The source attribution, references, description, topics, and update date are accurate.

Run from the repository root:

```powershell
npm run test:notes:source
bundle exec jekyll build
```

With the local site running at `http://127.0.0.1:4000/al-folio/`, also run:

```powershell
$env:REQUIRE_MATHJAX = "1"
npm run test:notes:browser
Remove-Item Env:REQUIRE_MATHJAX
```

The browser audit checks all note pages at 375, 768, 1024, and 1440 pixels for raw TeX, MathJax errors, malformed tables, overflow, misplaced formal statements, and boxed questions or answers.
