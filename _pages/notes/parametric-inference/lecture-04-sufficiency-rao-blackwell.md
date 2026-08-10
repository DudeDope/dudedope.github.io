---
layout: page
title: "Lecture 4: Sufficient Statistics, Factorisation, and Rao–Blackwell Improvement"
short_title: "Sufficiency and Rao–Blackwell"
course: "Parametric Inference"
lecture: 4
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Develops sufficiency through conditional distributions and factorisation, derives standard sufficient statistics, and proves the Rao–Blackwell theorem with a complete exponential example."
topics:
  - "sufficiency"
  - "factorisation theorem"
  - "Bernoulli"
  - "Poisson"
  - "exponential"
  - "uniform"
  - "Rao–Blackwell theorem"
previous: "lecture-03-existence-uniqueness-unbiased-estimators"
next: "lecture-05-completeness-standard-exponential-families"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-11"
status: "complete"
math: true
permalink: /notes/parametric-inference/lecture-04-sufficiency-rao-blackwell/
course_slug: parametric-inference
note_kind: lecture
course_order: 4
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Fall 2026 Parametric Inference lectures of Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata. The exposition includes additional definitions, derivations, and worked solutions. Any remaining errors belong to the note maintainer, not to the instructor or the Institute.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/parametric-inference/lecture-03-existence-uniqueness-unbiased-estimators/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture →]({{ '/notes/parametric-inference/lecture-05-completeness-standard-exponential-families/' | relative_url }})
</nav>

## Learning objectives

- State the definition of sufficiency and the Neyman–Fisher factorisation theorem.
- Find sufficient statistics in Bernoulli, Poisson, exponential, and uniform models.
- Prove the Rao–Blackwell theorem under squared-error loss.
- Compute a Rao–Blackwell improvement explicitly.

## 1. Definition

<div class="definition" markdown="1">

**Definition 4.1 — Sufficiency.**
A statistic $T=T(X)$ is _sufficient_ for $\theta$ if the conditional distribution of the full sample $X$, given $T$, does not depend on $\theta$.

</div>

Intuitively, once $T$ is known, the remaining variation in the sample contains no further information about the parameter.

## 2. Neyman–Fisher factorisation theorem

<div class="theorem" markdown="1">

**Theorem 4.2 — Factorisation criterion.**
Suppose the family has densities or mass functions $f_\theta(x)$ with respect to a common dominating measure. Then $T(X)$ is sufficient for $\theta$ if and only if there exist nonnegative functions $g_\theta$ and $h$ such that

$$
f_\theta(x)=g_\theta(T(x))h(x)
$$

for every $x$ and $\theta$, where $h$ does not depend on $\theta$.

</div>

The factorisation theorem is usually the fastest way to prove sufficiency.

## 3. Bernoulli sample

### Worked Example 4.1 — The total number of successes is sufficient

**Problem.**

For an iid Bernoulli sample, prove that $S=\sum_iX_i$ is sufficient, both by factorisation and directly from the conditional distribution.

**Solution.**

Let

$$
X_1,\dots,X_n\overset{\mathrm{iid}}{\sim}\operatorname{Bernoulli}(\theta),
\qquad 0<\theta<1,
$$

and define

$$
S=\sum_{i=1}^nX_i.
$$

The joint mass function is

$$
f_\theta(x_1,\dots,x_n)
=\prod_{i=1}^n\theta^{x_i}(1-\theta)^{1-x_i}
=\theta^{\sum x_i}(1-\theta)^{n-\sum x_i}.
$$

Thus

$$
f_\theta(x)=g_\theta(S(x))h(x),
$$

where

$$
g_\theta(s)=\theta^s(1-\theta)^{n-s},
\qquad h(x)=1.
$$

Hence $S$ is sufficient.\*

\*We can also verify the conditional definition. If $x_i\in\lbrace 0,1 \rbrace$ and $\sum x_i=t$, then

$$
\begin{aligned}
\mathbb{P}_\theta(X=x\mid S=t)
&=\frac{\mathbb{P}_\theta(X=x)}{\mathbb{P}_\theta(S=t)}\\
&=\frac{\theta^t(1-\theta)^{n-t}}
{\binom nt\theta^t(1-\theta)^{n-t}}\\
&=\frac1{\binom nt},
\end{aligned}
$$

which is independent of $\theta$. If $\sum x_i\ne t$, the conditional probability is zero.

**Final result.**

$S=\sum_iX_i$ is sufficient, and conditional on $S=t$ each binary sequence with $t$ successes has probability $1/\binom nt$, independent of $\theta$.

## 4. Poisson sample

### Worked Example 4.2 — The total count is sufficient

