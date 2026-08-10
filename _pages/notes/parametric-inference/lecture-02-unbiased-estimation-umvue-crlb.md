---
layout: page
title: "Lecture 2: Unbiased Estimation, UMVUEs, Fisher Information, and the Cramér–Rao Bound"
short_title: "Unbiased estimation and CRLB"
course: "Parametric Inference"
lecture: 2
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Introduces unbiased estimation and UMVUEs, proves uniqueness, derives Fisher information and the Cramér–Rao lower bound, and works through the normal, exponential, and normal-variance examples."
topics:
  - "unbiased estimation"
  - "UMVUE"
  - "Fisher information"
  - "Cramér–Rao lower bound"
  - "efficiency"
  - "normal and exponential examples"
previous: "lecture-01-point-estimation-risk-mse"
next: "lecture-03-existence-uniqueness-unbiased-estimators"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-11"
status: "complete"
math: true
permalink: /notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/
course_slug: parametric-inference
note_kind: lecture
course_order: 2
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Fall 2026 Parametric Inference lectures of Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata. The exposition includes additional definitions, derivations, and worked solutions. Any remaining errors belong to the note maintainer, not to the instructor or the Institute.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture →]({{ '/notes/parametric-inference/lecture-03-existence-uniqueness-unbiased-estimators/' | relative_url }})
</nav>

## Learning objectives

- Distinguish unbiasedness, variance optimality, and MSE optimality.
- Define a UMVUE and prove its uniqueness.
- Compute scores and Fisher information and derive the scalar and matrix Cramér–Rao bounds.
- Check equality and regularity conditions for CRLB attainment.
- Work through the normal mean, exponential mean, and normal variance examples in full.

> **Editorial note.**
> The handwritten argument for uniqueness was replaced in the expanded LaTeX notes by a variance-of-the-difference proof. This avoids relying on an informal correlation argument and proves almost-sure equality directly.

## 1. Unbiased estimators need not be unique

If $T_1$ and $T_2$ are unbiased for $\psi(\theta)$, then every affine combination

$$
T_a=aT_1+(1-a)T_2
$$

is also unbiased. Therefore unbiased estimators are often far from unique.

### Worked Example 2.1 — Exponential sample

**Problem.**

Exhibit distinct unbiased estimators of the exponential mean when more than one observation is available.

**Solution.**

If $X_1,\dots,X_n\overset{\mathrm{iid}}{\sim}\operatorname{Exp}(\text{mean }\theta)$, then each $X_i$ is unbiased for $\theta$, as are

$$
\overline X,\qquad \frac{X_1+X_2}{2},\qquad 2\overline X-X_1,
$$

provided the displayed expression has expectation $\theta$. Thus for $n\ge2$, unbiasedness alone does not give uniqueness.

**Final result.**

For $n\ge2$, unbiased estimators of $\theta$ are not unique.

## 2. Definition of a UMVUE

<div class="definition" markdown="1">

**Definition 2.1 — UMVUE.**
An estimator $T^*$ is a _uniformly minimum-variance unbiased estimator_ of $\psi(\theta)$ if\*

1.  $\operatorname{E}_\theta[T^*]=\psi(\theta)$ for every $\theta\in\Theta$, and

2.  \*for every other unbiased estimator $U$,

$$
\operatorname{Var}_\theta(T^*)\le \operatorname{Var}_\theta(U)
    \qquad\text{for every }\theta\in\Theta.
$$

</div>

<div class="theorem" markdown="1">

**Theorem 2.2 — A UMVUE is unique.**
If a UMVUE exists, then it is unique up to almost-sure equality under every $P_\theta$.

</div>

**Proof.**

Suppose $T_1$ and $T_2$ are both UMVUEs of the same function. Their average

$$
W=\frac{T_1+T_2}{2}
$$

is unbiased. Since both have minimum variance,

$$
\operatorname{Var}_\theta(T_1)=\operatorname{Var}_\theta(T_2)=v_\theta,
\qquad
\operatorname{Var}_\theta(W)\ge v_\theta.
$$

Because $T_1$ and $T_2$ have equal expectations,

$$
\begin{aligned}
\operatorname{Var}_\theta(W)
&=\frac14\operatorname{Var}_\theta(T_1+T_2)\\
&=\frac12\operatorname{Var}_\theta(T_1)
  +\frac12\operatorname{Var}_\theta(T_2)\\
&\quad-\frac14\operatorname{Var}_\theta(T_1-T_2)\\
&=v_\theta-\frac14\operatorname{Var}_\theta(T_1-T_2).
\end{aligned}
$$

