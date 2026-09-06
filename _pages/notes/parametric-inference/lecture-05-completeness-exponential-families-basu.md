---
layout: page
title: "Lecture 5: Completeness, Exponential Families, and Basu’s Theorem"
short_title: "Completeness and Basu"
course: "Parametric Inference"
lecture: 5
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Develops completeness in standard models, derives order-statistic and gamma identities used in the proofs, proves completeness for full one- and multiparameter exponential families using ordinary integral transforms, and proves and applies Basu’s theorem."
topics:
  - "completeness"
  - "exponential families"
  - "natural parameter space"
  - "complete sufficient statistics"
  - "uniform order statistics"
  - "Laplace-transform completeness"
  - "uniform endpoints"
  - "Basu’s theorem"
previous: "lecture-04-sufficiency-rao-blackwell-ancillarity"
next: "lecture-06-lehmann-scheffe-umvue-consistency"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-09-06"
status: "complete"
math: true
permalink: /notes/parametric-inference/lecture-05-completeness-exponential-families-basu/
course_slug: parametric-inference
note_kind: lecture
course_order: 5
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Fall 2026 Parametric Inference lectures of Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata. Additional exposition and any remaining errors are the responsibility of the note author.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell-ancillarity/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-consistency/' | relative_url }})
</nav>

## Learning objectives

<div class="intuition" markdown="1">

**Additional context.**
This section was added to make the lecture easier to use as a self-contained study note.

</div>

- State completeness as an injectivity property of the expectation operator.
- Prove completeness for the standard binomial, Poisson, exponential, and uniform statistics, including the distributional calculations needed in those proofs.
- Understand why continuity is unnecessary in the uniform proof.
- Apply the full natural exponential-family completeness theorem with its required conditions.
- Put one- and multiparameter models into natural exponential-family form.
- Prove completeness for a two-endpoint uniform family.
- State and prove Basu’s theorem and apply it in the normal model.

## 1. Definition and meaning

<div class="definition" markdown="1">

**Definition 5.1 — Completeness.**

A statistic \\(S=S(X)\\) is _complete_ for the family \\(\lbrace P\_\theta:\theta\in\Theta\rbrace \\) if, for every measurable function \\(g\\) for which the expectations exist,

$$
\operatorname{E}_\theta[g(S)]=0\quad\text{for every }\theta\in\Theta
$$

implies

$$
g(S)=0\quad P_\theta\text{-almost surely for every }\theta\in\Theta.
$$

</div>

Completeness is an injectivity property of the expectation operator. It says that two functions of \\(S\\) cannot have the same expectation for every parameter value unless they are almost surely equal.

<div class="proposition" markdown="1">

**Proposition 5.2 — Uniqueness among functions of a complete statistic.**

If \\(S\\) is complete and \\(h_1(S)\\) and \\(h_2(S)\\) are unbiased estimators of the same parametric function, then

$$
h_1(S)=h_2(S)
\quad\text{almost surely}.
$$

</div>

**Proof.**

Since both are unbiased,

$$
\operatorname{E}_\theta[h_1(S)-h_2(S)]=0
\qquad\text{for all }\theta.
$$

Completeness gives \\(h_1(S)-h_2(S)=0\\) almost surely.

\\(\square\\)

## 2. Completeness of binomial totals

<div class="theorem" markdown="1">

**Theorem 5.3.**

If \\(S\sim\operatorname{Bin}(n,\theta)\\), \\(0<\theta<1\\), then \\(S\\) is complete.

</div>

**Proof.**

Suppose

$$
\operatorname{E}_\theta[g(S)]
=\sum_{s=0}^n g(s)\binom ns\theta^s(1-\theta)^{n-s}=0
\qquad\text{for all }0<\theta<1.
$$

Divide by \\((1-\theta)^n\\) and put \\(z=\theta/(1-\theta)\in(0,\infty)\\). Then

$$
\sum_{s=0}^n g(s)\binom ns z^s=0
\qquad\text{for all }z>0.
$$

A polynomial that vanishes on an interval is identically zero. Hence every coefficient is zero:

$$
g(s)\binom ns=0,
$$

