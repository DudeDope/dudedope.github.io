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
description: "Develops conjugate and generalized Bayes inference, posterior-mean optimality, Bayes and minimax risk, exact binomial minimax construction, sequence-of-priors arguments, Pareto conjugacy, and the unbounded uniform-endpoint decision problem."
topics:
  - "Bayesian inference"
  - "prior and posterior"
  - "conjugate priors"
  - "Cauchy reciprocal-polynomial conjugate family"
  - "Bayes estimator"
  - "Bayes risk"
  - "minimax risk"
  - "equalizer rules and admissibility"
  - "sufficiency"
  - "improper priors"
  - "generalized Bayes"
  - "least favourable priors"
  - "sequence-of-priors minimax theorem"
  - "binomial minimax estimator"
  - "Pareto conjugacy"
  - "uniform endpoint maximum risk"
previous: "lecture-07-hypothesis-testing-likelihood-ratio"
next: null
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-09-06"
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
- define frequentist risk and Bayes risk and distinguish a risk function from its worst-case supremum;
- prove that the posterior mean is the Bayes estimator under squared-error loss;
- show that the posterior depends on the data only through a sufficient statistic;
- understand why a proper-prior posterior mean cannot usually also be unbiased for every parameter value;
- work with an improper prior when it yields a proper posterior and identify the resulting generalized Bayes estimator;
- derive the fundamental inequality relating Bayes risk and minimax risk, and use it to recognize minimax Bayes/equalizer rules;
- distinguish admissibility, dominance, minimaxity, and least-favourable-prior arguments.
- derive the exact symmetric-beta Bayes rule whose binomial risk is constant and prove that it is minimax.
- use a sequence of proper priors to prove minimaxity when a generalized Bayes equalizer argument cannot be used directly.
- derive the Pareto conjugate family for the endpoint of a uniform model and prove that the unbounded endpoint problem has infinite maximum squared-error risk for every estimator.

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
\frac{1}{\pi\left\lbrace1+(x-\theta)^2\right\rbrace}.
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
\frac{1}{\pi\left\lbrace1+(x-\theta)^2\right\rbrace}
\frac{1}{p(\theta)}\\
&=
\frac{1}
{\pi p(\theta)\left\lbrace1+(x-\theta)^2\right\rbrace}.
\end{aligned}
$$

Let

$$
Z_p(x)
=
\int_{-\infty}^{\infty}
\frac{1}
{\pi p(u)\left\lbrace1+(x-u)^2\right\rbrace}
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
p(\theta)\left\lbrace1+(x-\theta)^2\right\rbrace}.
$$

Define

$$
q_x(\theta)
=
\pi Z_p(x)\,
p(\theta)\left\lbrace1+(x-\theta)^2\right\rbrace.
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
\prod_{i=1}^{n}\left\lbrace1+(x_i-\theta)^2\right\rbrace}.
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

## 10. Minimax risk, equalizer rules, and admissibility

<div class="intuition" markdown="1">

**Additional context.**
The source develops Bayes risk as an average of the frequentist risk. The following decision-theoretic consequences make explicit how that average is used in minimax arguments.

</div>

For a fixed decision rule \\(\delta\\), the quantity

$$
R(\theta,\delta)
=
\operatorname{E}_{\theta}
\left[
L\bigl(\theta,\delta(X)\bigr)
\right]
$$

is generally a **function of the true parameter \\(\theta\\)**. By contrast,

$$
M(\delta)
:=
\sup_{\theta\in\Theta}R(\theta,\delta)
$$

is a single number once \\(\delta\\) has been fixed: it is the worst-case risk of the rule.

If the supremum is attained at some \\(\theta^{\star}\\), then

$$
M(\delta)
=
R(\theta^{\star},\delta).
$$

The symbol \\(\theta^{\star}\\) denotes a maximizing parameter value; the equality does not mean that \\(M(\delta)\\) remains a function of an arbitrary \\(\theta\\).

<div class="definition" markdown="1">

**Definition 8.11 — Minimax rule and minimax value.**
The minimax value is

$$
R^{\star}
=
\inf_{\delta}
\sup_{\theta\in\Theta}
R(\theta,\delta).
$$

