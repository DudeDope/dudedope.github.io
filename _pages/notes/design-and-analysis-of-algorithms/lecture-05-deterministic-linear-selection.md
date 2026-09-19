---
layout: page
title: "Lecture 5: Order Statistics and Deterministic Linear-Time Selection"
short_title: "Median of medians"
course: "Design and Analysis of Algorithms"
lecture: 5
instructor: "Sandip Das"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Presents BFPRT median-of-medians selection, proves its discard guarantee and linear worst-case complexity, and works through a complete selection example."
topics:
  - "Order statistics"
  - "Selection problem"
  - "Median of medians"
  - "BFPRT"
  - "Worst-case linear time"
previous: "lecture-04-simultaneous-minimum-maximum"
next: "lecture-06-binary-search-rotated-arrays"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-06"
status: "complete"
math: true
permalink: /notes/design-and-analysis-of-algorithms/lecture-05-deterministic-linear-selection/
course_slug: design-and-analysis-of-algorithms
note_kind: lecture
course_order: 5
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

- Define order statistics and distinguish selection from sorting.
- Execute the median-of-medians algorithm step by step.
- Prove that the chosen pivot discards a constant fraction on both sides.
- Solve the recurrence establishing deterministic $\Theta(n)$ time.
- Extend the method correctly to arrays with duplicate keys.

## 1. Order statistics

> **Definition 5.1 --- Order statistic.**  
> For an array of $n$ distinct numbers, let
>
> $$
> A_{(1)}<A_{(2)}<\cdots<A_{(n)}
> $$
>
> be the elements in sorted order. The value $A_{(i)}$ is the $i$th order statistic or the $i$th smallest element.

The selection problem is: given $A[1\dots n]$ and $i\in\lbrace1,\dots,n\rbrace$, return $A_{(i)}$. Sorting first takes $\Theta(n\log n)$ time, but full sorting reveals much more information than one order statistic. Selection can be done in deterministic $\Theta(n)$ worst-case time.

> **Editorial note.**  
> The lecture notes attribute the median-of-medians algorithm to Blum, Floyd, Pratt, Rivest, and Tarjan with the year 1993. The classic paper _Time Bounds for Selection_ was published in 1973. The algorithm is commonly called BFPRT or deterministic SELECT.

## 2. The median-of-medians algorithm

The core idea is to choose a pivot that is guaranteed not to be too close to either extreme.

**Algorithm --- Deterministic selection by median of medians.**

```text
SELECT(A, i)
Input: An array A of n >= 1 distinct elements and a rank 1 <= i <= n
Output: The i-th smallest element of A

if n is at most a fixed constant:
    sort A
    return A[i]

divide A into groups of five, with at most one final smaller group
sort each group and record one middle element as its group median
M <- array of group medians
x <- SELECT(M, ceil(|M| / 2))

partition A into:
    L = {a in A : a < x}
    {x}
    G = {a in A : a > x}

k <- |L| + 1
if i = k:
    return x
else if i < k:
    return SELECT(L, i)
else:
    return SELECT(G, i - k)
```

> **Theorem 5.2 --- Correctness.**  
> $\operatorname{Select}(A,i)$ returns the $i$th smallest element of $A$.

**Proof.**

Proceed by induction on $n$. The base case is correct because sorting explicitly places the $i$th smallest element at position $i$. For the recursive case, partitioning around $x$ puts exactly $\left\lvert L\right\rvert$ elements below $x$ and exactly $\left\lvert G\right\rvert$ elements above $x$. Thus $x$ has rank $k=\left\lvert L\right\rvert+1$. If $i=k$, returning $x$ is correct. If $i<k$, the desired element lies in $L$ with unchanged rank $i$. If $i>k$, it lies in $G$ and has rank $i-k$ within $G$. Each recursive call is on a smaller array, so the inductive hypothesis applies.

$\square$

## 3. Why the pivot is good

Let $m=\left\lceil n/5\right\rceil$ be the number of groups. Since $x$ is a median of the group medians, at least about half of the medians are at most $x$ and at least about half are at least $x$. Every full group whose median is below $x$ contributes at least three elements below $x$: its median and the two smaller elements in that group. The same holds symmetrically above $x$.

> **Lemma 5.3 --- Discard guarantee.**  
> For the pivot $x$ chosen by median of medians, the number of elements strictly smaller than $x$ and the number strictly larger than $x$ are each at least
>
> $$
> \frac{3n}{10}-6.
> $$
>
> Therefore the larger recursive partition has size at most
>
> $$
> \frac{7n}{10}+6.
> $$

**Proof.**

