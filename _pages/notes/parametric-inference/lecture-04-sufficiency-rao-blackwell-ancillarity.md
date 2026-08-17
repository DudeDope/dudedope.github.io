---
layout: page
title: "Lecture 4: Sufficiency, Rao–Blackwell Improvement, and Ancillary Statistics"
short_title: "Sufficiency and ancillarity"
course: "Parametric Inference"
lecture: 4
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Develops sufficiency and the factorisation theorem, proves Rao–Blackwell improvement, and studies ancillary statistics and non-completeness through normal, beta, Cauchy, and uniform examples."
topics:
  - "sufficiency"
  - "factorisation theorem"
  - "Rao–Blackwell theorem"
  - "ancillary statistics"
  - "normal and uniform examples"
  - "Cauchy location"
previous: "lecture-03-existence-uniqueness-unbiased-estimators"
next: "lecture-05-completeness-exponential-families-basu"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-17"
status: "complete"
math: true
permalink: /notes/parametric-inference/lecture-04-sufficiency-rao-blackwell-ancillarity/
course_slug: parametric-inference
note_kind: lecture
course_order: 4
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Fall 2026 Parametric Inference lectures of Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata. Additional exposition and any remaining errors are the responsibility of the note author.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-03-existence-uniqueness-unbiased-estimators/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-05-completeness-exponential-families-basu/' | relative_url }})
</nav>

## Learning objectives

<div class="intuition" markdown="1">

**Additional context.**
This section was added to make the lecture easier to use as a self-contained study note.

</div>

- State the definition of sufficiency and the Neyman–Fisher factorisation theorem.
- Find sufficient statistics in Bernoulli, Poisson, exponential, and uniform models.
- Prove the Rao–Blackwell theorem under squared-error loss.
- Compute Rao–Blackwell improvements explicitly.
- Define ancillarity and use ancillary functions to prove non-completeness.
- Find sufficient statistics in normal, beta, Cauchy, and translated-uniform models.

## 1. Definition

<div class="definition" markdown="1">

**Definition 4.1 — Sufficiency.**

A statistic \\(T=T(X)\\) is _sufficient_ for \\(\theta\\) if the conditional distribution of the full sample \\(X\\), given \\(T\\), does not depend on \\(\theta\\).

</div>

Intuitively, once \\(T\\) is known, the remaining variation in the sample contains no further information about the parameter.

## 2. Neyman–Fisher factorisation theorem

<div class="theorem" markdown="1">

**Theorem 4.2 — Factorisation criterion.**

Suppose the family has densities or mass functions \\(f\_\theta(x)\\) with respect to a common dominating measure. Then \\(T(X)\\) is sufficient for \\(\theta\\) if and only if there exist nonnegative functions \\(g\_\theta\\) and \\(h\\) such that

$$
f_\theta(x)=g_\theta(T(x))h(x)
$$

for every \\(x\\) and \\(\theta\\), where \\(h\\) does not depend on \\(\theta\\).

</div>

The factorisation theorem is usually the fastest way to prove sufficiency.

## 3. Bernoulli sample

### Worked Example 4.1 — The total number of successes is sufficient

**Problem.**

For an iid Bernoulli sample, prove that \\(S=\sum_iX_i\\) is sufficient, both by factorisation and directly from the conditional distribution.

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

Hence \\(S\\) is sufficient.

We can also verify the conditional definition. If \\(x_i\in\lbrace 0,1\rbrace \\) and \\(\sum x_i=t\\), then

$$
\begin{aligned}
\mathbb{P}_\theta(X=x\mid S=t)
&=\frac{\mathbb{P}_\theta(X=x)}{\mathbb{P}_\theta(S=t)}\\
&=\frac{\theta^t(1-\theta)^{n-t}}
{\binom nt\theta^t(1-\theta)^{n-t}}\\
&=\frac1{\binom nt},
\end{aligned}
$$

which is independent of \\(\theta\\). If \\(\sum x_i\ne t\\), the conditional probability is zero.

**Final result.**

\\(S=\sum_iX_i\\) is sufficient, and conditional on \\(S=t\\) each binary sequence with \\(t\\) successes has probability \\(1/\binom nt\\), independent of \\(\theta\\).