The inequality $\operatorname{Var}_\theta(W)\ge v_\theta$ therefore implies

$$
\operatorname{Var}_\theta(T_1-T_2)=0.
$$

Also $\operatorname{E}_\theta[T_1-T_2]=0$, hence $T_1=T_2$ almost surely under $P_\theta$.

$\square$

<div class="remark" markdown="1">

**Remark 2.3.**
The word “unique” in estimation theory always means unique up to probability-zero modifications. Two formulas that differ only on a set having probability zero under every model distribution represent the same estimator statistically.

</div>

## 3. Score and information

Assume the model has density or probability mass function $f_\theta(x)$ with respect to a common dominating measure.

<div class="definition" markdown="1">

**Definition 2.4 — Score.**
The score for one observation is

$$
\mathcal{S}_\theta(X)=\frac{\partial}{\partial\theta}\log f_\theta(X),
$$

whenever the derivative exists.

</div>

Under standard regularity conditions, differentiation may be passed under the integral sign:

$$
\operatorname{E}_\theta[\mathcal{S}_\theta(X)]
=\int \frac{\partial}{\partial\theta}f_\theta(x)\,\mathrm{d}x
=\frac{\partial}{\partial\theta}\int f_\theta(x)\,\mathrm{d}x=0.
$$

<div class="definition" markdown="1">

**Definition 2.5 — Fisher information.**
The Fisher information in one observation is

$$
\mathcal{I}_1(\theta)=\operatorname{E}_\theta[\mathcal{S}_\theta(X)^2].
$$

For an iid sample of size $n$,

$$
\mathcal{I}_n(\theta)=n\mathcal{I}_1(\theta).
$$

If differentiation is sufficiently regular, then also

$$
\mathcal{I}_1(\theta)=-\operatorname{E}_\theta\left[\frac{\partial^2}{\partial\theta^2}\log f_\theta(X)\right].
$$

</div>

## 4. Scalar Cramér–Rao inequality

<div class="theorem" markdown="1">

**Theorem 2.6 — Cramér–Rao lower bound.**
Let $T$ be unbiased for $\psi(\theta)$, and suppose the standard regularity conditions hold. Then

