---
layout: page
title: "Lecture 6: Binary Search and Medians in Rotated Sorted Arrays"
short_title: "Binary search and rotations"
course: "Design and Analysis of Algorithms"
lecture: 6
instructor: "Sandip Das"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Proves iterative binary search using a loop invariant, finds the rotation pivot in logarithmic time, and maps sorted indices to physical indices in a rotated array."
topics:
  - "Binary search"
  - "Loop invariants"
  - "Rotated arrays"
  - "Pivot search"
  - "Median indexing"
previous: "lecture-05-deterministic-linear-selection"
next: "lecture-07-binary-search-trees"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-06"
status: "complete"
math: true
permalink: /notes/design-and-analysis-of-algorithms/lecture-06-binary-search-rotated-arrays/
course_slug: design-and-analysis-of-algorithms
note_kind: lecture
course_order: 6
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

- State and prove the binary-search loop invariant.
- Derive the $\Theta(\log n)$ search bound.
- Locate the minimum element of a rotated strictly increasing array.
- Map a logical sorted index to its physical rotated-array position.
- Handle odd and even median conventions and understand the effect of duplicates.

## 1. Binary search

Let

$$
x_1<x_2<\cdots<x_n
$$

be a sorted array of distinct elements, and let $y$ be a target. Binary search repeatedly compares $y$ with the middle active element and discards the half that cannot contain $y$.

**Algorithm --- Iterative binary search.**

```text
BINARY-SEARCH(A, y)
Input: A sorted array A[1..n] and a target y
Output: An index j with A[j] = y, or NotFound

L <- 1
R <- n
while L <= R:
    m <- floor((L + R) / 2)
    if A[m] = y:
        return m
    else if A[m] < y:
        L <- m + 1
    else:
        R <- m - 1

return NotFound
```

> **Theorem 6.1 --- Correctness of binary search.**  
> The algorithm returns an index of $y$ if $y$ occurs, and returns otherwise.

**Proof.**

Use the loop invariant:

> If $y$ occurs in the array, then at the start of each iteration it occurs within the active interval $A[L\dots R]$.

Initially $[L,R]=[1,n]$, so the invariant holds. If $A[m]<y$, sortedness implies every index $j\le m$ satisfies $A[j]\le A[m]<y$, so none can contain $y$; setting $L=m+1$ preserves the invariant. The case $A[m]>y$ is symmetric. If equality holds, the returned index is correct. If the loop terminates with $L>R$, the active interval is empty; by the invariant, $y$ does not occur.

$\square$

> **Proposition 6.2 --- Running time.**  
> Binary search performs at most $\left\lfloor \log_2 n\right\rfloor+1$ iterations and runs in $\Theta(\log n)$ time.

**Proof.**

After $t$ unsuccessful comparisons, the active interval has size at most $n/2^t$. Once $2^t>n$, the interval is empty. Thus $t=O(\log n)$. A matching lower bound follows from the comparison decision-tree model: the search problem has at least $n+1$ distinguishable outcomes, and every comparison has only a constant number of outcomes. A decision tree of height $h$ therefore has at most $c^h$ leaves for a fixed constant $c$, so $c^h\ge n+1$ and $h=\Omega(\log n)$.

$\square$

### Worked Example 6.3 --- Tracing binary search

**Problem.**

Trace binary search for the target $31$ in $A=[2,5,9,12,18,23,31,44,57,63]$.

**Solution.**

Search for $31$ in

$$
A=[2,5,9,12,18,23,31,44,57,63].
$$

| Iteration | $L$ | $R$ | $m$ |       Comparison       |
| :-------: | :-: | :-: | :-: | :--------------------: |
|     1     |  1  | 10  |  5  | $A[5]=18<31$, so $L=6$ |
|     2     |  6  | 10  |  8  | $A[8]=44>31$, so $R=7$ |
|     3     |  6  |  7  |  6  | $A[6]=23<31$, so $L=7$ |
|     4     |  7  |  7  |  7  |    $A[7]=31$, found    |

**Final result.**

$$
31\text{ is found at index }7.
$$

**Interpretation.**

The active interval shrinks from ten entries to one in four iterations.

## 2. Rotated sorted arrays

> **Definition 6.4 --- Rotation.**  
> Let $B[0\dots n-1]$ be strictly increasing. For an offset $p$, the rotated array $A$ is
>
> $$
> A[j]=B[(j-p)\bmod n].
> $$
>
> Equivalently, $A$ consists of two increasing blocks, and $p$ is the index of the minimum element.

For example,