A rule \\(\delta^{\star}\\) is minimax if

$$
\sup_{\theta\in\Theta}
R(\theta,\delta^{\star})
=
R^{\star}.
$$

</div>

The Bayes risk of any fixed rule is an average of its risk function:

$$
r_{\pi}(\delta)
=
\int_{\Theta}
R(\theta,\delta)\pi(\theta)\,\mathrm d\theta.
$$

Since

$$
R(\theta,\delta)
\le
\sup_{\nu\in\Theta}R(\nu,\delta)
$$

for every \\(\theta\\), integration gives

$$
\begin{aligned}
r_{\pi}(\delta)
&=
\int_{\Theta}
R(\theta,\delta)\pi(\theta)\,\mathrm d\theta\\
&\le
\int_{\Theta}
\sup_{\nu\in\Theta}R(\nu,\delta)
\,\pi(\theta)\,\mathrm d\theta\\
&=
\sup_{\nu\in\Theta}R(\nu,\delta).
\end{aligned}
$$

Thus

$$
\boxed{
r_{\pi}(\delta)
\le
\sup_{\theta\in\Theta}R(\theta,\delta).
}
$$

This is simply the statement that an average cannot exceed the maximum of the quantities being averaged.

Now let

$$
r_{\pi}^{\star}
=
\inf_{\delta}r_{\pi}(\delta)
$$

denote the minimum Bayes risk under the prior \\(\pi\\). Because the preceding inequality holds for every \\(\delta\\),

$$
\boxed{
r_{\pi}^{\star}
\le
R^{\star}.
}
$$

So **every minimum Bayes risk is a lower bound on the minimax value**.

### Worked Example 8.7 — Average risk versus worst-case risk

Suppose a parameter can take three values and a rule has risks

$$
R(\theta_1,\delta)=2,
\qquad
R(\theta_2,\delta)=5,
\qquad
R(\theta_3,\delta)=8.
$$

Its worst-case risk is

$$
\sup_{\theta}R(\theta,\delta)=8.
$$

For prior probabilities \\(0.2,0.5,0.3\\),

$$
\begin{aligned}
r_{\pi}(\delta)
&=
0.2(2)+0.5(5)+0.3(8)\\
&=
5.3.
\end{aligned}
$$

Therefore

$$
5.3\le8,
$$

illustrating the general inequality.

<div class="definition" markdown="1">

**Definition 8.12 — Equalizer rule.**
A rule \\(\delta\\) is an equalizer rule if its risk is constant over the parameter space:

$$
R(\theta,\delta)=c
\qquad
\text{for every }\theta\in\Theta.
$$

Then

$$
\sup_{\theta}R(\theta,\delta)=c.
$$

</div>

Constant risk alone does **not** automatically prove minimaxity. One must still show that no competing rule has worst-case risk strictly below \\(c\\).

A particularly useful sufficient condition is the following.

<div class="proposition" markdown="1">

**Proposition 8.13 — A Bayes equalizer rule is minimax.**
Suppose \\(\delta\_{\pi}\\) is Bayes under a proper prior \\(\pi\\) and

$$
R(\theta,\delta_{\pi})=c
\qquad
\text{for every }\theta.
$$

Then \\(\delta\_{\pi}\\) is minimax and the minimax value is \\(c\\).

</div>

**Proof.**

Because the risk is constant,

$$
r_{\pi}(\delta_{\pi})
=
\int_{\Theta}
c\,\pi(\theta)\,\mathrm d\theta
=
c.
$$

The general Bayes lower bound gives

$$
r_{\pi}(\delta_{\pi})
\le
R^{\star}.
$$

On the other hand, using \\(\delta\_{\pi}\\) as one candidate in the minimax infimum gives

$$
R^{\star}
\le
\sup_{\theta}
R(\theta,\delta_{\pi})
=
c.
$$

Hence

$$
c
\le
R^{\star}
\le
c,
$$

and therefore

$$
\boxed{
R^{\star}=c.
}
$$

Thus \\(\delta\_{\pi}\\) is minimax.

\\(\square\\)

<div class="definition" markdown="1">

**Definition 8.14 — Dominance and admissibility.**
A rule \\(\delta_1\\) **dominates** \\(\delta_0\\) if

