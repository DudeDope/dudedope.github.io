---
layout: page
title: "Lecture 1: Algorithmic Foundations, Asymptotic Notation, and Correctness Proofs"
short_title: "Algorithmic foundations"
course: "Design and Analysis of Algorithms"
lecture: 1
instructor: "Sandip Das"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Introduces formal algorithm specifications, the RAM and comparison models, asymptotic notation, and standard proof templates used throughout algorithm design and analysis."
topics:
  - "Algorithm specifications"
  - "RAM and comparison models"
  - "Asymptotic notation"
  - "Correctness proofs"
previous: null
next: "lecture-02-minimum-enclosing-circles"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-06"
status: "complete"
math: true
permalink: /notes/design-and-analysis-of-algorithms/lecture-01-algorithmic-foundations/
course_slug: design-and-analysis-of-algorithms
note_kind: lecture
course_order: 1
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

- State precisely what an algorithm is and separate specification, correctness, and complexity.
- Distinguish the RAM model from the comparison model.
- Use the formal definitions of $O$, $\Omega$, and $\Theta$.
- Recognize loop-invariant, inductive, and structural proof strategies.

## Course conventions

> **Conventions.**  
> Unless stated otherwise, arrays use $1$-based indexing, all logarithms are to base $2$, and all keys in search trees are distinct. Two tree-height conventions occur in the literature:
>
> - **Edge-height:** the number of edges on a longest root-to-leaf path.
> - **Vertex-height:** the number of vertices on that path.
>
> For a nonempty tree, vertex-height is edge-height plus $1$. Each lecture states which convention is active when the distinction matters.

## 1. What is an algorithm?

> **Definition 1.1 --- Algorithm.**  
> An _algorithm_ is a finite, unambiguous sequence of elementary steps that transforms every valid input instance into an output satisfying a stated specification and terminates after finitely many steps.

A complete analysis has three logically separate parts:

1.  **Specification:** What are the allowed inputs and required outputs?

2.  **Correctness:** Why does the algorithm return a valid output on every valid input?

3.  **Complexity:** How many computational resources does it consume as a function of the input size?

### 1.1. The RAM and comparison models

In the unit-cost random-access machine (RAM) model, basic arithmetic, comparisons, assignments, and array accesses on machine-sized words take constant time. Some results in these lectures are more naturally stated in the _comparison model_, where the only way to learn the relative order of keys is to compare two of them. Exact comparison counts, such as $n-1$ comparisons for finding a maximum, refer to this model.

## 2. Asymptotic notation

> **Definition 1.2 --- Big-$O$, big-$\Omega$, and big-$\Theta$.**  
> Let $f,g:\mathbb{N}\to\mathbb{R}_{\ge 0}$.
>
> $$
> \begin{aligned}
> f(n)&=\mathcal{O}(g(n)) &&\Longleftrightarrow && \exists c>0,\exists n_0:\; f(n)\le c g(n)\ \forall n\ge n_0,\\
> f(n)&=\Omega(g(n)) &&\Longleftrightarrow && \exists c>0,\exists n_0:\; f(n)\ge c g(n)\ \forall n\ge n_0,\\
> f(n)&=\Theta(g(n)) &&\Longleftrightarrow && f(n)=\mathcal{O}(g(n))\text{ and }f(n)=\Omega(g(n)).
> \end{aligned}
> $$

Big-$O$ is an upper bound, big-$\Omega$ is a lower bound, and big-$\Theta$ is a matching two-sided bound. An exact count such as $3n/2-2$ contains more information than the asymptotic statement $\Theta(n)$.

## 3. Standard correctness templates

> **Additional context.**  
> This explanation was added to make the lecture self-contained.
>
> Three proof patterns recur throughout these notes.
>
> Loop invariant.  
> State a property true before the loop, prove initialization, maintenance, and termination. Binary search is the main example.
>
> Induction on input size or tree size.  
> Prove recursive algorithms correct assuming recursive calls are correct on smaller instances. Tree traversals and selection use this pattern.
>
> Exchange or structural argument.  
> Show every optimal solution must have a particular form. The minimum enclosing circle is supported by either two or three boundary points.

## Questions answered in this lecture

> **Question.**  
> What three claims must a complete algorithm analysis establish?

**Answer.**

It must state the input-output specification, prove correctness for every valid input, and bound the required resources in a stated model.

> **Question.**  
> Why can an exact comparison count be more informative than a $\Theta$ bound?

**Answer.**

A $\Theta$ bound suppresses constant factors, whereas an exact count such as $3n/2-2$ distinguishes algorithms with the same asymptotic order.

## Lecture summary

Algorithm analysis requires a precise input-output specification, a proof that the output is correct, and a resource bound in a stated computational model. The lecture fixes the asymptotic notation and proof templates used later.

## References and further reading

- T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, _Introduction to Algorithms_, for standard algorithmic models, asymptotic notation, and correctness techniques.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
← Previous lecture · [Course contents]({{ '/notes/design-and-analysis-of-algorithms/' | relative_url }}) · [Formula sheet]({{ '/notes/design-and-analysis-of-algorithms/formula-sheet/' | relative_url }}) · [Next lecture →]({{ '/notes/design-and-analysis-of-algorithms/lecture-02-minimum-enclosing-circles/' | relative_url }})
</nav>

</div>