so \\(g(s)=0\\) for all \\(s=0,\dots,n\\).

\\(\square\\)

## 3. Completeness of Poisson totals

<div class="theorem" markdown="1">

**Theorem 5.4.**

If \\(S\sim\operatorname{Poisson}(\lambda)\\) with \\(\lambda\\) ranging over \\((0,\infty)\\), then \\(S\\) is complete.

</div>

**Proof.**

Suppose

$$
0=\operatorname{E}_\lambda[g(S)]
=e^{-\lambda}\sum_{s=0}^\infty g(s)\frac{\lambda^s}{s!}
\qquad\text{for all }\lambda>0.
$$

Multiplying by \\(e^\lambda\\),

$$
\sum_{s=0}^\infty g(s)\frac{\lambda^s}{s!}=0.
$$

The left side is an analytic power series. Since it vanishes on an interval, all its coefficients vanish. Hence \\(g(s)=0\\) for every nonnegative integer \\(s\\).

\\(\square\\)

## 4. Completeness of exponential sums

<div class="theorem" markdown="1">

**Theorem 5.5.**

If \\(X_1,\dots,X_n\\) are iid exponential with mean \\(\theta>0\\), then

$$
S=\sum_{i=1}^nX_i
$$

is complete.

</div>

**Proof.**

First derive the distribution of the sum. For one exponential observation with mean \\(\theta\\),

$$
M_X(t)
=
\operatorname{E}[e^{tX}]
=
\frac{1}{1-\theta t},
\qquad t<\frac1\theta.
$$

By independence,

$$
M_S(t)
=
\prod_{i=1}^n M_{X_i}(t)
=
(1-\theta t)^{-n}.
$$

This is the moment-generating function of a gamma random variable with shape \\(n\\) and scale \\(\theta\\). Therefore

$$
\boxed{
S=\sum_{i=1}^nX_i
\sim
\operatorname{Gamma}(n,\text{scale }\theta).
}
$$

Its density is

$$
f_{S,\theta}(s)
=\frac{s^{n-1}}{\Gamma(n)\theta^n}e^{-s/\theta}\mathbf{1}_{(0,\infty)}(s).
$$

Suppose \\(\operatorname{E}\_\theta[g(S)]=0\\) for all \\(\theta>0\\). Then

$$
\int_0^\infty g(s)s^{n-1}e^{-s/\theta}\,\mathrm{d}s=0
\qquad\text{for every }\theta>0.
$$

Let \\(u=1/\theta\\). We obtain

$$
\int_0^\infty \bigl[g(s)s^{n-1}\bigr]e^{-us}\,\mathrm{d}s=0
\qquad\text{for every }u>0.
$$

By uniqueness of the Laplace transform,

$$
g(s)s^{n-1}=0
\quad\text{for almost every }s>0.
$$

Since \\(s^{n-1}>0\\) for \\(s>0\\), \\(g(s)=0\\) almost everywhere.

\\(\square\\)

## 5. Distribution of the minimum and maximum for \\(U(0,\theta)\\)

The uniform completeness argument uses the sample maximum, so it is useful to derive the order-statistic distributions explicitly.

### Worked Example 5.1 — Minimum and maximum of an iid uniform sample

Let

$$
X_1,\ldots,X_n
\overset{\mathrm{iid}}{\sim}
\operatorname{Uniform}(0,\theta),
$$

and define

$$
X_{(1)}=\min_iX_i,
\qquad
X_{(n)}=\max_iX_i.
$$

**Maximum.** For \\(0<m<\theta\\),

$$
\begin{aligned}
F_{X_{(n)}}(m)
&=\Pr(X_{(n)}\le m)\\
&=\Pr(X_1\le m,\ldots,X_n\le m)\\
&=\prod_{i=1}^n\Pr(X_i\le m)\\
&=\left(\frac{m}{\theta}\right)^n.
\end{aligned}
$$

Thus

$$
F_{X_{(n)}}(m)
=
\begin{cases}
0, & m\le0,\\
(m/\theta)^n, & 0<m<\theta,\\
1, & m\ge\theta,
\end{cases}
$$

and differentiating on \\((0,\theta)\\) gives

