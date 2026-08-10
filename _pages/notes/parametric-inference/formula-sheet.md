---
layout: page
title: "Parametric Inference — Formula and Notation Sheet"
description: "A cumulative formula, notation, and comparison sheet for the Parametric Inference lecture series."
course: "Parametric Inference"
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
last_updated: "2026-08-11"
status: "living"
math: true
permalink: /notes/parametric-inference/formula-sheet/
course_slug: parametric-inference
note_kind: formula-sheet
course_order: 99
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

This is a cumulative reference for the six-lecture version of the notes. It is not a substitute for the derivations in the lecture files. Distributional identities that previously appeared as a standalone chapter have been moved here and remain cross-referenced to the lectures where they are used.

## 1. Global notation

- $\theta$ denotes a scalar parameter unless a vector parameter is explicitly introduced; $\Theta$ is its parameter space. First used in [Lecture 1]({{ '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url }}).
- $\psi(\theta)$ is the parametric function being estimated. First used in [Lecture 1]({{ '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url }}).
- $X=(X_1,\ldots,X_n)$ is the random sample and $x=(x_1,\ldots,x_n)$ its realised value. First used in [Lecture 1]({{ '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url }}).
- $T=T(X)$ is a statistic and, when used to estimate a target, an estimator. $T(x)$ is the realised estimate. First used in [Lecture 1]({{ '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url }}).
- $\operatorname{E}_\theta$, $\operatorname{Var}_\theta$, and $\operatorname{Cov}_\theta$ denote expectation, variance, and covariance under $P_\theta$.
- “Unique” means unique up to almost-sure equality under every model distribution; see [Lecture 2]({{ '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url }}).

## 2. Lecture 1 — Point estimation, risk, and MSE

### Loss, risk, and estimator comparison

For a loss function $L(\theta,a)$, the risk of an estimator $T$ is

$$
R(\theta,T)=\operatorname{E}_\theta\!\left[L\bigl(\theta,T(X)\bigr)\right].
$$

Under squared-error loss for target $\psi(\theta)$,

$$
L(\theta,a)=\bigl(a-\psi(\theta)\bigr)^2,
$$

and therefore

$$
R(\theta,T)=\operatorname{E}_\theta\left[(T-\psi(\theta))^2\right]
=\operatorname{MSE}_\theta(T).
$$

Uniform comparison means $T_1$ is at least as good as $T_2$ if

$$
R(\theta,T_1)\le R(\theta,T_2)\qquad\text{for every }\theta\in\Theta.
$$

See [Lecture 1]({{ '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url }}).

### Bias and mean squared error

The bias of $T$ for $\psi(\theta)$ is

$$
\operatorname{Bias}_\theta(T)
=\operatorname{E}_\theta[T]-\psi(\theta).
$$

If $\operatorname{E}_\theta[T^2]<\infty$, then

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

## 3. Lecture 2 — Unbiased estimation, UMVUEs, and CRLB

### UMVUE

An estimator $T^*$ is a UMVUE of $\psi(\theta)$ when

$$
\operatorname{E}_\theta[T^*]=\psi(\theta)
$$

for every $\theta$, and for every other unbiased estimator $U$,

$$
\operatorname{Var}_\theta(T^*)
\le
\operatorname{Var}_\theta(U)
\qquad\text{for every }\theta.
$$

If $T_1$ and $T_2$ are both UMVUEs with common variance $v_\theta$, then for $W=(T_1+T_2)/2$,

$$
\operatorname{Var}_\theta(W)
=v_\theta-\frac14\operatorname{Var}_\theta(T_1-T_2).
$$

Minimality forces $\operatorname{Var}_\theta(T_1-T_2)=0$, proving almost-sure uniqueness. See [Lecture 2]({{ '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url }}).

### Score, Fisher information, and CRLB

For a regular scalar model with density or mass function $f_\theta$,

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

If $T$ is unbiased for $\psi(\theta)$ and the ordinary CRLB regularity assumptions hold,

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

For vector parameter $\eta$ and scalar target $g(\eta)$,

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

For iid $N(\theta,\sigma^2)$ with known $\sigma^2$,

$$
\operatorname{Var}(\overline X)=\frac{\sigma^2}{n},
\qquad
\mathcal I_n(\theta)=\frac{n}{\sigma^2}.
$$

Thus $\overline X$ attains the CRLB $\sigma^2/n$.

### Exponential mean

For iid exponential observations with mean $\theta$,

$$
\operatorname{Var}(\overline X)=\frac{\theta^2}{n},
\qquad
\mathcal I_n(\theta)=\frac{n}{\theta^2},
$$

so $\overline X$ again attains the CRLB.

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

For $T_c=cQ$,

$$
\operatorname{MSE}(T_c)
=\sigma^4\left[
2c^2(n-1)+\bigl(c(n-1)-1\bigr)^2
\right].
$$

The minimiser within this class is

$$
c^*=\frac{1}{n+1},
$$

with

$$
\operatorname{MSE}(T_{c^*})=\frac{2\sigma^4}{n+1}.
$$

With parameter $\eta=(\mu,\sigma^2)$,

$$
\mathcal I_n(\mu,\sigma^2)
=
\begin{pmatrix}
n/\sigma^2 & 0\\
0 & n/(2\sigma^4)
\end{pmatrix},
$$

and the matrix CRLB for unbiased estimation of $\sigma^2$ is $2\sigma^4/n$, although it is not attainable by a statistic when $\mu$ is unknown. See [Lecture 2]({{ '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url }}).

## 4. Lecture 3 — Existence and uniqueness of unbiased estimators

For $X\sim\operatorname{Bin}(n,\theta)$,

$$
\operatorname{E}_\theta[T(X)]
=\sum_{x=0}^n T(x)\binom nx\theta^x(1-\theta)^{n-x},
$$

so an unbiasedly estimable target must be a polynomial in $\theta$ of degree at most $n$. Falling factorials satisfy

$$
\operatorname{E}_\theta[(X)_k]=(n)_k\theta^k,
$$

hence

$$
\frac{(X)_k}{(n)_k}
$$

is unbiased for $\theta^k$.

For $X\sim\operatorname{Poisson}(\theta)$,

$$
e^\theta\psi(\theta)
=\sum_{x=0}^{\infty}T(x)\frac{\theta^x}{x!}.
$$

Under integrability for every positive $\theta$, the series has infinite radius of convergence, giving the entire-function condition and the coefficient identity

$$
T(x)=\left.\frac{d^x}{dz^x}\bigl(e^z\psi(z)\bigr)\right|_{z=0}.
$$

For one exponential observation with mean $\theta$, uniqueness is obtained from

$$
\int_0^\infty h(x)e^{-sx}\,\mathrm dx=0
\qquad\text{for every }s>0,
$$

where $h(x)=T(x)-x$. Laplace-transform uniqueness gives $h=0$ almost everywhere. See [Lecture 3]({{ '/notes/parametric-inference/lecture-03-existence-uniqueness-unbiased-estimators/' | relative_url }}).

## 5. Lecture 4 — Sufficiency and Rao–Blackwell

### Sufficiency

A statistic $S$ is sufficient for $\theta$ when the conditional distribution of $X$ given $S$ does not depend on $\theta$.

The Neyman-Fisher factorisation criterion is

$$
f_\theta(x)=g_\theta(S(x))h(x),
$$

where $h$ is free of $\theta$.

Canonical sufficient statistics from the lecture are

- Bernoulli sample: $S=\sum_iX_i$;
- Poisson sample: $S=\sum_iX_i$;
- exponential sample with mean $\theta$: $S=\sum_iX_i$;
- uniform endpoint model: $M=X_{(n)}$.

See [Lecture 4]({{ '/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell/' | relative_url }}).

### Rao–Blackwell theorem

Given a sufficient statistic $S$ and an estimator $U$ with finite second moment, define

$$
U^*=\operatorname{E}[U\mid S].
$$

Then

$$
\operatorname{E}[U^*]=\operatorname{E}[U]
$$

and, under squared-error loss,

$$
\operatorname{MSE}_\theta(U^*)
\le
\operatorname{MSE}_\theta(U).
$$

For unbiased estimators,

$$
\operatorname{Var}_\theta(U^*)
\le
\operatorname{Var}_\theta(U).
$$

The decomposition behind the result is

$$
\operatorname{MSE}_\theta(U)
=
\operatorname{E}_\theta[\operatorname{Var}_\theta(U\mid S)]
+
\operatorname{MSE}_\theta(U^*).
$$

In the exponential sample,

$$
\operatorname{E}[X_1\mid S]=\frac{S}{n}=\overline X.
$$

See [Lecture 4]({{ '/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell/' | relative_url }}).

## 6. Lecture 5 — Completeness

### Standard models

A statistic $S$ is complete if

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

- binomial total: a polynomial in $z=\theta/(1-\theta)$ must vanish coefficientwise;
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

Polynomial, power-series, Laplace-transform, and absolute-continuity uniqueness arguments respectively prove completeness. See [Lecture 5]({{ '/notes/parametric-inference/lecture-05-completeness-standard-exponential-families/' | relative_url }}).

### Full natural exponential families

For a natural exponential family

$$
f_\eta(x)
=h(x)\exp\lbrace \eta^\top T(x)-A(\eta) \rbrace,
$$

if the natural parameter space contains a nonempty open set and

$$
\operatorname{E}_\eta[g(T)]=0
$$

throughout that set, then

$$
\int g(T(x))h(x)e^{\eta^\top T(x)}\,\mathrm dx=0.
$$

The left side is a multivariate Laplace transform. Uniqueness of that transform implies $g(T)=0$ almost surely, establishing completeness under the stated full-family conditions. See [Lecture 5]({{ '/notes/parametric-inference/lecture-05-completeness-standard-exponential-families/' | relative_url }}).

## 7. Lecture 6 — Lehmann–Scheffé and UMVUE constructions

### Lehmann–Scheffé theorem

If $S$ is complete and sufficient and $h(S)$ is unbiased for $\psi(\theta)$, then $h(S)$ is the unique UMVUE.

For any unbiased $U$, Rao-Blackwellisation gives

$$
U^*=\operatorname{E}[U\mid S],
$$

with

$$
\operatorname{Var}_\theta(U^*)\le\operatorname{Var}_\theta(U).
$$

Completeness forces

$$
U^*=h(S)
$$

almost surely. See [Lecture 6]({{ '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-examples/' | relative_url }}).

### Canonical UMVUE formulas

For Bernoulli data with $S=\sum_iX_i$,

$$
\widehat\theta_{\mathrm{UMVUE}}=\frac{S}{n},
\qquad
\widehat{\theta^k}_{\mathrm{UMVUE}}=\frac{(S)_k}{(n)_k}.
$$

For Poisson data with total $S$,

$$
\widehat\theta_{\mathrm{UMVUE}}=\frac{S}{n},
\qquad
\widehat{\theta^k}_{\mathrm{UMVUE}}=\frac{(S)_k}{n^k}.
$$

For exponential data with mean $\theta$ and sum $S$,

$$
\widehat\theta_{\mathrm{UMVUE}}=\frac{S}{n},
$$

and, because $S\sim\operatorname{Gamma}(n,\text{scale }\theta)$,

$$
\widehat{\theta^k}_{\mathrm{UMVUE}}
=
\frac{\Gamma(n)}{\Gamma(n+k)}S^k.
$$

For iid $\operatorname{Uniform}(0,\theta)$ observations,

$$
\widehat\theta_{\mathrm{UMVUE}}
=
\frac{n+1}{n}X_{(n)}.
$$

For normal data with both $\mu$ and $\sigma^2$ unknown,

$$
S^2
=
\frac{1}{n-1}\sum_{i=1}^n(X_i-\overline X)^2
$$

is the unique UMVUE of $\sigma^2$. See [Lecture 6]({{ '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-examples/' | relative_url }}).

### Logical implications

The lecture separates the following statements:

1. A **unique unbiased estimator** is automatically a UMVUE.
2. A **unique UMVUE** may coexist with other unbiased estimators of larger variance.
3. In a regular model, an unbiased estimator that attains the CRLB at every parameter value is a UMVUE.
4. The converse need not hold: a UMVUE may fail to attain an unattainable bound.
5. In a nonregular model such as $\operatorname{Uniform}(0,\theta)$, the ordinary CRLB may not apply.

See [Lecture 6]({{ '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-examples/' | relative_url }}).

## 8. Useful distributional identities

For $X\sim\operatorname{Bin}(n,\theta)$,

$$
\operatorname{E}[(X)_k]=(n)_k\theta^k.
$$

For $X\sim\operatorname{Poisson}(\lambda)$,

$$
\operatorname{E}[(X)_k]=\lambda^k.
$$

If $Y\sim\chi^2_\nu$,

$$
\operatorname{E}[Y]=\nu,
\qquad
\operatorname{Var}(Y)=2\nu,
\qquad
\operatorname{E}[Y^2]=\nu(\nu+2).
$$

If $S\sim\operatorname{Gamma}(\alpha,\text{scale }\theta)$,

$$
\operatorname{E}[S^k]
=
\theta^k\frac{\Gamma(\alpha+k)}{\Gamma(\alpha)}.
$$

See [the useful distributional identities section]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}).

## 9. Quick model comparison

| Model                                       | Complete sufficient statistic | Typical target       | UMVUE         |
| ------------------------------------------- | ----------------------------- | -------------------- | ------------- |
| Bernoulli$(\theta)$, iid                    | $S=\sum X_i$                  | $\theta$             | $S/n$         |
| Binomial$(n,\theta)$, one count             | $X$                           | $\theta^k$, $k\le n$ | $(X)_k/(n)_k$ |
| Poisson$(\theta)$, iid                      | $S=\sum X_i$                  | $\theta^k$           | $(S)_k/n^k$   |
| Exponential, mean $\theta$                  | $S=\sum X_i$                  | $\theta$             | $S/n$         |
| Uniform$(0,\theta)$                         | $M=X_{(n)}$                   | $\theta$             | $(n+1)M/n$    |
| Normal$(\theta,\sigma^2)$, $\sigma^2$ known | $\overline X$                 | $\theta$             | $\overline X$ |
| Normal$(\mu,\sigma^2)$, both unknown        | $(\sum X_i,\sum X_i^2)$       | $\sigma^2$           | $Q/(n-1)$     |

See [the quick model comparison]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}).

## 10. Quick conceptual comparison

| Concept         | What is compared or required?                                | Typical tool                               |
| --------------- | ------------------------------------------------------------ | ------------------------------------------ |
| Unbiasedness    | $\operatorname{E}_\theta[T]=\psi(\theta)$ for every $\theta$ | Direct expectation                         |
| MSE             | Average squared error                                        | Bias-variance decomposition                |
| UMVUE           | Variance among unbiased estimators                           | CRLB or Lehmann-Scheffe                    |
| Sufficiency     | Conditional law given $S$ is parameter-free                  | Factorisation theorem                      |
| Completeness    | Zero expectation for all parameters forces zero function     | Polynomial / analytic / Laplace uniqueness |
| Rao-Blackwell   | Improve an estimator by conditioning                         | Conditional expectation                    |
| CRLB            | Lower bound for unbiased variance in regular models          | Fisher information                         |
| Lehmann-Scheffe | Unique UMVUE from complete sufficiency                       | Rao-Blackwell + completeness               |

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Course contents]({{ '/notes/parametric-inference/' | relative_url }})
</nav>

</div>
