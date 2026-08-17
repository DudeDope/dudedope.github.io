---
layout: page
title: "Lecture 1: Point Estimation, Risk, Mean Squared Error, and Estimator Comparison"
short_title: "Point estimation and MSE"
course: "Parametric Inference"
lecture: 1
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Develops the parametric estimation framework, squared-error risk, bias–variance decomposition, estimator comparison, and the likelihood and maximum-likelihood framework with a Cauchy location example."
topics:
  - "parametric models"
  - "estimators"
  - "loss and risk"
  - "mean squared error"
  - "bias–variance decomposition"
  - "estimator comparison"
  - "maximum likelihood"
  - "Cauchy location"
previous: null
next: "lecture-02-unbiased-estimation-umvue-crlb"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-17"
status: "complete"
math: true
permalink: /notes/parametric-inference/lecture-01-point-estimation-risk-mse/
course_slug: parametric-inference
note_kind: lecture
course_order: 1
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Fall 2026 Parametric Inference lectures of Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata. Additional exposition and any remaining errors are the responsibility of the note author.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url }})
</nav>

## Learning objectives

<div class="intuition" markdown="1">

**Additional context.**
This section was added to make the lecture easier to use as a self-contained study note.

</div>

- Formulate a parametric estimation problem precisely.
- Define loss, risk, MSE, bias, and variance.
- Derive the bias–variance decomposition.
- Explain why unrestricted pointwise risk comparison rarely produces a universally best estimator.
- Define likelihood, log-likelihood, and the MLE, and derive a likelihood equation.

## 1. Parametric statistical models

<div class="definition" markdown="1">

**Definition 1.1 — Parametric model.**

A _parametric statistical model_ is a family of probability distributions

$$
\mathcal P=\lbrace P_\theta:\theta\in\Theta\rbrace ,
$$

where \\(\Theta\subseteq\mathbb{R}^k\\) is the parameter space. The unknown quantity \\(\theta\\) indexes the distribution that generated the data.

</div>

A random sample is usually written

$$
X=(X_1,\dots,X_n),\qquad X_1,\dots,X_n\overset{\mathrm{iid}}{\sim}P_\theta.
$$

Before observation, \\(X\\) is random. After observation, its realised value is denoted

$$
x=(x_1,\dots,x_n).
$$

<div class="definition" markdown="1">

**Definition 1.2 — Statistic and estimator.**

A _statistic_ is any measurable function \\(T=T(X)\\) of the sample that does not involve the unknown parameter. When \\(T\\) is used to estimate a parameter or a parametric function \\(\psi(\theta)\\), it is called an _estimator_. The observed number \\(T(x)\\) is called the _estimate_.

</div>

<div class="warning" markdown="1">

**Common pitfall 1.3.**

An estimator may depend on known constants, but it cannot contain the unknown value of \\(\theta\\). For example, \\(T(X)=X_1\\) is an estimator of \\(\theta\\), while \\(T(X)=X_1-\theta\\) is not.

</div>

## 2. Point estimation as a decision problem

An estimator is a rule for choosing an action after observing the data. To decide whether one estimator is better than another, we must first specify how estimation error is measured.

<div class="definition" markdown="1">

**Definition 1.4 — Loss and risk.**

Let \\(a\\) be an action intended to estimate \\(\psi(\theta)\\). A _loss function_ \\(L(\theta,a)\\) measures the cost of taking action \\(a\\) when the true parameter is \\(\theta\\). The _risk function_ of an estimator \\(T\\) is

$$
R(\theta,T)=\operatorname{E}_\theta\!\left[L\bigl(\theta,T(X)\bigr)\right].
$$

</div>

The most common loss for estimating a real-valued quantity is squared-error loss:

$$
L(\theta,a)=\bigl(a-\psi(\theta)\bigr)^2.
$$

Then the risk is the mean squared error:

$$
R(\theta,T)=\operatorname{E}_\theta\left[(T-\psi(\theta))^2\right]=\operatorname{MSE}_\theta(T).
$$

<div class="definition" markdown="1">

**Definition 1.5 — Uniform comparison.**

Under a fixed loss, an estimator \\(T_1\\) is at least as good as \\(T_2\\) if

$$
R(\theta,T_1)\le R(\theta,T_2)\qquad\text{for every }\theta\in\Theta.
$$

It is strictly better if the inequality is strict for at least one \\(\theta\\).

</div>

## 3. Bias–variance decomposition

<div class="definition" markdown="1">

**Definition 1.6 — Bias.**

The bias of an estimator \\(T\\) of \\(\psi(\theta)\\) is

$$
\operatorname{Bias}_\theta(T)=\operatorname{E}_\theta[T]-\psi(\theta).
$$

The estimator is _unbiased_ if \\(\operatorname{E}\_\theta[T]=\psi(\theta)\\) for every \\(\theta\in\Theta\\).