## 4. Poisson sample

### Worked Example 4.2 — The total count is sufficient

**Problem.**

For an iid Poisson sample, prove that \\(S=\sum_iX_i\\) is sufficient and identify the conditional distribution of the sample given \\(S=t\\).

**Solution.**

Let

$$
X_1,\dots,X_n\overset{\mathrm{iid}}{\sim}\operatorname{Poisson}(\theta)
$$

and let \\(S=\sum_iX_i\\). The joint mass function is

$$
\begin{aligned}
f_\theta(x_1,\dots,x_n)
&=\prod_{i=1}^n e^{-\theta}\frac{\theta^{x_i}}{x_i!}\\
&=e^{-n\theta}\theta^{\sum x_i}\frac1{x_1!\cdots x_n!}.
\end{aligned}
$$

By factorisation, \\(S\\) is sufficient.

Since \\(S\sim\operatorname{Poisson}(n\theta)\\), for nonnegative integers \\(x_1,\dots,x_n\\) with \\(\sum x_i=t\\),

$$
\begin{aligned}
\mathbb{P}_\theta(X=x\mid S=t)
&=\frac{e^{-n\theta}\theta^t/(x_1!\cdots x_n!)}
{e^{-n\theta}(n\theta)^t/t!}\\
&=\frac{t!}{x_1!\cdots x_n!}\left(\frac1n\right)^t.
\end{aligned}
$$

This is the multinomial mass function with cell probabilities \\(1/n,\dots,1/n\\), and it is free of \\(\theta\\).

**Final result.**

\\(S\\) is sufficient; conditional on \\(S=t\\), \\((X_1,\ldots,X_n)\\) is multinomial with total \\(t\\) and cell probabilities \\(1/n,\ldots,1/n\\).

## 5. Exponential sample

### Worked Example 4.3 — The sum is sufficient

**Problem.**

For iid exponential observations with mean \\(\theta\\), prove that their sum is sufficient and interpret the conditional distribution after normalisation by the sum.

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

is sufficient by the factorisation theorem.

More explicitly, conditional on \\(S=s\\), the vector

$$
\left(\frac{X_1}{S},\dots,\frac{X_n}{S}\right)
$$

has the \\(\operatorname{Dirichlet}(1,\dots,1)\\) distribution, which does not involve \\(\theta\\). Thus the proportions describe how the total is split, while all information about the scale \\(\theta\\) is contained in \\(S\\).

**Final result.**

\\(S=\sum_iX_i\\) is sufficient; conditional on \\(S\\), the proportions \\((X_1/S,\ldots,X_n/S)\\) have a \\(\operatorname{Dirichlet}(1,\ldots,1)\\) law independent of \\(\theta\\).

## 6. Uniform sample

### Worked Example 4.4 — The sample maximum is sufficient

**Problem.**

For iid \\(\operatorname{Uniform}(0,\theta)\\) observations, prove that the sample maximum is sufficient.

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
=\theta^{-n}\mathbf{1}\lbrace 0<x_{(1)},\ x_{(n)}<\theta\rbrace .
$$

This can be written as

$$
f_\theta(x)
=\underbrace{\theta^{-n}\mathbf{1}\lbrace x_{(n)}<\theta\rbrace }_{g_\theta(x_{(n)})}
\underbrace{\mathbf{1}\lbrace x_{(1)}>0\rbrace }_{h(x)}.
$$

Hence the sample maximum \\(X\_{(n)}\\) is sufficient for \\(\theta\\).

**Final result.**

\\(X\_{(n)}\\) is sufficient for the endpoint parameter \\(\theta\\).

## 7. Rao–Blackwell theorem and variance improvement

<div class="theorem" markdown="1">

**Theorem 4.3 — Rao–Blackwell.**

Let \\(S\\) be sufficient for \\(\theta\\), and let \\(U\\) be an estimator with finite second moment. Define

$$
U^{\ast}=\operatorname{E}_\theta[U\mid S].
$$

Because \\(S\\) is sufficient, \\(U^{\ast}\\) can be chosen as a function of \\(S\\) that does not depend on \\(\theta\\). Then:

1.  \\(\operatorname{E}\_\theta[U^{\ast}]=\operatorname{E}\_\theta[U]\\);

2.  under squared-error loss,

$$
\operatorname{MSE}_\theta(U^{\ast})\le \operatorname{MSE}_\theta(U);
$$

3.  if \\(U\\) is unbiased, then \\(U^{\ast}\\) is unbiased and

$$
\operatorname{Var}_\theta(U^{\ast})\le \operatorname{Var}_\theta(U).
$$

Equality in the variance statement holds if and only if \\(U\\) is already a function of \\(S\\), almost surely.

</div>

**Proof.**

The expectation statement follows from iterated expectation:

$$
\operatorname{E}_\theta[U^{\ast}]
=\operatorname{E}_\theta\bigl[\operatorname{E}_\theta[U\mid S]\bigr]
=\operatorname{E}_\theta[U].
$$

For squared error, condition on \\(S\\):

$$
\begin{aligned}
\operatorname{E}_\theta[(U-a)^2\mid S]
&=\operatorname{Var}_\theta(U\mid S)+\bigl(\operatorname{E}_\theta[U\mid S]-a\bigr)^2\\
&=\operatorname{Var}_\theta(U\mid S)+(U^{\ast}-a)^2.
\end{aligned}
$$

Taking expectations yields

$$
\operatorname{MSE}_\theta(U)
=\operatorname{E}_\theta[\operatorname{Var}_\theta(U\mid S)]+\operatorname{MSE}_\theta(U^{\ast})
\ge \operatorname{MSE}_\theta(U^{\ast}).
$$

For unbiased estimators, MSE equals variance. Equality holds exactly when \\(\operatorname{Var}(U\mid S)=0\\), i.e. when \\(U\\) is almost surely a function of \\(S\\).

\\(\square\\)

### Worked Example 4.5 — Rao–Blackwellising \\(X_1\\) in the exponential model

**Problem.**

Work through the source example “Rao–Blackwellising \\(X_1\\) in the exponential model” in full.

**Solution.**

Let \\(X_1,\dots,X_n\\) be iid exponential with mean \\(\theta\\), and let \\(S=\sum_iX_i\\). Since \\(X_1\\) is unbiased for \\(\theta\\), Rao–Blackwell gives

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

Therefore each term equals \\(S/n\\), so

$$
\operatorname{E}[X_1\mid S]=\frac Sn=\overline X.
$$

Thus \\(\overline X\\) is the Rao–Blackwell improvement of \\(X_1\\), and

$$
\operatorname{Var}(\overline X)=\frac{\theta^2}{n}<\theta^2=\operatorname{Var}(X_1)
\qquad(n>1).
$$

**Final result.**

The conclusion is the final result derived in the solution above.

## 8. Further factorisation examples

The new handwritten pages add several examples in which the sufficient statistic is not merely a sum.

### Worked Example 4.6 — Normal location with known variance

Let

$$
X_1,\ldots,X_n
\overset{\mathrm{iid}}{\sim}
N(\theta,1).
$$

The joint density is

$$
\begin{aligned}
f_\theta(x_1,\ldots,x_n)
&=
(2\pi)^{-n/2}
\exp\left\lbrace -\frac12\sum_{i=1}^n(x_i-\theta)^2
\right\rbrace \\
&=
(2\pi)^{-n/2}
\exp\left\lbrace -\frac12\sum_{i=1}^n x_i^2
\right\rbrace \exp\left\lbrace \theta\sum_{i=1}^n x_i-\frac n2\theta^2
\right\rbrace .
\end{aligned}
$$

The first factor is free of \\(\theta\\), and the second depends on the sample only through

$$
S=\sum_{i=1}^nX_i.
$$

Hence \\(S\\), and equivalently \\(\bar X=S/n\\), is sufficient for \\(\theta\\).

### Worked Example 4.7 — A two-parameter beta family

Suppose

$$
X_1,\ldots,X_n
\overset{\mathrm{iid}}{\sim}
\operatorname{Beta}(\theta,d),
\qquad
\theta>0,\ d>0,
$$

with density

$$
f(x\mid\theta,d)
=
\frac{x^{\theta-1}(1-x)^{d-1}}
{B(\theta,d)}
\mathbf 1_{(0,1)}(x).
$$

