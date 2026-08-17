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
description: "Develops posterior distributions and conjugate priors, proves posterior-mean optimality under squared-error loss, and studies Bayes risk, sufficiency, improper priors, and generalized Bayes rules."
topics:
  - "Bayesian inference"
  - "prior and posterior"
  - "conjugate priors"
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
- derive conjugate posteriors in beta-binomial, gamma-Poisson, and normal-normal models;
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

## 2. Conjugate priors

<div class="definition" markdown="1">

**Definition 8.3 — Conjugate family.**
A family of prior distributions is _conjugate_ for a likelihood model if, whenever the prior belongs to that family, the posterior belongs to the same family, with updated parameters.

</div>

Conjugacy is a computational closure property. It is not a requirement of Bayesian inference.

### Worked Example 8.1 — Beta prior with binomial data

Let

$$
X\mid\theta
\sim
\operatorname{Binomial}(n,\theta),
$$

and place the prior

$$
\theta\sim\operatorname{Beta}(a,b),
\qquad a,b>0.
$$

The likelihood is

$$
f(x\mid\theta)
=
\binom nx
\theta^x(1-\theta)^{n-x},
$$

and the prior density is

$$
\pi(\theta)
=
\frac{
\theta^{a-1}(1-\theta)^{b-1}
}{
B(a,b)
}.
$$

Therefore

$$
\begin{aligned}
\pi(\theta\mid x)
&\propto
\theta^x(1-\theta)^{n-x}
\theta^{a-1}(1-\theta)^{b-1}\\
&=
\theta^{a+x-1}
(1-\theta)^{b+n-x-1}.
\end{aligned}
$$

Hence

$$
\boxed{
\theta\mid X=x
\sim
\operatorname{Beta}(a+x,b+n-x).
}
$$

Under squared-error loss, the Bayes estimator is the posterior mean:

$$
\boxed{
\delta_\pi(x)
=
\frac{a+x}{a+b+n}.
}
$$

For an iid Bernoulli sample with \\(S=\sum_iX_i\\), replace \\(x\\) by \\(S\\).

### Worked Example 8.2 — Gamma prior with Poisson data

<div class="intuition" markdown="1">

**Additional context.**
The handwritten material moves from the Poisson likelihood to a conjugacy calculation. The standard finite-dimensional conjugate family is the gamma family, written here in rate parametrisation.

</div>

Let

$$
X_1,\ldots,X_n\mid\theta
\overset{\mathrm{iid}}{\sim}
\operatorname{Poisson}(\theta),
$$

and let

$$
\theta\sim\operatorname{Gamma}(a,b)
$$

with shape \\(a>0\\) and rate \\(b>0\\):

$$
\pi(\theta)
=
\frac{b^a}{\Gamma(a)}
\theta^{a-1}e^{-b\theta}.
$$

If

$$
S=\sum_{i=1}^nX_i,
$$

then the likelihood kernel is

$$
L(\theta;x)
\propto
e^{-n\theta}\theta^S.
$$

Thus

$$
\begin{aligned}
\pi(\theta\mid x)
&\propto
e^{-n\theta}\theta^S
\theta^{a-1}e^{-b\theta}\\
&=
\theta^{a+S-1}
e^{-(b+n)\theta}.
\end{aligned}
$$

Hence

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

<div class="remark" markdown="1">

**Editorial note.**
The handwritten Poisson page contains a prior factor in which the symbol \\(x\\) is reused inside what should be a prior density for \\(\theta\\). Taken literally, that expression depends on the observed data and is not a prior specified before seeing \\(X\\). The gamma-Poisson calculation above is the mathematically well-defined conjugate version of the intended idea, with independent hyperparameters \\(a\\) and \\(b\\).

</div>

### Worked Example 8.3 — Normal likelihood with normal prior

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
\exp\left\lbrace -\frac{(x-\theta)^2}{2\sigma^2}
-\frac{(\theta-\mu)^2}{2\tau^2}
\right\rbrace .
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
\frac1{\sigma^2}
+
\frac1{\tau^2}
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

Define the posterior precision and variance by

$$
\frac1v
=
\frac1{\sigma^2}
+
\frac1{\tau^2},
\qquad
v
=
\left(
\frac1{\sigma^2}
+
\frac1{\tau^2}
\right)^{-1},
$$

and set

$$
m
=
v\left(
\frac{x}{\sigma^2}
+
\frac{\mu}{\tau^2}
\right).
$$

Then completing the square gives

$$
\pi(\theta\mid x)
\propto
\exp\left\lbrace -\frac{(\theta-m)^2}{2v}
\right\rbrace .
$$

