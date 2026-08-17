---
layout: page
title: "Lecture 8: Bayesian Point Estimation, Conjugate Priors, Bayes Risk, and Generalized Bayes Rules"
short_title: "Bayesian point estimation"
course: "Parametric Inference"
lecture: 8
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Develops posterior distributions and conjugate families through beta-binomial, Poisson, normal, and Cauchy examples; proves posterior-mean optimality under squared-error loss; and studies Bayes risk, sufficiency, improper priors, and generalized Bayes rules."
topics:
  - "Bayesian inference"
  - "prior and posterior"
  - "conjugate priors"
  - "Cauchy reciprocal-polynomial conjugate family"
  - "Bayes estimator"
  - "Bayes risk"
  - "sufficiency"
  - "improper priors"
  - "generalized Bayes"
previous: "lecture-07-hypothesis-testing-likelihood-ratio"
next: null
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-17"
status: "complete"
math: true
permalink: /notes/parametric-inference/lecture-08-bayesian-inference-bayes-risk/
course_slug: parametric-inference
note_kind: lecture
course_order: 8
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Fall 2026 Parametric Inference lectures of Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata. Additional exposition and any remaining errors are the responsibility of the note author.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-07-hypothesis-testing-likelihood-ratio/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }})
</nav>

## Learning objectives

After this lecture, you should be able to:

- distinguish the likelihood, prior, marginal distribution, and posterior distribution;
- test whether a proposed prior family is conjugate by multiplying the likelihood and prior kernels and checking closure;
- derive the beta-binomial and normal-normal conjugate updates and compare two Poisson prior constructions;
- prove that reciprocal-polynomial densities form a conjugate family for the Cauchy location model;
- explain why the family of all proper densities is formally a conjugate family for every model, and why this fact is mathematically important but computationally uninformative;
- define frequentist risk and Bayes risk;
- prove that the posterior mean is the Bayes estimator under squared-error loss;
- show that the posterior depends on the data only through a sufficient statistic;
- understand why a proper-prior posterior mean cannot usually also be unbiased for every parameter value;
- work with an improper prior when it yields a proper posterior and identify the resulting generalized Bayes estimator.

## 1. Prior, likelihood, marginal distribution, and posterior

In Bayesian inference the parameter is assigned a probability distribution.

<div class="definition" markdown="1">

**Definition 8.1 — Prior distribution.**
A prior density or mass function \\(\pi(\theta)\\) represents the distribution assigned to \\(\theta\\) before observing the data.

</div>

Conditional on \\(\theta\\), the data have sampling density

$$
f(x\mid\theta).
$$

The joint density of \\((X,\theta)\\) is

$$
m(x,\theta)
=
f(x\mid\theta)\pi(\theta).
$$

The marginal density of the data is

$$
m(x)
=
\int_\Theta
f(x\mid\theta)\pi(\theta)\,\mathrm d\theta,
$$

whenever the integral exists.

<div class="definition" markdown="1">

**Definition 8.2 — Posterior distribution.**
Bayes' formula gives

$$
\pi(\theta\mid x)
=
\frac{
f(x\mid\theta)\pi(\theta)
}{
\int_\Theta
f(x\mid u)\pi(u)\,\mathrm du
}.
$$

</div>

Equivalently,

$$
\pi(\theta\mid x)
\propto
f(x\mid\theta)\pi(\theta),
$$

where the proportionality is with respect to \\(\theta\\).

## 2. Conjugate families and how to check them

<div class="definition" markdown="1">

**Definition 8.3 — Conjugate family.**

Fix a sampling model \\(f(x\mid\theta)\\). A family \\(\mathcal C\\) of prior distributions is called _conjugate_ for this model if, whenever

$$
\pi\in\mathcal C
$$

and the posterior is well defined, the posterior distribution also belongs to \\(\mathcal C\\).

</div>

The operational procedure is exactly the one repeatedly used in the handwritten notes:

1. write the likelihood kernel as a function of \\(\theta\\);
2. multiply it by the prior kernel;
3. collect all factors involving \\(\theta\\);
4. identify the resulting posterior kernel;
5. check whether it belongs to the same proposed family;
6. finally check that the posterior can be normalized to integrate or sum to \\(1\\).

Conjugacy is therefore a _closure property under Bayesian updating_. The family need not be unique, and a model can have many conjugate families of very different sizes.

### Worked Example 8.1 — Beta family for binomial data

**Problem.**

Let

$$
X\mid\theta
\sim
\operatorname{Binomial}(n,\theta),
\qquad
0<\theta<1,
$$

and suppose the prior is beta:

$$
\theta\sim\operatorname{Beta}(a,b),
\qquad
a,b>0.
$$