The joint density is

$$
\begin{aligned}
f_{\theta,d}(x)
&=
B(\theta,d)^{-n}
\left(\prod_{i=1}^n x_i\right)^{\theta-1}
\left(\prod_{i=1}^n(1-x_i)\right)^{d-1}
\prod_{i=1}^n\mathbf 1_{(0,1)}(x_i).
\end{aligned}
$$

Therefore

$$
\boxed{
S(X)=
\left(
\prod_{i=1}^nX_i,\,
\prod_{i=1}^n(1-X_i)
\right)
}
$$

is sufficient for \\((\theta,d)\\).

Because \\(0<X_i<1\\) almost surely, the one-to-one logarithmic transformation gives the equivalent sufficient statistic

$$
\boxed{
\left(
\sum_{i=1}^n\log X_i,\,
\sum_{i=1}^n\log(1-X_i)
\right).
}
$$

<div class="remark" markdown="1">

**Remark.**
Sufficiency is preserved under one-to-one transformations of a statistic.

</div>

## 9. Ancillary statistics and a first non-completeness argument

<div class="definition" markdown="1">

**Definition 4.4 — Ancillary statistic.**
A statistic \\(A=A(X)\\) is _ancillary_ for \\(\theta\\) if its distribution does not depend on \\(\theta\\).

</div>

Ancillarity and sufficiency describe different ideas. A sufficient statistic retains all parameter information in the sample, while an ancillary statistic has a parameter-free distribution.

### Worked Example 4.8 — Cauchy location: sufficient but not complete

Let

$$
X_1,\ldots,X_n
\overset{\mathrm{iid}}{\sim}
\operatorname{Cauchy}(\theta,1),
\qquad
f_\theta(x)=\frac1{\pi\lbrace 1+(x-\theta)^2\rbrace }.
$$

Because the joint density is symmetric in the observations, it can be written as a function of the ordered sample

$$
S=(X_{(1)},\ldots,X_{(n)}).
$$

Thus the full vector of order statistics is sufficient. This is a valid sufficient statistic, although it does not reduce the dimension of the data.

Now consider the range

$$
R=X_{(n)}-X_{(1)}.
$$

Write \\(X_i=\theta+Z_i\\) with \\(Z_i\sim\operatorname{Cauchy}(0,1)\\). Then

$$
R
=
Z_{(n)}-Z_{(1)},
$$

so the distribution of \\(R\\) is independent of \\(\theta\\). Hence \\(R\\) is ancillary.

Choose any \\(c\\) such that

$$
0<\Pr(R\le c)<1,
$$

and define

$$
g(S)
=
\mathbf 1_{\lbrace R\le c\rbrace }-\Pr(R\le c).
$$

Then \\(g(S)\\) is bounded, not almost surely zero, and

$$
\operatorname{E}_\theta[g(S)]=0
\qquad\text{for every }\theta.
$$

Therefore the sufficient statistic \\(S\\) is **not complete**.

This is the basic pattern behind many non-completeness proofs: find a nonconstant ancillary function of the proposed sufficient statistic and centre it to have expectation zero.

### Worked Example 4.9 — Uniform location family and Rao–Blackwell improvement

Let

$$
X_1,\ldots,X_n
\overset{\mathrm{iid}}{\sim}
\operatorname{Uniform}(\theta,\theta+1),
\qquad
\theta\in\mathbb R,
\qquad n\ge2.
$$

The joint density is

$$
\prod_{i=1}^n
\mathbf 1_{\lbrace \theta\le x_i\le\theta+1\rbrace }
=
\mathbf 1_{\lbrace \theta\le X_{(1)}\rbrace }
\mathbf 1_{\lbrace X_{(n)}\le\theta+1\rbrace }.
$$

Hence

$$
S=(X_{(1)},X_{(n)})
$$

is sufficient by factorisation.

The range

$$
R=X_{(n)}-X_{(1)}
$$

is unchanged by translating every observation by \\(\theta\\), so its distribution does not depend on \\(\theta\\). Consequently \\(R\\) is ancillary. Since \\(R\\) is a nonconstant function of \\(S\\), the statistic \\(S\\) cannot be complete.