$$
\operatorname{Var}_\theta(T)\ge \frac{\bigl(\psi'(\theta)\bigr)^2}{\mathcal{I}_n(\theta)}.
$$

</div>

**Proof.**

Since $\operatorname{E}_\theta[T]=\psi(\theta)$, differentiation under the integral gives

$$
\begin{aligned}
\psi'(\theta)
&=\frac{\partial}{\partial\theta}\int T(x)f_\theta(x)\,\mathrm{d}x\\
&=\int T(x)\frac{\partial}{\partial\theta}f_\theta(x)\,\mathrm{d}x\\
&=\operatorname{E}_\theta[T\mathcal{S}_\theta(X)].
\end{aligned}
$$

Because $\operatorname{E}_\theta[\mathcal{S}_\theta]=0$,

$$
\psi'(\theta)=\operatorname{Cov}_\theta(T,\mathcal{S}_\theta).
$$

Cauchy–Schwarz gives

$$
\bigl(\psi'(\theta)\bigr)^2
\le \operatorname{Var}_\theta(T)\operatorname{Var}_\theta(\mathcal{S}_\theta)
=\operatorname{Var}_\theta(T)\mathcal{I}_n(\theta).
$$

Rearranging proves the result.

$\square$

<div class="proposition" markdown="1">

**Proposition 2.7 — Equality condition.**
Equality in the Cramér–Rao bound at a parameter value $\theta$ holds if and only if

$$
T(X)-\psi(\theta)=a(\theta)\mathcal{S}_\theta(X)
\quad P_\theta\text{-almost surely}
$$

for some scalar $a(\theta)$. For an unbiased estimator attaining the bound,

$$
a(\theta)=\frac{\psi'(\theta)}{\mathcal{I}_n(\theta)}.
$$

</div>

<div class="warning" markdown="1">

**Common pitfall 2.8.**
The ordinary Cramér–Rao theorem requires parameter-independent support and differentiation under the integral sign. It cannot be applied blindly to models such as $\operatorname{Uniform}(0,\theta)$, whose support depends on $\theta$.

</div>

## 5. Several parameters and nuisance parameters

Let $\eta=(\eta_1,\dots,\eta_k)^\top$. The Fisher information matrix is

$$
\mathcal{I}_n(\eta)=\operatorname{E}_\eta\left[\mathcal{S}_\eta\mathcal{S}_\eta^\top\right].
$$

For an unbiased estimator of a scalar function $g(\eta)$, the matrix Cramér–Rao inequality gives

$$
\operatorname{Var}_\eta(T)\ge \nabla g(\eta)^\top\mathcal{I}_n(\eta)^{-1}\nabla g(\eta).
$$

This is the appropriate form when some coordinates of $\eta$ are nuisance parameters.

## 6. Normal mean with known variance

### Worked Example 2.2 — Sample mean is efficient and UMVUE

**Problem.**

For iid $N(\theta,\sigma^2)$ observations with known $\sigma^2$, verify unbiasedness of $\overline X$, compute its variance and the Fisher information, and determine whether it attains the CRLB.

**Solution.**

Let

$$
X_1,\dots,X_n\overset{\mathrm{iid}}{\sim}N(\theta,\sigma^2),
$$

where $\sigma^2$ is known and $\theta\in\mathbb{R}$. We estimate $\theta$.\*

\*The sample mean is unbiased:

$$
\operatorname{E}_\theta[\overline X]
=\frac1n\sum_{i=1}^n\operatorname{E}_\theta[X_i]
=\theta.
$$

Its variance is

$$
\operatorname{Var}_\theta(\overline X)
=\frac1{n^2}\sum_{i=1}^n\operatorname{Var}_\theta(X_i)
=\frac{\sigma^2}{n}.
$$

- \*For one observation,

$$
\log f_\theta(x)
=-\frac12\log(2\pi\sigma^2)-\frac{(x-\theta)^2}{2\sigma^2},
$$

so

$$
\frac{\partial}{\partial\theta}\log f_\theta(x)
=\frac{x-\theta}{\sigma^2}.
$$

Therefore

$$
\mathcal{I}_1(\theta)
=\operatorname{E}_\theta\left[\frac{(X-\theta)^2}{\sigma^4}\right]
=\frac1{\sigma^2},
\qquad
\mathcal{I}_n(\theta)=\frac n{\sigma^2}.
$$

The CRLB for an unbiased estimator of $\theta$ is

$$
\operatorname{Var}_\theta(T)\ge \frac1{\mathcal{I}_n(\theta)}=\frac{\sigma^2}{n}.
$$

Since $\overline X$ achieves this bound, it is a UMVUE of $\theta$.

**Final result.**

$\overline X$ is unbiased, $\operatorname{Var}(\overline X)=\sigma^2/n$, and it attains the CRLB; hence it is a UMVUE of $\theta$.

## 7. Exponential mean

We use the mean parametrisation

$$
f_\theta(x)=\frac1\theta e^{-x/\theta}\mathbf{1}_{(0,\infty)}(x),
\qquad \theta>0.
$$

Then

$$
\operatorname{E}_\theta[X]=\theta,
\qquad
\operatorname{Var}_\theta(X)=\theta^2.
$$

### Worked Example 2.3 — CRLB for the exponential mean

**Problem.**

For iid exponential observations parametrised by their mean $\theta$, compute the CRLB for unbiased estimation of $\theta$ and compare it with $\overline X$.

**Solution.**

Let $X_1,\dots,X_n$ be iid exponential with mean $\theta$. The estimator $\overline X$ is unbiased and

$$
\operatorname{Var}_\theta(\overline X)=\frac{\theta^2}{n}.
$$

For one observation,

$$
\log f_\theta(x)=-\log\theta-\frac{x}{\theta},
$$

and hence

$$
\frac{\partial}{\partial\theta}\log f_\theta(x)
=-\frac1\theta+\frac{x}{\theta^2}
=\frac{x-\theta}{\theta^2}.
$$

Thus

$$
\mathcal{I}_1(\theta)
=\frac{\operatorname{Var}_\theta(X)}{\theta^4}
=\frac1{\theta^2},
\qquad
\mathcal{I}_n(\theta)=\frac n{\theta^2}.
$$

The CRLB is

$$
\operatorname{Var}_\theta(T)\ge \frac{\theta^2}{n}.
$$

Since $\overline X$ attains the bound, it is a UMVUE of $\theta$.

**Final result.**

$\operatorname{Var}(\overline X)=\theta^2/n$, exactly equal to the CRLB, so $\overline X$ is a UMVUE.

## 8. Normal variance with unknown mean

Let

$$
\begin{gathered}
X_1,\dots,X_n\overset{\mathrm{iid}}{\sim}N(\mu,\sigma^2),\\
n\ge2,\qquad \mu\in\mathbb{R},\qquad \sigma^2>0.
\end{gathered}
$$

Define

$$
Q=\sum_{i=1}^n(X_i-\overline X)^2.
$$

The standard chi-square result is

$$
\frac{Q}{\sigma^2}\sim\chi^2_{n-1}.
$$

Consequently,

$$
\operatorname{E}[Q]=(n-1)\sigma^2,
\qquad
\operatorname{Var}(Q)=2(n-1)\sigma^4.
$$

### Worked Example 2.4 — Unbiased sample variance

**Problem.**

For normal data with both $\mu$ and $\sigma^2$ unknown, use the chi-square distribution of the residual sum of squares to verify unbiasedness and compute the variance of $S^2$.

**Solution.**

The estimator

$$
S^2=\frac{1}{n-1}Q
$$

is unbiased because

$$
\operatorname{E}[S^2]=\frac1{n-1}\operatorname{E}[Q]=\sigma^2.
$$

Its variance is

$$
\operatorname{Var}(S^2)
=\frac1{(n-1)^2}\operatorname{Var}(Q)
=\frac{2\sigma^4}{n-1}.
$$

Therefore its squared-error risk is

$$
R((\mu,\sigma^2),S^2)=\frac{2\sigma^4}{n-1}.
$$

**Final result.**

$\operatorname{E}[S^2]=\sigma^2$ and $\operatorname{Var}(S^2)=2\sigma^4/(n-1)$.

### Worked Example 2.5 — A biased estimator can have smaller MSE

**Problem.**

Within the class $T_c=cQ$, where $Q=\sum_i(X_i-\overline X)^2$, find the value of $c$ that minimises MSE for estimating $\sigma^2$ and compare it with the unbiased sample variance.

**Solution.**

Consider the class

$$
T_c=cQ,
$$

where $c$ is a fixed constant. We estimate $\sigma^2$.\*

\*First compute the bias:

$$
\operatorname{E}[T_c]=c(n-1)\sigma^2,
$$

so

$$
\operatorname{Bias}(T_c)=\bigl(c(n-1)-1\bigr)\sigma^2.
$$

The variance is

$$
\operatorname{Var}(T_c)=c^2\operatorname{Var}(Q)=2c^2(n-1)\sigma^4.
$$

Hence

$$
\begin{aligned}
\operatorname{MSE}(T_c)
&=\operatorname{Var}(T_c)+\operatorname{Bias}(T_c)^2\\
&=\sigma^4\left[2c^2(n-1)+\bigl(c(n-1)-1\bigr)^2\right]\\
&=\sigma^4\left[c^2(n-1)(n+1)-2c(n-1)+1\right].
\end{aligned}
$$

Differentiate with respect to $c$:

$$
\frac{\,\mathrm{d}}{\,\mathrm{d}c}\operatorname{MSE}(T_c)
=2\sigma^4(n-1)\bigl((n+1)c-1\bigr).
$$

Thus the risk-minimising constant within this class is

$$
c^*=\frac1{n+1}.
$$

The optimal estimator within the class is therefore

$$
T_{c^*}=\frac1{n+1}\sum_{i=1}^n(X_i-\overline X)^2,
$$

and its MSE is

$$
\operatorname{MSE}(T_{c^*})=\frac{2\sigma^4}{n+1}.
$$

By comparison,

$$
\operatorname{MSE}(S^2)=\frac{2\sigma^4}{n-1}.
$$

Thus the biased estimator $Q/(n+1)$ has smaller MSE than the unbiased estimator $Q/(n-1)$.

**Final result.**

$c^*=1/(n+1)$ and $\operatorname{MSE}(T_{c^*})=2\sigma^4/(n+1)<2\sigma^4/(n-1)=\operatorname{MSE}(S^2)$.

<div class="remark" markdown="1">

**Remark 2.9 — The maximum-likelihood variance estimator.**
The usual maximum-likelihood estimator is

$$
\widehat{\sigma^2}_{\mathrm{ML}}=\frac Qn.
$$

Its bias and MSE are

$$
\begin{aligned}
\operatorname{Bias}\left(\frac Qn\right)
&=-\frac{\sigma^2}{n},\\
\operatorname{MSE}\left(\frac Qn\right)
&=\frac{2n-1}{n^2}\sigma^4.
\end{aligned}
$$

It has lower MSE than $S^2$, but it is not the best member of the full class $cQ$; the choice $c=1/(n+1)$ is slightly better.

</div>

## 9. CRLB for the variance when the mean is unknown

For one normal observation, with parameter $\eta=(\mu,\sigma^2)$, the information matrix is

$$
\mathcal{I}_1(\mu,\sigma^2)=
\begin{pmatrix}
1/\sigma^2 & 0\\
0 & 1/(2\sigma^4)
\end{pmatrix}.
$$

For $n$ observations,

$$
\mathcal{I}_n(\mu,\sigma^2)=
\begin{pmatrix}
n/\sigma^2 & 0\\
0 & n/(2\sigma^4)
\end{pmatrix}.
$$

To estimate $g(\mu,\sigma^2)=\sigma^2$,

$$
\nabla g=(0,1)^\top.
$$

Hence the matrix CRLB is

$$
\operatorname{Var}(T)\ge \frac{2\sigma^4}{n}.
$$

But

$$
\operatorname{Var}(S^2)=\frac{2\sigma^4}{n-1}>\frac{2\sigma^4}{n}.
$$

So $S^2$ does not attain the CRLB.

<div class="proposition" markdown="1">

**Proposition 2.10 — The CRLB is not attainable here.**
There is no unbiased estimator of $\sigma^2$ that attains $2\sigma^4/n$ simultaneously for every $(\mu,\sigma^2)$.

</div>

**Proof.**

Equality would require the centred estimator to be a linear combination of the two score components. Because $g(\mu,\sigma^2)=\sigma^2$, the required combination reduces to

$$
\begin{aligned}
T-\sigma^2
&=\frac{2\sigma^4}{n}\frac{\partial}{\partial\sigma^2}\log L(\mu,\sigma^2)\\
&=\frac1n\sum_{i=1}^n(X_i-\mu)^2-\sigma^2.
\end{aligned}
$$

Therefore equality would force

$$
T=\frac1n\sum_{i=1}^n(X_i-\mu)^2.
$$

This expression contains the unknown nuisance parameter $\mu$, so it is not a statistic. Hence no legitimate estimator can satisfy the equality condition for all $\mu$.

$\square$

Later, the Lehmann–Scheffé theorem will show that $S^2$ is nevertheless the UMVUE of $\sigma^2$. A UMVUE need not attain the CRLB when the bound is not attainable.

## Questions answered in this lecture

**Question.**

Can we define a “best” estimator after restricting attention to unbiased estimators?

**Answer.**

Yes. A UMVUE is an unbiased estimator whose variance is no larger than that of every other unbiased estimator for every parameter value.

**Question.**

If two formulas are both UMVUEs, can they genuinely differ?

**Answer.**

Only on sets of probability zero under the model. The UMVUE is unique up to almost-sure equality.

**Question.**

Why does the score have expectation zero?

**Answer.**

Under the regularity assumptions, differentiation may pass under the integral: $\operatorname{E}_\theta[\mathcal S_\theta]=\int \partial f_\theta/\partial\theta=\partial 1/\partial\theta=0$.

**Question.**

When is the ordinary CRLB unsafe to use?

**Answer.**

A key failure occurs when the support depends on the unknown parameter, as in $\operatorname{Uniform}(0,\theta)$.

**Question.**

What changes when a nuisance parameter is present?

**Answer.**

Use the full Fisher information matrix and the quadratic form $\nabla g(\eta)^\top \mathcal I_n(\eta)^{-1}\nabla g(\eta)$.

**Question.**

Does unbiasedness guarantee the smallest MSE?

**Answer.**

No. In the class $T_c=cQ$, the MSE-minimising choice is $c=1/(n+1)$, which is biased but has smaller MSE than $S^2=Q/(n-1)$.

**Question.**

Can an unbiased estimator of $\sigma^2$ attain the CRLB when $\mu$ is unknown?

**Answer.**

No. Equality would force $T=n^{-1}\sum_i(X_i-\mu)^2$, which depends on the unknown nuisance parameter and is therefore not a statistic.

**Question.**

Can $S^2$ still be a UMVUE if it does not attain the CRLB?

**Answer.**

Yes. Later the complete-sufficiency argument shows that $S^2$ is the UMVUE; CRLB attainment is sufficient for UMVUE status but is not necessary when the bound is unattainable.

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.
- Expanded source: the complete LaTeX notes and compiled PDF used for this Markdown conversion.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture →]({{ '/notes/parametric-inference/lecture-03-existence-uniqueness-unbiased-estimators/' | relative_url }})
</nav>

</div>