$$
\boxed{
f_{X_{(n)}}(m)
=
\frac{nm^{n-1}}{\theta^n},
\qquad 0<m<\theta.
}
$$

Equivalently,

$$
\frac{X_{(n)}}{\theta}
\sim
\operatorname{Beta}(n,1).
$$

**Minimum.** It is easiest to begin with the survival probability. For \\(0<m<\theta\\),

$$
\begin{aligned}
\Pr(X_{(1)}>m)
&=\Pr(X_1>m,\ldots,X_n>m)\\
&=\left(1-\frac{m}{\theta}\right)^n.
\end{aligned}
$$

Hence

$$
F_{X_{(1)}}(m)
=
1-\left(1-\frac{m}{\theta}\right)^n,
\qquad 0<m<\theta,
$$

and

$$
\boxed{
f_{X_{(1)}}(m)
=
\frac{n}{\theta}
\left(1-\frac{m}{\theta}\right)^{n-1}
=
\frac{n(\theta-m)^{n-1}}{\theta^n},
\qquad 0<m<\theta.
}
$$

Equivalently,

$$
\frac{X_{(1)}}{\theta}
\sim
\operatorname{Beta}(1,n).
$$

**Final result.**

The maximum has density proportional to \\(m^{n-1}\\), while the minimum has density proportional to \\((\theta-m)^{n-1}\\). These two formulas will repeatedly appear in endpoint-estimation problems.

## 6. Completeness of the uniform maximum

<div class="theorem" markdown="1">

**Theorem 5.6.**

For an iid sample from \\(\operatorname{Uniform}(0,\theta)\\), the maximum \\(M=X\_{(n)}\\) is complete.

</div>

**Proof.**

The density of \\(M\\) is

$$
f_{M,\theta}(m)=\frac{n m^{n-1}}{\theta^n}\mathbf{1}_{(0,\theta)}(m).
$$

Suppose \\(\operatorname{E}\_\theta[g(M)]=0\\) for all \\(\theta>0\\). Then

$$
0=\frac n{\theta^n}\int_0^\theta g(m)m^{n-1}\,\mathrm{d}m.
$$

Therefore

$$
\int_0^\theta g(m)m^{n-1}\,\mathrm{d}m=0
\qquad\text{for every }\theta>0.
$$

Define

$$
H(\theta)
=
\int_0^\theta g(m)m^{n-1}\,\mathrm dm.
$$

The preceding equation says

$$
H(\theta)=0
\qquad
\text{for every }\theta>0.
$$

Thus \\(H\\) is the constant-zero function. Because \\(g(m)m^{n-1}\\) is locally integrable, \\(H\\) is absolutely continuous. The fundamental theorem of calculus for such integrals gives

$$
H'(\theta)
=
g(\theta)\theta^{n-1}
$$

