---
layout: page
title: "Lecture 9: Consolidated Algorithmic Results and Exam Review"
short_title: "Consolidated review"
course: "Design and Analysis of Algorithms"
lecture: 9
instructor: "Sandip Das"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Consolidates the principal algorithms, structural results, exact bounds, and proof questions from the preceding lectures into a rigorous review lecture."
topics:
  - "Complexity summary"
  - "Proof checklist"
  - "Algorithm comparison"
  - "Exam review"
previous: "lecture-08-height-balanced-search-trees"
next: null
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-06"
status: "complete"
math: true
permalink: /notes/design-and-analysis-of-algorithms/lecture-09-consolidated-algorithm-review/
course_slug: design-and-analysis-of-algorithms
note_kind: lecture
course_order: 9
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> These are unofficial expanded notes based on the lectures of  
> Sandip Das, Indian Statistical Institute, Kolkata.  
> The exposition, additional derivations, and any remaining errors are the responsibility of the note author.

## Learning objectives

- Compare the central algorithms and data structures by idea and worst-case bound.
- Reconstruct the main correctness and complexity proofs without relying on memorized formulas.
- Identify the assumptions under which each result is valid.
- Use the checklist to locate gaps before revision or examination.

## 1. Core results

| **Problem / structure**                     | Main idea                                                  | Worst-case bound                             |
| :------------------------------------------ | :--------------------------------------------------------- | :------------------------------------------- |
| **Naive minimum enclosing circle**          | Test all pair-diameter and triple-circumcircle candidates  | $\Theta(n^4)$                                |
| **Master recurrence $aT(n/b)+\Theta(n^k)$** | Compare $a$ with $b^k$                                     | Three Master cases                           |
| **Simultaneous min and max**                | Pair elements; winner challenges max, loser challenges min | $\left\lceil 3n/2\right\rceil-2$ comparisons |
| **Deterministic selection**                 | Median of medians; discard a constant fraction             | $\Theta(n)$                                  |
| **Binary search**                           | Maintain candidate interval; halve it each step            | $\Theta(\log n)$                             |
| **Rotated-array median**                    | Find pivot, then map sorted index modulo $n$               | $O(\log n)$                                  |
| **Ordinary BST operation**                  | Follow one root-to-leaf path                               | $\Theta(h)$, worst $\Theta(n)$               |
| **Balanced BST operation**                  | Maintain height $O(\log n)$                                | $O(\log n)$                                  |
| **Height-balanced node count**              | $N_{\min}(h)=1+N_{\min}(h-1)+N_{\min}(h-2)$                | $F_{h+2}-1\le n\le2^h-1$                     |

## 2. Questions one should be able to answer

### 2.1. Why must an MEC have at least two essential support points unless all points coincide?

**Answer.**

With only one distinct boundary point, a sufficiently small motion of the center toward that point decreases its active distance while all other points remain inside by slack. The radius can then be reduced, contradicting optimality.

### 2.2. Why do two support points have to be diametrically opposite?

**Answer.**

If the center is not the midpoint of the two points, their segment is a proper chord. Moving the center along the perpendicular bisector toward the chord reduces both boundary distances, so a smaller enclosing circle exists. Therefore the segment must be a diameter.

### 2.3. Derive all three cases of the polynomial-form Master Theorem from a geometric series.

**Answer.**

$T(n)=n^{\log_b a}T(1)+cn^k\sum_{i=0}^{\log_b n-1}(a/b^k)^i$. The geometric ratio $r=a/b^k$ gives $\Theta(n^k)$ when $r<1$, $\Theta(n^k\log n)$ when $r=1$, and $\Theta(n^{\log_b a})$ when $r>1$.

### 2.4. Prove the exact comparison count of the pairing min-max algorithm.

**Answer.**

For even $n$, initialization costs one comparison and the remaining $(n-2)/2$ pairs cost three each, giving $1+3(n-2)/2=3n/2-2$. For odd $n$, one element initializes both extrema and $(n-1)/2$ pairs cost three each, giving $3(n-1)/2$. Together this is $\lceil3n/2\rceil-2$.

### 2.5. Explain why median of medians discards about $3n/10$ elements from each side.

**Answer.**

At least half of the group medians lie on either side of the pivot. Each qualifying full five-element group contributes its median and two more elements on that side. After conservatively excluding the pivot group and an incomplete group, each side contains at least $3n/10-6$ elements.

### 2.6. Prove binary search using a loop invariant.

**Answer.**

Invariant: if the target occurs, it lies in $A[L\dots R]$ at the start of each iteration. Sortedness justifies discarding the half that cannot contain the target; equality returns a correct index; termination with $L>R$ leaves an empty candidate interval.

### 2.7. Derive the modular index map for a rotated sorted array.

**Answer.**

If $p$ is the physical index of the minimum, the sorted sequence begins at $A[p]$. Advancing $j$ sorted positions wraps around the array, so logical index $j$ occurs at physical index $(p+j)\bmod n$.

### 2.8. Give all three BST deletion cases and justify successor replacement.

**Answer.**

A leaf is detached, a one-child node is replaced by its child, and a two-child node is replaced by its inorder successor before that successor is removed from its old location. The successor is the smallest key in the right subtree, so it is larger than every left-subtree key and no larger right-subtree key is violated.

### 2.9. State which traversal pairs uniquely determine a tree and provide the counterexample for preorder plus postorder.

**Answer.**

Preorder plus inorder and postorder plus inorder determine a distinct-label binary tree uniquely. Preorder $(A,B)$ and postorder $(B,A)$ are shared by the tree with $B$ as the left child of $A$ and the tree with $B$ as the right child, so preorder plus postorder alone is not unique.

### 2.10. Derive $N_{\min}(h)=F_{h+2}-1$ and use it to prove logarithmic height.

**Answer.**

Minimal balance gives $N_{\min}(h)=1+N_{\min}(h-1)+N_{\min}(h-2)$ with $N_{\min}(0)=0$ and $N_{\min}(1)=1$. Setting $M(h)=N_{\min}(h)+1$ yields the Fibonacci recurrence, so $M(h)=F_{h+2}$. Since $F_{h+2}$ grows exponentially, $n\ge F_{h+2}-1$ implies $h=O(\log n)$.

## Lecture summary

This lecture brings together the course results covered so far: geometric support arguments, recurrence analysis, exact comparison bounds, deterministic selection, binary search, BST operations, and balanced-tree node bounds.

## References and further reading

- All supplied lectures and the complete LaTeX notes for Lectures 1–3.
- The references listed in Lectures 1–8.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/design-and-analysis-of-algorithms/lecture-08-height-balanced-search-trees/' | relative_url }}) · [Course contents]({{ '/notes/design-and-analysis-of-algorithms/' | relative_url }}) · [Formula sheet]({{ '/notes/design-and-analysis-of-algorithms/formula-sheet/' | relative_url }}) · Next lecture →
</nav>

</div>
