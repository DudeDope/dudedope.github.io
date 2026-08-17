---
layout: page
title: "Parametric Inference — Formula and Notation Sheet"
course: "Parametric Inference"
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Cumulative notation, identities, estimator formulas, regularity conditions, testing results, exponential-family forms, and Bayesian updating formulas for the Parametric Inference lectures."
last_updated: "2026-08-17"
status: "complete"
math: true
permalink: /notes/parametric-inference/formula-sheet/
course_slug: parametric-inference
note_kind: formula-sheet
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** This cumulative sheet accompanies the unofficial expanded Fall 2026 Parametric Inference notes based on lectures of Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Course contents]({{ '/notes/parametric-inference/' | relative_url }})
</nav>

This is a cumulative reference for the eight-lecture version of the notes. It is not a substitute for the derivations in the lecture files. Distributional identities that previously appeared as a standalone chapter have been moved here and remain cross-referenced to the lectures where they are used.

## 1. Global notation

- \\(\theta\\) denotes a scalar parameter unless a vector parameter is explicitly introduced; \\(\Theta\\) is its parameter space. First used in [Lecture 1]({{ '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url }}).
- \\(\psi(\theta)\\) is the parametric function being estimated. First used in [Lecture 1]({{ '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url }}).
- \\(X=(X_1,\ldots,X_n)\\) is the random sample and \\(x=(x_1,\ldots,x_n)\\) its realised value. First used in [Lecture 1]({{ '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url }}).
- \\(T=T(X)\\) is a statistic and, when used to estimate a target, an estimator. \\(T(x)\\) is the realised estimate. First used in [Lecture 1]({{ '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url }}).
- \\(\operatorname{E}\_\theta\\), \\(\operatorname{Var}\_\theta\\), and \\(\operatorname{Cov}\_\theta\\) denote expectation, variance, and covariance under \\(P\_\theta\\).
- “Unique” means unique up to almost-sure equality under every model distribution; see [Lecture 2]({{ '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url }}).

## 2. Lecture 1 — Point estimation, risk, and MSE

### Loss, risk, and estimator comparison

For a loss function \\(L(\theta,a)\\), the risk of an estimator \\(T\\) is

$$
R(\theta,T)=\operatorname{E}_\theta\!\left[L\bigl(\theta,T(X)\bigr)\right].
$$

Under squared-error loss for target \\(\psi(\theta)\\),

$$
L(\theta,a)=\bigl(a-\psi(\theta)\bigr)^2,
$$

and therefore

$$
R(\theta,T)=\operatorname{E}_\theta\left[(T-\psi(\theta))^2\right]
=\operatorname{MSE}_\theta(T).
$$

Uniform comparison means \\(T_1\\) is at least as good as \\(T_2\\) if

$$
R(\theta,T_1)\le R(\theta,T_2)\qquad\text{for every }\theta\in\Theta.
$$

See [Lecture 1]({{ '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url }}).

### Bias and mean squared error

The bias of \\(T\\) for \\(\psi(\theta)\\) is

$$
\operatorname{Bias}_\theta(T)
=\operatorname{E}_\theta[T]-\psi(\theta).
$$

If \\(\operatorname{E}\_\theta[T^2]<\infty\\), then

$$
\operatorname{MSE}_\theta(T)
=\operatorname{Var}_\theta(T)
+\operatorname{Bias}_\theta(T)^2.
$$

For an unbiased estimator, the second term is zero, so

$$
\operatorname{MSE}_\theta(T)=\operatorname{Var}_\theta(T).
$$

See [Lecture 1]({{ '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url }}).

### Likelihood and maximum likelihood

For observed data \\(x\\) with joint density or mass function \\(f\_\theta(x)\\),

$$
L(\theta;x)=f_\theta(x),
\qquad
\ell(\theta;x)=\log L(\theta;x).
$$

An MLE satisfies

$$
\widehat\theta_{\mathrm{MLE}}
\in
\mathop{\mathrm{arg\,max}}_{\theta\in\Theta}L(\theta;x).
$$

At an interior differentiability point, the likelihood equation is

$$
\frac{\partial}{\partial\theta}\ell(\theta;x)=0,
$$

but solving this equation is only a necessary step; global maximisation still has to be checked.

For iid \\(\operatorname{Cauchy}(\theta,1)\\) observations,

$$
\ell(\theta;x)
=
-n\log\pi
-
\sum_{i=1}^n\log\lbrace 1+(x_i-\theta)^2\rbrace ,
$$

and

$$
\ell'(\theta;x)
=
2\sum_{i=1}^n
\frac{x_i-\theta}{1+(x_i-\theta)^2}.
$$

Thus every interior MLE must satisfy

$$
\boxed{
\sum_{i=1}^n
\frac{x_i-\widehat\theta}
{1+(x_i-\widehat\theta)^2}
=0.
}
$$

See [Lecture 1]({{ '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url }}).

## 3. Lecture 2 — Unbiased estimation, UMVUEs, and CRLB

### UMVUE

An estimator \\(T^{\ast}\\) is a UMVUE of \\(\psi(\theta)\\) when

$$
\operatorname{E}_\theta[T^{\ast}]=\psi(\theta)
$$

for every \\(\theta\\), and for every other unbiased estimator \\(U\\),

$$
\operatorname{Var}_\theta(T^{\ast})
\le
\operatorname{Var}_\theta(U)
\qquad\text{for every }\theta.
$$

If \\(T_1\\) and \\(T_2\\) are both UMVUEs with common variance \\(v\_\theta\\), then for \\(W=(T_1+T_2)/2\\),

$$
\operatorname{Var}_\theta(W)
=v_\theta-\frac14\operatorname{Var}_\theta(T_1-T_2).
$$

Minimality forces \\(\operatorname{Var}\_\theta(T_1-T_2)=0\\), proving almost-sure uniqueness. See [Lecture 2]({{ '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url }}).

### Score, Fisher information, and CRLB

For a regular scalar model with density or mass function \\(f\_\theta\\),

$$
\mathcal S_\theta(X)
=\frac{\partial}{\partial\theta}\log f_\theta(X)
$$

is the score. Under the interchange-of-differentiation regularity condition,

$$
\operatorname{E}_\theta[\mathcal S_\theta(X)]=0.
$$

The Fisher information in one observation is

$$
\mathcal I_1(\theta)
=\operatorname{E}_\theta[\mathcal S_\theta(X)^2],
$$

and for iid data,

$$
\mathcal I_n(\theta)=n\mathcal I_1(\theta).
$$

When the second-derivative identity is valid,

$$
\mathcal I_1(\theta)
=-\operatorname{E}_\theta\left[
\frac{\partial^2}{\partial\theta^2}\log f_\theta(X)
\right].
$$

If \\(T\\) is unbiased for \\(\psi(\theta)\\) and the ordinary CRLB regularity assumptions hold,

$$
\operatorname{Var}_\theta(T)
\ge
\frac{\bigl(\psi'(\theta)\bigr)^2}{\mathcal I_n(\theta)}.
$$

Equality at a parameter value holds exactly when

$$
T(X)-\psi(\theta)=a(\theta)\mathcal S_\theta(X)
$$

almost surely, with

$$
a(\theta)=\frac{\psi'(\theta)}{\mathcal I_n(\theta)}
$$

for an unbiased efficient estimator.

For vector parameter \\(\eta\\) and scalar target \\(g(\eta)\\),

$$
\operatorname{Var}_\eta(T)
\ge
\nabla g(\eta)^\top
\mathcal I_n(\eta)^{-1}
\nabla g(\eta).
$$

**Regularity warning:** the ordinary formula should not be used blindly when the support depends on the parameter. See [Lecture 2]({{ '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url }}).

### Standard estimation examples

### Normal mean with known variance

For iid \\(N(\theta,\sigma^2)\\) with known \\(\sigma^2\\),

$$
\operatorname{Var}(\overline X)=\frac{\sigma^2}{n},
\qquad
\mathcal I_n(\theta)=\frac{n}{\sigma^2}.
$$

Thus \\(\overline X\\) attains the CRLB \\(\sigma^2/n\\).

### Exponential mean

For iid exponential observations with mean \\(\theta\\),

$$
\operatorname{Var}(\overline X)=\frac{\theta^2}{n},
\qquad
\mathcal I_n(\theta)=\frac{n}{\theta^2},
$$

so \\(\overline X\\) again attains the CRLB.

### Normal variance with unknown mean

Let

$$
Q=\sum_{i=1}^n(X_i-\overline X)^2,
\qquad
\frac{Q}{\sigma^2}\sim\chi^2_{n-1}.
$$

Then

$$
\operatorname{E}[Q]=(n-1)\sigma^2,
\qquad
\operatorname{Var}(Q)=2(n-1)\sigma^4.
$$

The unbiased sample variance is

$$
S^2=\frac{Q}{n-1},
\qquad
\operatorname{Var}(S^2)=\frac{2\sigma^4}{n-1}.
$$

For \\(T_c=cQ\\),

$$
\operatorname{MSE}(T_c)
=\sigma^4\left[
2c^2(n-1)+\bigl(c(n-1)-1\bigr)^2
\right].
$$

The minimiser within this class is

$$
c^{\ast}=\frac{1}{n+1},
$$

with

$$
\operatorname{MSE}(T_{c^{\ast}})=\frac{2\sigma^4}{n+1}.
$$

With parameter \\(\eta=(\mu,\sigma^2)\\),

$$
\mathcal I_n(\mu,\sigma^2)
=
\begin{pmatrix}
n/\sigma^2 & 0\\
0 & n/(2\sigma^4)
\end{pmatrix},
$$

and the matrix CRLB for unbiased estimation of \\(\sigma^2\\) is \\(2\sigma^4/n\\), although it is not attainable by a statistic when \\(\mu\\) is unknown. See [Lecture 2]({{ '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url }}).

## 4. Lecture 3 — Existence and uniqueness of unbiased estimators

For \\(X\sim\operatorname{Bin}(n,\theta)\\),

$$
\operatorname{E}_\theta[T(X)]
=\sum_{x=0}^n T(x)\binom nx\theta^x(1-\theta)^{n-x},
$$

so an unbiasedly estimable target must be a polynomial in \\(\theta\\) of degree at most \\(n\\). Falling factorials satisfy

$$
\operatorname{E}_\theta[(X)_k]=(n)_k\theta^k,
$$

hence

$$
\frac{(X)_k}{(n)_k}
$$

is unbiased for \\(\theta^k\\).

For \\(X\sim\operatorname{Poisson}(\theta)\\),

$$
e^\theta\psi(\theta)
=\sum_{x=0}^{\infty}T(x)\frac{\theta^x}{x!}.
$$

Under integrability for every positive \\(\theta\\), the series has infinite radius of convergence, giving the entire-function condition and the coefficient identity

$$
T(x)=\left.\frac{d^x}{dz^x}\bigl(e^z\psi(z)\bigr)\right\rvert_{z=0}.
$$

For one exponential observation with mean \\(\theta\\), uniqueness is obtained from

$$
\int_0^\infty h(x)e^{-sx}\,\mathrm dx=0
\qquad\text{for every }s>0,
$$

where \\(h(x)=T(x)-x\\). Laplace-transform uniqueness gives \\(h=0\\) almost everywhere. See [Lecture 3]({{ '/notes/parametric-inference/lecture-03-existence-uniqueness-unbiased-estimators/' | relative_url }}).

### Negative-binomial stopping at the second tail

If \\(\Pr(H)=\theta\\) and \\(N\\) is the total number of tosses required to observe two tails, then

$$
\Pr_\theta(N=n)
=
(n-1)\theta^{n-2}(1-\theta)^2,
\qquad
n=2,3,\ldots.
$$

The statistic

$$
\boxed{
\widehat\theta
=
1-\frac1{N-1}
=
\frac{N-2}{N-1}
}
$$

is unbiased because

$$
\operatorname{E}_\theta\left[\frac1{N-1}\right]
=
1-\theta.
$$

This corrects the contrary statement in the handwritten source. See [Lecture 3]({{ '/notes/parametric-inference/lecture-03-existence-uniqueness-unbiased-estimators/' | relative_url }}).

## 5. Lecture 4 — Sufficiency, Rao–Blackwell, and ancillarity

### Sufficiency

A statistic \\(S\\) is sufficient for \\(\theta\\) when the conditional distribution of \\(X\\) given \\(S\\) does not depend on \\(\theta\\).

The Neyman-Fisher factorisation criterion is

$$
f_\theta(x)=g_\theta(S(x))h(x),
$$

where \\(h\\) is free of \\(\theta\\).

Canonical sufficient statistics from the lecture are

- Bernoulli sample: \\(S=\sum_iX_i\\);
- Poisson sample: \\(S=\sum_iX_i\\);
- exponential sample with mean \\(\theta\\): \\(S=\sum_iX_i\\);
- uniform endpoint model: \\(M=X\_{(n)}\\).

See [Lecture 4]({{ '/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell-ancillarity/' | relative_url }}).

### Rao–Blackwell theorem

Given a sufficient statistic \\(S\\) and an estimator \\(U\\) with finite second moment, define

$$
U^{\ast}=\operatorname{E}[U\mid S].
$$

Then

$$
\operatorname{E}[U^{\ast}]=\operatorname{E}[U]
$$

and, under squared-error loss,

$$
\operatorname{MSE}_\theta(U^{\ast})
\le
\operatorname{MSE}_\theta(U).
$$

For unbiased estimators,

$$
\operatorname{Var}_\theta(U^{\ast})
\le
\operatorname{Var}_\theta(U).
$$

The decomposition behind the result is

$$
\operatorname{MSE}_\theta(U)
=
\operatorname{E}_\theta[\operatorname{Var}_\theta(U\mid S)]
+
\operatorname{MSE}_\theta(U^{\ast}).
$$

In the exponential sample,

$$
\operatorname{E}[X_1\mid S]=\frac{S}{n}=\overline X.
$$

See [Lecture 4]({{ '/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell-ancillarity/' | relative_url }}).

### Additional sufficient statistics

For iid \\(N(\theta,1)\\),

$$
f_\theta(x)
\propto
\exp\left\lbrace \theta\sum_{i=1}^n x_i-\frac n2\theta^2
\right\rbrace ,
$$

so

$$
\sum_{i=1}^nX_i
$$

is sufficient.

For iid \\(\operatorname{Beta}(\theta,d)\\) with both parameters unknown,

$$
S=
\left(
\prod_iX_i,\,
\prod_i(1-X_i)
\right)
$$

is sufficient, equivalently

$$
\left(
\sum_i\log X_i,\,
\sum_i\log(1-X_i)
\right).
$$

### Ancillary statistics

A statistic \\(A(X)\\) is ancillary if its distribution is free of \\(\theta\\).

In a location family \\(X_i=\theta+Z_i\\), any translation-invariant statistic such as a range or difference has a distribution independent of \\(\theta\\).

For iid \\(\operatorname{Uniform}(\theta,\theta+1)\\),

$$
S=(X_{(1)},X_{(n)})
$$

is sufficient,

$$
R=X_{(n)}-X_{(1)}
$$

is ancillary, and \\(S\\) is therefore not complete.

The Rao–Blackwell improvement of \\(\bar X-\tfrac12\\) is

$$
\boxed{
\frac{X_{(1)}+X_{(n)}}2-\frac12.
}
$$

See [Lecture 4]({{ '/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell-ancillarity/' | relative_url }}).

## 6. Lecture 5 — Completeness, exponential families, and Basu’s theorem

### Standard models

A statistic \\(S\\) is complete if

$$
\operatorname{E}_\theta[g(S)]=0
\quad\text{for every }\theta
$$

implies

$$
g(S)=0
$$

almost surely under every model distribution.

The key model-specific identities are:

- binomial total: a polynomial in \\(z=\theta/(1-\theta)\\) must vanish coefficientwise;
- Poisson total:

$$
\sum_{s=0}^{\infty}g(s)\frac{\lambda^s}{s!}=0;
$$

- exponential sum:

$$
\int_0^\infty g(s)s^{n-1}e^{-us}\,\mathrm ds=0;
$$

- uniform maximum:

$$
\int_0^\theta g(m)m^{n-1}\,\mathrm dm=0.
$$

Polynomial, power-series, Laplace-transform, and absolute-continuity uniqueness arguments respectively prove completeness. See [Lecture 5]({{ '/notes/parametric-inference/lecture-05-completeness-exponential-families-basu/' | relative_url }}).

### Full natural exponential families

For a natural exponential family

$$
f_\eta(x)
=h(x)\exp\lbrace \eta^\top T(x)-A(\eta)\rbrace ,
$$

if the natural parameter space contains a nonempty open set and

$$
\operatorname{E}_\eta[g(T)]=0
$$

throughout that set, then

$$
\int g(T(x))h(x)e^{\eta^\top T(x)}\,\mathrm dx=0.
$$

The left side is a multivariate Laplace transform. Uniqueness of that transform implies \\(g(T)=0\\) almost surely, establishing completeness under the stated full-family conditions. See [Lecture 5]({{ '/notes/parametric-inference/lecture-05-completeness-exponential-families-basu/' | relative_url }}).

### Exponential-family form

A one-parameter natural exponential family has form

$$
f_\eta(x)
=
h(x)\exp\lbrace \eta T(x)-A(\eta)\rbrace ,
$$

with support independent of \\(\eta\\).

For an iid sample,

$$
S=\sum_{i=1}^nT(X_i)
$$

is sufficient.

If the natural parameter space contains a nonempty open interval, \\(S\\) is complete under the standard integrability conditions.

For a \\(k\\)-parameter family,

$$
f_\eta(x)
=
h(x)
\exp\left\lbrace \sum_{j=1}^k\eta_jT_j(x)-A(\eta)
\right\rbrace ,
$$

the canonical statistic is

$$
S=
\left(
\sum_iT_1(X_i),\ldots,\sum_iT_k(X_i)
\right).
$$

If the natural parameter space contains a nonempty open subset of \\(\mathbb R^k\\), then \\(S\\) is complete.

### Canonical examples

Binomial:

$$
\eta=\log\frac{\theta}{1-\theta},
\qquad
T(x)=x.
$$

Poisson:

$$
\eta=\log\theta,
\qquad
T(x)=x.
$$

Normal \\(N(\theta,1)\\):

$$
\eta=\theta,
\qquad
T(x)=x.
$$

Gamma with known shape \\(\nu\\) and scale \\(\theta\\):

$$
\eta=-\frac1\theta,
\qquad
T(x)=x.
$$

Normal with both \\(\mu\\) and \\(\sigma^2\\) unknown:

$$
S=
\left(
\sum_iX_i,\,
\sum_iX_i^2
\right),
$$

with natural parameters

$$
\eta_1=\frac{\mu}{\sigma^2},
\qquad
\eta_2=-\frac1{2\sigma^2}.
$$

### Power-series family

For

$$
f_\theta(x)
=
\frac{a(x)\theta^x}{g(\theta)},
\qquad
x=0,1,\ldots,
$$

we have

$$
\eta=\log\theta,
\qquad
T(x)=x.
$$

Hence \\(\sum_iX_i\\) is complete sufficient whenever the natural parameter interval has nonempty interior.

### Uniform with both endpoints unknown

For iid \\(\operatorname{Uniform}(\phi,\psi)\\), \\(\phi<\psi\\),

$$
S=(X_{(1)},X_{(n)})
$$

is complete sufficient for \\((\phi,\psi)\\) when \\(n\ge2\\), with joint density

$$
f_{U,V}(u,v)
=
\frac{n(n-1)}{(\psi-\phi)^n}
(v-u)^{n-2}
\mathbf 1_{\lbrace \phi<u<v<\psi\rbrace }.
$$

### Basu's theorem

If \\(T\\) is complete sufficient for \\(\theta\\) and \\(A\\) is ancillary, then

$$
\boxed{T\perp A.}
$$

For iid \\(N(\theta,\sigma^2)\\) with known \\(\sigma^2\\),

$$
\bar X
\perp
\sum_{i=1}^n(X_i-\bar X)^2.
$$

The residual sum of squares is ancillary only with respect to \\(\theta\\) when \\(\sigma^2\\) is known.

See [Lecture 5]({{ '/notes/parametric-inference/lecture-05-completeness-exponential-families-basu/' | relative_url }}).

## 7. Lecture 6 — Lehmann–Scheffé, UMVUE constructions, and consistency

### Lehmann–Scheffé theorem

If \\(S\\) is complete and sufficient and \\(h(S)\\) is unbiased for \\(\psi(\theta)\\), then \\(h(S)\\) is the unique UMVUE.

For any unbiased \\(U\\), Rao-Blackwellisation gives

$$
U^{\ast}=\operatorname{E}[U\mid S],
$$

with

$$
\operatorname{Var}_\theta(U^{\ast})\le\operatorname{Var}_\theta(U).
$$

Completeness forces

$$
U^{\ast}=h(S)
$$

almost surely. See [Lecture 6]({{ '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-consistency/' | relative_url }}).

### Canonical UMVUE formulas

For Bernoulli data with \\(S=\sum_iX_i\\),

$$
\widehat\theta_{\mathrm{UMVUE}}=\frac{S}{n},
\qquad
\widehat{\theta^k}_{\mathrm{UMVUE}}=\frac{(S)_k}{(n)_k}.
$$

For Poisson data with total \\(S\\),

$$
\widehat\theta_{\mathrm{UMVUE}}=\frac{S}{n},
\qquad
\widehat{\theta^k}_{\mathrm{UMVUE}}=\frac{(S)_k}{n^k}.
$$

For exponential data with mean \\(\theta\\) and sum \\(S\\),

$$
\widehat\theta_{\mathrm{UMVUE}}=\frac{S}{n},
$$

and, because \\(S\sim\operatorname{Gamma}(n,\text{scale }\theta)\\),

$$
\widehat{\theta^k}_{\mathrm{UMVUE}}
=
\frac{\Gamma(n)}{\Gamma(n+k)}S^k.
$$

For iid \\(\operatorname{Uniform}(0,\theta)\\) observations,

$$
\widehat\theta_{\mathrm{UMVUE}}
=
\frac{n+1}{n}X_{(n)}.
$$

For normal data with both \\(\mu\\) and \\(\sigma^2\\) unknown,

$$
S^2
=
\frac{1}{n-1}\sum_{i=1}^n(X_i-\overline X)^2
$$

is the unique UMVUE of \\(\sigma^2\\). See [Lecture 6]({{ '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-consistency/' | relative_url }}).

### Logical implications

The lecture separates the following statements:

1. A **unique unbiased estimator** is automatically a UMVUE.
2. A **unique UMVUE** may coexist with other unbiased estimators of larger variance.
3. In a regular model, an unbiased estimator that attains the CRLB at every parameter value is a UMVUE.
4. The converse need not hold: a UMVUE may fail to attain an unattainable bound.
5. In a nonregular model such as \\(\operatorname{Uniform}(0,\theta)\\), the ordinary CRLB may not apply.

See [Lecture 6]({{ '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-consistency/' | relative_url }}).

### Consistency of UMVUE sequences

Weak consistency for \\(\psi(\theta)\\) means

$$
T_n\xrightarrow{P_\theta}\psi(\theta).
$$

If a one-observation unbiased estimator \\(U(X_1)\\) exists with finite variance and \\(T_n\\) is a UMVUE based on \\(n\\) iid observations, then

$$
\operatorname{Var}_\theta(T_n)
\le
\frac{\operatorname{Var}_\theta(U(X_1))}{n}.
$$

Therefore

$$
\operatorname{MSE}_\theta(T_n)
=
\operatorname{Var}_\theta(T_n)
\to0,
$$

and Chebyshev's inequality gives

$$
T_n\xrightarrow{P_\theta}\psi(\theta).
$$

See [Lecture 6]({{ '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-consistency/' | relative_url }}).

## 8. Lecture 7 — Hypothesis testing and likelihood ratios

A randomized test is a measurable function

$$
\phi(X)\in[0,1],
$$

interpreted as the probability of rejecting \\(H_0\\) after observing \\(X\\).

The power function is

$$
\boxed{
\beta_\phi(\theta)
=
\operatorname{E}_\theta[\phi(X)].
}
$$

The size is

$$
\boxed{
\alpha(\phi)
=
\sup_{\theta\in\Theta_0}
\beta_\phi(\theta).
}
$$

For a simple null \\(\theta=\theta_0\\),

$$
\alpha(\phi)=E_{\theta_0}[\phi(X)].
$$

If \\(T\\) is sufficient, the test

$$
\psi(T)=\operatorname{E}[\phi(X)\mid T]
$$

has the same power function:

$$
\operatorname{E}_\theta[\psi(T)]
=
\operatorname{E}_\theta[\phi(X)]
\qquad
\forall\theta.
$$

For simple hypotheses

$$
H_0:\theta=\theta_0,
\qquad
H_1:\theta=\theta_1,
$$

the likelihood ratio in favour of \\(H_1\\) is

$$
\Lambda(x)
=
\frac{f_{\theta_1}(x)}{f_{\theta_0}(x)}.
$$

The Neyman–Pearson most powerful level-\\(\alpha\\) test rejects for large \\(\Lambda(x)\\), with possible randomization on the boundary.

Let \\(\Phi\\) denote the standard normal cdf and \\(z_q=\Phi^{-1}(q)\\) its \\(q\\)th quantile. For \\(X\sim N(\theta,1)\\) and \\(\theta_1>\theta_0\\),

$$
\log\Lambda(x)
=
(\theta_1-\theta_0)x
-\frac12(\theta_1^2-\theta_0^2),
$$

so the most powerful level-\\(\alpha\\) test rejects when

$$
\boxed{
X>\theta_0+z_{1-\alpha}.
}
$$

For iid \\(N(\theta,\sigma^2)\\) observations, reject when

$$
\boxed{
\bar X
>
\theta_0+
\frac{\sigma}{\sqrt n}z_{1-\alpha}.
}
$$

See [Lecture 7]({{ '/notes/parametric-inference/lecture-07-hypothesis-testing-likelihood-ratio/' | relative_url }}).

## 9. Lecture 8 — Bayesian point estimation and Bayes risk

Bayes' formula:

$$
\boxed{
\pi(\theta\mid x)
=
\frac{
f(x\mid\theta)\pi(\theta)
}{
\int f(x\mid u)\pi(u)\,\mathrm du
}.
}
$$

Under squared-error loss, the Bayes estimator is the posterior mean:

$$
\boxed{
\delta_\pi(X)
=
\operatorname{E}[\theta\mid X].
}
$$

The posterior expected-loss decomposition is

$$
\operatorname{E}[(a-\theta)^2\mid X]
=
\operatorname{Var}(\theta\mid X)
+
\lbrace a-\operatorname{E}(\theta\mid X)\rbrace ^2.
$$

The Bayes risk is

$$
r_\pi(\delta)
=
\int R(\theta,\delta)\pi(\theta)\,\mathrm d\theta
=
\operatorname{E}_m[L(\theta,\delta(X))].
$$

For the posterior-mean Bayes rule,

$$
\boxed{
r_\pi(\delta_\pi)
=
\operatorname{E}[
\operatorname{Var}(\theta\mid X)
].
}
$$

and for any \\(\delta\\),

$$
r_\pi(\delta)-r_\pi(\delta_\pi)
=
\operatorname{E}[
\lbrace \delta(X)-\delta_\pi(X)\rbrace ^2
].
$$

### Conjugate updates

Beta-binomial:

$$
\theta\sim\operatorname{Beta}(a,b),
\quad
X\mid\theta\sim\operatorname{Binomial}(n,\theta)
$$

implies

$$
\boxed{
\theta\mid X=x
\sim
\operatorname{Beta}(a+x,b+n-x).
}
$$

Gamma-Poisson, using a rate \\(b\\):

$$
\theta\sim\operatorname{Gamma}(a,b),
\quad
X_i\mid\theta\sim\operatorname{Poisson}(\theta),
$$

with \\(S=\sum_iX_i\\), gives

$$
\boxed{
\theta\mid X
\sim
\operatorname{Gamma}(a+S,b+n).
}
$$

Normal-normal:

$$
X\mid\theta\sim N(\theta,\sigma^2),
\qquad
\theta\sim N(\mu,\tau^2)
$$

gives

$$
v=
\left(
\frac1{\sigma^2}
+
\frac1{\tau^2}
\right)^{-1},
$$

$$
m=
v\left(
\frac{x}{\sigma^2}
+
\frac{\mu}{\tau^2}
\right),
$$

and

$$
\boxed{
\theta\mid X=x\sim N(m,v).
}
$$

For \\(n\\) iid observations,

$$
v_n=
\left(
\frac n{\sigma^2}
+
\frac1{\tau^2}
\right)^{-1},
$$

$$
m_n=
v_n\left(
\frac{n\bar X}{\sigma^2}
+
\frac{\mu}{\tau^2}
\right).
$$

### Sufficiency and the posterior

If

$$
f(x\mid\theta)
=
g_\theta(T(x))h(x),
$$

then

$$
\pi(\theta\mid x)
=
\pi(\theta\mid T(x)).
$$

Thus posterior means and other posterior summaries are functions of the sufficient statistic.

### Improper flat prior for a normal mean

For iid \\(N(\theta,1)\\) data with

$$
\pi(\theta)\propto1,
$$

the generalized posterior is

$$
\theta\mid x
\sim
N\left(\bar x,\frac1n\right),
$$

so the generalized Bayes estimator is

$$
\boxed{\bar X.}
$$

See [Lecture 8]({{ '/notes/parametric-inference/lecture-08-bayesian-inference-bayes-risk/' | relative_url }}).

## 10. Useful distributional identities

For \\(X\sim\operatorname{Bin}(n,\theta)\\),

$$
\operatorname{E}[(X)_k]=(n)_k\theta^k.
$$

For \\(X\sim\operatorname{Poisson}(\lambda)\\),

$$
\operatorname{E}[(X)_k]=\lambda^k.
$$

If \\(Y\sim\chi^2\_\nu\\),

$$
\operatorname{E}[Y]=\nu,
\qquad
\operatorname{Var}(Y)=2\nu,
\qquad
\operatorname{E}[Y^2]=\nu(\nu+2).
$$

If \\(S\sim\operatorname{Gamma}(\alpha,\text{scale }\theta)\\),

$$
\operatorname{E}[S^k]
=
\theta^k\frac{\Gamma(\alpha+k)}{\Gamma(\alpha)}.
$$

See [the useful distributional identities section]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}).

## 11. Quick model comparison

| Model                                               | Complete sufficient statistic | Typical target               | UMVUE               |
| --------------------------------------------------- | ----------------------------- | ---------------------------- | ------------------- |
| Bernoulli\\((\theta)\\), iid                        | \\(S=\sum X_i\\)              | \\(\theta\\)                 | \\(S/n\\)           |
| Binomial\\((n,\theta)\\), one count                 | \\(X\\)                       | \\(\theta^k\\), \\(k\le n\\) | \\((X)\_k/(n)\_k\\) |
| Poisson\\((\theta)\\), iid                          | \\(S=\sum X_i\\)              | \\(\theta^k\\)               | \\((S)\_k/n^k\\)    |
| Exponential, mean \\(\theta\\)                      | \\(S=\sum X_i\\)              | \\(\theta\\)                 | \\(S/n\\)           |
| Uniform\\((0,\theta)\\)                             | \\(M=X\_{(n)}\\)              | \\(\theta\\)                 | \\((n+1)M/n\\)      |
| Normal\\((\theta,\sigma^2)\\), \\(\sigma^2\\) known | \\(\overline X\\)             | \\(\theta\\)                 | \\(\overline X\\)   |
| Normal\\((\mu,\sigma^2)\\), both unknown            | \\((\sum X_i,\sum X_i^2)\\)   | \\(\sigma^2\\)               | \\(Q/(n-1)\\)       |

See [the quick model comparison]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}).

## 12. Quick conceptual comparison

| Concept         | What is compared or required?                                         | Typical tool                               |
| --------------- | --------------------------------------------------------------------- | ------------------------------------------ |
| Unbiasedness    | \\(\operatorname{E}\_\theta[T]=\psi(\theta)\\) for every \\(\theta\\) | Direct expectation                         |
| MSE             | Average squared error                                                 | Bias-variance decomposition                |
| UMVUE           | Variance among unbiased estimators                                    | CRLB or Lehmann-Scheffe                    |
| Sufficiency     | Conditional law given \\(S\\) is parameter-free                       | Factorisation theorem                      |
| Completeness    | Zero expectation for all parameters forces zero function              | Polynomial / analytic / Laplace uniqueness |
| Rao-Blackwell   | Improve an estimator by conditioning                                  | Conditional expectation                    |
| CRLB            | Lower bound for unbiased variance in regular models                   | Fisher information                         |
| Lehmann-Scheffe | Unique UMVUE from complete sufficiency                                | Rao-Blackwell + completeness               |

[Course contents]({{ '/notes/parametric-inference/' | relative_url }})

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Course contents]({{ '/notes/parametric-inference/' | relative_url }})
</nav>

</div>