$$
R(\theta,\delta_1)
\le
R(\theta,\delta_0)
\qquad
\text{for every }\theta,
$$

with strict inequality for at least one parameter value.

A rule is **admissible** if no other rule dominates it. Otherwise it is inadmissible.

</div>

Admissibility and minimaxity answer different questions:

- admissibility asks whether a rule can be uniformly improved;
- minimaxity asks whether its **largest** risk is as small as possible.

An equalizer rule that is admissible is automatically minimax.

<div class="proposition" markdown="1">

**Proposition 8.15 — An admissible equalizer rule is minimax.**
If

$$
R(\theta,\delta)=c
\qquad
\text{for every }\theta
$$

and \\(\delta\\) is admissible, then \\(\delta\\) is minimax.

</div>

**Proof.**

Suppose \\(\delta\\) were not minimax. Then there would exist a rule \\(\delta_1\\) such that

$$
\sup_{\theta}R(\theta,\delta_1)<c.
$$

Therefore, for every \\(\theta\\),

$$
R(\theta,\delta_1)
<
c
=
R(\theta,\delta).
$$

Thus \\(\delta_1\\) would dominate \\(\delta\\), contradicting admissibility. Hence \\(\delta\\) must be minimax.

\\(\square\\)

<div class="definition" markdown="1">

**Definition 8.16 — Least favourable prior.**
A prior \\(\pi^{\star}\\) is called least favourable, when the relevant extrema exist, if its minimum Bayes risk is as large as possible:

$$
r_{\pi^{\star}}^{\star}
=
\sup_{\pi}r_{\pi}^{\star}.
$$

</div>

The terminology reflects the game-theoretic interpretation: the statistician chooses a rule while an adversary chooses a prior or parameter value. A least favourable prior makes the best achievable average risk as large as possible.

A standard minimax proof strategy is to find a prior \\(\pi^{\star}\\) and its Bayes rule \\(\delta^{\star}\\) such that

$$
r_{\pi^{\star}}(\delta^{\star})
=
\sup_{\theta}R(\theta,\delta^{\star}).
$$

Then

$$
r_{\pi^{\star}}(\delta^{\star})
\le
R^{\star}
\le
\sup_{\theta}R(\theta,\delta^{\star}),
$$

and the two endpoints are equal. Hence \\(\delta^{\star}\\) is minimax.

### 10.1 Exact binomial minimax construction from the source notes

The 21 August notes ask for a choice of beta-prior hyperparameters that makes the Bayes estimator's frequentist risk independent of \\(\theta\\).

Let

$$
X\sim\operatorname{Bin}(n,\theta),
\qquad 0<\theta<1,
$$

and place the prior

$$
\theta\sim\operatorname{Beta}(p,q).
$$

Under squared-error loss, the Bayes estimator is the posterior mean

$$
\delta_{p,q}(X)
=
\frac{p+X}{p+q+n}.
$$

The source chooses a symmetric beta prior, so set

$$
p=q=a.
$$

Then

$$
\delta_a(X)
=
\frac{X+a}{n+2a}.
$$

We now compute its **frequentist** risk as a function of the fixed true \\(\theta\\).

First,

$$
\operatorname{E}_\theta[\delta_a(X)]
=
\frac{n\theta+a}{n+2a}.
$$

Therefore the bias is

$$
\begin{aligned}
\operatorname{Bias}_\theta(\delta_a)
&=
\frac{n\theta+a}{n+2a}-\theta\\
&=
\frac{a-2a\theta}{n+2a}\\
&=
\frac{a(1-2\theta)}{n+2a}.
\end{aligned}
$$

The variance is

$$
\operatorname{Var}_\theta(\delta_a)
=
\frac{n\theta(1-\theta)}{(n+2a)^2}.
$$

Hence

$$
\boxed{
R(\theta,\delta_a)
=
\frac{
 n\theta(1-\theta)+a^2(1-2\theta)^2
}{(n+2a)^2}.
}
$$

To make this independent of \\(\theta\\), expand the numerator:

$$
\begin{aligned}
n\theta(1-\theta)+a^2(1-2\theta)^2
&=
n\theta-n\theta^2
+a^2-4a^2\theta+4a^2\theta^2\\
&=
a^2
+(n-4a^2)\theta
+(-n+4a^2)\theta^2.
\end{aligned}
$$

Both coefficients involving \\(\theta\\) vanish exactly when

$$
4a^2=n.
$$

Thus

$$
\boxed{
a=\frac{\sqrt n}{2},
\qquad
p=q=\frac{\sqrt n}{2}.
}
$$

For this choice, the numerator becomes simply \\(n/4\\), and

$$
\begin{aligned}
R(\theta,\delta^{\ast})
&=
\frac{n/4}{(n+\sqrt n)^2}\\
&=
\frac{1}{4(\sqrt n+1)^2},
\end{aligned}
$$

which is constant in \\(\theta\\).

<div class="proposition" markdown="1">

**Proposition 8.17 — The symmetric-beta Bayes rule is minimax.**

For

$$
p=q=\frac{\sqrt n}{2},
$$

the Bayes estimator

$$
\boxed{
\delta^{\ast}(X)
=
\frac{X+\sqrt n/2}{n+\sqrt n}
}
$$

has constant risk

$$
\boxed{
R(\theta,\delta^{\ast})
=
\frac{1}{4(\sqrt n+1)^2}.
}
$$

Since it is Bayes under a proper beta prior and is an equalizer rule, it is minimax.

</div>

The chosen prior is symmetric about \\(1/2\\). Its mean is \\(1/2\\), and for \\(a=\sqrt n/2\\),

$$
\operatorname{Var}(\theta)
=
\frac{1}{4(2a+1)}
=
\frac{1}{4(\sqrt n+1)}
\longrightarrow0.
$$

Thus, as the sample size indexing this minimax construction grows, the least-favourable-style beta prior becomes increasingly concentrated around \\(1/2\\), the parameter value where the unbiased estimator \\(X/n\\) has its largest risk.

For comparison, the unbiased estimator \\(X/n\\) has

$$
R\left(\theta,\frac Xn\right)
=
\frac{\theta(1-\theta)}{n},
$$

whose maximum is

$$
\sup_{0<\theta<1}
R\left(\theta,\frac Xn\right)
=
\frac{1}{4n}.
$$

Thus unbiasedness and minimaxity lead to different estimators and different worst-case risks.

### 10.2 Can the equalizer argument be used for generalized Bayes rules?

The 21 August notes explicitly ask whether the preceding result remains true for a generalized Bayes estimator.

The answer is: **not automatically**.

The proof of Proposition 8.13 used a proper prior \\(\pi\\) to write

$$
r_\pi(\delta_\pi)
=
\int R(\theta,\delta_\pi)\pi(\theta)\,\mathrm d\theta.
$$

For an improper prior, the integral of the prior kernel need not be \\(1\\), and the corresponding integrated risk may be infinite or undefined. Therefore the simple implication

$$
\text{generalized Bayes}+\text{constant risk}
\Longrightarrow
\text{minimax}
$$

is **not** valid without additional assumptions.

A standard replacement is the sequence-of-proper-priors argument in the 25 August notes.

<div class="theorem" markdown="1">

**Theorem 8.18 — Minimaxity from a sequence of proper priors.**

Let \\(\delta^{\ast}\\) be a candidate rule with finite worst-case risk

$$
C
=
\sup_{\theta\in\Theta}R(\theta,\delta^{\ast}).
$$

Suppose there exists a sequence of proper priors \\(\pi_k\\), with Bayes rules \\(\delta\_{\pi_k}\\), such that

$$
\boxed{
r_{\pi_k}(\delta_{\pi_k})\longrightarrow C.
}
$$

Then \\(\delta^{\ast}\\) is minimax and the minimax value equals \\(C\\).

</div>

**Proof.**

For any competing rule \\(\delta\\) and every \\(k\\),

$$
\sup_\theta R(\theta,\delta)
\ge
r_{\pi_k}(\delta)
\ge
r_{\pi_k}(\delta_{\pi_k}),
$$

because a Bayes rule minimizes integrated risk under \\(\pi_k\\). Taking \\(k\to\infty\\),

$$
\sup_\theta R(\theta,\delta)
\ge C.
$$