</div>

<div class="theorem" markdown="1">

**Theorem 1.7 — Bias–variance decomposition.**

Suppose \\(\operatorname{E}\_\theta[T^2]<\infty\\). Then

$$
\operatorname{MSE}_\theta(T)=\operatorname{Var}_\theta(T)+\operatorname{Bias}_\theta(T)^2.
$$

</div>

**Proof.**

Write \\(m\_\theta=\operatorname{E}\_\theta[T]\\). Then

$$
T-\psi(\theta)=\bigl(T-m_\theta\bigr)+\bigl(m_\theta-\psi(\theta)\bigr).
$$

Squaring and taking expectations gives

$$
\begin{aligned}
\operatorname{E}_\theta[(T-\psi(\theta))^2]
&=\operatorname{E}_\theta[(T-m_\theta)^2]
+2\bigl(m_\theta-\psi(\theta)\bigr)\operatorname{E}_\theta[T-m_\theta]\\
&\qquad+\bigl(m_\theta-\psi(\theta)\bigr)^2.
\end{aligned}
$$

The middle term is zero, so the result follows.

\\(\square\\)

For an unbiased estimator,

$$
\operatorname{MSE}_\theta(T)=\operatorname{Var}_\theta(T).
$$

This is why variance is the relevant criterion when comparing unbiased estimators.

## 4. Why a universally best estimator usually does not exist

The following argument explains why we generally restrict the class of estimators, for example to unbiased estimators.

<div class="proposition" markdown="1">

**Proposition 1.8 — No uniformly best estimator over all estimators.**

Suppose \\(\Theta\\) contains at least two points, the loss is squared error, and the model distributions overlap sufficiently that no statistic can equal two different constants almost surely under different parameter values. Then there is no estimator that has risk no larger than every other estimator at every \\(\theta\in\Theta\\).

</div>

**Proof.**

Assume that \\(T^{\ast}\\) is uniformly best among all estimators. Fix any \\(\theta_0\in\Theta\\), and compare \\(T^{\ast}\\) with the constant estimator

$$
T_{\theta_0}(X)\equiv \psi(\theta_0).
$$

At \\(\theta=\theta_0\\),

$$
R(\theta_0,T_{\theta_0})=0.
$$

Uniform optimality would therefore imply

$$
0\le R(\theta_0,T^{\ast})\le 0,
$$

so \\(T^{\ast}=\psi(\theta_0)\\) almost surely under \\(P\_{\theta_0}\\). Since \\(\theta_0\\) was arbitrary, \\(T^{\ast}\\) would have to equal a different constant almost surely for each parameter value. In ordinary overlapping models this is impossible.

\\(\square\\)

### Worked Example 1.1 — Binomial illustration

**Problem.**

Show, in a concrete binomial model, why an estimator cannot be uniformly best among all estimators under squared-error loss.

**Solution.**

Let \\(X\sim\operatorname{Bin}(n,\theta)\\), \\(0<\theta<1\\), and suppose we estimate \\(\theta\\). If a universally best estimator \\(T^{\ast}\\) existed, then comparison with the constant estimator \\(T_0\equiv 1/2\\) would force

$$
R(1/2,T^{\ast})=0,
$$

so \\(T^{\ast}=1/2\\) for every \\(x\in\lbrace 0,\dots,n\rbrace \\), because every such \\(x\\) has positive probability when \\(\theta=1/2\\). Thus \\(T^{\ast}\equiv1/2\\). But at, say, \\(\theta=1/4\\), the constant estimator \\(T_1\equiv1/4\\) has risk zero, whereas \\(T^{\ast}\equiv1/2\\) has risk \\(1/16\\). This contradicts universal optimality.

**Final result.**

No universally best estimator exists over the unrestricted estimator class in this binomial problem.

> **Key point.**
> There is usually no best estimator among _all_ estimators. The UMVUE problem is different: it asks for the estimator with minimum variance only within the class of unbiased estimators.

## 5. Maximum likelihood and the likelihood equation

<div class="intuition" markdown="1">

**Additional context.**
The handwritten continuation asks for the maximum-likelihood equation in the Cauchy location model. The definitions below are added so that the example is self-contained.

</div>

<div class="definition" markdown="1">

**Definition 1.9 — Likelihood and log-likelihood.**
For observed data \\(x=(x_1,\ldots,x_n)\\) from a model with joint density or mass function \\(f\_\theta(x)\\), the likelihood is

$$
L(\theta;x)=f_\theta(x),
$$

viewed as a function of \\(\theta\\) with the data held fixed. The _log-likelihood_ is

$$
\ell(\theta;x)=\log L(\theta;x).
$$

</div>

<div class="definition" markdown="1">

**Definition 1.10 — Maximum-likelihood estimator.**
A maximum-likelihood estimator is any measurable choice

