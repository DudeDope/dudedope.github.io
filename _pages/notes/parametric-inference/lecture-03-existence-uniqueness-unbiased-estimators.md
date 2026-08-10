---
layout: page
title: "Lecture 3: Existence and Uniqueness of Unbiased Estimators"
short_title: "Existence of unbiased estimators"
course: "Parametric Inference"
lecture: 3
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Characterises unbiasedly estimable functions in binomial and Poisson models, explains the analytic power-series condition, and proves uniqueness for one exponential observation using Laplace transforms."
topics:
  - "unbiased estimability"
  - "binomial polynomials"
  - "Poisson power series"
  - "analytic functions"
  - "Laplace transform"
  - "exponential model"
previous: "lecture-02-unbiased-estimation-umvue-crlb"
next: "lecture-04-sufficiency-rao-blackwell"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-11"
status: "complete"
math: true
permalink: /notes/parametric-inference/lecture-03-existence-uniqueness-unbiased-estimators/
course_slug: parametric-inference
note_kind: lecture
course_order: 3
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Fall 2026 Parametric Inference lectures of Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata. The exposition includes additional definitions, derivations, and worked solutions. Any remaining errors belong to the note maintainer, not to the instructor or the Institute.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture →]({{ '/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell/' | relative_url }})
</nav>

## Learning objectives

- Determine when a target function can possess an unbiased estimator in finite-support models.
- Use polynomial and power-series identities to construct or rule out unbiased estimators.
- Explain precisely what analyticity means in the Poisson argument.
- Prove uniqueness of the unbiased estimator of an exponential mean from one observation.

## 1. The binomial model

Let

$$
X\sim\operatorname{Bin}(n,\theta),\qquad 0<\theta<1.
$$

For any statistic $T=T(X)$,

$$
\operatorname{E}_\theta[T]
=\sum_{x=0}^n T(x)\binom nx\theta^x(1-\theta)^{n-x}.
$$

The right side is a polynomial in $\theta$ of degree at most $n$.

<div class="theorem" markdown="1">

**Theorem 3.1 — Unbiasedly estimable functions in the binomial model.**
A function $\psi:(0,1)\to\mathbb{R}$ has an unbiased estimator based on $X\sim\operatorname{Bin}(n,\theta)$ if and only if $\psi$ is the restriction to $(0,1)$ of a polynomial of degree at most $n$.

</div>

**Proof.**

Necessity follows from the expectation formula above.

For sufficiency, write

$$
\psi(\theta)=\sum_{k=0}^n a_k\theta^k.
$$

Let $(x)_{k}=x(x-1)\cdots(x-k+1)$ denote the falling factorial, with $(x)_{0}=1$. A standard binomial factorial-moment calculation gives

$$
\operatorname{E}_\theta[(X)_{k}]=(n)_{k}\theta^k.
$$

Therefore

$$
T(X)=\sum_{k=0}^n a_k\frac{(X)_{k}}{(n)_{k}}
$$

satisfies

$$
\operatorname{E}_\theta[T(X)]
=\sum_{k=0}^n a_k\theta^k
=\psi(\theta).
$$

$\square$

### Worked Example 3.1 — No unbiased estimator of the binomial odds

**Problem.**

Work through the source example “No unbiased estimator of $(1-\theta)/\theta$” in full.

**Solution.**

Suppose we want to estimate

$$
\psi(\theta)=\frac{1-\theta}{\theta}=\frac1\theta-1.
$$

This is not a polynomial on $(0,1)$. Therefore no statistic $T(X)$ can satisfy

$$
\operatorname{E}_\theta[T(X)]=\frac{1-\theta}{\theta}
\qquad\text{for every }0<\theta<1.
$$

- \*A direct contradiction can also be seen by multiplying by $\theta$: if an unbiased estimator existed, then

$$
\sum_{x=0}^n T(x)\binom nx\theta^{x+1}(1-\theta)^{n-x}=1-\theta.
$$

Every term on the left contains a factor $\theta$, so the left side vanishes at $\theta=0$, whereas the right side equals $1$. Polynomial identity makes this impossible.

**Final result.**

The conclusion is the final result derived in the solution above.

### Worked Example 3.2 — Constructing unbiased estimators

**Problem.**

