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
description: "Develops point estimation, squared-error risk and MSE, maximum likelihood, likelihood equations, Newton–Raphson and Fisher scoring, sufficiency reduction for MLEs, and the invariance principle."
topics:
  - "parametric models"
  - "estimators"
  - "loss and risk"
  - "mean squared error"
  - "bias–variance decomposition"
  - "estimator comparison"
  - "maximum likelihood"
  - "Cauchy location"
  - "Newton–Raphson"
  - "Fisher scoring"
  - "MLE invariance"
  - "MLE and sufficiency"
previous: null
next: "lecture-02-unbiased-estimation-umvue-crlb"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-09-06"
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
- Derive Newton–Raphson and Fisher-scoring iterations for likelihood maximisation.
- Explain why an MLE can be taken to be a function of a sufficient statistic.
- State and prove the invariance principle for MLEs, and contrast it with unbiased and squared-error Bayes estimation.

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
\widehat\theta_{\mathrm{MLE}}\in\underset{\theta\in\Theta}{\operatorname{arg\,max}}\,L(\theta;X).
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

## 6. Newton–Raphson and Fisher scoring for the MLE

The 21 August notes introduce a numerical procedure for solving likelihood equations. For iid data,

$$
X_1,\ldots,X_n\overset{\mathrm{iid}}{\sim}f(x\mid\theta),
$$

the log-likelihood is

$$
\ell_n(\theta)
=
\sum_{i=1}^n\log f(X_i\mid\theta).
$$

Its first derivative is the sample score

$$
U_n(\theta)
=
\ell_n'(\theta)
=
\sum_{i=1}^n
\frac{\partial f(X_i\mid\theta)/\partial\theta}
{f(X_i\mid\theta)}.
$$

An interior MLE therefore satisfies

$$
U_n(\widehat\theta)=0.
$$

When this equation cannot be solved explicitly, one can iterate numerically.

<div class="definition" markdown="1">

**Definition 1.11 — Newton–Raphson iteration for a likelihood equation.**

Starting from an initial value \\(\theta^{(0)}\\), Newton–Raphson applies Newton's method to the equation \\(U_n(\theta)=0\\):