**Problem.**

For an iid Poisson sample, prove that $S=\sum_iX_i$ is sufficient and identify the conditional distribution of the sample given $S=t$.

**Solution.**

Let

$$
X_1,\dots,X_n\overset{\mathrm{iid}}{\sim}\operatorname{Poisson}(\theta)
$$

and let $S=\sum_iX_i$. The joint mass function is

$$
\begin{aligned}
f_\theta(x_1,\dots,x_n)
&=\prod_{i=1}^n e^{-\theta}\frac{\theta^{x_i}}{x_i!}\\
&=e^{-n\theta}\theta^{\sum x_i}\frac1{x_1!\cdots x_n!}.
\end{aligned}
$$

By factorisation, $S$ is sufficient.\*

\*Since $S\sim\operatorname{Poisson}(n\theta)$, for nonnegative integers $x_1,\dots,x_n$ with $\sum x_i=t$,

$$
\begin{aligned}
\mathbb{P}_\theta(X=x\mid S=t)
&=\frac{e^{-n\theta}\theta^t/(x_1!\cdots x_n!)}
{e^{-n\theta}(n\theta)^t/t!}\\
&=\frac{t!}{x_1!\cdots x_n!}\left(\frac1n\right)^t.
\end{aligned}
$$

This is the multinomial mass function with cell probabilities $1/n,\dots,1/n$, and it is free of $\theta$.

**Final result.**

$S$ is sufficient; conditional on $S=t$, $(X_1,\ldots,X_n)$ is multinomial with total $t$ and cell probabilities $1/n,\ldots,1/n$.

## 5. Exponential sample

### Worked Example 4.3 — The sum is sufficient

**Problem.**

For iid exponential observations with mean $\theta$, prove that their sum is sufficient and interpret the conditional distribution after normalisation by the sum.

**Solution.**

Let

$$
X_1,\dots,X_n\overset{\mathrm{iid}}{\sim}\operatorname{Exp}(\text{mean }\theta).
$$

The joint density is

$$
\begin{aligned}
f_\theta(x_1,\dots,x_n)
&=\prod_{i=1}^n\frac1\theta e^{-x_i/\theta}\mathbf{1}_{(0,\infty)}(x_i)\\
&=\theta^{-n}\exp\left(-\frac{\sum_i x_i}{\theta}\right)
\prod_{i=1}^n\mathbf{1}_{(0,\infty)}(x_i).
\end{aligned}
$$

Therefore

$$
S=\sum_{i=1}^nX_i
$$

is sufficient by the factorisation theorem.\*

\*More explicitly, conditional on $S=s$, the vector

$$
\left(\frac{X_1}{S},\dots,\frac{X_n}{S}\right)
$$

has the $\operatorname{Dirichlet}(1,\dots,1)$ distribution, which does not involve $\theta$. Thus the proportions describe how the total is split, while all information about the scale $\theta$ is contained in $S$.

**Final result.**

$S=\sum_iX_i$ is sufficient; conditional on $S$, the proportions $(X_1/S,\ldots,X_n/S)$ have a $\operatorname{Dirichlet}(1,\ldots,1)$ law independent of $\theta$.

## 6. Uniform sample

### Worked Example 4.4 — The sample maximum is sufficient

**Problem.**

For iid $\operatorname{Uniform}(0,\theta)$ observations, prove that the sample maximum is sufficient.

**Solution.**

Let

$$
X_1,\dots,X_n\overset{\mathrm{iid}}{\sim}\operatorname{Uniform}(0,\theta),
\qquad \theta>0.
$$

The joint density is

$$
f_\theta(x)
=\theta^{-n}\prod_{i=1}^n\mathbf{1}_{(0,\theta)}(x_i)
=\theta^{-n}\mathbf{1}\lbrace 0<x_{(1)},\ x_{(n)}<\theta \rbrace.
$$

This can be written as

$$
f_\theta(x)
=\underbrace{\theta^{-n}\mathbf{1}\lbrace x_{(n)}<\theta \rbrace}_{g_\theta(x_{(n)})}
\underbrace{\mathbf{1}\lbrace x_{(1)}>0 \rbrace}_{h(x)}.
$$

Hence the sample maximum $X_{(n)}$ is sufficient for $\theta$.

**Final result.**

$X_{(n)}$ is sufficient for the endpoint parameter $\theta$.

## 7. Rao–Blackwell theorem and variance improvement

<div class="theorem" markdown="1">

**Theorem 4.3 — Rao–Blackwell.**
Let $S$ be sufficient for $\theta$, and let $U$ be an estimator with finite second moment. Define

$$
U^*=\operatorname{E}_\theta[U\mid S].
$$