There are $m=\left\lceil n/5\right\rceil$ group medians. The algorithm chooses the element of rank $r=\left\lceil m/2\right\rceil$ among them (the lower median when $m$ is even). Therefore $r$ group medians are at most $x$, while $m-r+1$ group medians are at least $x$.

For the lower side, discard the group containing $x$ and also discard the possibly incomplete final group. At least $r-2$ full groups remain with median strictly below $x$, and each contributes three elements strictly below $x$. Hence

$$
\#\lbrace{}a\in A:a<x\rbrace
\ge 3(r-2)
\ge 3\left(\frac m2-2\right)
\ge \frac{3n}{10}-6.
$$

For the upper side, after the same two conservative exclusions, at least $m-r-1$ full groups remain with median strictly above $x$. Since $r=\left\lceil m/2\right\rceil$, this yields at least $\left\lfloor m/2\right\rfloor-1$ such groups, and therefore an equally strong (in fact slightly stronger) bound of $3n/10-6$ elements above $x$.

The lecture derivation adds two elements from the group containing $x$. That improvement is valid when this group is full, but it need not be valid if $x$ comes from the incomplete remainder group. The conservative argument above avoids that case distinction while preserving the stated $3n/10-6$ guarantee. Hence, after discarding the pivot and at least $3n/10-6$ elements on the opposite side, the recursive partition has size at most

$$
n-\left(\frac{3n}{10}-6\right)=\frac{7n}{10}+6.
$$

$\square$

> **Remark 5.4.**  
> The constants $-6$ and $+6$ are unimportant asymptotically. What matters is that a fixed positive fraction of the array is discarded on each recursive selection step.

## 4. Worst-case running time

Grouping, finding each five-element median, and partitioning all take $\Theta(n)$ total time. The recursive call for the median of medians has size $\left\lceil n/5\right\rceil$, and the selected partition has size at most $7n/10+6$. Thus

$$
T(n)\le T\left(\left\lceil n/5\right\rceil\right)+T\left(\frac{7n}{10}+6\right)+cn
$$

for a constant $c>0$ and all sufficiently large $n$.

The sum of the leading subproblem fractions is

$$
\frac15+\frac7{10}=\frac9{10}<1,
$$

leaving enough “slack” to pay for the linear partitioning work.

> **Theorem 5.5 --- Deterministic linear selection.**  
> The BFPRT selection algorithm runs in $\Theta(n)$ worst-case time.

**Proof.**

The lower bound $\Omega(n)$ is immediate because, in the worst case, every input element must be inspected. For the upper bound, define the monotone envelope

$$
T'(n)=\max_{1\le q\le n}T(q).
$$

Then $T(n)\le T'(n)$ and

$$
T'(n)\le T'\left(\left\lceil n/5\right\rceil\right)+T'\left(\frac{7n}{10}+6\right)+cn.
$$

Choose a threshold $n_0=140$ and a constant $b$ such that $T'(n)\le b$ for $n<n_0$. We prove by strong induction that $T'(n)\le Cn$ for a sufficiently large constant $C$.

For $n\ge140$, the induction hypothesis gives

$$
\begin{aligned}
T'(n)
&\le C\left\lceil n/5\right\rceil+C\left(\frac{7n}{10}+6\right)+cn\\
&\le C\left(\frac n5+1\right)+C\left(\frac{7n}{10}+6\right)+cn\\
&=\frac9{10}Cn+7C+cn\\
&=Cn+\left(-\frac{Cn}{10}+7C+cn\right).
\end{aligned}
$$

The parenthesized term is nonpositive provided

$$
C\left(\frac n{10}-7\right)\ge cn.
$$

For $n\ge140$, we have $n/10-7\ge n/20$, so it is enough to choose $C\ge20c$. Increasing $C$ further handles the finitely many base cases, for example by requiring $C\ge b/1$ or any convenient bound. Therefore $T'(n)\le Cn$ and hence $T(n)=O(n)$.

$\square$

## 5. Worked selection example

### Worked Example 5.6 --- Finding the ninth smallest element

**Problem.**

Use deterministic median-of-medians selection to find the ninth smallest element of the given $21$-element array.

**Solution.**

Let

$$
A=[23,1,45,12,7,\ 34,19,8,41,5,\ 29,16,3,38,21,\ 10,47,14,27,6,\ 31]
$$

and let $i=9$.

**Step 1: form groups of five and sort only within each group.**

$$
\begin{array}{c|c|c}
\text{Group} & \text{Sorted group} & \text{Median}\\
\hline
(23,1,45,12,7) & (1,7,12,23,45) & 12\\
(34,19,8,41,5) & (5,8,19,34,41) & 19\\
(29,16,3,38,21) & (3,16,21,29,38) & 21\\
(10,47,14,27,6) & (6,10,14,27,47) & 14\\
(31) & (31) & 31
\end{array}
$$

