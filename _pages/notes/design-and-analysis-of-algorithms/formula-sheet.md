---
layout: page
title: "Design and Analysis of Algorithms: Formula and Notation Sheet"
description: "A cumulative notation and formula sheet for the Design and Analysis of Algorithms lecture series."
course: "Design and Analysis of Algorithms"
instructor: "Sandip Das"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
last_updated: "2026-08-06"
status: "living"
math: true
permalink: /notes/design-and-analysis-of-algorithms/formula-sheet/
course_slug: design-and-analysis-of-algorithms
note_kind: formula-sheet
course_order: 99
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

This sheet is cumulative. Every symbol is defined and every bound is accompanied by the assumptions under which it is valid. The lecture in which an item first appears is indicated explicitly.

## 1. Global notation and conventions

{% assign lecture_1_url = '/notes/design-and-analysis-of-algorithms/lecture-01-algorithmic-foundations/' | relative_url %}
{% assign lecture_2_url = '/notes/design-and-analysis-of-algorithms/lecture-02-minimum-enclosing-circles/' | relative_url %}
{% assign lecture_4_url = '/notes/design-and-analysis-of-algorithms/lecture-04-simultaneous-minimum-maximum/' | relative_url %}
{% assign lecture_5_url = '/notes/design-and-analysis-of-algorithms/lecture-05-deterministic-linear-selection/' | relative_url %}

| Symbol                               | Meaning                                                                   | Conditions / first appearance                        |
| ------------------------------------ | ------------------------------------------------------------------------- | ---------------------------------------------------- |
| $n$                                  | Input size, array length, or number of nodes/points, according to context | [Lecture 1]({{ lecture_1_url }})                     |
| $T(n)$                               | Worst-case running time on an input of size $n$                           | [Lecture 1]({{ lecture_1_url }})                     |
| $\mathbb{N}$                         | Natural numbers                                                           | [Lecture 1]({{ lecture_1_url }})                     |
| $\mathbb{R}^2$                       | Euclidean plane                                                           | [Lecture 2]({{ lecture_2_url }})                     |
| $\lvert S \rvert$                    | Cardinality of a finite set $S$                                           | [Lecture 5]({{ lecture_5_url }})                     |
| $\lfloor x\rfloor$, $\lceil x\rceil$ | Floor and ceiling of $x$                                                  | [Lecture 4]({{ lecture_4_url }})                     |
| $h$                                  | Tree height; the active convention must be stated                         | Edge-height in Lecture 7, vertex-height in Lecture 8 |

Unless stated otherwise, arrays use $1$-based indexing, logarithms are base $2$, and BST keys are distinct. Rotated arrays in Lecture 6 use $0$-based indexing for the pivot formula.

## 2. Lecture 1: asymptotic notation

For functions $f,g:\mathbb{N}\to\mathbb{R}_{\ge0}$:

$$
f(n)=O(g(n))
\iff
\exists c>0,\exists n_0:\ f(n)\le c g(n)\quad\forall n\ge n_0.
$$

$$
f(n)=\Omega(g(n))
\iff
\exists c>0,\exists n_0:\ f(n)\ge c g(n)\quad\forall n\ge n_0.
$$

$$
f(n)=\Theta(g(n))
\iff
f(n)=O(g(n))\text{ and }f(n)=\Omega(g(n)).
$$

**Interpretation.** $O$ is an asymptotic upper bound, $\Omega$ a lower bound, and $\Theta$ a matching two-sided bound. Exact counts retain constants that asymptotic notation suppresses.

## 3. Lecture 2: minimum enclosing circles

For points $S=\lbrace{}P_1,\dots,P_n\rbrace\subset\mathbb{R}^2$ and candidate center $P$:

$$
F(P)=\max_{1\le i\le n}\|P-P_i\|_2.
$$

The optimal center and radius satisfy

$$
P^\star\in\operatorname{argmin}_{P\in\mathbb{R}^2}F(P),
\qquad
R^\star=F(P^\star).
$$

For a pair $A,B$, the diameter candidate is

$$
O=\frac{A+B}{2},
\qquad
R=\frac{\|A-B\|}{2}.
$$

For non-collinear $A=(x_1,y_1)$, $B=(x_2,y_2)$, and $C=(x_3,y_3)$, the circumcenter $O=(u,v)$ solves

