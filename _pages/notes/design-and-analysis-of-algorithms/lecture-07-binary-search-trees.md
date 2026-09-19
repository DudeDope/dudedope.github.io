---
layout: page
title: "Lecture 7: Binary Search Trees: Operations, Traversals, and Reconstruction"
short_title: "Binary search trees"
course: "Design and Analysis of Algorithms"
lecture: 7
instructor: "Sandip Das"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Develops binary-tree terminology and the BST invariant, then treats search, insertion, deletion, traversals, predecessor/successor, reconstruction, and height-dependent complexity."
topics:
  - "Binary trees"
  - "Binary search trees"
  - "Insertion and deletion"
  - "Tree traversals"
  - "Predecessor and successor"
  - "Tree reconstruction"
previous: "lecture-06-binary-search-rotated-arrays"
next: "lecture-08-height-balanced-search-trees"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-06"
status: "complete"
math: true
permalink: /notes/design-and-analysis-of-algorithms/lecture-07-binary-search-trees/
course_slug: design-and-analysis-of-algorithms
note_kind: lecture
course_order: 7
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

- Use the recursive definition and terminology of binary trees.
- Prove search, insertion, and deletion correct under the BST invariant.
- Compute preorder, inorder, and postorder traversals.
- Find inorder predecessors and successors in all structural cases.
- Determine which traversal pairs uniquely reconstruct a binary tree.
- Relate operation costs to tree height.

## 1. Basic tree terminology

> **Definition 7.1 --- Binary tree.**  
> A binary tree is either empty or consists of a root node together with a left subtree and a right subtree, each itself a binary tree.

For a node $v$:

- its _parent_ is the adjacent node one step closer to the root;

- its left and right adjacent descendants are its _children_;

- two distinct children of the same parent are _siblings_;

- a node with no children is a _leaf_;

- the subtree rooted at $v$ contains $v$ and all of its descendants;

- the _depth_ of $v$ is the number of edges from the root to $v$;

- the _label_ or _key_ is the value stored at the node.

Under the edge-height convention, a leaf has height $0$ and the empty tree has height $-1$. Under the vertex-height convention, a leaf has height $1$ and the empty tree has height $0$.

## 2. Binary search tree invariant

> **Definition 7.2 --- Binary search tree.**  
> A binary search tree (BST) is a binary tree with a key at each node such that for every node $v$:
>
> - every key in the left subtree of $v$ is strictly smaller than $v.\mathrm{key}$;
> - every key in the right subtree of $v$ is strictly larger than $v.\mathrm{key}$.

Distinct keys are assumed. With duplicates, a fixed policy is required, such as storing a multiplicity counter or always sending equal keys to one designated side.

## 3. Search, minimum, and maximum

**Algorithm --- BST search.**

```text
BST-SEARCH(root, k)
Input: The root of a BST and a key k
Output: The node with key k, or None

v <- root
while v is not null and v.key != k:
    if k < v.key:
        v <- v.left
    else:
        v <- v.right
return v
```

At each step, the BST invariant proves that one whole subtree cannot contain $k$. The minimum is found by following left-child pointers until no left child exists; the maximum is found symmetrically by following right-child pointers.

## 4. Insertion

**Algorithm --- BST insertion.**

```text
BST-INSERT(root, k)
Input: The root of a BST and a new key k
Output: The BST with k inserted

p <- null
v <- root
while v is not null:
    p <- v
    if k < v.key:
        v <- v.left
    else if k > v.key:
        v <- v.right
    else:
        return root       // duplicates are not inserted

create a new node z with z.key = k and no children
if p is null:
    root <- z
else if k < p.key:
    p.left <- z
else:
    p.right <- z
return root
```

> **Theorem 7.3 --- Insertion correctness.**  
> BST insertion preserves the BST invariant and adds exactly one node with key $k$.

**Proof.**

The search path ends at a null child position of a node $p$. Every ancestor comparison constrains $k$ to the corresponding left or right region. If $k<p.\mathrm{key}$, attaching $k$ as the left child places it below $p$ and respects all ancestor inequalities; the right-child case is symmetric. No existing nodes or keys are changed, and exactly one new node is attached.

$\square$

## 5. Worked insertion example: inserting 36

**Problem.**

Insert the key $36$ into the BST shown below, identify every comparison on the search path, and state the final attachment point.

**Solution.**

The lecture diagram uses the following BST before insertion:

```text
            50
          /    \
        25      62
       /  \    /  \
     10   45  53   94
       \        \  / \
       12       57 69 100
```

To insert $36$:

$$
\begin{aligned}
36&<50 &&\Rightarrow \text{move left to }25,\\
36&>25 &&\Rightarrow \text{move right to }45,\\
36&<45 &&\Rightarrow \text{move to the null left child of }45.
\end{aligned}
$$

Therefore $36$ becomes the left child of $45$:

```text
            50
          /    \
        25      62
       /  \    /  \
     10   45  53   94
       \  /     \  / \
       12 36    57 69 100
```

The path has three existing nodes, so the insertion performs three key comparisons and one pointer update.

**Final result.**

The new node with key $36$ is attached as the left child of the node with key $45$.

**Interpretation.**

Insertion changes no existing key order; it follows one search path and performs one pointer update at the first null child position.

## 6. Deletion

Deletion must preserve the BST order while removing a node $z$.

### 6.1. Case 1: $z$ is a leaf

Set the appropriate child pointer of its parent to null. No subtree must be reattached.

### 6.2. Case 2: $z$ has exactly one child

Replace $z$ by its only child. Every key in that child’s subtree already lies in the correct interval determined by $z$’s ancestors.

### 6.3. Case 3: $z$ has two children

Let $y$ be the inorder successor of $z$, equivalently the minimum node in $z$’s right subtree. Then $y$ has no left child. Replace $z$’s key by $y$’s key, then delete $y$ using Case 1 or Case 2. Alternatively, a pointer-based implementation can transplant $y$ into $z$’s position.

> **Theorem 7.4 --- Deletion correctness.**  
> The three-case deletion procedure removes the target key and preserves the BST invariant.

**Proof.**

The leaf and one-child cases only splice out $z$ and preserve all ancestor intervals. In the two-child case, the successor $y$ is the smallest key greater than $z.\mathrm{key}$. Hence every key in $z$’s left subtree is below $y.\mathrm{key}$, and every remaining key in $z$’s right subtree is above $y.\mathrm{key}$. Replacing $z$ by $y$ therefore preserves order. Since $y$ has no left child, removing its old occurrence reduces to a simpler case.

$\square$

### Worked Example 7.5 --- Deleting a node with two children

**Problem.**

Delete key $25$ from the post-insertion BST and preserve the BST invariant.

**Solution.**

In the post-insertion tree, delete key $25$. Its left subtree contains $10,12$ and its right subtree contains $45,36$. The successor is the minimum of the right subtree, namely $36$. Replace $25$ by $36$, then remove the old leaf $36$ from below $45$. The resulting local structure is

```text
       36
      /  \
    10    45
      \
      12
```

and the BST order remains valid.

**Final result.**

$$
25\text{ is replaced by its successor }36.
$$

**Interpretation.**

Successor replacement reduces the two-child deletion to deletion of a node with at most one child.

## 7. Traversals

> **Definition 7.6 --- Tree traversals.**  
> For a node $v$:
>
> $$
> \begin{aligned}
> \text{inorder:} &\quad \text{left subtree},\ v,\ \text{right subtree},\\
> \text{preorder:} &\quad v,\ \text{left subtree},\ \text{right subtree},\\
> \text{postorder:} &\quad \text{left subtree},\ \text{right subtree},\ v.
> \end{aligned}
> $$

Each traversal visits every node exactly once and therefore runs in $\Theta(n)$ time using $\Theta(h)$ recursion-stack space, where $h$ is the tree height.

> **Theorem 7.7 --- Inorder traversal of a BST is sorted.**  
> An inorder traversal of a BST lists its keys in strictly increasing order.

**Proof.**

Use induction on the number of nodes. By the BST invariant, every left-subtree key is below the root and every right-subtree key is above it. By induction, the recursive inorder lists of both subtrees are individually sorted. Concatenating left list, root, and right list is therefore globally sorted.

$\square$

### Worked Example 7.8 --- Traversal sequences

**Problem.**

Compute the preorder, inorder, and postorder traversals of the BST after inserting $36$.

**Solution.**

For the tree after inserting $36$:

$$
\begin{aligned}
\text{inorder }&=10,12,25,36,45,50,53,57,62,69,94,100,\\
\text{preorder }&=50,25,10,12,45,36,62,53,57,94,69,100,\\
\text{postorder }&=12,10,36,45,25,57,53,69,100,94,62,50.
\end{aligned}
$$

The inorder sequence confirms that the structure satisfies the BST invariant.

**Final result.**

The inorder sequence is sorted; the exact three sequences are derived in the solution.

**Interpretation.**

The traversal orders differ only in the position at which the root is visited.

