# Website-ready blog Markdown guide

This is the authoritative content and formatting guide for research and technical posts under `_posts/`. Follow it whenever a blog post is created or edited.

The site renders posts with Jekyll's `post` layout, Kramdown's GFM input, and MathJax 3. Blog posts use the normal article layout; do not wrap them in the note-only `aa-course-note` container.

## 1. File location and publication state

Published posts belong directly inside `_posts/` and must follow Jekyll's filename convention:

```text
_posts/YYYY-MM-DD-short-descriptive-slug.md
```

Example:

```text
_posts/2026-08-13-why-calibration-matters.md
```

Rules:

- Use lowercase words separated by hyphens; do not use spaces or underscores.
- Make the filename date match the front-matter date.
- Do not future-date a post unless delayed publication is intentional; Jekyll does not publish future posts by default.
- Store unfinished posts in `_drafts/short-descriptive-slug.md`, not `_posts/`.
- The current site configuration gives posts URLs of the form `/notes/:year/:title/`. Do not hard-code a different post URL inside the article. If a separate `/blog/` section is introduced later, update `_config.yml` and the blog landing/navigation together.
- This repository does not currently have a blog landing page. Before publishing the first post, add a post index and navigation entry or deliberately surface the post from an existing page; otherwise the direct URL may work while the post remains difficult to discover.

## 2. Recommended front matter

Copy this template and remove optional fields that are not being used. Do not leave fake paths or placeholder metadata in a published post.

```yaml
---
layout: post
title: "Why Calibration Matters in Probabilistic Forecasting"
date: 2026-08-13 10:00:00 +0530
author: "Aditya Aryan"
description: "An intuitive and mathematical account of forecast calibration, its relationship to sharpness, and the diagnostics used to evaluate both."
tags:
  - probabilistic-forecasting
  - statistics
  - calibration
categories:
  - research-notes
math: true
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
related_posts: true
giscus_comments: false
og_image: /assets/img/blog/why-calibration-matters/preview.png
last_updated: "2026-08-13"
---
```

Field rules:

- `layout: post` is required.
- Keep the title specific and readable, ideally under 60 characters when possible. Do not repeat it as an H1 in the body.
- Write a self-contained description of roughly 120–160 characters. It should say what the reader will learn, not "a post about my work."
- Use two to five focused, lowercase, hyphenated tags. Reuse established tags so related-post matching works.
- Use one broad category at most unless the post genuinely belongs to more than one series.
- Set `math: true` only when the article contains MathJax mathematics.
- Add a sidebar TOC for a substantial article with at least three main sections; omit `toc` for a short update.
- Set `related_posts: false` when related links would be misleading or the post is unusually short.
- Turn on `giscus_comments` only after valid Giscus repository and category IDs have been configured.
- Include `og_image` only when that file exists. The site already enables Open Graph metadata; a good preview image is 1200 by 630 pixels.
- Update `last_updated` only for a meaningful content revision, not punctuation-only edits.

## 3. Recommended research-post structure

Use the structure that matches the argument; do not force empty sections into a short post.

```markdown
Write a concise opening paragraph that states the problem, why it matters, and the main conclusion. Avoid biography, scene-setting, or a long list of niche methods here.

## Motivation

Explain the broader research or practical question before introducing technical details.

## Problem setup

Define the data, assumptions, notation, target quantity, and evaluation criterion.

## Method or argument

Develop the method, derivation, experiment, or proof in a reproducible order.

## Results and interpretation

Report what was actually observed. Include baselines, units, uncertainty, and limitations where relevant.

## Limitations and open questions

Separate established conclusions from conjectures, preliminary findings, and future work.

## Reproducibility

State the code, data, environment, and random-seed status. Omit a GitHub link until a real public repository exists.

## References

- Author, "Title," venue or publisher, year. [DOI or official source](https://example.org/).
```