$$
A=[31,71,78,93,94,1,5,10,20,25,30]
$$

has pivot $p=5$ under $0$-based indexing.

### 2.1. Finding the pivot in logarithmic time

For distinct keys, compare the middle element with the rightmost active element.

**Algorithm --- Find the minimum index in a rotated sorted array.**

```text
FIND-PIVOT(A)
Input: A rotated strictly increasing array A[0..n-1]
Output: The pivot p such that A[p] is minimum

L <- 0
R <- n - 1
while L < R:
    m <- floor((L + R) / 2)
    if A[m] > A[R]:
        L <- m + 1
    else:
        R <- m

return L
```

**Proof (correctness).**

Maintain the invariant that the pivot belongs to $[L,R]$. If $A[m]>A[R]$, the descent from the large block to the small block must occur strictly to the right of $m$, so the pivot is in $[m+1,R]$. Otherwise $A[m]\le A[R]$, so $m$ lies in the low sorted block and the pivot is in $[L,m]$, possibly at $m$. Each update preserves the pivot and strictly shrinks the interval. When $L=R$, that index is the pivot.

$\square$

### 2.2. Mapping sorted indices to rotated indices

If $p$ is the pivot, then the element at logical sorted index $j\in\lbrace0,\dots,n-1\rbrace$ occurs at physical index

$$
(p+j)\bmod n.
$$

Thus, after finding $p$ in $O(\log n)$ time, any order statistic with a known sorted index can be read in $O(1)$ time.

### Worked Example 6.5 --- Median of the lecture's rotated array

**Problem.**

Find the median of $A=[31,71,78,93,94,1,5,10,20,25,30]$ using the rotation pivot.

**Solution.**

Consider

$$
A=[31,71,78,93,94,1,5,10,20,25,30].
$$

The pivot search finds $p=5$, where $A[5]=1$. Since $n=11$ is odd, the median has sorted $0$-based index

$$
j=\left\lfloor n/2\right\rfloor=5.
$$

Its physical index is

$$
(p+j)\bmod n=(5+5)\bmod11=10.
$$

Therefore the median is

$$
A[10]=\boxed{30}.
$$

Indeed, the unrotated sorted order is

$$
[1,5,10,20,25,30,31,71,78,93,94].
$$

**Final result.**

$$
\operatorname{median}(A)=30.
$$

**Interpretation.**

The median is obtained by mapping the logical sorted index through the pivot, without explicitly unrotating the array.

> **Remark 6.6 --- Even length.**  
> For even $n$, one must specify the convention. The lower median has sorted index $n/2-1$, the upper median has index $n/2$, and the numerical median is often defined as the average of those two values. Both physical indices are obtained using the same modular mapping.

> **Caution --- Duplicates.**  
> If duplicates are permitted, the comparison $A[m]=A[R]$ may not reveal which side contains the pivot. A safe algorithm may decrement $R$ in this tie case, which preserves correctness but can degrade to $\Theta(n)$ in the worst case, for example when most entries are equal.

## Questions answered in this lecture

> **Question.**  
> What invariant proves binary search correct?

**Answer.**

If the target occurs, it lies in the active interval $A[L\dots R]$ at the start of every iteration.

> **Question.**  
> How is a sorted index mapped into a rotated array?

**Answer.**

If $p$ is the index of the minimum element and $j$ is a zero-based sorted index, the physical index is $(p+j)\bmod n$.

> **Question.**  
> Why can duplicates destroy the logarithmic pivot bound?

**Answer.**

When $A[m]=A[R]$, the comparison may reveal no side information. Safely shrinking one endpoint can remove only one element per iteration, giving $\Theta(n)$ in the worst case.

## Lecture summary

Binary search repeatedly preserves a candidate interval and halves it. A related logarithmic search locates the pivot of a rotated sorted array; once the pivot is known, any logical sorted index maps to $(p+j)\bmod n$.

## References and further reading

- Supplied _Lecture 2, 23 July_: binary search and rotated sorted arrays.
- T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, _Introduction to Algorithms_, for binary-search correctness and complexity.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/design-and-analysis-of-algorithms/lecture-05-deterministic-linear-selection/' | relative_url }}) · [Course contents]({{ '/notes/design-and-analysis-of-algorithms/' | relative_url }}) · [Formula sheet]({{ '/notes/design-and-analysis-of-algorithms/formula-sheet/' | relative_url }}) · [Next lecture →]({{ '/notes/design-and-analysis-of-algorithms/lecture-07-binary-search-trees/' | relative_url }})
</nav>

</div>
