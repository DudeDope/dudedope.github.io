# Design and Analysis of Algorithms — Website Markdown Package

This repository contains complete, lecture-wise Markdown notes converted from the final chapter-wise LaTeX notes, the compiled PDF, and the supplied lecture material for the course taught by Sandip Das at Indian Statistical Institute, Kolkata.

The notes are unofficial. The exposition, added derivations, and any remaining errors are the responsibility of Aditya.

## Repository contents

- `lecture-01-algorithmic-foundations.md` — Lecture 1: Algorithmic Foundations, Asymptotic Notation, and Correctness Proofs
- `lecture-02-minimum-enclosing-circles.md` — Lecture 2: Minimum Enclosing Circles: Structure, Candidate Construction, and Exhaustive Search
- `lecture-03-divide-and-conquer-recurrences.md` — Lecture 3: Divide-and-Conquer Recurrences and the Polynomial Master Theorem
- `lecture-04-simultaneous-minimum-maximum.md` — Lecture 4: Simultaneous Minimum and Maximum by the Pairing Method
- `lecture-05-deterministic-linear-selection.md` — Lecture 5: Order Statistics and Deterministic Linear-Time Selection
- `lecture-06-binary-search-rotated-arrays.md` — Lecture 6: Binary Search and Medians in Rotated Sorted Arrays
- `lecture-07-binary-search-trees.md` — Lecture 7: Binary Search Trees: Operations, Traversals, and Reconstruction
- `lecture-08-height-balanced-search-trees.md` — Lecture 8: Height-Balanced Trees and Balanced Search Structures
- `lecture-09-consolidated-algorithm-review.md` — Lecture 9: Consolidated Algorithmic Results and Exam Review
- `course-contents.md` — living lecture index and navigation page
- `formula-sheet.md` — cumulative notation, formulas, assumptions, and complexity bounds
- `README.md` — repository structure and update workflow

## Naming convention

Lecture files use the pattern

```text
lecture-NN-descriptive-slug.md
```

where `NN` is a two-digit lecture number. The numbering ensures correct lexical sorting. Every current LaTeX chapter maps to one lecture file, in the same order as the source.

The intended website base path is

```text
/notes/design-and-analysis-of-algorithms/
```

All links inside the package are relative, so the directory may be moved without rewriting navigation links.

## Mathematical notation

The files use standard Markdown with MathJax/KaTeX-compatible LaTeX:

```markdown
Inline mathematics uses $T(n)=O(n\log n)$.

Display mathematics uses

$$
T(n)=2T(n/2)+\Theta(n).
$$
```

Custom LaTeX macros from the book source have been expanded. Document-only commands such as `\chapter`, theorem environments, labels, and cross-reference commands do not appear in the Markdown. Algorithms are fenced text blocks, and tree diagrams are portable monospaced diagrams.

## Updating the course

To add Lecture $N+1$:

1. Expand the master chapter-wise LaTeX notes with the new lecture material.
2. Create `lecture-N+1-topic.md` using the next two-digit number and a descriptive slug.
3. Set the new file's `previous` field to Lecture $N$ and its `next` field to `null`.
4. Update Lecture $N$ so its `next` field points to the new lecture slug.
5. Add the new lecture to `course-contents.md`.
6. Add every new definition, formula, assumption, and complexity result to `formula-sheet.md`, noting the lecture where it first appears.
7. Update `last_updated` in all files changed during the edit.
8. Run the quality checks below and rebuild the ZIP archive.

## Quality checks before publishing

- Every source chapter or approved lecture unit has exactly one Markdown file.
- Headings are properly nested and lecture numbers match filenames.
- YAML front matter appears exactly once at the top of each lecture.
- Every display-math delimiter is balanced.
- Every `\begin{...}` inside display mathematics has a matching `\end{...}`.
- No unsupported custom macro remains.
- Every previous/next/content/formula-sheet link resolves to an existing file.
- The contents page lists every lecture.
- The formula sheet includes material from every lecture.
- Source questions are answered near the relevant theory.
- Added self-contained explanations are visibly marked as **Additional context**.
- Editorial corrections are visibly marked as **Editorial note**.

## Source policy

The lecture files preserve definitions, assumptions, propositions, theorems, proofs, derivations, examples, algorithms, source questions, and formula summaries from the final notes. Clear typographical or mathematical transcription corrections are identified rather than silently changed. Material added for self-containment is explicitly labeled.