Since this holds for every \\(\delta\\),

$$
R^{\star}
=
\inf_\delta\sup_\theta R(\theta,\delta)
\ge C.
$$

But \\(\delta^{\ast}\\) itself has worst-case risk \\(C\\), so

$$
R^{\star}\le C.
$$

Hence

$$
\boxed{R^{\star}=C,}
$$

and \\(\delta^{\ast}\\) is minimax.

\\(\square\\)

This theorem is especially useful for generalized Bayes rules: one often approximates an improper prior by proper priors \\(\pi_k\\) and shows that their Bayes risks approach the constant risk of the generalized Bayes rule.

<div class="remark" markdown="1">

**Connection with least favourable priors.**
A sequence \\(\pi_k\\) whose minimum Bayes risks rise to the minimax value behaves like an approximating sequence of least favourable priors, even if no single least favourable proper prior exists.

</div>

### 10.3 Uniform endpoint model: Pareto conjugacy

The 25 August notes ask for a convenient conjugate family when

$$
X_1,\ldots,X_n
\overset{\mathrm{iid}}{\sim}
\operatorname{Uniform}(0,\theta),
\qquad
\theta\ge a>0.
$$

The likelihood is

$$
L(\theta;x)
=
\theta^{-n}
\mathbf 1_{\lbrace \theta\ge X_{(n)}\rbrace }.
$$

A natural prior family is the Pareto-type family

$$
\boxed{
\pi_{\alpha,a}(\theta)
=
(\alpha-1)a^{\alpha-1}
\theta^{-\alpha}
\mathbf 1_{\lbrace \theta\ge a\rbrace },
\qquad
\alpha>1.
}
$$

The constant is correct because

$$
\int_a^\infty
\theta^{-\alpha}\,\mathrm d\theta
=
\frac{a^{1-\alpha}}{\alpha-1}.
$$

Multiplying prior and likelihood gives

$$
\begin{aligned}
\pi(\theta\mid x)
&\propto
\theta^{-n}
\mathbf 1_{\lbrace \theta\ge X_{(n)}\rbrace }
\theta^{-\alpha}
\mathbf 1_{\lbrace \theta\ge a\rbrace }\\
&=
\theta^{-(\alpha+n)}
\mathbf 1_{\lbrace \theta\ge m\rbrace },
\end{aligned}
$$

where

$$
m=\max\lbrace a,X_{(n)}\rbrace .
$$

Thus the posterior is in the same family with updated parameters

$$
\boxed{
\alpha' = \alpha+n,
\qquad
a' = m.
}
$$

The normalized posterior is

$$
\boxed{
\pi(\theta\mid x)
=
(\alpha+n-1)m^{\alpha+n-1}
\theta^{-(\alpha+n)}
\mathbf 1_{\lbrace \theta\ge m\rbrace }.
}
$$

Under squared-error loss, if \\(\alpha+n>2\\), the Bayes estimator is the posterior mean,

$$
\boxed{
\delta_\pi(x)
=
\operatorname{E}[\theta\mid x]
=
\frac{\alpha+n-1}{\alpha+n-2}
\max\lbrace a,X_{(n)}\rbrace .
}
$$

This solves the conjugate-family question in the source.

### 10.4 Why every estimator has infinite maximum squared-error risk in \\(U(0,\theta)\\) with unbounded \\(\theta\\)

The 25 August page also asks to show that if

$$
\Theta=(0,\infty),
$$

then no estimator can have finite maximum squared-error risk.

<div class="theorem" markdown="1">

**Theorem 8.19 — Infinite maximum risk for the unbounded uniform endpoint problem.**

Let

$$
X_1,\ldots,X_n
\overset{\mathrm{iid}}{\sim}
\operatorname{Uniform}(0,\theta),
\qquad \theta>0,
$$

and let \\(\delta(X)\\) be any estimator of \\(\theta\\). Under squared-error loss,

$$
\boxed{
\sup_{\theta>0}R(\theta,\delta)=\infty.
}
$$

</div>

**Proof.**

Fix \\(t>0\\) and compare the two parameter values

$$
\theta_0=t,
\qquad
\theta_1=2t.
$$

Define the event