for almost every \\(\theta>0\\). But \\(H(\theta)\equiv0\\), so \\(H'(\theta)=0\\) wherever the derivative exists. Therefore

$$
g(\theta)\theta^{n-1}=0
\qquad\text{for almost every }\theta>0.
$$

Since \\(\theta^{n-1}>0\\) for every \\(\theta>0\\),

$$
\boxed{
g(\theta)=0
\quad\text{for almost every }\theta>0.
}
$$

Renaming the dummy variable \\(\theta\\) as \\(m\\) gives the desired conclusion \\(g(m)=0\\) almost everywhere on the support of the maximum. Hence \\(g(M)=0\\) almost surely for every parameter value, proving completeness.

\\(\square\\)

## 7. Exponential families: structure and sufficient statistics

The new handwritten material develops exponential families explicitly. It is useful to place that material here because exponential-family structure explains both sufficiency and many completeness results.

<div class="definition" markdown="1">

**Definition 5.7 — One-parameter exponential family.**
A family of densities or mass functions with common support is a one-parameter exponential family if it can be written as

$$
f_\theta(x)
=
h(x)\,p(\theta)
\exp\lbrace c(\theta)T(x)\rbrace ,
$$

where \\(h(x)\ge0\\), \\(p(\theta)>0\\), and the support does not depend on \\(\theta\\).

</div>

Equivalently, one often writes

$$
f_\eta(x)
=
h(x)\exp\lbrace \eta T(x)-A(\eta)\rbrace ,
$$

where

$$
\eta=c(\theta)
$$

is the _natural parameter_ and

$$
A(\eta)
$$

is the log-normalising function.

<div class="remark" markdown="1">

**Remark.**
The fixed-support condition is essential for the usual regular exponential-family theory. Families such as \\(\operatorname{Uniform}(0,\theta)\\) have parameter-dependent support and therefore do not fit this regular form.

</div>

For an iid sample,

$$
\begin{aligned}
\prod_{i=1}^n f_\theta(x_i)
&=
p(\theta)^n
\exp\left\lbrace c(\theta)\sum_{i=1}^nT(x_i)
\right\rbrace \prod_{i=1}^nh(x_i).
\end{aligned}
$$

Hence the factorisation theorem gives

<div class="proposition" markdown="1">

**Proposition 5.8 — Canonical sufficient statistic in an iid exponential family.**
If \\(X_1,\ldots,X_n\\) are iid from the one-parameter exponential family above, then

$$
S=\sum_{i=1}^nT(X_i)
$$

is sufficient for \\(\theta\\).

</div>

### Worked Example 5.2 — Binomial distribution as an exponential family

For

$$
X\sim\operatorname{Binomial}(m,\theta),
\qquad
0<\theta<1,
$$

we have

$$
\begin{aligned}
f_\theta(x)
&=
\binom mx\theta^x(1-\theta)^{m-x}\\
&=
\binom mx(1-\theta)^m
\left(\frac{\theta}{1-\theta}\right)^x\\
&=
\binom mx
\exp\left\lbrace x\log\frac{\theta}{1-\theta}
+
m\log(1-\theta)
\right\rbrace .
\end{aligned}
$$

Thus

$$
T(x)=x,
\qquad
\eta(\theta)=\log\frac{\theta}{1-\theta},
$$

and the natural parameter space is all of \\(\mathbb R\\).

### Worked Example 5.3 — Poisson distribution as an exponential family

For

$$
X\sim\operatorname{Poisson}(\theta),
\qquad \theta>0,
$$

$$
f_\theta(x)
=
\frac{e^{-\theta}\theta^x}{x!}
=
\frac1{x!}
\exp\lbrace x\log\theta-\theta\rbrace .
$$

Hence

$$
T(x)=x,
\qquad
\eta=\log\theta\in\mathbb R.
$$

### Worked Example 5.4 — Normal location with known variance

Let

$$
X\sim N(\theta,1).
$$

Then

$$
\begin{aligned}
f_\theta(x)
&=
\frac1{\sqrt{2\pi}}
\exp\left\lbrace -\frac12(x-\theta)^2\right\rbrace \\
&=
\frac1{\sqrt{2\pi}}e^{-x^2/2}
\exp\left\lbrace \theta x-\frac12\theta^2\right\rbrace .
\end{aligned}
$$

Therefore

$$
T(x)=x,
\qquad
\eta=\theta.
$$

<div class="remark" markdown="1">

**Editorial note.**
One handwritten expansion has the sign of the \\(x\theta\\) term reversed. Expanding

$$
-\frac12(x-\theta)^2
=
-\frac12x^2+x\theta-\frac12\theta^2
$$

shows that the correct sign is positive.

</div>

### Worked Example 5.5 — Gamma scale family with known shape

Suppose

$$
X\sim\operatorname{Gamma}(\nu,\text{scale }\theta),
\qquad
\nu>0\text{ known},\quad \theta>0,
$$

with density

$$
f_\theta(x)
=
\frac{1}{\Gamma(\nu)\theta^\nu}
x^{\nu-1}e^{-x/\theta},
\qquad x>0.
$$

This can be written as

$$
f_\theta(x)
=
\frac{x^{\nu-1}}{\Gamma(\nu)}
\exp\left\lbrace -\frac{x}{\theta}
-\nu\log\theta
\right\rbrace .
$$

Thus

$$
T(x)=x,
\qquad
\eta=-\frac1\theta\in(-\infty,0).
$$

For an iid sample, \\(\sum_iX_i\\) is sufficient. Since \\((-\infty,0)\\) contains a nonempty open interval, the full-family completeness theorem applies as well.

## 8. Completeness in full exponential families

The natural parameter space is the set of all \\(\eta\\) for which the normalising integral is finite:

$$
\mathcal N
=
\left\lbrace \eta:
\int_{\mathcal X} h(x)e^{\eta T(x)}\,\mathrm dx<\infty
\right\rbrace


$$

For a discrete model, the corresponding normalising condition is the same statement with the integral replaced by a sum over the support.

<div class="theorem" markdown="1">

**Theorem 5.9 — Completeness of a full one-parameter natural exponential family.**
Suppose the natural parameter space \\(\mathcal N\subseteq\mathbb R\\) contains a nonempty open interval. For an iid sample, the canonical sufficient statistic

$$
S=\sum_{i=1}^nT(X_i)
$$

is complete, provided the relevant expectations exist.

</div>

**Proof.**

We give the continuous version using ordinary integrals. The discrete proof is the same argument with sums.

Because the joint density of the iid sample is

$$
\left(\prod_{i=1}^nh(x_i)\right)
\exp\left\lbrace
\eta\sum_{i=1}^nT(x_i)-nA(\eta)
\right\rbrace,
$$

the density of

$$
S=\sum_{i=1}^nT(X_i)
$$

has the form

$$
\boxed{
f_{S,\eta}(s)
=
q(s)e^{\eta s-nA(\eta)},
}
$$

where \\(q(s)\\) does not depend on \\(\eta\\). The exact expression for \\(q\\) is usually unnecessary.

Assume

$$
\operatorname{E}_\eta[g(S)]=0
\qquad
\text{for every }\eta\in\mathcal N,
$$

with \\(\operatorname{E}\_\eta[\lvert g(S)\rvert]<\infty\\). Then

$$
\begin{aligned}
0
&=\int g(s)f_{S,\eta}(s)\,\mathrm ds\\
&=e^{-nA(\eta)}
\int g(s)q(s)e^{\eta s}\,\mathrm ds.
\end{aligned}
$$

Since the normalising factor is positive,

$$
\int g(s)q(s)e^{\eta s}\,\mathrm ds
=0
\qquad
\text{for every }\eta\in\mathcal N.
$$

Choose an interior point \\(\eta_0\\) of an open interval contained in \\(\mathcal N\\). Then there is \\(\varepsilon>0\\) such that \\(\eta_0+t\in\mathcal N\\) whenever \\(\lvert t\rvert<\varepsilon\\). Hence

$$
\int
\left[g(s)q(s)e^{\eta_0s}\right]e^{ts}\,\mathrm ds
=0
\qquad
\text{for every }\lvert t\rvert<\varepsilon.
$$

Define

$$
h_0(s)=g(s)q(s)e^{\eta_0s}.
$$

The preceding integral is the bilateral Laplace transform of \\(h_0\\). By uniqueness of the Laplace transform, a transform that is zero on a nonempty open interval forces

$$
h_0(s)=0
$$

for almost every \\(s\\). Because \\(e^{\eta_0s}>0\\), and \\(q(s)>0\\) on the support of \\(S\\),

$$
g(s)=0
$$

for almost every \\(s\\) in that support. Therefore

$$
g(S)=0
\quad\text{almost surely},
$$

which proves completeness.

\\(\square\\)

The open-interval condition is doing real work: it gives a whole interval of transform values, not merely one isolated equation.

<div class="theorem" markdown="1">

**Theorem 5.10 — Multiparameter version.**
Consider a \\(k\\)-parameter natural exponential family

$$
f_\eta(x)
=
h(x)\exp\left\lbrace \sum_{j=1}^k\eta_jT_j(x)-A(\eta)
\right\rbrace ,
\qquad
\eta\in\mathcal N\subseteq\mathbb R^k.
$$

If \\(\mathcal N\\) contains a nonempty open subset of \\(\mathbb R^k\\), then for an iid sample the vector

$$
S=
\left(
\sum_{i=1}^nT_1(X_i),
\ldots,
\sum_{i=1}^nT_k(X_i)
\right)
$$

is complete under the usual integrability conditions.

</div>

A \\(k\\)-dimensional rectangle contained in \\(\mathcal N\\) is a convenient sufficient condition, but the essential requirement is a nonempty open subset of the full \\(k\\)-dimensional natural parameter space.

### Worked Example 5.6 — Normal family with both mean and variance unknown

Let

$$
X_1,\ldots,X_n
\overset{\mathrm{iid}}{\sim}
N(\mu,\sigma^2),
\qquad
\mu\in\mathbb R,\quad \sigma^2>0.
$$

The joint log-density, apart from terms free of \\((\mu,\sigma^2)\\), is

$$
-\frac1{2\sigma^2}
\sum_{i=1}^n(x_i-\mu)^2
-\frac n2\log\sigma^2.
$$

Expanding,

$$
\begin{aligned}
-\frac1{2\sigma^2}
\sum_{i=1}^n(x_i-\mu)^2
&=
-\frac1{2\sigma^2}\sum_{i=1}^n x_i^2
+
\frac{\mu}{\sigma^2}\sum_{i=1}^n x_i
-
\frac{n\mu^2}{2\sigma^2}.
\end{aligned}
$$

Thus the canonical statistic is

$$
\boxed{
S=
\left(
\sum_{i=1}^nX_i,\,
\sum_{i=1}^nX_i^2
\right).
}
$$

The natural parameters are

$$
\eta_1=\frac{\mu}{\sigma^2},
\qquad
\eta_2=-\frac1{2\sigma^2}.
$$

Their space is

$$
\mathcal N
=
\lbrace (\eta_1,\eta_2):\eta_1\in\mathbb R,\ \eta_2<0\rbrace ,
$$

which is an open subset of \\(\mathbb R^2\\). Therefore the canonical sufficient statistic is complete.

<div class="remark" markdown="1">

**Remark.**
The equivalent statistic \\((\bar X,\sum_i(X_i-\bar X)^2)\\) is also sufficient because it is a one-to-one transformation of \\((\sum_iX_i,\sum_iX_i^2)\\).

</div>

### Worked Example 5.7 — Multinomial family

Let

$$
(Y_1,\ldots,Y_{k+1})
\sim
\operatorname{Multinomial}
\left(
m;p_1,\ldots,p_{k+1}
\right),
$$

where

$$
p_j>0,
\qquad
\sum_{j=1}^{k+1}p_j=1.
$$

The mass function is

$$
\frac{m!}{\prod_{j=1}^{k+1}y_j!}
\prod_{j=1}^{k+1}p_j^{y_j}.
$$

Using

$$
p_{k+1}=1-\sum_{j=1}^kp_j,
$$

write

$$
\prod_{j=1}^{k+1}p_j^{y_j}
=
p_{k+1}^m
\exp\left\lbrace \sum_{j=1}^k
y_j\log\frac{p_j}{p_{k+1}}
\right\rbrace .
$$

Hence the natural parameters are

$$
\eta_j=\log\frac{p_j}{p_{k+1}},
\qquad j=1,\ldots,k.
$$

As \\((p_1,\ldots,p\_{k+1})\\) ranges over the interior of the probability simplex, \\(\eta\\) ranges over all of \\(\mathbb R^k\\). Thus the corresponding count vector is complete for the full multinomial family.

## 9. Power-series families

The handwritten notes also isolate a useful discrete family:

$$
f_\theta(x)
=
\frac{a(x)\theta^x}{g(\theta)},
\qquad
x=0,1,2,\ldots,
\qquad
0<\theta<b,
$$

where

$$
g(\theta)
=
\sum_{x=0}^\infty a(x)\theta^x
<\infty.
$$

Because

$$
\theta^x=e^{x\log\theta},
$$

this is a natural exponential family with

$$
T(x)=x,
\qquad
\eta=\log\theta.
$$

For an iid sample,

$$
S=\sum_{i=1}^nX_i
$$

is sufficient. The natural parameter space contains

$$
(-\infty,\log b),
$$

which has nonempty interior, so \\(S\\) is complete.

This framework includes many familiar count distributions as special cases.

## 10. A complete sufficient statistic outside the regular exponential-family template

### Worked Example 5.8 — Uniform distribution with both endpoints unknown

Let

$$
X_1,\ldots,X_n
\overset{\mathrm{iid}}{\sim}
\operatorname{Uniform}(\phi,\psi),
\qquad
\phi<\psi,
\qquad
n\ge2.
$$

The joint density is

$$
\frac1{(\psi-\phi)^n}
\mathbf 1_{\lbrace \phi<X_{(1)}<X_{(n)}<\psi\rbrace },
$$

so

$$
S=(U,V)=(X_{(1)},X_{(n)})
$$

is sufficient.

The joint density of \\((U,V)\\) is

$$
f_{U,V}(u,v)
=
\frac{n(n-1)}{(\psi-\phi)^n}
(v-u)^{n-2}
\mathbf 1_{\lbrace \phi<u<v<\psi\rbrace }.
$$

Suppose

$$
\operatorname{E}_{\phi,\psi}[g(U,V)]=0
\qquad
\text{for every }\phi<\psi.
$$

After removing the positive normalising constant, this means

$$
F(\phi,\psi)
:=
\int_{\phi}^{\psi}
\int_{u}^{\psi}
 g(u,v)(v-u)^{n-2}
\,\mathrm dv\,\mathrm du
=0
\qquad
\text{for every }\phi<\psi.
$$

Fix \\(\phi\\). Under the integrability assumption, \\(F(\phi,\psi)\\) is absolutely continuous as a function of \\(\psi\\). Differentiating with respect to \\(\psi\\) gives, for almost every \\(\psi>\phi\\),

$$
\frac{\partial F}{\partial\psi}(\phi,\psi)
=
\int_{\phi}^{\psi}
 g(u,\psi)(\psi-u)^{n-2}
\,\mathrm du
=0.
$$

Now fix such a \\(\psi\\) and regard the last integral as a function of its lower limit \\(\phi\\). Differentiating with respect to \\(\phi\\) gives

$$
-\,g(\phi,\psi)(\psi-\phi)^{n-2}=0
$$

for almost every pair \\(\phi<\psi\\). Since

$$
(\psi-\phi)^{n-2}>0
\qquad
\text{whenever }\phi<\psi,
$$

we conclude that

$$
g(\phi,\psi)=0
$$

for almost every \\((\phi,\psi)\\) with \\(\phi<\psi\\). Relabeling \\((\phi,\psi)\\) as generic values \\((u,v)\\) shows

$$
g(u,v)=0
$$

almost everywhere on the support of \\((U,V)\\).

Thus

$$
\boxed{
(X_{(1)},X_{(n)})
\text{ is complete and sufficient for }(\phi,\psi).
}
$$

<div class="remark" markdown="1">

**Remark.**
This is a useful contrast with the location family \\(\operatorname{Uniform}(\theta,\theta+1)\\). When both endpoints are free, \\((X\_{(1)},X\_{(n)})\\) is complete; when the interval length is fixed, the range is ancillary and the same statistic is not complete.

</div>

## 11. Basu's theorem

<div class="theorem" markdown="1">

**Theorem 5.11 — Basu.**
Let \\(T\\) be a complete sufficient statistic for \\(\theta\\), and let \\(A\\) be ancillary for \\(\theta\\). Then \\(T\\) and \\(A\\) are independent.

</div>

**Proof.**

Fix a Borel set \\(B\\) in the range of \\(A\\) and define

$$
q_B(T)
=
\Pr_\theta(A\in B\mid T).
$$

Because \\(T\\) is sufficient, the conditional distribution of the full data given \\(T\\) does not depend on \\(\theta\\). Therefore \\(q_B(T)\\) is a function of \\(T\\) that does not depend on \\(\theta\\).

Since \\(A\\) is ancillary,

$$
\Pr_\theta(A\in B)=c_B
$$

is constant in \\(\theta\\). Taking expectations,

$$
\operatorname{E}_\theta[q_B(T)]
=
\Pr_\theta(A\in B)
=
c_B.
$$

Hence

$$
\operatorname{E}_\theta[q_B(T)-c_B]=0
\qquad
\text{for every }\theta.
$$

Completeness of \\(T\\) implies

$$
q_B(T)=c_B
\quad\text{almost surely}.
$$

Therefore

$$
\Pr(A\in B\mid T)
=
\Pr(A\in B)
$$

almost surely for every Borel set \\(B\\), which is exactly independence of \\(A\\) and \\(T\\).

\\(\square\\)

### Worked Example 5.9 — Normal sample mean and residual sum of squares

Let

$$
X_1,\ldots,X_n
\overset{\mathrm{iid}}{\sim}
N(\theta,\sigma^2),
$$

where \\(\sigma^2\\) is known.

The statistic

$$
T=\bar X
$$

is complete and sufficient for \\(\theta\\).

The residual sum of squares

$$
A=
\sum_{i=1}^n(X_i-\bar X)^2
$$

satisfies

$$
\frac{A}{\sigma^2}
\sim
\chi^2_{n-1},
$$

whose distribution does not involve \\(\theta\\). Thus \\(A\\) is ancillary for \\(\theta\\).

By Basu's theorem,

$$
\boxed{
\bar X
\ \perp\
\sum_{i=1}^n(X_i-\bar X)^2.
}
$$

<div class="warning" markdown="1">

**Important qualification.**
If \\(\sigma^2\\) is also unknown, the residual sum of squares is not ancillary for the full parameter \\((\theta,\sigma^2)\\) because its distribution depends on \\(\sigma^2\\). The statement above uses known \\(\sigma^2\\).

</div>

## Questions answered in this lecture

**Question.**
What extra property does completeness add beyond sufficiency?

**Answer.**

Sufficiency concerns information retained after conditioning; completeness concerns uniqueness of functions of the statistic through the expectation operator.

**Question.**
Why does a polynomial that vanishes for all positive \\(z\\) prove binomial completeness?

**Answer.**

A nonzero polynomial has only finitely many roots. Vanishing on an interval forces every coefficient to be zero.

**Question.**
Why is continuity of \\(g\\) unnecessary in the uniform completeness proof?

**Answer.**

The indefinite integral is absolutely continuous, so the fundamental theorem for Lebesgue integrals gives its derivative almost everywhere; that is enough to conclude \\(g=0\\) almost everywhere.

**Question.**
What is the essential structural condition behind the theorem?

**Answer.**

The natural parameter set must contain a nonempty open subset of the correct dimension; this rules out curved subfamilies for this direct argument.

**Question.**
Why does a Laplace-transform identity prove completeness?

**Answer.**

After centering at an interior natural-parameter value, the expectation identity is a Laplace transform of an integrable function. Uniqueness of the Laplace transform forces that function, and hence the original \\(g\\), to be zero almost everywhere.

**Question.**
Why should this theorem not be invoked mechanically?

**Answer.**

Fullness, natural-parameter dimension, common support, and the transform/integrability assumptions all need to be checked.

**Question.**
When does the canonical statistic of a full exponential family become complete?

**Answer.**

For a \\(k\\)-parameter natural exponential family, a standard sufficient condition is that the natural parameter space contain a nonempty open subset of \\(\mathbb R^k\\), together with the usual integrability assumptions. A rectangle with nonempty interior is a convenient stronger condition.

**Question.**
Is \\((X\_{(1)},X\_{(n)})\\) complete for iid \\(\operatorname{Uniform}(\phi,\psi)\\) observations when both endpoints are unknown?

**Answer.**

Yes, for \\(n\ge2\\). The proof writes the zero-expectation condition as a double integral over \\(\phi<u<v<\psi\\) and differentiates first with respect to the upper endpoint and then with respect to the lower endpoint, forcing \\(g(u,v)=0\\) almost everywhere.

**Question.**
Why are \\(\bar X\\) and the residual sum of squares independent in the normal location model with known variance?

**Answer.**

\\(\bar X\\) is complete sufficient for the unknown mean, while the residual sum of squares has a distribution free of that mean. Basu's theorem therefore gives independence.

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.
- Expanded source: the complete LaTeX notes and compiled PDF used for this Markdown conversion.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell-ancillarity/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-consistency/' | relative_url }})
</nav>

</div>