The first paragraph should work as an abstract-like summary, but it should still read naturally. Use broader areas such as statistical inference, probabilistic modelling, machine learning, optimisation, or stochastic decision-making in the opening. Introduce specialised model names only when the technical discussion begins.

## 4. MathJax rules

If the post contains any mathematics, set `math: true` and follow these rules throughout.

### Inline mathematics

Use escaped MathJax parentheses in the Markdown source:

```markdown
A forecast \\(F\_{t}\\) is calibrated when its stated probabilities agree with long-run frequencies.
```

Do not use single-dollar inline delimiters such as `$F_t$`. They are more vulnerable to Markdown parsing, currency symbols, and malformed copied text.

### Display mathematics

Put each `$$` delimiter on its own line with blank lines around the display:

```markdown
The pinball loss at quantile level \\(\tau\\) is

$$
L_{\tau}(y,q)
=\bigl(\tau-\mathbf{1}\lbrace y<q\rbrace\bigr)(y-q).
$$

This loss is minimised by a conditional \\(\tau\\)-quantile.
```

Never mix prose and `$$` on one line. Keep display equations outside blockquotes, lists, and Markdown tables.

Use `aligned` for multi-line work:

```markdown
$$
\begin{aligned}
\operatorname{MSE}(T)
&=\operatorname{E}\!\left[(T-\theta)^2\right] \\
&=\operatorname{Var}(T)+\operatorname{Bias}(T)^2.
\end{aligned}
$$
```

Use Markdown-safe TeX:

- `\lvert x\rvert`, not raw `|x|`.
- `\lVert x\rVert`, not raw `||x||`.
- `X\mid Y`, not raw `X|Y`.
- `\lbrace x:x>0\rbrace`, not `\{x:x>0\}`.
- `T^{\star}` or `T^{\ast}`, not raw `T*` or `T^*`.
- `\text{}` for words inside an equation.
- Braced subscripts such as `X_{ij}` and `\theta_{0}`.
- Named operators such as `\operatorname{E}`, `\operatorname{Var}`, `\operatorname{Cov}`, and `\Pr`.

Keep every TeX environment balanced. Do not paste LaTeX preambles, `\documentclass`, packages, theorem environments, labels, or cross-reference commands. Break wide equations into aligned lines so they remain usable on mobile screens.

## 5. Formal statements in mathematical posts

Most blog posts should use ordinary prose and headings. When a post genuinely presents a formal definition or theorem, the site's existing callout classes are available:

```markdown
<div class="definition" markdown="1">

**Definition — Calibration.**
State the definition precisely and introduce every symbol.

</div>
```

```markdown
<div class="theorem" markdown="1">

**Theorem — Descriptive name.**
State assumptions and the conclusion.

</div>
```

Leave blank lines inside the HTML wrapper. Use these boxes sparingly, and do not use the `aa-course-note` wrapper, lecture navigation, learning objectives, or question-and-answer section in a blog post.

## 6. Markdown, links, tables, and code

- Let the layout generate the only H1. Start body sections at `##`, then use `###` for subsections.
- Leave blank lines around headings, lists, equations, blockquotes, HTML wrappers, tables, and code fences.
- Keep paragraphs reasonably short and give each paragraph one job.
- Use descriptive link text; avoid "click here."
- Link to stable primary sources such as papers, documentation, datasets, and official project pages.
- Use public website URLs for internal links, never source paths ending in `.md`.
- Do not publish dead `#`, `TODO`, fake DOI, or placeholder GitHub links.

Use `relative_url` for internal content:

```markdown
[Read the related inference notes]({{ '/notes/parametric-inference/' | relative_url }}).
```

Use tables for compact comparisons, not long explanations or derivations. Keep all rows the same width and use inline math only. Replace raw TeX vertical bars with named delimiters. If a Liquid URL filter is needed in a table, assign it before the table so the filter's pipe does not become a column separator.

Code blocks must specify a language:

````markdown
```python
from numpy.random import default_rng

rng = default_rng(2026)
```
````

For computational research posts:

- Include package versions or an environment file when results depend on them.
- Set and report random seeds where reproducibility matters.
- Distinguish commands, source code, and output.
- Never commit API keys, tokens, private paths, personal data, or confidential datasets.
- Explain what the code demonstrates rather than pasting a notebook without a narrative.

## 7. Images and figures

Store post-specific media in a descriptive folder:

```text
assets/img/blog/<post-slug>/
```

Embed an image with meaningful alt text and a deployment-safe path:

```markdown
![Reliability diagram comparing predicted probabilities with observed frequencies]({{ '/assets/img/blog/why-calibration-matters/reliability-diagram.webp' | relative_url }})

_Reliability diagram for the held-out evaluation set; the diagonal denotes perfect calibration._
```

Rules:

- Prefer SVG for simple diagrams and WebP or optimized PNG/JPEG for raster figures.
- Use descriptive lowercase filenames rather than `image1.png`.
- Label axes, units, legends, data splits, and uncertainty intervals.
- Ensure colors remain distinguishable in both light and dark mode; do not rely on color alone.
- Compress files and check the 375-pixel mobile layout.
- Do not hotlink an image that may disappear. Record its source and licence when it is not original.
- Enable `images.lightbox2: true` in front matter only when opening figures at full size materially helps the reader.

## 8. Citations, evidence, and research integrity

- Cite claims that depend on prior literature, datasets, software, or external factual information.
- Prefer the paper DOI, publisher page, arXiv record, official documentation, or dataset landing page over a search-result URL.
- Never invent a citation or cite a source that was not checked.
- Use quotation marks only for actual quotations and keep quotations brief.
- Distinguish correlation, prediction, and causal evidence.
- Report the sample, time period, train/validation/test split, baselines, metric definitions, and units when discussing results.
- Include uncertainty, sensitivity analysis, or limitations when they affect the conclusion.
- Label unfinished work as ongoing or preliminary. Do not describe an unpublished note, private experiment, or planned repository as a publication.
- Do not claim that code, data, notes, or a paper are public until the corresponding link works.

For a small number of supporting comments, Markdown footnotes are acceptable:

```markdown
The estimate depends on the sampling design.[^design]

[^design]: See the linked technical report for the exact inclusion-probability assumptions.
```

For a research-heavy post, finish with a visible `## References` section so readers can audit the sources without searching through footnotes.

## 9. Final readiness checklist

Before publishing a blog post, verify:

- [ ] The file is directly under `_posts/` and follows `YYYY-MM-DD-slug.md`.
- [ ] The filename date and front-matter date match and are not unintentionally in the future.
- [ ] The title, description, tags, category, author, and update date are accurate.
- [ ] Optional front-matter fields refer to real configured features and existing files.
- [ ] The body has no manual H1 and uses a logical H2/H3 hierarchy.
- [ ] The opening states the broad problem and main takeaway without niche keyword stuffing.
- [ ] Technical claims are supported, limitations are visible, and preliminary work is labelled honestly.
- [ ] Inline math uses `\\(...\\)` in the Markdown source; display delimiters are on their own lines.
- [ ] No raw math bars, escaped set braces, raw math asterisks, unbalanced environments, or overflowing equations remain.
- [ ] Tables have consistent columns; code fences name their language; figures have alt text, captions, and legible labels.
- [ ] Every internal link uses a public URL and every external reference works.
- [ ] No secret, private path, confidential datum, fake citation, placeholder link, or unsupported publication claim remains.
- [ ] The post has been checked in both light and dark mode at desktop and mobile widths.

Run from the repository root:

```powershell
npm run lint:prettier
bundle exec jekyll build
```

Then view the generated post through the local Jekyll server rather than opening the Markdown or generated HTML file directly. Check the browser console for MathJax errors and inspect the page at approximately 375, 768, and 1440 pixels wide.