Because $S$ is sufficient, $U^*$ can be chosen as a function of $S$ that does not depend on $\theta$. Then:\*

1.  $\operatorname{E}_\theta[U^*]=\operatorname{E}_\theta[U]$;

2.  under squared-error loss,

$$
\operatorname{MSE}_\theta(U^*)\le \operatorname{MSE}_\theta(U);
$$

3.  if $U$ is unbiased, then $U^*$ is unbiased and

$$
\operatorname{Var}_\theta(U^*)\le \operatorname{Var}_\theta(U).
$$

\*Equality in the variance statement holds if and only if $U$ is already a function of $S$, almost surely.

</div>

**Proof.**

The expectation statement follows from iterated expectation:

$$
\operatorname{E}_\theta[U^*]
=\operatorname{E}_\theta\bigl[\operatorname{E}_\theta[U\mid S]\bigr]
=\operatorname{E}_\theta[U].
$$

For squared error, condition on $S$:

$$
\begin{aligned}
\operatorname{E}_\theta[(U-a)^2\mid S]
&=\operatorname{Var}_\theta(U\mid S)+\bigl(\operatorname{E}_\theta[U\mid S]-a\bigr)^2\\
&=\operatorname{Var}_\theta(U\mid S)+(U^*-a)^2.
\end{aligned}
$$

Taking expectations yields

$$
\operatorname{MSE}_\theta(U)
=\operatorname{E}_\theta[\operatorname{Var}_\theta(U\mid S)]+\operatorname{MSE}_\theta(U^*)
\ge \operatorname{MSE}_\theta(U^*).
$$

For unbiased estimators, MSE equals variance. Equality holds exactly when $\operatorname{Var}(U\mid S)=0$, i.e. when $U$ is almost surely a function of $S$.

$\square$

### Worked Example 4.5 — Rao–Blackwellising the first exponential observation

**Problem.**

Work through the source example “Rao–Blackwellising $X_1$ in the exponential model” in full.

**Solution.**

Let $X_1,\dots,X_n$ be iid exponential with mean $\theta$, and let $S=\sum_iX_i$. Since $X_1$ is unbiased for $\theta$, Rao–Blackwell gives

$$
\operatorname{E}[X_1\mid S].
$$

By exchangeability,

$$
\operatorname{E}[X_1\mid S]=\cdots=\operatorname{E}[X_n\mid S].
$$

Summing these conditional expectations,

$$
\sum_{i=1}^n\operatorname{E}[X_i\mid S]
=\operatorname{E}[S\mid S]=S.
$$

Therefore each term equals $S/n$, so

$$
\operatorname{E}[X_1\mid S]=\frac Sn=\overline X.
$$

Thus $\overline X$ is the Rao–Blackwell improvement of $X_1$, and

$$
\operatorname{Var}(\overline X)=\frac{\theta^2}{n}<\theta^2=\operatorname{Var}(X_1)
\qquad(n>1).
$$

**Final result.**

The conclusion is the final result derived in the solution above.

## Questions answered in this lecture

**Question.**

What does it mean for a statistic to contain all information about the parameter?

**Answer.**

Formally, the conditional law of the full sample given the statistic must be free of the parameter.

**Question.**

Why is $\sum_i X_i$ sufficient for Bernoulli and Poisson samples?

**Answer.**

Their joint mass functions factor into a parameter-dependent term involving the sample only through the total and a parameter-free remainder.

**Question.**

Why is the maximum sufficient for $\operatorname{Uniform}(0,\theta)$?

**Answer.**

The parameter enters the joint density only through $\theta^{-n}\mathbf 1\lbrace X_{(n)}<\theta \rbrace$ once positivity of the observations is separated into the parameter-free factor.

**Question.**

Why does Rao-Blackwellisation preserve unbiasedness?

**Answer.**

By the tower property, $\operatorname{E}[\operatorname{E}(U\mid S)]=\operatorname{E}[U]$.

**Question.**

When is there no variance improvement?

**Answer.**

Exactly when the original estimator is already almost surely a function of the sufficient statistic.

**Question.**

Why is $\operatorname{E}[X_1\mid S]=S/n$ in the exponential sample?

**Answer.**

Exchangeability makes all $\operatorname{E}[X_i\mid S]$ equal, and their sum is $\operatorname{E}[S\mid S]=S$.

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.
- Expanded source: the complete LaTeX notes and compiled PDF used for this Markdown conversion.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/parametric-inference/lecture-03-existence-uniqueness-unbiased-estimators/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture →]({{ '/notes/parametric-inference/lecture-05-completeness-standard-exponential-families/' | relative_url }})
</nav>

</div>
