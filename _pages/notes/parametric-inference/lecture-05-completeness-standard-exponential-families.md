---
layout: page
title: "Lecture 5: Completeness in Standard Models and Full Exponential Families"
short_title: "Completeness"
course: "Parametric Inference"
lecture: 5
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Defines completeness and proves it for binomial, Poisson, exponential, and uniform statistics, then gives the general Laplace-transform argument for full natural exponential families."
topics:
  - "completeness"
  - "binomial completeness"
  - "Poisson completeness"
  - "Laplace transforms"
  - "uniform maximum"
  - "natural exponential families"
previous: "lecture-04-sufficiency-rao-blackwell"
next: "lecture-06-lehmann-scheffe-umvue-examples"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-11"
status: "complete"
math: true
permalink: /notes/parametric-inference/lecture-05-completeness-standard-exponential-families/
course_slug: parametric-inference
note_kind: lecture
course_order: 5
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Fall 2026 Parametric Inference lectures of Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata. The exposition includes additional definitions, derivations, and worked solutions. Any remaining errors belong to the note maintainer, not to the instructor or the Institute.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture →]({{ '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-examples/' | relative_url }})
</nav>

## Learning objectives

- State completeness as an injectivity property of the expectation operator.
- Prove completeness for the standard binomial, Poisson, exponential, and uniform statistics.
- Understand why continuity is unnecessary in the uniform proof.
- Apply the full natural exponential-family completeness theorem with its required conditions.

## 1. Definition and meaning

<div class="definition" markdown="1">

**Definition 5.1 — Completeness.**
A statistic $S=S(X)$ is _complete_ for the family $\lbrace P_\theta:\theta\in\Theta \rbrace$ if, for every measurable function $g$ for which the expectations exist,

$$
\operatorname{E}_\theta[g(S)]=0\quad\text{for every }\theta\in\Theta
$$

implies

$$
g(S)=0\quad P_\theta\text{-almost surely for every }\theta\in\Theta.
$$

</div>

Completeness is an injectivity property of the expectation operator. It says that two functions of $S$ cannot have the same expectation for every parameter value unless they are almost surely equal.

<div class="proposition" markdown="1">

**Proposition 5.2 — Uniqueness among functions of a complete statistic.**
If $S$ is complete and $h_1(S)$ and $h_2(S)$ are unbiased estimators of the same parametric function, then

$$
h_1(S)=h_2(S)
\quad\text{almost surely}.
$$

</div>

**Proof.**

Since both are unbiased,

$$
\operatorname{E}_\theta[h_1(S)-h_2(S)]=0
\qquad\text{for all }\theta.
$$

Completeness gives $h_1(S)-h_2(S)=0$ almost surely.

$\square$

## 2. Completeness of binomial totals

<div class="theorem" markdown="1">

**Theorem 5.3.**
If $S\sim\operatorname{Bin}(n,\theta)$, $0<\theta<1$, then $S$ is complete.

</div>

**Proof.**

Suppose

$$
\operatorname{E}_\theta[g(S)]
=\sum_{s=0}^n g(s)\binom ns\theta^s(1-\theta)^{n-s}=0
\qquad\text{for all }0<\theta<1.
$$

Divide by $(1-\theta)^n$ and put $z=\theta/(1-\theta)\in(0,\infty)$. Then

$$
\sum_{s=0}^n g(s)\binom ns z^s=0
\qquad\text{for all }z>0.
$$

A polynomial that vanishes on an interval is identically zero. Hence every coefficient is zero:

$$
g(s)\binom ns=0,
$$

so $g(s)=0$ for all $s=0,\dots,n$.

$\square$

## 3. Completeness of Poisson totals

<div class="theorem" markdown="1">

**Theorem 5.4.**
If $S\sim\operatorname{Poisson}(\lambda)$ with $\lambda$ ranging over $(0,\infty)$, then $S$ is complete.

</div>

**Proof.**

Suppose

$$
0=\operatorname{E}_\lambda[g(S)]
=e^{-\lambda}\sum_{s=0}^\infty g(s)\frac{\lambda^s}{s!}
\qquad\text{for all }\lambda>0.
$$

Multiplying by $e^\lambda$,

$$
\sum_{s=0}^\infty g(s)\frac{\lambda^s}{s!}=0.
$$

The left side is an analytic power series. Since it vanishes on an interval, all its coefficients vanish. Hence $g(s)=0$ for every nonnegative integer $s$.

$\square$

## 4. Completeness of exponential sums

<div class="theorem" markdown="1">

**Theorem 5.5.**
If $X_1,\dots,X_n$ are iid exponential with mean $\theta>0$, then

