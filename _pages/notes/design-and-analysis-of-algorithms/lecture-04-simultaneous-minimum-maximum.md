---
layout: page
title: "Lecture 4: Simultaneous Minimum and Maximum by the Pairing Method"
short_title: "Simultaneous minimum and maximum"
course: "Design and Analysis of Algorithms"
lecture: 4
instructor: "Sandip Das"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Compares the naive scan with the optimal pairing method for finding both extrema and proves the exact worst-case comparison count."
topics:
  - "Comparison model"
  - "Minimum and maximum"
  - "Pairing method"
  - "Loop invariants"
  - "Exact comparison counts"
previous: "lecture-03-divide-and-conquer-recurrences"
next: "lecture-05-deterministic-linear-selection"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-06"
status: "complete"
math: true
permalink: /notes/design-and-analysis-of-algorithms/lecture-04-simultaneous-minimum-maximum/
course_slug: design-and-analysis-of-algorithms
note_kind: lecture
course_order: 4
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

- Explain why the straightforward scan can require $2n-3$ comparisons.
- Implement and prove the correctness of the pairing algorithm.
- Derive the exact bound $\lceil 3n/2\rceil-2$.
- Understand why this comparison bound is optimal.

## 1. The problem

Given an array $A[1\dots n]$ of totally ordered elements, return

$$
\min_{1\le j\le n}A[j]
\qquad\text{and}\qquad
\max_{1\le j\le n}A[j].
$$

The running time is necessarily $\Theta(n)$ because every element must be inspected in the worst case. The interesting question is the exact number of comparisons.

## 2. Naive scan

Initialize both values using $A[1]$. For each later element, compare first with the current maximum; if it is not larger, compare it with the current minimum.

In the worst case, the maximum test is performed $n-1$ times and the minimum test $n-2$ times, for

$$
(n-1)+(n-2)=2n-3
$$

comparisons.

## 3. Pairing algorithm

The pairing method first compares elements within each pair. The pair winner can only challenge the current maximum, while the pair loser can only challenge the current minimum.

**Algorithm --- Simultaneous minimum and maximum.**

```text
Input: A nonempty array A[1..n]
Output: (minimum, maximum)

if n is even:
    if A[1] < A[2]:
        minimum <- A[1]
        maximum <- A[2]
    else:
        minimum <- A[2]
        maximum <- A[1]
    j <- 3
else:
    minimum <- A[1]
    maximum <- A[1]
    j <- 2

while j <= n - 1:
    if A[j] < A[j + 1]:
        small <- A[j]
        large <- A[j + 1]
    else:
        small <- A[j + 1]
        large <- A[j]

    if small < minimum:
        minimum <- small
    if large > maximum:
        maximum <- large

    j <- j + 2

return (minimum, maximum)
```

> **Theorem 4.1 --- Correctness.**  
> The pairing algorithm returns the minimum and maximum of the whole array.

**Proof.**

Within each processed pair, the smaller element cannot be the global maximum because the larger member of the same pair exceeds it. Therefore only the larger member must be compared with the running maximum. Symmetrically, only the smaller member must be compared with the running minimum. After each iteration, the maintained values are the minimum and maximum among all elements processed so far. This loop invariant is true after initialization, is preserved by each pair update, and at termination covers the entire array.

$\square$

> **Proposition 4.2 --- Exact comparison count.**  
> The algorithm uses
>
> $$
> \begin{cases}
> \frac{3n}{2}-2, & n\text{ even},\\[0.3em]
> \frac{3(n-1)}2, & n\text{ odd},
> \end{cases}
> $$
>
> which equals $\left\lceil 3n/2\right\rceil-2$ for every $n\ge2$.

**Proof.**

For even $n$, initialization costs one comparison and the remaining $(n-2)/2$ pairs cost three comparisons each:

$$
1+3\frac{n-2}{2}=\frac{3n}{2}-2.
$$

For odd $n$, initialization costs none and the remaining $(n-1)/2$ pairs cost three each:

$$
3\frac{n-1}{2}.
$$

$\square$

> **Additional context.**  
> This explanation was added to make the lecture self-contained.
>
> This bound is optimal in the comparison model. An adversary can require every element except the maximum to lose at least one comparison and every element except the minimum to win at least one comparison. A comparison between two previously unseen elements can simultaneously create one win and one loss; after this first comparison, resolving which candidates are globally smallest and largest needs separate evidence. Formalizing this bookkeeping yields the lower bound $\left\lceil 3n/2\right\rceil-2$.

## 4. Worked example

### Worked Example 4.3

**Problem.**

Apply the pairing algorithm to $A=[8,3,11,6,2,10,7,4]$ and count the comparisons.

**Solution.**

Apply the pairing algorithm to

$$
A=[8,3,11,6,2,10,7,4].
$$

Since $n=8$ is even, compare $8$ and $3$:

$$
\textit{minimum}=3,\qquad \textit{maximum}=8.
$$

Now process the remaining pairs.

|   Pair   | Internal comparison | Smaller vs. min | Larger vs. max | New $(\min,\max)$ |
| :------: | :-----------------: | :-------------: | :------------: | :---------------: |
| $(11,6)$ |       $6<11$        |   $6<3$ false   |  $11>8$ true   |     $(3,11)$      |
| $(2,10)$ |       $2<10$        |   $2<3$ true    | $10>11$ false  |     $(2,11)$      |
| $(7,4)$  |        $4<7$        |   $4<2$ false   |  $7>11$ false  |     $(2,11)$      |

The final answer is $\min A=2$ and $\max A=11$. The number of comparisons is

$$
1+3\cdot3=10=\frac{3(8)}2-2.
$$

**Final result.**

$$
\min A=2,\qquad \max A=11,\qquad 10\text{ comparisons}.
$$

**Interpretation.**

The observed count equals $3n/2-2$ for the even case $n=8$.

## Questions answered in this lecture

> **Question.**  
> Why can the smaller member of a pair skip the maximum comparison?

**Answer.**

It has already lost to the larger member of its own pair, so it cannot be the global maximum. Symmetrically, the pair winner cannot be the global minimum.

> **Question.**  
> What is the exact worst-case comparison count?

**Answer.**

For $n\ge2$, the count is $\lceil 3n/2\rceil-2$: $3n/2-2$ for even $n$ and $3(n-1)/2$ for odd $n$.

## Lecture summary

Pairing elements lets the smaller member challenge only the running minimum and the larger member challenge only the running maximum. This reduces the exact worst-case comparison count from $2n-3$ to $\lceil 3n/2\rceil-2$.

## References and further reading

- Vrajishnu Chakraborty, _Design and Analysis of Algorithms, Lecture 1_, supplied class notes.
- T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, _Introduction to Algorithms_, for comparison-model analysis.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/design-and-analysis-of-algorithms/lecture-03-divide-and-conquer-recurrences/' | relative_url }}) · [Course contents]({{ '/notes/design-and-analysis-of-algorithms/' | relative_url }}) · [Formula sheet]({{ '/notes/design-and-analysis-of-algorithms/formula-sheet/' | relative_url }}) · [Next lecture →]({{ '/notes/design-and-analysis-of-algorithms/lecture-05-deterministic-linear-selection/' | relative_url }})
</nav>

</div>