Show directly that the beta family is conjugate and obtain the posterior mean.

**Solution.**

The likelihood is

$$
f(x\mid\theta)
=
\binom{n}{x}
\theta^x(1-\theta)^{n-x}.
$$

The prior density is

$$
\pi(\theta)
=
\frac{1}{B(a,b)}
\theta^{a-1}(1-\theta)^{b-1}.
$$

Bayes' formula gives

$$
\begin{aligned}
\pi(\theta\mid x)
&\propto
f(x\mid\theta)\pi(\theta)\\
&\propto
\theta^x(1-\theta)^{n-x}
\theta^{a-1}(1-\theta)^{b-1}\\
&=
\theta^{a+x-1}
(1-\theta)^{b+n-x-1}.
\end{aligned}
$$

This is again a beta kernel. Hence

$$
\boxed{
\theta\mid X=x
\sim
\operatorname{Beta}(a+x,b+n-x).
}
$$

Therefore, under squared-error loss, the posterior-mean Bayes estimator is

$$
\boxed{
\delta_\pi(x)
=
\operatorname{E}[\theta\mid X=x]
=
\frac{a+x}{a+b+n}.
}
$$

For an iid Bernoulli sample \\(X_1,\ldots,X_n\\), write

$$
S=\sum_{i=1}^{n}X_i.
$$

Then

$$
\boxed{
\theta\mid X_1,\ldots,X_n
\sim
\operatorname{Beta}(a+S,b+n-S).
}
$$

**Final result.**

The beta family is closed under binomial/Bernoulli updating: the posterior parameters equal the prior parameters plus the observed success and failure counts.

### Worked Example 8.2 — The Poisson calculation in the source: checking a proposed prior family

The handwritten notes next consider

$$
X\mid\theta
\sim
\operatorname{Poisson}(\theta),
\qquad
\theta>0,
$$

so

$$
f(x\mid\theta)
=
\frac{e^{-\theta}\theta^x}{x!}.
$$

The prior factor written in the source has the kernel of an inverse-gamma-type density. The handwriting reuses the symbol \\(x\\) inside the prior, which conflicts with the observed count. To separate the two roles, write the prior hyperparameter as \\(c>0\\) and consider the kernel

$$
\pi(\theta)
\propto
\theta^{-\nu}
\exp\!\left(-\frac{c}{\theta}\right),
\qquad
\theta>0.
$$

For checking conjugacy, the normalizing constant is not needed. Multiplying likelihood and prior gives

$$
\begin{aligned}
\pi(\theta\mid x)
&\propto
\frac{e^{-\theta}\theta^x}{x!}
\theta^{-\nu}
\exp\!\left(-\frac{c}{\theta}\right)\\
&\propto
\theta^{x-\nu}
\exp\!\left(-\theta-\frac{c}{\theta}\right).
\end{aligned}
$$

The factor \\(e^{-\theta}\\) introduced by the Poisson likelihood remains in the posterior. Therefore the posterior is not of the original inverse-gamma form