## 8. Inorder predecessor and successor

> **Definition 7.9.**  
> The inorder predecessor of a node $v$ is the node immediately before $v$ in inorder traversal. The inorder successor is the node immediately after $v$.

### 8.1. Predecessor

- If $v$ has a left subtree, its predecessor is the maximum node in that subtree.

- Otherwise, move upward until first moving up from a right child; that ancestor is the predecessor. If no such ancestor exists, $v$ is the minimum and has no predecessor.

### 8.2. Successor

- If $v$ has a right subtree, its successor is the minimum node in that subtree.

- Otherwise, move upward until first moving up from a left child; that ancestor is the successor. If no such ancestor exists, $v$ is the maximum and has no successor.

### Worked Example 7.10

**Problem.**

Determine selected inorder predecessors and successors in the displayed BST.

**Solution.**

In the post-insertion tree:

- the predecessor of $50$ is the maximum of its left subtree, namely $45$;

- the successor of $45$ is $50$ because $45$ has no right subtree and the first ancestor reached from a left branch is $50$;

- the successor of $53$ is the minimum of its right subtree, namely $57$;

- the predecessor of $10$ does not exist because $10$ is the minimum key.

**Final result.**

The predecessor or successor is found either inside the appropriate subtree or at the first qualifying ancestor.

**Interpretation.**

The subtree and ancestor cases are exhaustive.

## 9. Which traversal pairs determine a tree?

Assume all node labels are distinct.

> **Theorem 7.11 --- Reconstruction from traversals.**  
> Either of the following pairs uniquely determines a binary tree:
>
> 1.  preorder and inorder;
> 2.  postorder and inorder.
>
> Preorder and postorder alone do not uniquely determine an arbitrary binary tree.

**Proof.**

In preorder, the first element is the root. Its position in inorder uniquely separates the labels of the left and right subtrees. The corresponding blocks in preorder are then determined by their sizes, and the argument recurses. For postorder, the last element is the root and the same inorder split applies.

For non-uniqueness of preorder plus postorder, consider two nodes $A,B$. The tree with $B$ as the left child of $A$ and the tree with $B$ as the right child of $A$ both have preorder $(A,B)$ and postorder $(B,A)$, yet they are different trees.

$\square$

> **Remark 7.12.**  
> For a _full_ binary tree, where every internal node has exactly two children, preorder and postorder together do determine the tree when labels are distinct. The ambiguity above comes from nodes with exactly one child.

## 10. Height and operation costs

Search, insertion, deletion, minimum, maximum, predecessor, and successor all follow at most one root-to-leaf path, so each takes $\Theta(h)$ time where $h$ is the edge-height.

A BST can be maximally skewed. Inserting keys in increasing order produces a chain with

$$
h=n-1,
$$

so operations can take $\Theta(n)$ time. A balanced tree keeps $h=\Theta(\log n)$ and therefore supports these operations in logarithmic time.

## Questions answered in this lecture

> **Question.**  
> Which traversal pairs uniquely determine a binary tree with distinct labels?

**Answer.**

Preorder plus inorder and postorder plus inorder each determine the tree uniquely. Preorder plus postorder does not determine an arbitrary binary tree.

> **Question.**  
> Why does replacing a two-child node by its successor preserve BST order?

**Answer.**

The successor is the smallest key larger than the deleted key. All left-subtree keys remain smaller, and all remaining right-subtree keys are larger.

> **Question.**  
> What determines the running time of an ordinary BST operation?

**Answer.**

Search, insertion, deletion, extrema, predecessor, and successor follow at most one root-to-leaf path, so each costs $\Theta(h)$ for tree height $h$.

## Lecture summary

BST operations follow a single root-to-leaf path and therefore cost $\Theta(h)$. Inorder traversal lists keys in sorted order; preorder or postorder paired with inorder determines the tree, while preorder plus postorder alone is generally insufficient.

## References and further reading

- Supplied _Lecture 3, 27 July_: binary search trees, traversals, predecessor, and successor.
- T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, _Introduction to Algorithms_, for BST operations and proofs.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/design-and-analysis-of-algorithms/lecture-06-binary-search-rotated-arrays/' | relative_url }}) · [Course contents]({{ '/notes/design-and-analysis-of-algorithms/' | relative_url }}) · [Formula sheet]({{ '/notes/design-and-analysis-of-algorithms/formula-sheet/' | relative_url }}) · [Next lecture →]({{ '/notes/design-and-analysis-of-algorithms/lecture-08-height-balanced-search-trees/' | relative_url }})
</nav>

</div>