Therefore

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
m
=
\frac{
x/\sigma^2+\mu/\tau^2
}{
1/\sigma^2+1/\tau^2
},
\qquad
v
=
\frac1{
1/\sigma^2+1/\tau^2
}.
}
$$

The posterior mean is a precision-weighted average of the data and prior mean.

For \\(n\\) iid observations,

$$
X_i\mid\theta\sim N(\theta,\sigma^2),
$$

the same calculation gives

$$
\boxed{
v_n
=
\frac1{n/\sigma^2+1/\tau^2},
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

## 3. Cauchy likelihood and the meaning of conjugacy

The handwritten notes ask whether the Cauchy location family has a conjugate prior.

For

$$
X\mid\theta
\sim
\operatorname{Cauchy}(\theta,1),
$$

the likelihood kernel is

$$
L(\theta;x)
\propto
\frac1{1+(x-\theta)^2}.
$$

There is no standard low-dimensional conjugate family analogous to beta-binomial or normal-normal that is routinely used for the Cauchy location parameter.

<div class="remark" markdown="1">

**Editorial note.**
The source observes that the set of _all_ prior densities is closed under Bayesian updating. In that very broad formal sense, the class of all priors is indeed conjugate for any likelihood. This is mathematically true but not useful: in statistical practice, “a conjugate family” normally means a tractable finite-dimensional or otherwise structured family whose form is preserved by updating.

</div>

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

**Definition 8.4 — Bayes risk.**
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

**Theorem 8.5 — Bayes estimator under squared-error loss.**
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

## 6. A Bayes estimator is a function of a sufficient statistic

Suppose \\(T(X)\\) is sufficient and

$$
f(x\mid\theta)
=
g_\theta(T(x))h(x).
$$

Then

$$
\begin{aligned}
\pi(\theta\mid x)
&=
\frac{
g_\theta(T(x))h(x)\pi(\theta)
}{
\int g_u(T(x))h(x)\pi(u)\,\mathrm du
}\\
&=
\frac{
g_\theta(T(x))\pi(\theta)
}{
\int g_u(T(x))\pi(u)\,\mathrm du
}.
\end{aligned}
$$

The factor \\(h(x)\\) cancels. Therefore the entire posterior distribution depends on \\(x\\) only through \\(T(x)\\):

$$
\boxed{
\pi(\theta\mid X)
=
\pi(\theta\mid T).
}
$$

Consequently every posterior functional, including the posterior mean, is a function of the sufficient statistic.

<div class="remark" markdown="1">

**Remark.**
This is the Bayesian analogue of the information-reduction interpretation of sufficiency: once a sufficient statistic is known, the rest of the sample does not change the posterior.

</div>

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

**Proposition 8.6 — Proper-prior posterior mean plus exact unbiasedness forces zero Bayes risk.**
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

**Definition 8.7 — Improper prior.**
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

**Definition 8.8 — Generalized Bayes rule.**
A rule obtained by Bayesian posterior minimisation from an improper prior is called a generalized Bayes rule.

</div>

### Worked Example 8.4 — Flat prior for a normal mean

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

Notice that \\(\bar X\\) is unbiased. This does not contradict Proposition 8.6 because the flat prior is improper, so the proper-prior integrated-risk argument does not apply.

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
Does every model have a useful conjugate prior?

**Answer.**

No. The class of all priors is trivially closed under updating, but useful conjugacy refers to a tractable structured family. Models such as the Cauchy location family do not have a standard low-dimensional conjugate family comparable to beta-binomial or normal-normal conjugacy.

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

Conjugate priors give algebraically closed posterior families. Improper priors can lead to generalized Bayes rules, as in the flat-prior normal example.

## Review problems

1. Derive the beta posterior for \\(n\\) iid Bernoulli observations with \\(S\\) successes.
2. Derive the gamma posterior for the Poisson mean using both shape-rate and shape-scale parametrisations.
3. Verify directly that the normal-normal posterior mean is a weighted average of \\(x\\) and \\(\mu\\), with weights proportional to precisions.
4. Prove the Bayes-risk decomposition in Section 9 from the law of total expectation.
5. For \\(X_1,\ldots,X_n\sim N(\theta,\sigma^2)\\) with known \\(\sigma^2\\), derive the generalized Bayes estimator under the flat prior.
6. Explain exactly where properness of the prior is used in Proposition 8.6.

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.
- Additional context has been added only where needed to make the Bayesian calculations and decision-theoretic statements self-contained.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-07-hypothesis-testing-likelihood-ratio/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }})
</nav>

</div>
