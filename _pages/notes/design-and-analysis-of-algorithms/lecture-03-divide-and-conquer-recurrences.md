---
layout: page
title: "Lecture 3: Divide-and-Conquer Recurrences and the Polynomial Master Theorem"
short_title: "Divide-and-conquer recurrences"
course: "Design and Analysis of Algorithms"
lecture: 3
instructor: "Sandip Das"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Derives the three standard Master-Theorem cases by repeated substitution and a geometric series, then applies them to several representative recurrences."
topics:
  - "Divide and conquer"
  - "Recurrence relations"
  - "Master Theorem"
  - "Geometric series"
  - "Recursion trees"
previous: "lecture-02-minimum-enclosing-circles"
next: "lecture-04-simultaneous-minimum-maximum"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-06"
status: "complete"
math: true
permalink: /notes/design-and-analysis-of-algorithms/lecture-03-divide-and-conquer-recurrences/
course_slug: design-and-analysis-of-algorithms
note_kind: lecture
course_order: 3
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

- Translate a divide-and-conquer algorithm into a recurrence.
- Iterate $T(n)=aT(n/b)+cn^k$ and simplify the resulting geometric series.
- Derive and apply all three polynomial Master-Theorem cases.
- Recognize recurrences to which the theorem does not apply directly.

## 1. From recursive algorithms to recurrences

A divide-and-conquer algorithm typically:

1.  divides an instance of size $n$ into smaller instances;

2.  solves those instances recursively;

3.  combines their answers.

If there are $a$ subproblems of size $n/b$ and the nonrecursive work is $g(n)$, the running time often satisfies

$$
T(n)=aT(n/b)+g(n).
$$

For a clean derivation, we first assume $n=b^m$ and ignore floors and ceilings. They do not change the final asymptotic order in the standard cases.

## 2. Iteration of the recurrence $T(n)=aT(n/b)+cn^k$

Assume $a>0$, $b>1$, $k\ge 0$, and $T(1)=\Theta(1)$. Put $n=b^m$, so $m=\log_b n$. Repeated substitution gives

$$
\begin{aligned}
T(b^m)
&=aT(b^{m-1})+cb^{mk}\\
&=a^2T(b^{m-2})+ca b^{(m-1)k}+cb^{mk}\\
&=a^mT(1)+cb^{mk}\sum_{i=0}^{m-1}\left(\frac{a}{b^k}\right)^i.
\end{aligned}
$$

Since $a^m=(b^m)^{\log_b a}=n^{\log_b a}$ and $b^{mk}=n^k$,

$$
T(n)=n^{\log_b a}T(1)+cn^k\sum_{i=0}^{\log_b n-1}\left(\frac{a}{b^k}\right)^i.
$$

The common ratio $r=a/b^k$ yields three cases.

> **Theorem 3.1 --- Polynomial-form Master Theorem.**  
> For
>
> $$
> T(n)=aT(n/b)+\Theta(n^k),
> \qquad a\ge1,\ b>1,\ k\ge0,
> $$
>
> we have
>
> $$
> T(n)=
> \begin{cases}
> \Theta(n^k), & a<b^k,\\
> \Theta(n^k\log n), & a=b^k,\\
> \Theta(n^{\log_b a}), & a>b^k.
> \end{cases}
> $$

**Proof.**

If $r<1$, the geometric sum is bounded above and below by positive constants, so the $n^k$ term dominates. If $r=1$, the sum has exactly $\log_b n$ terms and equals $\log_b n$. If $r>1$, the sum is $\Theta(r^{\log_b n})$; hence

$$
n^k r^{\log_b n}
=n^k\left(\frac{a}{b^k}\right)^{\log_b n}
=n^k\frac{n^{\log_b a}}{n^k}
=n^{\log_b a}.
$$

The leaf term has the same order in the third case and no larger order in the first two.

$\square$

## 3. Worked recurrences

### Worked Example 3.2 --- Merge-sort recurrence

**Problem.**

Solve the merge-sort recurrence $T(n)=2T(n/2)+\Theta(n)$.

**Solution.**

$$
T(n)=2T(n/2)+\Theta(n).
$$

Here $a=2$, $b=2$, $k=1$, and $a=b^k=2$. Therefore