$$
A_t
=
\left\lbrace
\lvert\delta(X)-t\rvert<\frac t2
\right\rbrace .
$$

On \\(A_t^c\\), the squared error at parameter \\(t\\) is at least \\(t^2/4\\), so

$$
R(t,\delta)
\ge
\frac{t^2}{4}P_t(A_t^c).
$$

On \\(A_t\\), the estimator lies between \\(t/2\\) and \\(3t/2\\), hence its distance from \\(2t\\) is at least \\(t/2\\). Therefore

$$
R(2t,\delta)
\ge
\frac{t^2}{4}P_{2t}(A_t).
$$

Now add the two lower bounds. The joint density under \\(t\\) is

$$
f_t(x)
=
t^{-n}
\mathbf 1_{(0,t)^n}(x),
$$

and under \\(2t\\),

$$
f_{2t}(x)
=
(2t)^{-n}
\mathbf 1_{(0,2t)^n}(x).
$$

For any event \\(A\\),

$$
P_t(A^c)+P_{2t}(A)
\ge
\int \min\lbrace f_t(x),f_{2t}(x)\rbrace\,\mathrm dx.
$$

The two densities overlap on \\((0,t)^n\\), and on this region the smaller density is \\((2t)^{-n}\\). Hence

$$
\begin{aligned}
\int \min\lbrace f_t,f_{2t}\rbrace\,\mathrm dx
&=
\int_{(0,t)^n}(2t)^{-n}\,\mathrm dx\\
&=
\frac{t^n}{(2t)^n}\\
&=
2^{-n}.
\end{aligned}
$$

Therefore

$$
\begin{aligned}
R(t,\delta)+R(2t,\delta)
&\ge
\frac{t^2}{4}
\left[P_t(A_t^c)+P_{2t}(A_t)\right]\\
&\ge
\frac{t^2}{4}\,2^{-n}.
\end{aligned}
$$

Thus at least one of the two risks satisfies

$$
\max\lbrace R(t,\delta),R(2t,\delta)\rbrace
\ge
\frac{t^2}{2^{n+3}}.
$$

Letting \\(t\to\infty\\) gives

$$
\sup_{\theta>0}R(\theta,\delta)=\infty.
$$

\\(\square\\)

<div class="remark" markdown="1">

**Interpretation.**
With a fixed sample size and an unbounded scale parameter, absolute squared error necessarily grows on the scale of \\(\theta^2\\) somewhere in the parameter space. Hence the ordinary minimax value under unscaled squared-error loss is infinite in this problem.

</div>

## 11. Relationship with earlier lectures

The same estimator can be evaluated under several different criteria:

- **unbiasedness:** \\(\operatorname{E}\_\theta[\delta(X)]=\theta\\) for every \\(\theta\\);
- **frequentist risk:** \\(R(\theta,\delta)\\) is compared pointwise in \\(\theta\\);
- **UMVUE:** minimum variance among unbiased estimators at every \\(\theta\\);
- **Bayes rule:** minimum integrated risk under a specified prior;
- **minimax rule:** minimum worst-case risk over the parameter space;
- **admissible rule:** no competing rule has everywhere no larger risk and somewhere strictly smaller risk;
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

**Question.**
Why is Bayes risk no larger than the worst-case risk of the same rule?

**Answer.**

For fixed \\(\delta\\), \\(r\_{\pi}(\delta)\\) is an average of the numbers \\(R(\theta,\delta)\\) under the prior, while \\(\sup\_{\theta}R(\theta,\delta)\\) is their largest possible value. Hence

$$
r_{\pi}(\delta)
\le
\sup_{\theta}R(\theta,\delta).
$$

Taking the infimum over rules yields the useful lower bound

$$
r_{\pi}^{\star}
\le
R^{\star}.
$$

**Question.**
Is \\(R(\theta,\delta)\\) generally a function of \\(\theta\\), and what does \\(\sup\_{\theta}R(\theta,\delta)\\) represent?

**Answer.**

Yes. For fixed \\(\delta\\), the risk function \\(\theta\mapsto R(\theta,\delta)\\) generally varies with \\(\theta\\). The supremum is a single worst-case number. If it is attained at \\(\theta^{\star}\\), then

