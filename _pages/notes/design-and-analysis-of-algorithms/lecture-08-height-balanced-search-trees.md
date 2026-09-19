---
layout: page
title: "Lecture 8: Height-Balanced Trees and Balanced Search Structures"
short_title: "Balanced search structures"
course: "Design and Analysis of Algorithms"
lecture: 8
instructor: "Sandip Das"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Derives exact minimum and maximum node counts for height-balanced trees and introduces AVL, red-black, B-tree, and B+ tree structures."
topics:
  - "Height balance"
  - "Fibonacci recurrence"
  - "AVL trees"
  - "Red-black trees"
  - "B-trees"
  - "B+ trees"
previous: "lecture-07-binary-search-trees"
next: "lecture-09-consolidated-algorithm-review"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-06"
status: "complete"
math: true
permalink: /notes/design-and-analysis-of-algorithms/lecture-08-height-balanced-search-trees/
course_slug: design-and-analysis-of-algorithms
note_kind: lecture
course_order: 8
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

- Apply the height-balance condition using a fixed height convention.
- Derive $N_{\min}(h)=F_{h+2}-1$ and $N_{\max}(h)=2^h-1$.
- Use the Fibonacci bound to prove logarithmic height.
- Describe AVL rotations and red-black height guarantees.
- Distinguish binary balanced trees from multiway B-trees and B+ trees.

## 1. Height balance

For this chapter’s counting problem, use _vertex-height_: a leaf has height $1$ and the empty tree has height $0$.

> **Definition 8.1 --- Height-balanced binary tree.**  
> A binary tree is height-balanced if every node $v$ satisfies
>
> $$
> \left|h(v.\mathrm{left})-h(v.\mathrm{right})\right|\le1.
> $$

## 2. Minimum and maximum number of nodes

Let $N_{\min}(h)$ and $N_{\max}(h)$ denote the minimum and maximum possible number of nodes in a height-balanced binary tree of vertex-height $h$.

### 2.1. Maximum

The maximum occurs for a perfect binary tree:

$$
N_{\max}(0)=0,
\qquad
N_{\max}(h)=1+2N_{\max}(h-1).
$$

Solving gives

$$
\boxed{N_{\max}(h)=2^h-1}.
$$

### 2.2. Minimum

To attain height $h$ with as few nodes as possible, one child subtree must have height $h-1$, and the other should have the smallest permitted height, namely $h-2$. Thus

$$
N_{\min}(0)=0,
\qquad
N_{\min}(1)=1,
\qquad
N_{\min}(h)=1+N_{\min}(h-1)+N_{\min}(h-2).
$$

> **Theorem 8.2 --- Exact minimum via Fibonacci numbers.**  
> Let $F_0=0$, $F_1=1$, and $F_{r}=F_{r-1}+F_{r-2}$. Then
>
> $$
> \boxed{N_{\min}(h)=F_{h+2}-1}.
> $$
>
> Therefore every height-balanced binary tree of vertex-height $h$ and size $n$ satisfies
>
> $$
> F_{h+2}-1\le n\le 2^h-1.
> $$

**Proof.**

Set $M(h)=N_{\min}(h)+1$. The recurrence becomes

$$
M(h)=M(h-1)+M(h-2),
$$

with $M(0)=1=F_2$ and $M(1)=2=F_3$. Hence $M(h)=F_{h+2}$ by induction, so $N_{\min}(h)=F_{h+2}-1$.

$\square$

### Worked Example 8.3 --- The lecture question: height $4$

**Problem.**

Find the minimum number of nodes in a height-balanced binary tree of vertex-height $4$.

**Solution.**

Using the recurrence,

$$
N_{\min}(0)=0,
\quad N_{\min}(1)=1,
\quad N_{\min}(2)=2,
\quad N_{\min}(3)=4,
\quad N_{\min}(4)=7.
$$

Thus the minimum is

$$
\boxed{7}.
$$

One extremal shape is shown below; at each internal node, the two subtree heights differ by at most one.

```text
          a
        /   \
       b     c
      / \   /
     d   e f
    /
   g
```

The left subtree has height $3$ and the right subtree height $2$; recursively, each subtree is itself minimally balanced.

**Final result.**

$$
N_{\min}(4)=7.
$$