Because

$$
\operatorname{E}_\theta[\bar X]
=
\theta+\frac12,
$$

the estimator

$$
\bar X-\frac12
$$

is unbiased for \\(\theta\\).

Rao–Blackwellising with respect to \\(S\\) gives

$$
\operatorname{E}_\theta\!\left[
\bar X-\frac12
\middle\vert
X_{(1)},X_{(n)}
\right].
$$

Conditional on \\(X\_{(1)}=a\\) and \\(X\_{(n)}=b\\), each of the remaining \\(n-2\\) observations has conditional mean \\((a+b)/2\\). Therefore

$$
\begin{aligned}
\operatorname{E}[\bar X\mid a,b]
&=
\frac1n
\left[
a+b+(n-2)\frac{a+b}{2}
\right]\\
&=
\frac{a+b}{2}.
\end{aligned}
$$

Thus the Rao–Blackwell improvement is

$$
\boxed{
\frac{X_{(1)}+X_{(n)}}2-\frac12.
}
$$

It is unbiased and has variance no larger than that of \\(\bar X-\tfrac12\\).

<div class="remark" markdown="1">

**Editorial note.**
The handwritten page writes \\((X\_{(1)}+X\_{(n)})/2\\) as the improved estimator of \\(\theta\\). Its expectation is \\(\theta+\tfrac12\\), so the required \\(-\tfrac12\\) term must be retained when the target is \\(\theta\\).

</div>

<div class="remark" markdown="1">

**Remark.**
The fact that \\(S\\) is sufficient but not complete does not prevent Rao–Blackwell improvement. Completeness becomes crucial when one wants uniqueness and the Lehmann–Scheffé conclusion.

</div>

## Questions answered in this lecture

**Question.**
What does it mean for a statistic to contain all information about the parameter?

**Answer.**

Formally, the conditional law of the full sample given the statistic must be free of the parameter.

**Question.**
Why is \\(\sum_i X_i\\) sufficient for Bernoulli and Poisson samples?

**Answer.**

Their joint mass functions factor into a parameter-dependent term involving the sample only through the total and a parameter-free remainder.

**Question.**
Why is the maximum sufficient for \\(\operatorname{Uniform}(0,\theta)\\)?

**Answer.**

The parameter enters the joint density only through \\(\theta^{-n}\mathbf 1\lbrace X\_{(n)}<\theta\rbrace \\) once positivity of the observations is separated into the parameter-free factor.

**Question.**
Why does Rao-Blackwellisation preserve unbiasedness?

**Answer.**

By the tower property, \\(\operatorname{E}[\operatorname{E}(U\mid S)]=\operatorname{E}[U]\\).

**Question.**
When is there no variance improvement?

**Answer.**

Exactly when the original estimator is already almost surely a function of the sufficient statistic.

**Question.**
Why is \\(\operatorname{E}[X\_1\mid S]=S/n\\) in the exponential sample?

**Answer.**

Exchangeability makes all \\(\operatorname{E}[X\_i\mid S]\\) equal, and their sum is \\(\operatorname{E}[S\mid S]=S\\).

**Question.**
How can an ancillary statistic be used to show that a sufficient statistic is not complete?

**Answer.**

If a nonconstant ancillary statistic \\(A\\) is a function of a sufficient statistic \\(S\\), choose a bounded nonconstant function \\(h(A)\\) and subtract its parameter-free expectation. This gives a nonzero function \\(g(S)\\) satisfying

$$
\operatorname{E}_\theta[g(S)]=0
$$

for every \\(\theta\\), contradicting completeness.

**Question.**
For \\(X_i\sim\operatorname{Uniform}(\theta,\theta+1)\\), what is the Rao–Blackwell improvement of \\(\bar X-\tfrac12\\)?

**Answer.**

It is

$$
\frac{X_{(1)}+X_{(n)}}2-\frac12.
$$

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.
- Expanded source: the complete LaTeX notes and compiled PDF used for this Markdown conversion.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-03-existence-uniqueness-unbiased-estimators/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-05-completeness-exponential-families-basu/' | relative_url }})
</nav>

</div>