Construct unbiased estimators of $\theta$, $\theta^2$, and more generally $\theta^k$ in the binomial model.

**Solution.**

For $X\sim\operatorname{Bin}(n,\theta)$:

$$
\frac Xn\quad\text{is unbiased for }\theta,
$$

$$
\frac{X(X-1)}{n(n-1)}\quad\text{is unbiased for }\theta^2,
$$

and more generally

$$
\frac{(X)_{k}}{(n)_{k}}
\quad\text{is unbiased for }\theta^k,
\qquad 0\le k\le n.
$$

**Final result.**

For $0\le k\le n$, $(X)_k/(n)_k$ is unbiased for $\theta^k$.

## 2. The Poisson model

Let

$$
X\sim\operatorname{Poisson}(\theta),\qquad \theta>0.
$$

Then

$$
\operatorname{E}_\theta[T(X)]
=e^{-\theta}\sum_{x=0}^\infty T(x)\frac{\theta^x}{x!}.
$$

Hence unbiasedness for $\psi(\theta)$ requires

$$
e^\theta\psi(\theta)
=\sum_{x=0}^\infty T(x)\frac{\theta^x}{x!}.
$$

<div class="theorem" markdown="1">

**Theorem 3.2 — Unbiasedly estimable functions in the Poisson model.**
Suppose $T(X)$ is integrable for every $\theta>0$. Then $T$ is unbiased for $\psi$ if and only if

$$
F(z)=e^z\psi(z)
$$

has an entire power-series expansion

$$
F(z)=\sum_{x=0}^\infty a_x z^x,
$$

in which case the unbiased estimator is uniquely determined by

$$
T(x)=x!a_x=F^{(x)}(0).
$$

Equivalently, $\psi$ must extend to an entire function on $\mathbb C$.

</div>

**Proof.**

If $T$ is integrable for every positive $\theta$, then for every $r>0$,

$$
\sum_{x=0}^\infty |T(x)|\frac{r^x}{x!}<\infty.
$$

Thus the series

$$
F(z)=\sum_{x=0}^\infty T(x)\frac{z^x}{x!}
$$

converges absolutely for every complex $z$, so it is entire, and $F(\theta)=e^\theta\psi(\theta)$.

Conversely, if $F(z)=\sum a_xz^x$ is entire, define $T(x)=x!a_x$. Then

$$
\operatorname{E}_\theta[T(X)]
=e^{-\theta}\sum_{x=0}^\infty a_x\theta^x
=e^{-\theta}F(\theta)
=\psi(\theta).
$$

Uniqueness follows from uniqueness of power-series coefficients.

$\square$

### Worked Example 3.3 — Poisson powers

**Problem.**

Use Poisson factorial moments to construct unbiased estimators of powers of the Poisson mean.

**Solution.**

The factorial moments satisfy

$$
\operatorname{E}_\theta[(X)_{k}]=\theta^k.
$$

Hence $(X)_{k}$ is unbiased for $\theta^k$. For example,

$$
X(X-1)\quad\text{is unbiased for }\theta^2.
$$

**Final result.**

$(X)_k$ is unbiased for $\theta^k$; in particular, $X(X-1)$ is unbiased for $\theta^2$.

### Worked Example 3.4 — No unbiased estimator of the reciprocal Poisson mean

**Problem.**

Work through the source example “No unbiased estimator of $1/\theta$” in full.

**Solution.**

The function $1/\theta$ has a pole at zero and does not extend to an entire function. Therefore no integrable unbiased estimator of $1/\theta$ exists in the one-observation Poisson model.

**Final result.**

The conclusion is the final result derived in the solution above.

## Additional context: Analytic functions and the Poisson power-series condition

> **Additional context.**
> This explanation was added to make the lecture self-contained.

A real-valued function $f$ is **analytic at $a$** if there exists $r>0$ and coefficients $c_0,c_1,\ldots$ such that

$$
f(x)=\sum_{m=0}^{\infty}c_m(x-a)^m,\qquad |x-a|<r,
$$

and this power series converges to $f(x)$ throughout that neighbourhood. The coefficients are necessarily the Taylor coefficients,

$$
c_m=\frac{f^{(m)}(a)}{m!},
$$

so analyticity at $a$ means