$$
\theta^{-\nu'}
\exp\!\left(-\frac{c'}{\theta}\right).
$$

So the inverse-gamma family by itself is not conjugate for a Poisson mean.

<div class="intuition" markdown="1">

**Additional context.**
The posterior kernel

$$
\theta^{\lambda-1}
\exp\!\left[
-\frac{1}{2}
\left(
a\theta+\frac{b}{\theta}
\right)
\right],
\qquad
\theta>0,
$$

is of generalized-inverse-Gaussian type. Consider the larger collection of such kernels, with \\(a\ge0\\), \\(b\ge0\\), and \\(\lambda\\) restricted so that the kernel is integrable. Multiplication by a Poisson likelihood kernel gives

$$
\begin{aligned}
\theta^x e^{-\theta}
\theta^{\lambda-1}
\exp\!\left[
-\frac{1}{2}
\left(
a\theta+\frac{b}{\theta}
\right)
\right]
&=
\theta^{(\lambda+x)-1}
\exp\!\left[
-\frac{1}{2}
\left(
(a+2)\theta+\frac{b}{\theta}
\right)
\right].
\end{aligned}
$$

Thus the update is

$$
\boxed{
\lambda\mapsto\lambda+x,
\qquad
a\mapsto a+2,
\qquad
b\mapsto b.
}
$$

So the broader generalized-inverse-Gaussian-type family is closed under Poisson updating. The inverse-gamma-type prior used in the source is a boundary case with no linear \\(\theta\\) term before observing data; the Poisson likelihood creates that term in the posterior.

</div>

This example illustrates why the procedure “multiply first, then identify the posterior family” matters. A prior can be perfectly valid without being conjugate.

### Worked Example 8.3 — Gamma family for a Poisson mean

<div class="intuition" markdown="1">

**Additional context.**
A standard finite-dimensional conjugate family for the Poisson mean is the gamma family. It is useful to contrast it with the source's inverse-gamma-type trial above.

</div>

Let

$$
X_1,\ldots,X_n\mid\theta
\overset{\mathrm{iid}}{\sim}
\operatorname{Poisson}(\theta),
$$

and use the gamma prior in shape-rate parametrization,

$$
\theta\sim\operatorname{Gamma}(a,b),
\qquad
a,b>0,
$$

with density

$$
\pi(\theta)
=
\frac{b^a}{\Gamma(a)}
\theta^{a-1}e^{-b\theta}.
$$

Let

$$
S=\sum_{i=1}^{n}X_i.
$$

The likelihood kernel is

$$
L(\theta;x)
\propto
\theta^S e^{-n\theta}.
$$

Hence

$$
\begin{aligned}
\pi(\theta\mid x)
&\propto
\theta^S e^{-n\theta}
\theta^{a-1}e^{-b\theta}\\
&=
\theta^{a+S-1}
e^{-(b+n)\theta}.
\end{aligned}
$$

Therefore

$$
\boxed{
\theta\mid X
\sim
\operatorname{Gamma}(a+S,b+n).
}
$$

The posterior mean is

$$
\boxed{
\operatorname{E}[\theta\mid X]
=
\frac{a+S}{b+n}.
}
$$

### Worked Example 8.4 — Normal likelihood with normal prior

Suppose

$$
X\mid\theta
\sim
N(\theta,\sigma^2),
$$

where \\(\sigma^2\\) is known, and

$$
\theta\sim N(\mu,\tau^2).
$$

The posterior kernel is

$$
\pi(\theta\mid x)
\propto
\exp\left\lbrace
-\frac{(x-\theta)^2}{2\sigma^2}
-\frac{(\theta-\mu)^2}{2\tau^2}
\right\rbrace.
$$

Expand the quadratic terms:

$$
\begin{aligned}
\frac{(x-\theta)^2}{\sigma^2}
+
\frac{(\theta-\mu)^2}{\tau^2}
&=
\frac{x^2-2x\theta+\theta^2}{\sigma^2}
+
\frac{\theta^2-2\mu\theta+\mu^2}{\tau^2}\\
&=
\left(
\frac{1}{\sigma^2}
+
\frac{1}{\tau^2}
\right)\theta^2
-
2\left(
\frac{x}{\sigma^2}
+
\frac{\mu}{\tau^2}
\right)\theta\\
&\qquad+
\frac{x^2}{\sigma^2}
+
\frac{\mu^2}{\tau^2}.
\end{aligned}
$$

Define

$$
A
=
\frac{1}{\sigma^2}
+
\frac{1}{\tau^2},
\qquad
B
=
\frac{x}{\sigma^2}
+
\frac{\mu}{\tau^2}.
$$

Then

$$
A\theta^2-2B\theta
=
A\left(\theta-\frac{B}{A}\right)^2
-
\frac{B^2}{A}.
$$

Terms not involving \\(\theta\\) are absorbed into the normalizing constant. Therefore

$$
\boxed{
\theta\mid X=x
\sim
N(m,v),
}
$$

where

$$
\boxed{
v
=
\left(
\frac{1}{\sigma^2}
+
\frac{1}{\tau^2}
\right)^{-1},
\qquad
m
=
v\left(
\frac{x}{\sigma^2}
+
\frac{\mu}{\tau^2}
\right).
}
$$

Equivalently,

$$
m
=
\frac{x/\sigma^2+\mu/\tau^2}
{1/\sigma^2+1/\tau^2}.
$$

For \\(n\\) iid observations with known variance \\(\sigma^2\\),

$$
\boxed{
v_n
=
\frac{1}{n/\sigma^2+1/\tau^2},
\qquad
m_n
=
v_n
\left(
\frac{n\bar X}{\sigma^2}
+
\frac{\mu}{\tau^2}
\right).
}
$$

The posterior mean is a precision-weighted average of the sample mean and the prior mean.

## 3. Cauchy location model: the reciprocal-polynomial conjugate family

The handwritten notes explicitly ask:

**Question.**
Does the Cauchy location model have a conjugate family of priors?

**Answer.**

Yes. The notes construct one by considering densities of the form \\(1/p(\theta)\\), where \\(p\\) is a polynomial satisfying the conditions required for \\(1/p\\) to be a density.

Suppose

$$
X\mid\theta
\sim
\operatorname{Cauchy}(\theta,1),
$$

so

$$
f(x\mid\theta)
=
\frac{1}{\pi\left\lbrace 1+(x-\theta)^2\right\rbrace}.
$$

### 3.1 Conditions on the reciprocal-polynomial prior

Let \\(p\\) be a real polynomial satisfying

$$
p(\theta)>0
\qquad
\text{for every }\theta\in\mathbb R,
$$

and

$$
\int_{-\infty}^{\infty}
\frac{1}{p(\theta)}
\,\mathrm d\theta
=
1.
$$

Then

$$
\pi_p(\theta)
=
\frac{1}{p(\theta)}
$$

is a proper prior density.

Both conditions matter:

- \\(p(\theta)>0\\) guarantees nonnegativity and prevents poles on the real line;
- the integral condition guarantees that \\(1/p\\) has total mass \\(1\\).

Equivalently, one may begin with a strictly positive polynomial \\(p_0\\) for which

$$
0<
\int_{\mathbb R}\frac{1}{p_0(\theta)}\,\mathrm d\theta
<
\infty
$$

and then multiply \\(p_0\\) by the appropriate positive constant so that its reciprocal integrates to \\(1\\).

Define

$$
\mathcal C
=
\left\lbrace
\pi_p:
\pi_p(\theta)=\frac{1}{p(\theta)},
\;
p\text{ polynomial},
\;
p(\theta)>0,
\;
\int_{\mathbb R}\frac{1}{p(\theta)}\,\mathrm d\theta=1
\right\rbrace.
$$

### Worked Example 8.5 — Proving conjugacy for the Cauchy location likelihood

**Problem.**

Show that if \\(\pi_p\in\mathcal C\\), then after observing one Cauchy location observation, the posterior also belongs to \\(\mathcal C\\).

**Solution.**

Start from

$$
\pi_p(\theta)
=
\frac{1}{p(\theta)}.
$$

After observing \\(X=x\\),

$$
\begin{aligned}
f(x\mid\theta)\pi_p(\theta)
&=
\frac{1}{\pi\left\lbrace 1+(x-\theta)^2\right\rbrace}
\frac{1}{p(\theta)}\\
&=
\frac{1}
{\pi p(\theta)\left\lbrace 1+(x-\theta)^2\right\rbrace}.
\end{aligned}
$$

Let

$$
Z_p(x)
=
\int_{-\infty}^{\infty}
\frac{1}
{\pi p(u)\left\lbrace 1+(x-u)^2\right\rbrace}
\,\mathrm du.
$$

Since

$$
1+(x-u)^2\ge1,
$$

we have

$$
0<Z_p(x)
\le
\frac{1}{\pi}
\int_{-\infty}^{\infty}
\frac{1}{p(u)}
\,\mathrm du
=
\frac{1}{\pi}.
$$

Thus the posterior is proper. Normalizing,

$$
\pi_p(\theta\mid x)
=
\frac{1}
{\pi Z_p(x)\,
p(\theta)\left\lbrace 1+(x-\theta)^2\right\rbrace}.
$$

Define

$$
q_x(\theta)
=
\pi Z_p(x)\,
p(\theta)\left\lbrace 1+(x-\theta)^2\right\rbrace.
$$

Now verify the family conditions. First, \\(q_x\\) is a polynomial in \\(\theta\\). Second, \\(q_x(\theta)>0\\) for every real \\(\theta\\). Third, by construction,

$$
\int_{-\infty}^{\infty}
\frac{1}{q_x(\theta)}
\,\mathrm d\theta
=
1.
$$

Therefore

$$
\boxed{
\pi_p(\theta\mid x)
=
\frac{1}{q_x(\theta)}
\in
\mathcal C.
}
$$

Hence \\(\mathcal C\\) is conjugate.

For an iid sample \\(x_1,\ldots,x_n\\),

$$
L(\theta;x)
\propto
\prod_{i=1}^{n}
\frac{1}{1+(x_i-\theta)^2},
$$

so

$$
\pi_p(\theta\mid x_1,\ldots,x_n)
\propto
\frac{1}
{p(\theta)
\prod_{i=1}^{n}\left\lbrace 1+(x_i-\theta)^2\right\rbrace}.
$$

The denominator is again a strictly positive polynomial. After normalization, the posterior again has the form \\(1/q(\theta)\\) with reciprocal integral \\(1\\).

**Final result.**

$$
\boxed{
\mathcal C
=
\left\lbrace
\frac{1}{p(\theta)}:
p\text{ polynomial},
\;
p(\theta)>0,
\;
\int_{\mathbb R}\frac{1}{p(\theta)}\,\mathrm d\theta=1
\right\rbrace
}
$$

is a conjugate family for the Cauchy location model.

### 3.2 Why the ordinary Cauchy family is not closed

A single Cauchy density has a quadratic denominator. Multiplying one Cauchy prior by one Cauchy likelihood generally produces a reciprocal quartic polynomial, not another ordinary two-parameter Cauchy density.

So the ordinary location-scale Cauchy family is not conjugate. The reciprocal-polynomial family is conjugate because it allows the polynomial degree to increase after each update.

### 3.3 The family of all densities is always conjugate

The source notes also state the following fact explicitly.

<div class="proposition" markdown="1">

**Proposition 8.4 — Universal conjugate family.**

For any likelihood model, the family of all proper densities on the parameter space is a conjugate family, provided the posterior is proper.

</div>

**Proof.**

Let \\(\mathcal D\\) be the class of all proper densities on \\(\Theta\\). Choose any \\(\pi\in\mathcal D\\). If

$$
0<
m(x)
=
\int_\Theta
f(x\mid\theta)\pi(\theta)
\,\mathrm d\theta
<
\infty,
$$

then

$$
\pi(\theta\mid x)
=
\frac{f(x\mid\theta)\pi(\theta)}{m(x)}
$$

is itself a proper density on \\(\Theta\\). Therefore

$$
\pi(\cdot\mid x)\in\mathcal D.
$$

Hence \\(\mathcal D\\) is closed under Bayesian updating.

\\(\square\\)

This is not merely a remark: it clarifies what the word _conjugate_ can mean. If the family is allowed to be arbitrarily large, existence of a conjugate family is almost automatic. The statistically useful question is whether there is a smaller structured family whose posterior remains easy to identify and compute.

The beta-binomial, gamma-Poisson, and normal-normal examples give finite-dimensional conjugate families. The reciprocal-polynomial Cauchy construction gives a larger, non-fixed-dimensional but explicit conjugate family.

## 4. Frequentist risk and Bayes risk

For an estimator \\(\delta(X)\\) and loss \\(L(\theta,a)\\), the frequentist risk is

$$
R(\theta,\delta)
=
\operatorname{E}_\theta[
L(\theta,\delta(X))
].
$$

Under squared-error loss,

$$
L(\theta,a)=(a-\theta)^2,
$$

so

$$
R(\theta,\delta)
=
\operatorname{E}_\theta[
(\delta(X)-\theta)^2
].
$$

<div class="definition" markdown="1">

**Definition 8.5 — Bayes risk.**
For a proper prior \\(\pi\\),

$$
r_\pi(\delta)
=
\int_\Theta
R(\theta,\delta)\pi(\theta)\,\mathrm d\theta.
$$

</div>

Using the joint distribution of \\((X,\theta)\\),

$$
r_\pi(\delta)
=
\operatorname{E}_m[
L(\theta,\delta(X))
].
$$

A _Bayes rule_ is a decision rule that minimises \\(r\_\pi(\delta)\\).

## 5. Posterior mean minimises squared-error Bayes risk

<div class="theorem" markdown="1">

**Theorem 8.6 — Bayes estimator under squared-error loss.**
Assume

$$
\operatorname{E}[\theta^2\mid X]<\infty
$$

almost surely. Under squared-error loss, the Bayes estimator is

$$
\boxed{
\delta_\pi(X)
=
\operatorname{E}[\theta\mid X].
}
$$

</div>

**Proof.**

For any action \\(a\\) and fixed observed \\(X\\),

$$
\begin{aligned}
\operatorname{E}[
(a-\theta)^2
\mid X
]
&=
\operatorname{E}\left[
\lbrace a-\operatorname{E}(\theta\mid X)
+\operatorname{E}(\theta\mid X)-\theta\rbrace ^2
\middle\vert\, X
\right]\\
&=
\lbrace a-\operatorname{E}(\theta\mid X)\rbrace ^2
+
\operatorname{Var}(\theta\mid X),
\end{aligned}
$$

because the cross term has conditional expectation zero.

The second term does not depend on \\(a\\). Therefore the conditional expected loss is uniquely minimised at

$$
a=\operatorname{E}[\theta\mid X].
$$

Averaging over \\(X\\) shows that this rule also minimises the Bayes risk.

\\(\square\\)

The minimum Bayes risk is

$$
\boxed{
r_\pi(\delta_\pi)
=
\operatorname{E}[
\operatorname{Var}(\theta\mid X)
].
}
$$

This identity quantifies the posterior uncertainty that remains after observing the data.

## 6. Bayes and generalized Bayes rules are functions of sufficient statistics

The source notes explicitly ask whether a Bayes estimator must be a function of a sufficient statistic. The answer is yes. The same argument also applies to a generalized Bayes calculation whenever an improper prior kernel produces a proper posterior.

<div class="proposition" markdown="1">

**Proposition 8.7 — Sufficiency determines the posterior.**

Suppose \\(T(X)\\) is sufficient for \\(\theta\\), so that

$$
f(x\mid\theta)
=
g_\theta(T(x))h(x).
$$

Let \\(\pi(\theta)\\) be either

- a proper prior density, or
- a nonnegative improper prior kernel for which the posterior normalizing integral is finite and positive.

Then the posterior depends on \\(x\\) only through \\(T(x)\\). Consequently, every Bayes or generalized Bayes rule obtained from that posterior is a function of \\(T(X)\\).

</div>

**Proof.**

Bayes' formula gives

$$
\begin{aligned}
\pi(\theta\mid x)
&=
\frac{
g_\theta(T(x))h(x)\pi(\theta)
}{
\int_\Theta
g_u(T(x))h(x)\pi(u)
\,\mathrm du
}\\
&=
\frac{
g_\theta(T(x))\pi(\theta)
}{
\int_\Theta
g_u(T(x))\pi(u)
\,\mathrm du
}.
\end{aligned}
$$

The factor \\(h(x)\\), which contains the part of the sample not carrying information about \\(\theta\\), cancels. Therefore

$$
\boxed{
\pi(\theta\mid X)
=
\pi(\theta\mid T).
}
$$

Thus every posterior functional is a function of \\(T\\). In particular, under squared-error loss,

$$
\boxed{
\operatorname{E}[\theta\mid X]
=
\operatorname{E}[\theta\mid T].
}
$$

The cancellation argument only requires the posterior ratio to be well defined. It does not require the prior kernel itself to integrate to one, so the conclusion also applies to generalized Bayes rules whenever the formal posterior is proper.

\\(\square\\)

## 7. Can a posterior-mean Bayes estimator be unbiased?

The handwritten notes ask whether

$$
\delta_\pi(X)=\operatorname{E}[\theta\mid X]
$$

can also satisfy

$$
\operatorname{E}_\theta[\delta_\pi(X)]=\theta
$$

for every \\(\theta\\).

Under a proper prior and finite second moments, this can happen only in a degenerate situation.

<div class="proposition" markdown="1">

**Proposition 8.8 — Proper-prior posterior mean plus exact unbiasedness forces zero Bayes risk.**
Suppose \\(\pi\\) is proper,

$$
\operatorname{E}_\pi[\theta^2]<\infty,
$$

and

$$
\delta_\pi(X)=\operatorname{E}[\theta\mid X]
$$

is unbiased for \\(\theta\\) for every parameter value in the support of \\(\pi\\). Then

$$
\operatorname{E}_m[(\delta_\pi(X)-\theta)^2]=0.
$$

Hence

$$
\delta_\pi(X)=\theta
$$

almost surely under the joint model.

</div>

**Proof.**

First, by the defining property of conditional expectation,

$$
\begin{aligned}
\operatorname{E}_m[\delta_\pi(X)\theta]
&=
\operatorname{E}_m[
\delta_\pi(X)
\operatorname{E}(\theta\mid X)
]\\
&=
\operatorname{E}_m[\delta_\pi(X)^2].
\end{aligned}
$$

On the other hand, using unbiasedness and integrating over the prior,

$$
\begin{aligned}
\operatorname{E}_m[\delta_\pi(X)\theta]
&=
\int
\theta
\operatorname{E}_\theta[\delta_\pi(X)]
\pi(\theta)\,\mathrm d\theta\\
&=
\int\theta^2\pi(\theta)\,\mathrm d\theta\\
&=
\operatorname{E}_\pi[\theta^2].
\end{aligned}
$$

Thus

$$
\operatorname{E}_m[\delta_\pi(X)^2]
=
\operatorname{E}_\pi[\theta^2]
=
\operatorname{E}_m[\delta_\pi(X)\theta].
$$

Therefore

$$
\begin{aligned}
\operatorname{E}_m[(\delta_\pi(X)-\theta)^2]
&=
\operatorname{E}_m[\delta_\pi(X)^2]
+
\operatorname{E}_m[\theta^2]
-
2\operatorname{E}_m[\delta_\pi(X)\theta]\\
&=
0.
\end{aligned}
$$

A nonnegative random variable with expectation zero is zero almost surely, so

$$
\delta_\pi(X)=\theta
$$

almost surely.

\\(\square\\)

**Interpretation.**

In an ordinary noisy model, the data do not determine \\(\theta\\) exactly, so a proper-prior posterior mean is generally not exactly unbiased for every \\(\theta\\). This is not a defect: Bayesian estimators optimise integrated posterior/frequentist loss, not unbiasedness.

## 8. Improper priors and generalized Bayes estimators

<div class="definition" markdown="1">

**Definition 8.9 — Improper prior.**
A nonnegative function \\(\pi(\theta)\\) is called an improper prior if

$$
\int_\Theta\pi(\theta)\,\mathrm d\theta=\infty.
$$

It is not a probability density.

</div>

If the formal posterior

$$
\pi(\theta\mid x)
\propto
f(x\mid\theta)\pi(\theta)
$$

is nevertheless proper for almost every sample, one can still minimise posterior expected loss.

<div class="definition" markdown="1">

**Definition 8.10 — Generalized Bayes rule.**
A rule obtained by Bayesian posterior minimisation from an improper prior is called a generalized Bayes rule.

</div>

### Worked Example 8.6 — Flat prior for a normal mean: one observation and an iid sample

Let

$$
X\mid\theta
\sim
N(\theta,1),
\qquad
\theta\in\mathbb R,
$$

and use the flat improper prior

$$
\pi(\theta)\propto1.
$$

Then

$$
\pi(\theta\mid x)
\propto
\exp\left\lbrace -\frac12(x-\theta)^2
\right\rbrace ,
$$

which is the kernel of

$$
N(x,1).
$$

Hence the generalized Bayes estimator under squared-error loss is

$$
\boxed{
\delta(x)=x.
}
$$

For an iid sample

$$
X_1,\ldots,X_n\mid\theta
\overset{\mathrm{iid}}{\sim}
N(\theta,1),
$$

$$
\begin{aligned}
\pi(\theta\mid x)
&\propto
\exp\left\lbrace -\frac12\sum_{i=1}^n(x_i-\theta)^2
\right\rbrace \\
&\propto
\exp\left\lbrace -\frac n2(\theta-\bar x)^2
\right\rbrace .
\end{aligned}
$$

Thus

$$
\boxed{
\theta\mid x
\sim
N\left(\bar x,\frac1n\right)
}
$$

in the generalized Bayes calculation, and

$$
\boxed{
\delta(x)=\bar x.
}
$$

Notice that \\(\bar X\\) is unbiased. This does not contradict Proposition 8.8 because the flat prior is improper, so the proper-prior integrated-risk argument does not apply.

## 9. Bayes-risk decomposition

<div class="intuition" markdown="1">

**Additional context.**
The following identity is often the cleanest way to remember why posterior means are optimal.

</div>

For any estimator \\(\delta(X)\\),

$$
\begin{aligned}
r_\pi(\delta)
&=
\operatorname{E}[
(\delta(X)-\theta)^2
]\\
&=
\operatorname{E}[
\operatorname{Var}(\theta\mid X)
]
+
\operatorname{E}[
\lbrace \delta(X)-\operatorname{E}(\theta\mid X)\rbrace ^2
].
\end{aligned}
$$

Therefore

$$
\boxed{
r_\pi(\delta)
-
r_\pi(\delta_\pi)
=
\operatorname{E}[
\lbrace \delta(X)-\delta_\pi(X)\rbrace ^2
]
\ge0.
}
$$

The excess Bayes risk is exactly the mean squared distance from the posterior mean.

## 10. Relationship with earlier lectures

The same estimator can be evaluated under several different criteria:

- **unbiasedness:** \\(\operatorname{E}\_\theta[\delta(X)]=\theta\\) for every \\(\theta\\);
- **frequentist risk:** \\(R(\theta,\delta)\\) is compared pointwise in \\(\theta\\);
- **UMVUE:** minimum variance among unbiased estimators at every \\(\theta\\);
- **Bayes rule:** minimum integrated risk under a specified prior;
- **MLE:** maximises the likelihood for the observed sample.

None of these definitions is interchangeable with another.

The normal flat-prior example is particularly instructive:

$$
\bar X
$$

is simultaneously the MLE, unbiased estimator, UMVUE, and generalized Bayes estimator under squared-error loss. This coincidence is model-specific and should not be taken as a general theorem.

## Questions answered in this lecture

**Question.**
Why does a sufficient statistic contain everything needed for the posterior?

**Answer.**

Factorisation gives

$$
f(x\mid\theta)=g_\theta(T(x))h(x),
$$

and \\(h(x)\\) cancels from Bayes' formula. Hence the posterior depends on \\(x\\) only through \\(T(x)\\).

**Question.**
Why is the posterior mean the Bayes estimator under squared-error loss?

**Answer.**

Conditional squared error decomposes into posterior variance plus a nonnegative squared distance from the posterior mean.

**Question.**
Can a proper-prior posterior mean be unbiased for every \\(\theta\\)?

**Answer.**

Only in a degenerate situation where the Bayes risk is zero and the data determine \\(\theta\\) almost surely.

**Question.**
What is the difference between a Bayes estimator and a generalized Bayes estimator?

**Answer.**

A Bayes estimator uses a proper prior probability distribution. A generalized Bayes estimator is obtained from an improper prior when the resulting posterior calculation is still meaningful.

**Question.**
Is a generalized Bayes estimator also a function of a sufficient statistic?

**Answer.**

Yes, provided the improper prior kernel yields a proper posterior. The factorization

$$
f(x\mid\theta)=g_\theta(T(x))h(x)
$$

still causes \\(h(x)\\) to cancel from the formal posterior, so the posterior and every generalized Bayes rule derived from it depend on the sample only through \\(T(X)\\).

**Question.**
Does the Cauchy location model have a conjugate family?

**Answer.**

Yes. The source notes construct the reciprocal-polynomial family

$$
\pi_p(\theta)
=
\frac{1}{p(\theta)},
$$

where \\(p\\) is a strictly positive polynomial and \\(1/p\\) is normalized to integrate to \\(1\\). Multiplication by the Cauchy likelihood multiplies the denominator by another strictly positive quadratic polynomial, so the posterior remains in the same reciprocal-polynomial class.

**Question.**
Why is the family of all proper densities a conjugate family for every likelihood model?

**Answer.**

Because whenever a proper prior produces a proper posterior, that posterior is itself a proper density on the same parameter space. Therefore the class of all densities is closed under updating. The fact is formally important, but the family is usually too large to provide computational simplification.

**Question.**
What happens to the inverse-gamma-type prior kernel used in the source Poisson calculation?

**Answer.**

Multiplying

$$
\theta^{-\nu}
\exp\!\left(-\frac{c}{\theta}\right)
$$

by the Poisson likelihood kernel \\(\theta^x e^{-\theta}\\) gives

$$
\theta^{x-\nu}
\exp\!\left(-\theta-\frac{c}{\theta}\right).
$$

This is not inverse-gamma, so that smaller family is not conjugate. The resulting kernel belongs to the broader generalized inverse Gaussian class.

**Question.**
What conditions must be checked before \\(1/p(\theta)\\) can be used as a prior density?

**Answer.**

The source construction requires \\(p(\theta)>0\\) for every real \\(\theta\\) and

$$
\int_{\mathbb R}\frac{1}{p(\theta)}\,\mathrm d\theta
=
1.
$$

More generally, if the integral is finite and positive, a constant rescaling of \\(p\\) can normalize the reciprocal to a density.

## Lecture summary

The posterior is

$$
\pi(\theta\mid x)
\propto
f(x\mid\theta)\pi(\theta).
$$

Under squared-error loss,

$$
\boxed{
\delta_\pi(x)=\operatorname{E}[\theta\mid X=x]
}
$$

minimises both posterior expected loss and Bayes risk. If \\(T\\) is sufficient, the posterior and therefore every Bayes rule based on it are functions of \\(T\\).

Conjugate families are closed under Bayesian updating, but the family need not be unique. The beta-binomial, gamma-Poisson, and normal-normal examples are finite-dimensional conjugate families; the reciprocal-polynomial Cauchy construction is a larger conjugate family; and the class of all proper densities is the universal, formally conjugate family. Improper priors can lead to generalized Bayes rules, as in the flat-prior normal example.

## Review problems

1. Derive the beta posterior for \\(n\\) iid Bernoulli observations with \\(S\\) successes.
2. Starting from the inverse-gamma-type kernel \\(\theta^{-\nu}e^{-c/\theta}\\), multiply by a Poisson likelihood and identify exactly which factor destroys inverse-gamma conjugacy.
3. Derive the gamma posterior for the Poisson mean using both shape-rate and shape-scale parametrizations.
4. Verify directly that the normal-normal posterior mean is a weighted average of \\(x\\) and \\(\mu\\), with weights proportional to precisions.
5. Prove that the reciprocal-polynomial family in Section 3 remains conjugate after \\(n\\) iid Cauchy observations.
6. Explain why positivity of \\(p\\) is not by itself enough for \\(1/p\\) to define a prior density.
7. Prove Proposition 8.4 directly from the definition of a posterior density.
8. Prove the Bayes-risk decomposition in Section 9 from the law of total expectation.
9. For \\(X_1,\ldots,X_n\sim N(\theta,\sigma^2)\\) with known \\(\sigma^2\\), derive the generalized Bayes estimator under the flat prior.
10. Explain exactly where properness of the prior is used in Proposition 8.8.

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.
- Additional context has been added only where needed to make the Bayesian calculations and decision-theoretic statements self-contained.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-07-hypothesis-testing-likelihood-ratio/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }})
</nav>

</div>