$$
\sup_{\theta}R(\theta,\delta)
=
R(\theta^{\star},\delta).
$$

**Question.**
Does constant risk by itself imply that a rule is minimax?

**Answer.**

No. Constant risk only makes the rule an equalizer rule. Minimaxity follows, for example, if the equalizer rule is Bayes for some proper prior or if it is admissible.

**Question.**
What does admissible mean?

**Answer.**

A rule is admissible if no other rule has risk no larger for every parameter value and strictly smaller for at least one parameter value. In other words, an admissible rule cannot be uniformly improved.

**Question.**
How do we choose the symmetric beta prior in the binomial problem so that the Bayes estimator has constant frequentist risk?

**Answer.**

For \\(p=q=a\\),

$$
R(\theta,\delta_a)
=
\frac{n\theta(1-\theta)+a^2(1-2\theta)^2}{(n+2a)^2}.
$$

The coefficients of \\(\theta\\) and \\(\theta^2\\) vanish when \\(4a^2=n\\), hence

$$
p=q=\frac{\sqrt n}{2}.
$$

The resulting proper-Bayes equalizer rule is minimax.

**Question.**
Does “generalized Bayes + constant risk” automatically imply minimaxity?

**Answer.**

No. The proper-prior Bayes-risk proof cannot be used directly with an improper prior. A standard sufficient replacement is to find proper priors \\(\pi_k\\) whose minimum Bayes risks converge to the candidate rule's constant worst-case risk.

**Question.**
What is a conjugate prior family for the endpoint in \\(U(0,\theta)\\)?

**Answer.**

A Pareto-type density

$$
\pi_{\alpha,a}(\theta)
=
(\alpha-1)a^{\alpha-1}\theta^{-\alpha}
\mathbf 1_{\lbrace\theta\ge a\rbrace},
\qquad \alpha>1,
$$

is conjugate. After observing \\(X\_{(n)}\\), the posterior has updated lower bound \\(\max\lbrace a,X\_{(n)}\rbrace\\) and exponent \\(\alpha+n\\).

**Question.**
Why is the maximum squared-error risk infinite for every estimator of an unbounded uniform endpoint?

**Answer.**

Compare the two parameter values \\(t\\) and \\(2t\\). Their sample distributions retain an overlap of probability order \\(2^{-n}\\), so no estimator can distinguish them perfectly. On one of the two models it must incur squared error of order \\(t^2\\). Letting \\(t\to\infty\\) forces the supremum risk to diverge.

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

Conjugate families are closed under Bayesian updating, but the family need not be unique. The beta-binomial, gamma-Poisson, and normal-normal examples are finite-dimensional conjugate families; the reciprocal-polynomial Cauchy construction is a larger conjugate family; and the class of all proper densities is the universal, formally conjugate family. Improper priors can lead to generalized Bayes rules, as in the flat-prior normal example. Bayes risk is always bounded above by the worst-case risk of the same rule, so minimum Bayes risks provide lower bounds on the minimax value. Bayes or admissible equalizer rules therefore give important routes to minimaxity.

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
11. Prove that the minimum Bayes risk under any proper prior is a lower bound on the minimax value.
12. Give an example of two risk functions that cross, and explain why neither rule necessarily dominates the other.
13. Prove that a Bayes equalizer rule is minimax.
14. Explain why an admissible equalizer rule must be minimax.
15. For the beta-binomial Bayes estimator with \\(p=q=a\\), derive the full risk function and solve for the value of \\(a\\) that makes it constant.
16. Prove Theorem 8.18 using the two inequalities \\(\sup\_\theta R(\theta,\delta)\ge r\_{\pi_k}(\delta)\ge r\_{\pi_k}(\delta\_{\pi_k})\\).
17. Derive the Pareto posterior for the endpoint of \\(U(0,\theta)\\) and compute its posterior mean.
18. Reproduce the two-point lower-bound proof showing that every estimator of an unbounded uniform endpoint has infinite maximum squared-error risk.

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.
- Additional context has been added only where needed to make the Bayesian calculations and decision-theoretic statements self-contained.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-07-hypothesis-testing-likelihood-ratio/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }})
</nav>

</div>