**Interpretation.**

The extremal tree uses child heights $h-1$ and $h-2$ recursively.

> **Corollary 8.4 --- Logarithmic height.**  
> A height-balanced tree with $n$ nodes has height $O(\log n)$.

**Proof.**

Fibonacci numbers grow exponentially: $F_r\ge \varphi^{r-2}$ for $r\ge2$, where $\varphi=(1+\sqrt5)/2$. Since $n\ge F_{h+2}-1$, we obtain $n+1\ge\varphi^h$, so

$$
h\le\log_{\varphi}(n+1)=O(\log n).
$$

$\square$

## 3. AVL trees

> **Definition 8.5 --- AVL tree.**  
> An AVL tree is a BST in which every node has balance factor
>
> $$
> \mathrm{bf}(v)=h(v.\mathrm{left})-h(v.\mathrm{right})\in\lbrace-1,0,1\rbrace.
> $$

After an ordinary BST insertion or deletion, AVL trees restore balance using local rotations:

- left-left imbalance: one right rotation;

- right-right imbalance: one left rotation;

- left-right imbalance: left rotation on the child, then right rotation;

- right-left imbalance: right rotation on the child, then left rotation.

Rotations preserve inorder order, hence preserve the BST invariant. The Fibonacci bound above implies AVL height $O(\log n)$, so search, insertion, and deletion are $O(\log n)$.

## 4. Red-black trees

A red-black tree is a BST with a red/black bit satisfying standard constraints: the root is black, null leaves are black, no red node has a red child, and every path from a node to a descendant null leaf contains the same number of black nodes. These properties imply

$$
h\le 2\log_2(n+1).
$$

Red-black trees permit slightly weaker balance than AVL trees but often require fewer rotations during updates. Search, insertion, and deletion remain $O(\log n)$.

## 5. B-trees and B+ trees

> **Editorial note.**  
> The lecture page groups AVL, red-black, B-tree, and B+ tree under “weight balanced binary search tree.” AVL and red-black trees are binary search trees. B-trees and B+ trees are _multiway_ balanced search trees designed especially for block storage; they are not binary trees.

A B-tree node stores several ordered keys and may have many children. For minimum degree $t$, every non-root internal node has between $t$ and $2t$ children. All leaves occur at the same depth, giving height $O(\log_t n)$. Because one node can match a disk or database page, B-trees reduce expensive block accesses.

A B+ tree stores all records (or record pointers) in the leaves, while internal nodes act only as routing indexes. Leaves are commonly linked from left to right, making range scans efficient. B+ trees are widely used in database and file-system indexes.

## Questions answered in this lecture

> **Question.**  
> What is the minimum size of a height-balanced tree of vertex-height $h$?

**Answer.**

$N_{\min}(h)=F_{h+2}-1$, from $N_{\min}(h)=1+N_{\min}(h-1)+N_{\min}(h-2)$ with bases $0$ and $1$.

> **Question.**  
> Why is the height logarithmic in the number of nodes?

**Answer.**

Since Fibonacci numbers grow exponentially and $n\ge F_{h+2}-1$, rearrangement gives $h=O(\log n)$.

> **Question.**  
> Are B-trees and B+ trees binary search trees?

**Answer.**

No. They are balanced multiway search trees; AVL and red-black trees are the binary search-tree structures in this group.

## Lecture summary

A height-balanced tree has minimum size governed by a Fibonacci recurrence and maximum size $2^h-1$. Consequently its height is logarithmic. AVL and red-black trees enforce binary-tree balance, whereas B-trees and B+ trees are multiway structures for block-oriented storage.

## References and further reading

- Supplied _Lecture 3, 27 July_: height balance and balanced search structures.
- T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, _Introduction to Algorithms_, for AVL, red-black, and B-tree terminology.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/design-and-analysis-of-algorithms/lecture-07-binary-search-trees/' | relative_url }}) · [Course contents]({{ '/notes/design-and-analysis-of-algorithms/' | relative_url }}) · [Formula sheet]({{ '/notes/design-and-analysis-of-algorithms/formula-sheet/' | relative_url }}) · [Next lecture →]({{ '/notes/design-and-analysis-of-algorithms/lecture-09-consolidated-algorithm-review/' | relative_url }})
</nav>

</div>