$$
\begin{bmatrix}
2(x_2-x_1) & 2(y_2-y_1)\\
2(x_3-x_1) & 2(y_3-y_1)
\end{bmatrix}
\begin{bmatrix}u\\v\end{bmatrix}
=
\begin{bmatrix}
x_2^2+y_2^2-x_1^2-y_1^2\\
x_3^2+y_3^2-x_1^2-y_1^2
\end{bmatrix}.
$$

The matrix is invertible exactly when the three points are non-collinear. The exhaustive candidate count is

$$
\binom{n}{2}+\binom{n}{3}=\Theta(n^3),
$$

and testing every candidate against all $n$ points gives

$$
\Theta(n)\left(\binom{n}{2}+\binom{n}{3}\right)=\Theta(n^4).
$$

A uniqueness identity used for the MEC center is

$$
\|P_i-M\|^2
=
\frac{\|P_i-A\|^2+\|P_i-B\|^2}{2}
-
\frac{\|A-B\|^2}{4},
$$

where $M=(A+B)/2$.

## 4. Lecture 3: divide-and-conquer recurrences

For

$$
T(n)=aT(n/b)+cn^k,
\qquad a>0,\ b>1,\ k\ge0,
$$

assuming $n=b^m$ and $T(1)=\Theta(1)$, repeated substitution gives

$$
T(n)
=
n^{\log_b a}T(1)
+
cn^k\sum_{i=0}^{\log_b n-1}
\left(\frac{a}{b^k}\right)^i.
$$

Let $r=a/b^k$. Then

$$
T(n)=
\begin{cases}
\Theta(n^k), & a<b^k,\\
\Theta(n^k\log n), & a=b^k,\\
\Theta(n^{\log_b a}), & a>b^k.
\end{cases}
$$

**Conditions.** This polynomial-form theorem assumes equal subproblem sizes $n/b$ and nonrecursive work $\Theta(n^k)$. It does not directly cover $T(n)=T(n-1)+n$ or unequal splits such as $T(n)=T(n/3)+T(2n/3)+n$.

Representative applications:

| Recurrence               | Result            |
| ------------------------ | ----------------- |
| $T(n)=2T(n/2)+\Theta(n)$ | $\Theta(n\log n)$ |
| $T(n)=T(n/2)+\Theta(1)$  | $\Theta(\log n)$  |
| $T(n)=4T(n/2)+\Theta(n)$ | $\Theta(n^2)$     |
| $T(n)=2T(n/4)+\Theta(n)$ | $\Theta(n)$       |

## 5. Lecture 4: simultaneous minimum and maximum

Naive worst-case comparison count:

$$
(n-1)+(n-2)=2n-3.
$$

Pairing-method count for $n\ge2$:

$$
C(n)=
\begin{cases}
\dfrac{3n}{2}-2, & n\text{ even},\\[0.4em]
\dfrac{3(n-1)}{2}, & n\text{ odd},
\end{cases}
$$

or equivalently

$$
\boxed{C(n)=\left\lceil\frac{3n}{2}\right\rceil-2}.
$$

This is optimal in the comparison model.

## 6. Lecture 5: order statistics and deterministic selection

For distinct elements sorted as

$$
A_{(1)}<A_{(2)}<\cdots<A_{(n)},
$$

$A_{(i)}$ is the $i$th order statistic.

With groups of five, median of medians guarantees

$$
\#\lbrace{}a\in A:a<x\rbrace\ge\frac{3n}{10}-6,
\qquad
\#\lbrace{}a\in A:a>x\rbrace\ge\frac{3n}{10}-6.
$$

Hence the larger partition has size at most

$$
\frac{7n}{10}+6.
$$

The recurrence is

$$
T(n)
\le
T\left(\left\lceil\frac{n}{5}\right\rceil\right)
+
T\left(\frac{7n}{10}+6\right)
+
cn.
$$

Because

$$
\frac15+\frac7{10}=\frac9{10}<1,
$$

induction yields $T(n)=O(n)$, and reading the input gives the matching lower bound $\Omega(n)$; therefore

$$
\boxed{T(n)=\Theta(n)}.
$$

For duplicates, use

$$
L=\lbrace{}a:a<x\rbrace,
\qquad
E=\lbrace{}a:a=x\rbrace,
\qquad
G=\lbrace{}a:a>x\rbrace.
$$

Return $x$ when $\lvert{}L\rvert<i\le \lvert{}L\rvert+\lvert{}E\rvert$; otherwise recurse with the corresponding adjusted rank.

## 7. Lecture 6: binary search and rotated arrays