$$
f(x)=\sum_{m=0}^{\infty}\frac{f^{(m)}(a)}{m!}(x-a)^m
$$

for all $x$ sufficiently close to $a$.

Analyticity is stronger than infinite differentiability. For example,

$$
f(x)=
\begin{cases}
e^{-1/x^2}, & x\ne0,\\
0, & x=0,
\end{cases}
$$

is infinitely differentiable at $0$ and satisfies $f^{(m)}(0)=0$ for every $m$, so its Taylor series at $0$ is identically zero. Yet $f(x)>0$ for $x\ne0$, so the Taylor series does not recover the function near $0$; hence $f$ is not analytic at $0$.

For the Poisson unbiased-estimation problem,

$$
e^\theta\psi(\theta)
=\sum_{x=0}^{\infty}T(x)\frac{\theta^x}{x!}.
$$

If $T$ is integrable for every $\theta>0$, then for each $r>0$,

$$
\sum_{x=0}^{\infty}|T(x)|\frac{r^x}{x!}<\infty.
$$

Thus the same power series converges absolutely for every complex $z$, so it has **infinite radius of convergence** and defines an **entire function**. Entire is stronger than merely analytic on $(0,\infty)$: it means analytic on all of $\mathbb C$.

This distinction explains why $1/\theta$ fails. Although $1/\theta$ is analytic around every positive point, it has a pole at $0$ and does not extend to an entire function. Therefore it cannot satisfy the Poisson unbiased-estimation condition above.

## 3. The one-observation exponential model

<div class="theorem" markdown="1">

**Theorem 3.3 — Uniqueness of the unbiased estimator of an exponential mean.**
Let

$$
X\sim\operatorname{Exp}(\text{mean }\theta),\qquad \theta>0.
$$

Then $X$ is the unique unbiased estimator of $\theta$, up to almost-sure equality.

</div>

**Proof.**

Clearly $\operatorname{E}_\theta[X]=\theta$. Suppose $T(X)$ is any other integrable unbiased estimator. Then

$$
\operatorname{E}_\theta[T(X)-X]=0
\qquad\text{for every }\theta>0.
$$

Let $h(x)=T(x)-x$. Since the exponential density is $\theta^{-1}e^{-x/\theta}$,

$$
\int_0^\infty h(x)\frac1\theta e^{-x/\theta}\,\mathrm{d}x=0.
$$

Multiplying by $\theta$ and writing $s=1/\theta$,

$$
\int_0^\infty h(x)e^{-sx}\,\mathrm{d}x=0
\qquad\text{for every }s>0.
$$

The left side is the Laplace transform of $h$. By uniqueness of the Laplace transform,

$$
h(x)=0
\quad\text{for Lebesgue-almost every }x>0.
$$

Therefore $T(X)=X$ almost surely under every $P_\theta$.

$\square$

<div class="remark" markdown="1">

**Remark 3.4.**
For $n\ge2$ exponential observations, $\overline X$ is not the only unbiased estimator; for example, $X_1$ is also unbiased. What is unique is the UMVUE, namely $\overline X$.

</div>

## Questions answered in this lecture

**Question.**

Which functions of $\theta$ admit an unbiased estimator from $X\sim\operatorname{Bin}(n,\theta)$?

**Answer.**

Exactly the restrictions to $(0,1)$ of polynomials of degree at most $n$.

**Question.**

Why is there no unbiased estimator of $(1-\theta)/\theta$ in the binomial model?

**Answer.**

Its expectation would have to be a polynomial of degree at most $n$, but $(1-\theta)/\theta$ is not a polynomial.

**Question.**

What does “analytic” mean in the Poisson power-series argument?

**Answer.**

A function is analytic at a point when it equals a convergent power series in a neighbourhood of that point. Here the integrability condition is stronger: the relevant series has infinite radius of convergence, yielding an entire extension.

**Question.**

Why is $X$ the unique unbiased estimator of the mean from one exponential observation?

**Answer.**

The difference between any two unbiased estimators has Laplace transform zero for every positive transform parameter; uniqueness of the Laplace transform implies that difference is zero almost everywhere.

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.
- Expanded source: the complete LaTeX notes and compiled PDF used for this Markdown conversion.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture →]({{ '/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell/' | relative_url }})
</nav>

</div>