Thus the median array is $M=[12,19,21,14,31]$. Its median is $x=19$.

**Step 2: partition around $19$.**

$$
\begin{aligned}
L&=[1,12,7,8,5,16,3,10,14,6],\\
G&=[23,45,34,41,29,38,21,47,27,31].
\end{aligned}
$$

There are $10$ elements in $L$, so $19$ has rank $11$. Since $i=9<11$, recurse on $L$ with rank $9$.

**Step 3: select the ninth smallest of $L$.** Group $L$ as

$$
(1,12,7,8,5),\qquad (16,3,10,14,6).
$$

Their sorted forms and medians are

$$
(1,5,7,8,12)\to7,
\qquad
(3,6,10,14,16)\to10.
$$

Choose $10$ as the upper median of $[7,10]$. In $L$, the elements below $10$ are

$$
[1,7,8,5,3,6],
$$

so $10$ has rank $7$. We need rank $9$, hence recurse on

$$
[12,16,14]
$$

with adjusted rank $9-7=2$. Sorting this constant-size base case gives

$$
[12,14,16],
$$

whose second element is $14$. Therefore the ninth smallest element of the original array is

$$
\boxed{14}.
$$

A complete sort, used only to verify the answer, is

$$
1,3,5,6,7,8,10,12,\boxed{14},16,19,21,23,27,29,31,34,38,41,45,47.
$$

**Final result.**

$$
A_{(9)}=14.
$$

**Interpretation.**

The algorithm finds the requested order statistic without fully sorting the input.

## 6. Duplicates and three-way partitioning

If duplicate keys are allowed, partition into

$$
L=\lbrace{}a:a<x\rbrace,\qquad E=\lbrace{}a:a=x\rbrace,\qquad G=\lbrace{}a:a>x\rbrace.
$$

Then:

- if $i\le\left\lvert L\right\rvert$, recurse on $L$ with rank $i$;

- if $\left\lvert L\right\rvert<i\le\left\lvert L\right\rvert+\left\lvert E\right\rvert$, return $x$;

- otherwise recurse on $G$ with rank $i-\left\lvert L\right\rvert-\left\lvert E\right\rvert$.

This avoids ambiguity about the “rank of the pivot” when the pivot occurs several times.

> **Additional context.**  
> This explanation was added to make the lecture self-contained.
>
> Why groups of five? Groups of three do not give enough shrinkage: the standard recurrence is roughly
>
> $$
> T(n)\le T(n/3)+T(2n/3)+O(n),
> $$
>
> whose subproblem fractions sum to $1$ and lead to an $O(n\log n)$ bound by this analysis. Any fixed odd group size at least five can yield linear time; five is the smallest such choice and gives a simple proof.

## Questions answered in this lecture

> **Question.**  
> Why does median of medians discard a constant fraction?

**Answer.**

At least about half of the group medians lie on each side of the pivot, and every full five-element group on one side contributes at least three elements on that side. Conservatively, at least $3n/10-6$ elements are discarded from either direction.

> **Question.**  
> Why are groups of five used?

**Answer.**

Groups of five are the smallest fixed odd group size for which the standard recurrence has leading subproblem fractions summing to less than one, yielding a linear bound.

> **Question.**  
> How are duplicates handled?

**Answer.**

Use a three-way partition $L=\lbrace{}a:a<x\rbrace$, $E=\lbrace{}a:a=x\rbrace$, and $G=\lbrace{}a:a>x\rbrace$ and compare the desired rank with $\lvert{}L\rvert$ and $\lvert{}L\rvert+\lvert{}E\rvert$.

## Lecture summary

BFPRT chooses a pivot recursively from medians of five-element groups. At least roughly $3n/10$ elements lie on each side, so the two recursive subproblem fractions sum to less than one and the total worst-case time is linear.

## References and further reading

- Supplied _Lecture 2, 23 July_: deterministic selection and order statistics.
- M. Blum, R. W. Floyd, V. Pratt, R. L. Rivest, and R. E. Tarjan, “Time Bounds for Selection,” _Journal of Computer and System Sciences_, 1973.
- T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, _Introduction to Algorithms_, for deterministic selection.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/design-and-analysis-of-algorithms/lecture-04-simultaneous-minimum-maximum/' | relative_url }}) · [Course contents]({{ '/notes/design-and-analysis-of-algorithms/' | relative_url }}) · [Formula sheet]({{ '/notes/design-and-analysis-of-algorithms/formula-sheet/' | relative_url }}) · [Next lecture →]({{ '/notes/design-and-analysis-of-algorithms/lecture-06-binary-search-rotated-arrays/' | relative_url }})
</nav>

</div>