$$
\boxed{
\theta^{(m+1)}
=
\theta^{(m)}
-
\frac{U_n(\theta^{(m)})}
{U_n'(\theta^{(m)})}
}
$$

whenever the denominator is nonzero.

</div>

Because \\(U_n'(\theta)=\ell_n''(\theta)\\), this can also be written as

$$
\theta^{(m+1)}
=
\theta^{(m)}
-
\frac{\ell_n'(\theta^{(m)})}
{\ell_n''(\theta^{(m)})}.
$$

For one observation,

$$
\frac{\partial^2}{\partial\theta^2}
\log f(x\mid\theta)
=
\frac{f_{\theta\theta}(x\mid\theta)}{f(x\mid\theta)}
-
\left(
\frac{f_\theta(x\mid\theta)}{f(x\mid\theta)}
\right)^2,
$$

so for the full sample,

$$
\ell_n''(\theta)
=
\sum_{i=1}^n
\left[
\frac{f_{\theta\theta}(X_i\mid\theta)}{f(X_i\mid\theta)}
-
\left(
\frac{f_\theta(X_i\mid\theta)}{f(X_i\mid\theta)}
\right)^2
\right].
$$

The handwritten note remarks that multiplying the likelihood equation by \\(1/n\\) does not change its roots. This is useful because the average score and average observed curvature have the same zeros and are often numerically better scaled.

### 6.1 From Newton–Raphson to Fisher scoring

Under the regularity conditions from Lecture 2,

$$
\mathcal I_n(\theta)
=
-\operatorname{E}_\theta[\ell_n''(\theta)].
$$

Fisher scoring replaces the random observed curvature \\(-\ell_n''(\theta)\\) by its expectation, the Fisher information.

<div class="definition" markdown="1">

**Definition 1.12 — Fisher-scoring iteration.**

The Fisher-scoring update is

$$
\boxed{
\theta^{(m+1)}
=
\theta^{(m)}
+
\mathcal I_n(\theta^{(m)})^{-1}
U_n(\theta^{(m)}).
}
$$

For a vector parameter, the same formula holds with the score vector and Fisher information matrix.

</div>

The sign is positive because

$$
\operatorname{E}_\theta[\ell_n''(\theta)]
=
-\mathcal I_n(\theta).
$$

So the Newton denominator \\(\ell_n''\\) is replaced by approximately \\(-\mathcal I_n\\), producing

$$
-\frac{U_n}{-\mathcal I_n}
=
\mathcal I_n^{-1}U_n.
$$

<div class="remark" markdown="1">

**Remark — observed versus expected information.**
Newton–Raphson uses the _observed_ second derivative at the current sample and iterate. Fisher scoring uses its expected value. In regular models the two are asymptotically close near the true parameter, but their finite-sample iterations can differ.

</div>

<div class="proposition" markdown="1">

**Proposition 1.13 — Fisher information is parameter-free in a regular location family.**

Suppose

$$
f_\theta(x)=f_0(x-\theta),
$$

with support independent of \\(\theta\\) and the usual differentiability and integrability conditions. Then the Fisher information in one observation does not depend on \\(\theta\\).

</div>

**Proof.**

Let \\(U=X-\theta\\). Under \\(P\_\theta\\), the distribution of \\(U\\) is always \\(f_0\\), independent of \\(\theta\\). The score can be written as a function of \\(U\\) alone:

$$
\mathcal S_\theta(X)
=
-\frac{\mathrm d}{\mathrm du}
\log f_0(u)
\bigg\vert_{u=X-\theta}.
$$

Hence

$$
\mathcal I_1(\theta)
=
\operatorname{E}_\theta[\mathcal S_\theta(X)^2]
=
\int
\left[
\frac{\mathrm d}{\mathrm du}\log f_0(u)
\right]^2
f_0(u)\,\mathrm du,
$$

which contains no \\(\theta\\).

\\(\square\\)

### Worked Example 1.3 — Fisher scoring for a normal mean

**Problem.**

Let

$$
X_1,\ldots,X_n\overset{\mathrm{iid}}{\sim}N(\mu,\sigma^2),
$$

with \\(\sigma^2\\) known. Derive one Fisher-scoring step for \\(\mu\\).

**Solution.**

The score is

$$
U_n(\mu)
=
\frac{1}{\sigma^2}
\sum_{i=1}^n(X_i-\mu)
=
\frac{n}{\sigma^2}(\bar X-\mu).
$$

The Fisher information is

$$
\mathcal I_n(\mu)=\frac{n}{\sigma^2}.
$$

Hence

$$
\begin{aligned}
\mu^{(m+1)}
&=
\mu^{(m)}
+
\frac{\sigma^2}{n}
\frac{n}{\sigma^2}(\bar X-\mu^{(m)})\\
&=\bar X.
\end{aligned}
$$

**Final result.**

From any starting value, Fisher scoring reaches

$$
\boxed{\widehat\mu_{\mathrm{MLE}}=\bar X}
$$

in one step.

## 7. The MLE and sufficient statistics

The 21 August notes connect the Neyman–Fisher factorisation theorem to maximum likelihood.

<div class="proposition" markdown="1">

**Proposition 1.14 — An MLE can be chosen as a function of a sufficient statistic.**

Suppose \\(T(X)\\) is sufficient and the likelihood factorises as

$$
L(\theta;x)
=
g_\theta(T(x))h(x),
$$

where \\(h(x)\\) does not depend on \\(\theta\\). Then the set of likelihood maximisers depends on the sample only through \\(T(x)\\). Consequently, with a fixed tie-breaking rule, an MLE can be chosen as a function of \\(T(X)\\).

</div>

**Proof.**

For fixed observed data \\(x\\), the factor \\(h(x)\\) is constant as a function of \\(\theta\\). Therefore

$$
\underset{\theta\in\Theta}{\operatorname{arg\,max}}\,L(\theta;x)
=
\underset{\theta\in\Theta}{\operatorname{arg\,max}}\,g_\theta(T(x)).
$$

The right side depends on \\(x\\) only through \\(T(x)\\). Thus any deterministic choice from the set of maximisers can be made using only \\(T(x)\\).

\\(\square\\)

> **Key point.** Sufficiency does not say that every statistic computed from the data is a function of \\(T\\). It says that for likelihood maximisation, the part of the likelihood that depends on \\(\theta\\) can be evaluated from \\(T\\) alone.

## 8. Invariance principle of maximum likelihood

<div class="theorem" markdown="1">

**Theorem 1.15 — Invariance of the MLE.**

Let \\(\widehat\theta\\) be an MLE of \\(\theta\\), and let \\(\eta=g(\theta)\\). Under the usual induced-likelihood definition for \\(\eta\\),

$$
\boxed{
\widehat\eta_{\mathrm{MLE}}
=
g(\widehat\theta).
}
$$

</div>

**Proof for one-to-one \\(g\\).**

If \\(g\\) is one-to-one, write \\(\theta=g^{-1}(\eta)\\). The likelihood for \\(\eta\\) is

$$
L_\eta(\eta;x)
=
L(g^{-1}(\eta);x).
$$

Since \\(\widehat\theta\\) maximises \\(L(\theta;x)\\), the value \\(g(\widehat\theta)\\) maximises \\(L\_\eta(\eta;x)\\). Hence

$$
\widehat\eta=g(\widehat\theta).
$$

For a many-to-one transformation, define the profile likelihood

$$
L_\eta(\eta;x)
=
\sup_{\theta:g(\theta)=\eta}L(\theta;x).
$$

If \\(\widehat\theta\\) is a global maximiser of the original likelihood, then \\(g(\widehat\theta)\\) attains the maximum of this profile likelihood.

\\(\square\\)

### Why unbiased estimators are not invariant in this sense

Suppose \\(T\\) is unbiased for \\(\theta\\). In general,

$$
\operatorname{E}_\theta[g(T)]
\neq
g(\operatorname{E}_\theta[T])
=
g(\theta).
$$

So \\(g(T)\\) need not be unbiased for \\(g(\theta)\\). If \\(g\\) is affine,

$$
g(t)=a+bt,
$$

then expectation passes through the transformation and invariance is recovered:

$$
\operatorname{E}[g(T)]
=a+b\operatorname{E}[T]
=g(\theta).
$$

### Why squared-error Bayes estimators are not generally invariant

Under squared-error loss, the Bayes estimator of \\(\theta\\) is

$$
\delta_\pi(X)=\operatorname{E}[\theta\mid X].
$$

The Bayes estimator of \\(g(\theta)\\) is instead

$$
\operatorname{E}[g(\theta)\mid X],
$$

which generally differs from

$$
g\!\left(\operatorname{E}[\theta\mid X]\right).
$$

Again, equality holds automatically for affine \\(g\\), but not for nonlinear transformations.

<div class="remark" markdown="1">

**Editorial note — source reference to Assignment 1.**
The 21 August page says “solve Q3 when \\(\sigma^2\\) is unknown (of Assignment 1).” The statement of Assignment 1, Question 3 is not contained in the supplied PDFs, so reproducing a solution here would require inventing the missing problem. The reference is retained, but no unsupported solution is inserted.

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

**Question.**
What is the difference between Newton–Raphson and Fisher scoring?

**Answer.**

Newton–Raphson uses the observed second derivative \\(\ell_n''(\theta)\\), whereas Fisher scoring replaces \\(-\ell_n''(\theta)\\) by its expectation \\(\mathcal I_n(\theta)\\). Thus

$$
\theta^{(m+1)}
=
\theta^{(m)}
-
\frac{U_n(\theta^{(m)})}{\ell_n''(\theta^{(m)})}
$$

for Newton–Raphson, while

$$
\theta^{(m+1)}
=
\theta^{(m)}
+
\mathcal I_n(\theta^{(m)})^{-1}U_n(\theta^{(m)})
$$

for Fisher scoring.

**Question.**
Why can an MLE be taken to be a function of a sufficient statistic?

**Answer.**

Factorisation writes the likelihood as \\(g\_\theta(T(x))h(x)\\). Since \\(h(x)\\) does not depend on \\(\theta\\), maximising the likelihood is equivalent to maximising \\(g\_\theta(T(x))\\), which depends on the data only through \\(T(x)\\).

**Question.**
What is the invariance principle of the MLE?

**Answer.**

If \\(\widehat\theta\\) is an MLE of \\(\theta\\), then the MLE of \\(g(\theta)\\) is \\(g(\widehat\theta)\\), using the induced or profile likelihood. This property does not generally hold for unbiased or squared-error Bayes estimators under nonlinear \\(g\\).

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.
- Expanded source: the complete LaTeX notes and compiled PDF used for this Markdown conversion.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url }})
</nav>

</div>