After $t$ unsuccessful binary-search comparisons, the active interval has size at most

$$
\frac{n}{2^t}.
$$

Thus binary search performs at most

$$
\left\lfloor\log_2 n\right\rfloor+1
$$

iterations and has worst-case running time $\Theta(\log n)$.

For a strictly increasing base array $B[0\dots n-1]$ rotated by pivot $p$:

$$
A[j]=B[(j-p)\bmod n].
$$

A logical sorted index $j$ appears at physical index

$$
\boxed{(p+j)\bmod n}.
$$

Median indices:

- odd $n$: $j=\lfloor n/2\rfloor$;
- even $n$: lower median $j=n/2-1$, upper median $j=n/2$;
- numerical median for even $n$: average the values at those two mapped indices.

With duplicate keys, pivot search can degrade from $O(\log n)$ to $\Theta(n)$ because equality may reveal no side information.

## 8. Lecture 7: binary search trees

The BST invariant at every node $v$ is

$$
\operatorname{keys}(v.\operatorname{left})<v.\operatorname{key}<\operatorname{keys}(v.\operatorname{right}).
$$

Search, insertion, deletion, minimum, maximum, predecessor, and successor each take

$$
\Theta(h),
$$

where $h$ is edge-height. A maximally skewed $n$-node BST has

$$
h=n-1,
$$

so the worst case is $\Theta(n)$. A balanced BST has $h=\Theta(\log n)$.

Traversal orders:

- inorder: left subtree, root, right subtree;
- preorder: root, left subtree, right subtree;
- postorder: left subtree, right subtree, root.

For distinct labels, preorder plus inorder and postorder plus inorder uniquely determine the tree. Preorder plus postorder alone does not determine an arbitrary binary tree.

## 9. Lecture 8: height-balanced trees and balanced search structures

Using vertex-height, a tree is height-balanced when

$$
\left|h(v.\text{left})-h(v.\text{right})\right|\le1
$$

for every node $v$.

Maximum node count:

$$
N_{\max}(0)=0,
\qquad
N_{\max}(h)=1+2N_{\max}(h-1),
$$

so

$$
\boxed{N_{\max}(h)=2^h-1}.
$$

Minimum node count:

$$
N_{\min}(0)=0,
\qquad
N_{\min}(1)=1,
\qquad
N_{\min}(h)=1+N_{\min}(h-1)+N_{\min}(h-2).
$$

With $F_0=0$, $F_1=1$, and $F_r=F_{r-1}+F_{r-2}$,

$$
\boxed{N_{\min}(h)=F_{h+2}-1}.
$$

Therefore

$$
F_{h+2}-1\le n\le2^h-1.
$$

Using $F_r\ge\varphi^{r-2}$ for $r\ge2$, where $\varphi=(1+\sqrt5)/2$,

$$
h\le\log_\varphi(n+1)=O(\log n).
$$

AVL balance factor:

$$
\operatorname{bf}(v)
=
h(v.\text{left})-h(v.\text{right})
\in\lbrace-1,0,1\rbrace.
$$

Red-black height bound:

$$
h\le2\log_2(n+1).
$$

For a B-tree of minimum degree $t$, all leaves have the same depth and the height is $O(\log_t n)$.

## 10. Lecture 9: quick comparison table

| Problem or structure     | Main idea                                             | Worst-case result                |
| ------------------------ | ----------------------------------------------------- | -------------------------------- |
| Naive MEC                | Test pair-diameter and triple-circumcircle candidates | $\Theta(n^4)$                    |
| Master recurrence        | Compare $a$ with $b^k$                                | Three cases above                |
| Simultaneous min and max | Pair elements                                         | $\lceil3n/2\rceil-2$ comparisons |
| Deterministic selection  | Median of medians                                     | $\Theta(n)$                      |
| Binary search            | Halve a valid candidate interval                      | $\Theta(\log n)$                 |
| Rotated-array median     | Find pivot, then map index modulo $n$                 | $O(\log n)$ for distinct keys    |
| Ordinary BST operation   | Follow one root-to-leaf path                          | $\Theta(h)$, worst $\Theta(n)$   |
| Balanced BST operation   | Maintain logarithmic height                           | $O(\log n)$                      |
| Height-balanced size     | Fibonacci minimum and perfect-tree maximum            | $F_{h+2}-1\le n\le2^h-1$         |

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Course contents]({{ '/notes/design-and-analysis-of-algorithms/' | relative_url }})
</nav>

</div>