$$
S=\sum_{i=1}^nX_i
$$

is complete.

</div>

**Proof.**

The density of $S$ is gamma:

$$
f_{S,\theta}(s)
=\frac{s^{n-1}}{\Gamma(n)\theta^n}e^{-s/\theta}\mathbf{1}_{(0,\infty)}(s).
$$

Suppose $\operatorname{E}_\theta[g(S)]=0$ for all $\theta>0$. Then

$$
\int_0^\infty g(s)s^{n-1}e^{-s/\theta}\,\mathrm{d}s=0
\qquad\text{for every }\theta>0.
$$

Let $u=1/\theta$. We obtain

$$
\int_0^\infty \bigl[g(s)s^{n-1}\bigr]e^{-us}\,\mathrm{d}s=0
\qquad\text{for every }u>0.
$$

By uniqueness of the Laplace transform,

$$
g(s)s^{n-1}=0
\quad\text{for almost every }s>0.
$$

Since $s^{n-1}>0$ for $s>0$, $g(s)=0$ almost everywhere.

$\square$

## 5. Completeness of the uniform maximum

<div class="theorem" markdown="1">

**Theorem 5.6.**
For an iid sample from $\operatorname{Uniform}(0,\theta)$, the maximum $M=X_{(n)}$ is complete.

</div>

**Proof.**

The density of $M$ is

$$
f_{M,\theta}(m)=\frac{n m^{n-1}}{\theta^n}\mathbf{1}_{(0,\theta)}(m).
$$

Suppose $\operatorname{E}_\theta[g(M)]=0$ for all $\theta>0$. Then

$$
0=\frac n{\theta^n}\int_0^\theta g(m)m^{n-1}\,\mathrm{d}m.
$$

Therefore

$$
\int_0^\theta g(m)m^{n-1}\,\mathrm{d}m=0
\qquad\text{for every }\theta>0.
$$

The left side is an absolutely continuous function of $\theta$. Differentiating almost everywhere gives

$$
g(\theta)\theta^{n-1}=0.
$$

Hence $g(\theta)=0$ for almost every $\theta>0$, proving completeness.

$\square$

## 6. Completeness of full natural exponential families

Consider a natural exponential family

$$
f_\eta(x)=h(x)\exp\lbrace \eta^\top T(x)-A(\eta) \rbrace,
\qquad \eta\in\mathcal N\subseteq\mathbb{R}^k,
$$

where $\mathcal N$ contains a nonempty open set. Suppose $\operatorname{E}_\eta[g(T)]=0$ for every $\eta\in\mathcal N$. Then

$$
\int g(T(x))h(x)e^{\eta^\top T(x)}\,\mathrm{d}x=0
$$

throughout an open set of $\eta$-values. This is a multivariate Laplace transform of the signed measure induced by $g(T)h(x)\,\mathrm{d}x$. Uniqueness of the multivariate Laplace transform implies that the signed measure is zero, and therefore $g(T)=0$ almost surely. Hence $T$ is complete.

This theorem is useful, but it should not be invoked mechanically: the family must be full rather than curved, the natural parameter set must contain an open subset of the correct dimension, and the support must be common across parameter values.

## Questions answered in this lecture

**Question.**

What extra property does completeness add beyond sufficiency?

**Answer.**

Sufficiency concerns information retained after conditioning; completeness concerns uniqueness of functions of the statistic through the expectation operator.

**Question.**

Why does a polynomial that vanishes for all positive $z$ prove binomial completeness?

**Answer.**

A nonzero polynomial has only finitely many roots. Vanishing on an interval forces every coefficient to be zero.

**Question.**

Why is continuity of $g$ unnecessary in the uniform completeness proof?

**Answer.**

The indefinite integral is absolutely continuous, so the fundamental theorem for Lebesgue integrals gives its derivative almost everywhere; that is enough to conclude $g=0$ almost everywhere.

**Question.**

What is the essential structural condition behind the theorem?

**Answer.**

The natural parameter set must contain a nonempty open subset of the correct dimension; this rules out curved subfamilies for this direct argument.

**Question.**

Why does a Laplace-transform identity prove completeness?

**Answer.**

The transform uniquely determines the underlying signed measure under the stated integrability conditions, so a transform that is zero on an open set forces that measure to be zero.

**Question.**

Why should this theorem not be invoked mechanically?

**Answer.**

Fullness, natural-parameter dimension, common support, and the transform/integrability assumptions all need to be checked.

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.
- Expanded source: the complete LaTeX notes and compiled PDF used for this Markdown conversion.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture →]({{ '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-examples/' | relative_url }})
</nav>

</div>