$$
T(n)=\Theta(n\log n).
$$

At recursion level $j$, there are $2^j$ subproblems of size $n/2^j$, so the total combine work is

$$
2^j\cdot \Theta(n/2^j)=\Theta(n).
$$

There are $\log n$ levels, giving the same conclusion.

**Final result.**

$$
T(n)=\Theta(n\log n).
$$

**Interpretation.**

Every recursion level contributes $\Theta(n)$ work and there are $\log n$ levels.

### Worked Example 3.3 --- Binary-search recurrence

**Problem.**

Solve the binary-search recurrence $T(n)=T(n/2)+\Theta(1)$.

**Solution.**

$$
T(n)=T(n/2)+\Theta(1).
$$

Here $a=1$, $b=2$, $k=0$, and $a=b^k=1$. Hence

$$
T(n)=\Theta(\log n).
$$

**Final result.**

$$
T(n)=\Theta(\log n).
$$

**Interpretation.**

The work is constant per level and the instance size halves at each level.

### Worked Example 3.4 --- Leaf-dominated recurrence

**Problem.**

Solve $T(n)=4T(n/2)+\Theta(n)$.

**Solution.**

$$
T(n)=4T(n/2)+\Theta(n).
$$

Here $a=4>b^k=2$, so

$$
T(n)=\Theta(n^{\log_2 4})=\Theta(n^2).
$$

Although each node performs linear work in its own subproblem size, the number of subproblems grows quickly enough that the leaves dominate.

**Final result.**

$$
T(n)=\Theta(n^2).
$$

**Interpretation.**

The branching factor makes the leaves dominate the total work.

### Worked Example 3.5 --- Root-dominated recurrence

**Problem.**

Solve $T(n)=2T(n/4)+\Theta(n)$.

**Solution.**

$$
T(n)=2T(n/4)+\Theta(n).
$$

Here $a=2<4^1$, so the nonrecursive work at the root dominates and

$$
T(n)=\Theta(n).
$$

**Final result.**

$$
T(n)=\Theta(n).
$$

**Interpretation.**

The nonrecursive work at the root and upper levels dominates.

> **Caution --- When the theorem does not apply directly.**  
> The recurrence $T(n)=T(n-1)+n$ does not have subproblem size $n/b$ for a fixed $b>1$. Iterating gives
>
> $$
> T(n)=T(1)+\sum_{j=2}^n j=\Theta(n^2).
> $$
>
> Likewise, recurrences with unequal subproblem sizes, such as $T(n)=T(n/3)+T(2n/3)+n$, require another method such as a recursion tree or the Akra-Bazzi theorem.

## Questions answered in this lecture

> **Question.**  
> Why are there three Master-Theorem cases?

**Answer.**

Repeated substitution produces a geometric sum with ratio $r=a/b^k$. The cases $r<1$, $r=1$, and $r>1$ correspond respectively to root-dominated, level-balanced, and leaf-dominated work.

> **Question.**  
> Why does $T(n)=T(n-1)+n$ not fit the theorem?

**Answer.**

Its recursive subproblem has size $n-1$, not $n/b$ for a fixed $b>1$; direct summation gives $T(n)=\Theta(n^2)$.

## Lecture summary

For $T(n)=aT(n/b)+\Theta(n^k)$, the comparison between $a$ and $b^k$ determines whether the root work, all levels equally, or the leaves dominate. The result follows directly from a geometric-series expansion.

## References and further reading

- Vrajishnu Chakraborty, _Design and Analysis of Algorithms, Lecture 1_, supplied class notes.
- T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, _Introduction to Algorithms_, for recurrence analysis and the Master Theorem.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/design-and-analysis-of-algorithms/lecture-02-minimum-enclosing-circles/' | relative_url }}) · [Course contents]({{ '/notes/design-and-analysis-of-algorithms/' | relative_url }}) · [Formula sheet]({{ '/notes/design-and-analysis-of-algorithms/formula-sheet/' | relative_url }}) · [Next lecture →]({{ '/notes/design-and-analysis-of-algorithms/lecture-04-simultaneous-minimum-maximum/' | relative_url }})
</nav>

</div>