$$
\widehat\theta_{\mathrm{MLE}}\in\mathop{\mathrm{arg\,max}}_{\theta\in\Theta}L(\theta;X).
$$

Equivalently, when the logarithm is finite, it maximises \\(\ell(\theta;X)\\).

</div>

If \\(\Theta\\) is open and the maximiser is an interior differentiability point, it must satisfy the _likelihood equation_

$$
\frac{\partial}{\partial\theta}\ell(\theta;x)=0.
$$

This is only a necessary condition in general. One must still check boundaries, nondifferentiable points, and which stationary point gives the global maximum.

### Worked Example 1.2 — Likelihood equation for a Cauchy location parameter

**Problem.**

Let

$$
X_1,\ldots,X_n\overset{\mathrm{iid}}{\sim}\operatorname{Cauchy}(\theta,1),
\qquad
f_\theta(x)=\frac{1}{\pi\lbrace 1+(x-\theta)^2\rbrace },
\qquad
\theta\in\mathbb R.
$$

Derive the maximum-likelihood equation for \\(\theta\\).

**Solution.**

The likelihood is

$$
L(\theta;x)
=
\prod_{i=1}^n
\frac{1}{\pi\lbrace 1+(x_i-\theta)^2\rbrace }
=
\pi^{-n}
\prod_{i=1}^n
\lbrace 1+(x_i-\theta)^2\rbrace ^{-1}.
$$

Hence

$$
\ell(\theta;x)
=
-n\log\pi
-
\sum_{i=1}^n
\log\lbrace 1+(x_i-\theta)^2\rbrace .
$$

Differentiate term by term:

$$
\begin{aligned}
\ell'(\theta;x)
&=
-\sum_{i=1}^n
\frac{1}{1+(x_i-\theta)^2}
\frac{\mathrm d}{\mathrm d\theta}(x_i-\theta)^2\\
&=
-\sum_{i=1}^n
\frac{-2(x_i-\theta)}
{1+(x_i-\theta)^2}\\
&=
2\sum_{i=1}^n
\frac{x_i-\theta}
{1+(x_i-\theta)^2}.
\end{aligned}
$$

Therefore every interior MLE must satisfy

$$
\boxed{
\sum_{i=1}^n
\frac{x_i-\widehat\theta}
{1+(x_i-\widehat\theta)^2}
=0.
}
$$

There is generally no closed-form solution. The score need not be monotone, so the equation can have more than one root. A numerical root must therefore be checked against the likelihood to identify a global maximiser.

For \\(n=1\\),

$$
L(\theta;x_1)
=
\frac{1}{\pi\lbrace 1+(x_1-\theta)^2\rbrace }
$$

is maximised uniquely at \\(\widehat\theta=x_1\\).

**Final result.**

$$
\boxed{
\ell'(\theta;x)=
2\sum_{i=1}^n
\frac{x_i-\theta}{1+(x_i-\theta)^2},
\qquad
\ell'(\widehat\theta;x)=0.
}
$$

**Interpretation.**

Unlike the normal location model, the Cauchy likelihood does not reduce to a quadratic function of \\(\theta\\). The MLE is therefore not generally the sample mean and need not have a simple algebraic form.

<div class="remark" markdown="1">

**Remark.**
Maximum likelihood, unbiasedness, minimum MSE, and the UMVUE property are different optimality criteria. An MLE need not be unbiased or a UMVUE, and a UMVUE need not be an MLE.

</div>

## Questions answered in this lecture

**Question.**
What is the difference between an estimator and an estimate?

**Answer.**

The estimator \\(T(X)\\) is a random variable before the sample is observed; the estimate \\(T(x)\\) is its realised numerical value after observing \\(x\\).

**Question.**
Why can an estimator not contain the unknown parameter?

**Answer.**

An estimator must be computable from the observed data and known constants. An expression such as \\(X_1-\theta\\) is not computable without already knowing \\(\theta\\).

**Question.**
Why do we compare variances when all competing estimators are unbiased?

**Answer.**

Because unbiasedness makes the bias term zero, so \\(\operatorname{MSE}\_\theta(T)=\operatorname{Var}\_\theta(T)\\).

**Question.**
Can there be an estimator that is uniformly best among all estimators?

**Answer.**

Generally no. At any fixed parameter value, the constant estimator equal to the target at that value has zero risk; an estimator uniformly beating every such constant would have to equal incompatible constants under overlapping model distributions.

**Question.**
What is the likelihood equation for the Cauchy location parameter?

**Answer.**

For iid \\(\operatorname{Cauchy}(\theta,1)\\) observations it is

$$
\sum_{i=1}^n
\frac{x_i-\theta}{1+(x_i-\theta)^2}=0.
$$

A root is only a candidate MLE; the likelihood must still be globally maximised.

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.
- Expanded source: the complete LaTeX notes and compiled PDF used for this Markdown conversion.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url }})
</nav>

</div>
