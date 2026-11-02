---
layout: page
title: "Lecture 12: Likelihood-Ratio Tests, Classical t/F Tests, and Multivariate Hotelling Tests"
short_title: "Likelihood-ratio and multivariate tests"
course: "Parametric Inference"
lecture: 12
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Gives a complete Neyman–Pearson characterization and develops generalized likelihood-ratio tests, their equivalence to one- and two-sample t and F tests, Poisson equality tests, Hotelling T-squared tests, the union-intersection principle, and likelihood-ratio tests for equality of covariance matrices."
topics:
  - "Neyman-Pearson lemma"
  - "likelihood-ratio test"
  - "generalized likelihood ratio"
  - "one-sample t test"
  - "two-sample t test"
  - "Poisson equality test"
  - "unbiased two-sided tests"
  - "Hotelling T-squared"
  - "union-intersection principle"
  - "two-sample multivariate normal"
  - "F test for variances"
  - "equality of covariance matrices"
  - "simulation calibration"
previous: "lecture-11-admissibility-equivariance-stein"
next: null
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-11-02"
status: "complete"
math: true
permalink: /notes/parametric-inference/lecture-12-likelihood-ratio-classical-multivariate-tests/
course_slug: parametric-inference
note_kind: lecture
course_order: 12
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the 13 October and 27 October 2026 Parametric Inference classes of Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata. Every likelihood-ratio exercise written in those pages is derived here, including the multivariate and simulation-based problems. Substantial corrections to shorthand claims in the source are marked explicitly.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-11-admissibility-equivariance-stein/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }})
</nav>

## Learning objectives

After this lecture, you should be able to:

- state all three useful parts of the Neyman–Pearson lemma and prove the optimality inequality;
- define the generalized likelihood-ratio statistic for a composite null;
- derive the one-sample and pooled two-sample \\(t\\)-tests as likelihood-ratio tests;
- derive the Poisson equality GLR and explain precisely when “large \\(\lvertX-Y\rvert\\)” is an equivalent description;
- prove unbiasedness of the usual two-sided normal \\(t\\)-tests;
- derive the one- and two-sample Hotelling \\(T^2\\) tests from determinants;
- derive the same Hotelling statistics by the union-intersection principle;
- derive the likelihood-ratio test for equality of two normal variances and connect it to the \\(F\\)-statistic;
- formulate the multivariate covariance-equality likelihood ratio and calibrate it by simulation.

## 1. Neyman–Pearson lemma: complete characterization

Consider the simple-versus-simple problem

$$
H_0:f=f_0
\qquad\text{versus}\qquad
H_1:f=f_1.
$$

For \\(k\ge0\\), define a likelihood-ratio-form test

$$
\phi^{\star}(x)=
\begin{cases}
1,&f_1(x)>k f_0(x),\\
\gamma(x),&f_1(x)=k f_0(x),\\
0,&f_1(x)<k f_0(x),
\end{cases}
$$

where \\(0\le\gamma(x)\le1\\) is chosen on the tie set to obtain the prescribed size.

<div class="theorem" markdown="1">

**Theorem 12.1 — Neyman–Pearson lemma.** For every \\(0<\alpha<1\\):

1. there exists a level-\\(\alpha\\) test of the likelihood-ratio form above, with suitable \\(k\\) and tie randomization;
2. every such size-\\(\alpha\\) likelihood-ratio test is most powerful among all level-\\(\alpha\\) tests;
3. conversely, if a size-\\(\alpha\\) test is most powerful, then, apart from changes on the tie set \\(\lbracef_1=kf_0\rbrace\\) and null sets, it has the likelihood-ratio form.

</div>

### 1.1 Existence

Under \\(H_0\\), consider

$$
L(X)=\frac{f_1(X)}{f_0(X)}.
$$

Choose \\(k\\) so that

$$
P_0(L>k)\le\alpha\le P_0(L\ge k).
$$

Then randomize on \\(L=k\\) with probability

$$
\gamma
=
\frac{\alpha-P_0(L>k)}{P_0(L=k)}
$$

when the denominator is nonzero. This gives exact size \\(\alpha\\).

### 1.2 Most-powerful property

Let \\(\phi\\) be any other test with

$$
E_0[\phi]\le E_0[\phi^{\star}]=\alpha.
$$

Pointwise,

$$
(\phi^{\star}-\phi)(f_1-kf_0)\ge0.
$$

Why? Where \\(f_1>kf_0\\), \\(\phi^{\star}=1\ge\phi\\); where \\(f_1<kf_0\\), \\(\phi^{\star}=0\le\phi\\), so both factors change sign; on the tie set the product is zero.

Integrating,

$$
\int(\phi^{\star}-\phi)f_1
\ge
k\int(\phi^{\star}-\phi)f_0.
$$

The right side is nonnegative because \\(E_0\phi^{\star}\ge E_0\phi\\). Therefore

$$
E_1[\phi^{\star}]\ge E_1[\phi].
$$

So \\(\phi^{\star}\\) is MP.

### 1.3 Converse form

If an MP size-\\(\alpha\\) test differed from the likelihood-ratio rule on a set where \\(f_1-kf_0\ne0\\), the same inequality would be strict, producing strictly larger power for the likelihood-ratio rule and contradicting maximality. Thus any MP rule has the same ordering structure, with freedom only on the tie set.

## 2. Generalized likelihood-ratio tests

For

$$
H_0:\theta\in\Theta_0
\qquad\text{versus}\qquad
H_1:\theta\in\Theta\setminus\Theta_0,
$$

define

$$
\boxed{
\Lambda(x)
=
\frac{\sup_{\theta\in\Theta_0}L(\theta;x)}
{\sup_{\theta\in\Theta}L(\theta;x)}.
}
$$

Because \\(\Theta_0\subseteq\Theta\\),

$$
0\le\Lambda(x)\le1.
$$

Small \\(\Lambda\\) means that restricting the parameter to the null causes a large loss of maximized likelihood. Therefore the generalized likelihood-ratio test rejects for sufficiently small values of \\(\Lambda\\), or equivalently for sufficiently large values of any monotone decreasing transform such as

$$
-2\log\Lambda.
$$

## 3. One-sample normal mean, unknown variance: GLRT gives the two-sided t-test

Let

$$
X_1,\ldots,X_n\overset{\text{iid}}\sim N(\mu,\sigma^2),
$$

and test

$$
H_0:\mu=0
\qquad\text{versus}\qquad
H_1:\mu\ne0,
$$

with \\(\sigma^2\\) unknown.

The likelihood is

$$
L(\mu,\sigma^2)
=(2\pi\sigma^2)^{-n/2}
\exp\left\lbrace-\frac1{2\sigma^2}\sum_i(X_i-\mu)^2\right\rbrace.
$$

### 3.1 Unrestricted maximization

The unrestricted MLEs are

$$
\widehat\mu=\bar X,
$$

and

$$
\widehat\sigma^2
=
\frac1n\sum_i(X_i-\bar X)^2.
$$

Write

$$
A=\sum_i(X_i-\bar X)^2.
$$

Then the unrestricted maximized likelihood is proportional to

$$
(A/n)^{-n/2}.
$$

### 3.2 Maximization under the null

Under \\(\mu=0\\),

$$
\widehat\sigma_0^2
=
\frac1n\sum_iX_i^2.
$$

Using

$$
\sum_iX_i^2
=A+n\bar X^2,
$$

the restricted maximized likelihood is proportional to

$$
\left(\frac{A+n\bar X^2}{n}\right)^{-n/2}.
$$

Therefore

$$
\Lambda
=
\left(
\frac{A}{A+n\bar X^2}
\right)^{n/2}.
$$

Let

$$
S^2=\frac{A}{n-1}
$$

and

$$
t=\frac{\sqrt n\,\bar X}{S}.
$$

Then

$$
\frac{n\bar X^2}{A}
=
\frac{t^2}{n-1}.
$$

Hence

$$
\boxed{
\Lambda
=
\left(1+\frac{t^2}{n-1}\right)^{-n/2}.
}
$$

Thus \\(\Lambda\\) is strictly decreasing in \\(t^2\\), so the GLRT rejects for large \\(\lvertt\rvert\\). Under \\(H_0\\),

$$
t\sim t_{n-1}.
$$

Therefore the level-\\(\alpha\\) GLRT is exactly

$$
\boxed{
\text{Reject }H_0
\iff
\lvertt\rvert>t_{n-1,1-\alpha/2}.
}
$$

## 4. Two normal means with common unknown variance: pooled two-sample t-test

Let

$$
X_1,\ldots,X_n\overset{\text{iid}}\sim N(\mu_1,\sigma^2),
$$

$$
Y_1,\ldots,Y_m\overset{\text{iid}}\sim N(\mu_2,\sigma^2),
$$

independently, and test

$$
H_0:\mu_1=\mu_2
\qquad\text{versus}\qquad
H_1:\mu_1\ne\mu_2.
$$

Let

$$
A
=
\sum_{i=1}^n(X_i-\bar X)^2
+
\sum_{j=1}^m(Y_j-\bar Y)^2,
$$

and \\(N=n+m\\).

Under the unrestricted model, the MLEs are \\(\bar X,\bar Y\\) and

$$
\widehat\sigma^2=A/N.
$$

Under \\(H_0\\), the common mean MLE is

$$
\widehat\mu_0
=
\frac{n\bar X+m\bar Y}{N}.
$$

The restricted residual sum of squares satisfies the ANOVA identity

$$
A_0
=
A+
\frac{nm}{N}(\bar X-\bar Y)^2.
$$

Therefore

$$
\Lambda
=
\left(
\frac{A}{A_0}
\right)^{N/2}
=
\left[
1+
\frac{nm}{N}
\frac{(\bar X-\bar Y)^2}{A}
\right]^{-N/2}.
$$

Define the pooled variance

$$
S_p^2=\frac{A}{N-2}
$$

and the pooled two-sample statistic

$$
t
=
\frac{\bar X-\bar Y}
{S_p\sqrt{1/n+1/m}}.
$$

Then

$$
\frac{nm}{N}
\frac{(\bar X-\bar Y)^2}{A}
=
\frac{t^2}{N-2}.
$$

Hence

$$
\boxed{
\Lambda
=
\left(1+\frac{t^2}{N-2}\right)^{-N/2}.
}
$$

Thus the GLRT is exactly the standard two-sided pooled \\(t\\)-test:

$$
\boxed{
\lvertt\rvert>t_{N-2,1-\alpha/2}.
}
$$

## 5. Are the two-sided t-tests unbiased?

Yes.

For the one-sample problem, under \\((\mu,\sigma)\\), the statistic has a noncentral \\(t\\) distribution with noncentrality

$$
\delta=\frac{\sqrt n\,\mu}{\sigma}.
$$

A useful representation is

$$
T=\frac{Z+\delta}{\sqrt{V/\nu}},
$$

where

$$
Z\sim N(0,1),
\qquad
V\sim\chi^2_\nu,
\qquad
Z\perp V,
$$

and \\(\nu=n-1\\).

The two-sided test rejects for \\(\lvertT\rvert>c\\). Conditional on \\(V=v\\), put

$$
a=c\sqrt{v/\nu}>0.
$$

Then the conditional rejection probability is

$$
q_v(\delta)
=P(\lvertZ+\delta\rvert>a).
$$

It is an even function of \\(\delta\\). For \\(\delta>0\\),

$$
\begin{aligned}
q_v'(\delta)
&=
\phi(a-\delta)-\phi(a+\delta)\\
&\ge0,
\end{aligned}
$$

because \\(\lverta-\delta\rvert\le a+\delta\\) and the standard normal density decreases with absolute value. Therefore \\(q_v(\delta)\\) is minimized at \\(\delta=0\\). Averaging over \\(V\\),

$$
P_\delta(\lvertT\rvert>c)
\ge
P_0(\lvertT\rvert>c)=\alpha.
$$

Thus the two-sided one-sample \\(t\\)-test is unbiased. The same proof applies to the pooled two-sample \\(t\\)-test, with noncentrality

$$
\delta
=
\frac{\mu_1-\mu_2}{\sigma\sqrt{1/n+1/m}}.
$$

Hence both two-sided tests asked about in the 13 October notes are unbiased.

## 6. Two Poisson means: likelihood-ratio test

Let

$$
X\sim\operatorname{Poisson}(\mu_1),
\qquad
Y\sim\operatorname{Poisson}(\mu_2),
$$

independently, and test

$$
H_0:\mu_1=\mu_2
\qquad\text{versus}\qquad
H_1:\mu_1\ne\mu_2.
$$

For observed \\((x,y)\\), the unrestricted MLEs are

$$
\widehat\mu_1=x,
\qquad
\widehat\mu_2=y.
$$

Under \\(H_0\\), write the common mean as \\(\mu\\). The restricted MLE is

$$
\widehat\mu_0=\frac{x+y}{2}.
$$

Thus, with \\(s=x+y\\),

$$
\boxed{
\Lambda(x,y)
=
\frac{(s/2)^s}{x^x y^y},
}
$$

using the convention \\(0^0=1\\).

Equivalently,

$$
-2\log\Lambda
=
2\left[
x\log\frac{2x}{s}
+y\log\frac{2y}{s}
\right].
$$

For **fixed** \\(s=x+y\\), this statistic is symmetric about \\(x=s/2\\) and increases as \\(\lvertx-y\rvert\\) increases. Therefore, conditional on \\(S=X+Y=s\\), the LRT rejects for large \\(\lvertX-Y\rvert\\). Under \\(H_0\\),

$$
X\mid S=s\sim\operatorname{Bin}(s,1/2),
$$

so the exact conditional test is the two-sided binomial test.

<div class="remark" markdown="1">

**Editorial note.** The handwritten exercise says that the LR test is “equivalent to rejecting for large \\(\lvertX-Y\rvert\\).” This is exactly true **conditional on \\(X+Y=s\\)**. Unconditionally, the GLR also depends on \\(s\\); the same absolute difference can correspond to different likelihood ratios at different totals. The conditional formulation is the precise exact statement.

</div>

## 7. Polar decomposition of two independent standard normals

The 27 October page records the useful transformation

$$
Z_1=R\cos\Theta,
\qquad
Z_2=R\sin\Theta,
$$

for independent

$$
Z_1,Z_2\sim N(0,1).
$$

Let

$$
R=\sqrt{Z_1^2+Z_2^2},
\qquad
0\le\Theta<2\pi.
$$

The joint density of \\((Z_1,Z_2)\\) is

$$
f(z_1,z_2)=\frac1{2\pi}\exp\left[-\frac12(z_1^2+z_2^2)\right].
$$

The Jacobian of the polar transformation is

$$
\left\lvert\frac{\partial(z_1,z_2)}{\partial(r,\theta)}\right\rvert=r.
$$

Hence

$$
\begin{aligned}
f_{R,\Theta}(r,\theta)
&=\frac1{2\pi}e^{-r^2/2}r,
\qquad r>0,\ 0\le\theta<2\pi\\
&=\left(re^{-r^2/2}\right)\left(\frac1{2\pi}\right).
\end{aligned}
$$

The density factors, so

$$
\boxed{R\perp\!\!\!\perp\Theta,}
$$

and

$$
\boxed{\Theta\sim U(0,2\pi).}
$$

Also

$$
f_R(r)=re^{-r^2/2},\qquad r>0,
$$

so

$$
R^2=Z_1^2+Z_2^2\sim\chi^2_2.
$$

Since \\(\chi^2_2\\) is exponential with rate \\(1/2\\),

$$
\boxed{R^2\sim\operatorname{Exp}(\text{rate }1/2),}
$$

while \\(R\\) itself has the Rayleigh distribution. This is the complete polar-coordinate fact recorded in the class note.

## 8. One-sample multivariate normal mean: Hotelling's T-squared from the GLRT

Let

$$
X_1,\ldots,X_n\overset{\text{iid}}\sim N_p(\mu,\Sigma),
$$

with both \\(\mu\\) and positive-definite \\(\Sigma\\) unknown. Test

$$
H_0:\mu=0
\qquad\text{versus}\qquad
H_1:\mu\ne0.
$$

Define

$$
A
=
\sum_{i=1}^n(X_i-\bar X)(X_i-\bar X)^T,
$$

and

$$
B
=
\sum_{i=1}^nX_iX_i^T.
$$

The identity

$$
\boxed{B=A+n\bar X\bar X^T}
$$

is the multivariate analogue of total sum of squares = residual + mean sum of squares.

### 8.1 MLEs

Unrestricted:

$$
\widehat\mu=\bar X,
\qquad
\widehat\Sigma=A/n.
$$

Under \\(H_0\\):

$$
\widehat\Sigma_0=B/n.
$$

The maximized multivariate-normal likelihood is proportional to \\(\lvert\widehat\Sigma\rvert^{-n/2}\\). Therefore

$$
\Lambda
=
\left(\frac{\lvertA\rvert}{\lvertB\rvert}\right)^{n/2}.
$$

Use the matrix determinant lemma

$$
\lvertA+uv^T\rvert
=
\lvertA\rvert(1+v^TA^{-1}u).
$$

With \\(u=n\bar X\\) and \\(v=\bar X\\),

$$
\lvertB\rvert
=
\lvertA\rvert\left(1+n\bar X^TA^{-1}\bar X\right).
$$

Hence

$$
\Lambda
=
\left(1+n\bar X^TA^{-1}\bar X\right)^{-n/2}.
$$

Let the usual unbiased sample covariance be

$$
S=\frac{A}{n-1}.
$$

Define Hotelling's statistic

$$
\boxed{T^2=n\bar X^TS^{-1}\bar X.}
$$

Since

$$
n\bar X^TA^{-1}\bar X
=
\frac{T^2}{n-1},
$$

we obtain

$$
\boxed{
\Lambda
=
\left(1+\frac{T^2}{n-1}\right)^{-n/2}.
}
$$

Therefore the LRT rejects for large \\(T^2\\).

Under \\(H_0\\), provided \\(n>p\\),

$$
\boxed{
\frac{n-p}{p(n-1)}T^2
\sim
F_{p,n-p}.
}
$$

Thus the exact level-\\(\alpha\\) test rejects when

$$
T^2
>
\frac{p(n-1)}{n-p}F_{p,n-p,1-\alpha}.
$$

### 8.2 A fixed linear contrast

The handwritten page next considers, for a fixed nonzero vector \\(\ell\in\mathbb R^p\\),

$$
H_{0,\ell}:\ell^T\mu=0
\qquad\text{versus}\qquad
H_{1,\ell}:\ell^T\mu\ne0.
$$

Project the observations:

$$
Y_i=\ell^TX_i.
$$

Then

$$
Y_i\overset{\text{iid}}\sim
N\!\left(\ell^T\mu,\ell^T\Sigma\ell\right).
$$

Thus this is exactly a one-sample normal mean problem with unknown variance. Since

$$
\bar Y=\ell^T\bar X,
$$

and its sample variance is

$$
S_Y^2=\ell^TS\ell,
$$

the ordinary two-sided \\(t\\)-statistic is

$$
\boxed{
T_\ell
=
\frac{\sqrt n\,\ell^T\bar X}
{\sqrt{\ell^TS\ell}}.
}
$$

Under \\(H\_{0,\ell}\\),

$$
T_\ell\sim t_{n-1}.
$$

Therefore the level-\\(\alpha\\) test of the fixed directional hypothesis rejects for

$$
\boxed{\lvertT_\ell\rvert>t_{n-1,1-\alpha/2}.}
$$

The quantity relevant to the union-intersection construction is

$$
\frac{T_\ell^2}{n}
=
\frac{(\ell^T\bar X)^2}{\ell^TS\ell}.
$$

## 9. Union-intersection principle gives the same Hotelling test

The multivariate null can be written as

$$
H_0:\mu=0
=
\bigcap_{\ell\ne0}\lbrace\ell^T\mu=0\rbrace.
$$

The alternative is the union over directions \\(\ell\\) for which \\(\ell^T\mu\ne0\\). For a fixed \\(\ell\\), the projected observations \\(\ell^TX_i\\) are univariate normal with mean \\(\ell^T\mu\\) and variance \\(\ell^T\Sigma\ell\\). The corresponding squared \\(t\\)-type statistic is proportional to

$$
\frac{(\ell^T\bar X)^2}{\ell^TS\ell}.
$$

The union-intersection principle rejects if the strongest directional evidence is large, i.e. for large

$$
\sup_{\ell\ne0}
\frac{(\ell^T\bar X)^2}{\ell^TS\ell}.
$$

By Cauchy–Schwarz,

$$
(\ell^T\bar X)^2
=
\left[(S^{1/2}\ell)^T(S^{-1/2}\bar X)\right]^2
\le
(\ell^TS\ell)(\bar X^TS^{-1}\bar X).
$$

Equality occurs for \\(\ell\propto S^{-1}\bar X\\). Therefore

$$
\boxed{
\sup_{\ell\ne0}
\frac{(\ell^T\bar X)^2}{\ell^TS\ell}
=
\bar X^TS^{-1}\bar X.
}
$$

Multiplying by \\(n\\) gives the same Hotelling \\(T^2\\) statistic as the GLRT. Thus the likelihood-ratio and union-intersection principles lead to the same test.

## 10. Two-sample multivariate normal means

Let

$$
X_1,\ldots,X_n\overset{\text{iid}}\sim N_p(\mu_1,\Sigma),
$$

$$
Y_1,\ldots,Y_m\overset{\text{iid}}\sim N_p(\mu_2,\Sigma),
$$

independently, with common unknown covariance \\(\Sigma\\). Test

$$
H_0:\mu_1=\mu_2
\qquad\text{versus}\qquad
H_1:\mu_1\ne\mu_2.
$$

Let \\(N=n+m\\), \\(D=\bar X-\bar Y\\), and define the within-group SSCP matrix

$$
A
=
\sum_{i=1}^n(X_i-\bar X)(X_i-\bar X)^T
+
\sum_{j=1}^m(Y_j-\bar Y)(Y_j-\bar Y)^T.
$$

Under the unrestricted model,

$$
\widehat\Sigma=A/N.
$$

Under \\(H_0\\), the common mean is the pooled grand mean, and the restricted SSCP is

$$
A_0
=
A+
\frac{nm}{N}DD^T.
$$

Thus

$$
\Lambda
=
\left(\frac{\lvertA\rvert}{\lvertA_0\rvert}\right)^{N/2}.
$$

By the determinant lemma,

$$
\lvertA_0\rvert
=
\lvertA\rvert
\left(1+\frac{nm}{N}D^TA^{-1}D\right).
$$

Define pooled covariance

$$
S_p=\frac{A}{N-2}
$$

and two-sample Hotelling statistic

$$
\boxed{
T^2
=
\frac{nm}{N}D^TS_p^{-1}D.
}
$$

Then

$$
\frac{nm}{N}D^TA^{-1}D
=
\frac{T^2}{N-2},
$$

so

$$
\boxed{
\Lambda
=
\left(1+\frac{T^2}{N-2}\right)^{-N/2}.
}
$$

Hence the GLRT rejects for large \\(T^2\\).

Under \\(H_0\\), assuming the required sample-size conditions,

$$
\boxed{
\frac{N-p-1}{p(N-2)}T^2
\sim
F_{p,N-p-1}.
}
$$

The union-intersection derivation is identical in spirit: project onto every direction \\(\ell\\), form the two-sample pooled \\(t\\)-statistic in that direction, and maximize over \\(\ell\\). The supremum again equals the Hotelling quadratic form.

## 11. Equality of two normal variances: GLRT and the F-test

Let

$$
X_1,\ldots,X_n\overset{\text{iid}}\sim N(\mu_1,\sigma_1^2),
$$

$$
Y_1,\ldots,Y_m\overset{\text{iid}}\sim N(\mu_2,\sigma_2^2),
$$

independently. Test

$$
H_0:\sigma_1^2=\sigma_2^2
\qquad\text{versus}\qquad
H_1:\sigma_1^2\ne\sigma_2^2.
$$

The means are nuisance parameters and are always estimated by \\(\bar X\\) and \\(\bar Y\\). Let

$$
A=\sum_{i=1}^n(X_i-\bar X)^2,
\qquad
B=\sum_{j=1}^m(Y_j-\bar Y)^2.
$$

Unrestricted MLEs:

$$
\widehat\sigma_1^2=A/n,
\qquad
\widehat\sigma_2^2=B/m.
$$

Under \\(H_0\\), the common variance MLE is

$$
\widehat\sigma_0^2=\frac{A+B}{n+m}.
$$

Therefore, up to constants independent of the data,

$$
\boxed{
\Lambda
=
\frac{(A/n)^{n/2}(B/m)^{m/2}}
{\lbrace(A+B)/(n+m)\rbrace^{(n+m)/2}}.
}
$$

This depends on \\(A,B\\) only through their ratio. It is largest when the fitted variances are close and decreases when the ratio becomes very large or very small. Hence the LRT is a two-tail variance-ratio test.

The usual statistic is

$$
\boxed{
F
=
\frac{A/(n-1)}{B/(m-1)}.
}
$$

Under \\(H_0\\),

$$
F\sim F_{n-1,m-1}.
$$

Therefore reject for sufficiently small or sufficiently large values of \\(F\\).

<div class="remark" markdown="1">

**Editorial note.** The shorthand \\(\max\lbraceF,1/F\rbrace\\) is exactly symmetric when the two degrees of freedom are the same. For unequal sample sizes, the GLR is still a two-tail function of \\(F\\), but the two critical tails need not be represented by one common reciprocal cutoff, because \\(F\_{n-1,m-1}\\) is not invariant under reciprocal transformation without swapping degrees of freedom.

</div>

## 12. Equality of two multivariate covariance matrices

Let

$$
X_1,\ldots,X_n\overset{\text{iid}}\sim N_p(\mu_1,\Sigma_1),
$$

$$
Y_1,\ldots,Y_m\overset{\text{iid}}\sim N_p(\mu_2,\Sigma_2),
$$

independently, and test

$$
H_0:\Sigma_1=\Sigma_2
\qquad\text{versus}\qquad
H_1:\Sigma_1\ne\Sigma_2.
$$

Let

$$
A_X=\sum_{i=1}^n(X_i-\bar X)(X_i-\bar X)^T,
$$

$$
A_Y=\sum_{j=1}^m(Y_j-\bar Y)(Y_j-\bar Y)^T.
$$

Under the unrestricted model,

$$
\widehat\Sigma_1=A_X/n,
\qquad
\widehat\Sigma_2=A_Y/m.
$$

Under \\(H_0\\), the pooled covariance MLE is

$$
\widehat\Sigma_0
=
\frac{A_X+A_Y}{n+m}.
$$

Hence the covariance-equality likelihood ratio is

$$
\boxed{
\Lambda
=
\frac{
\lvertA_X/n\rvert^{n/2}\lvertA_Y/m\rvert^{m/2}
}{
\lvert(A_X+A_Y)/(n+m)\rvert^{(n+m)/2}
}.
}
$$

Reject for small \\(\Lambda\\), equivalently large

$$
-2\log\Lambda.
$$

This is the likelihood-ratio statistic underlying Box's \\(M\\)-type procedures.

### 12.1 Why simulation can calibrate the test

The 27 October note explicitly asks to use simulation. Under \\(H_0\\), after centering each sample, the distribution of an affine-invariant covariance statistic does not depend on the common mean. By whitening with \\(\Sigma^{-1/2}\\), its null distribution can be generated using

$$
\mu_1=\mu_2=0,
\qquad
\Sigma=I_p.
$$

A parametric simulation algorithm is therefore:

```text
Input: n, m, p, significance alpha, number of simulations B.
For b = 1,...,B:
    1. Generate n iid N_p(0, I_p) observations.
    2. Generate m iid N_p(0, I_p) observations independently.
    3. Form A_X and A_Y.
    4. Compute Lambda_b from the determinant formula.
    5. Store W_b = -2 log Lambda_b.
Use the empirical (1-alpha)-quantile of W_1,...,W_B as the critical value.
Reject the observed data when W_obs exceeds this critical value.
```

This gives a finite-sample Monte Carlo calibration of the LR statistic without relying on a large-sample chi-square approximation.

## 13. Questions answered in this lecture

**Why do LR tests reject for small \\(\Lambda\\)?**

Because \\(\Lambda\\) compares the best null likelihood with the best unrestricted likelihood. A small ratio means the null constraint severely worsens the fit.

**Why do the normal LR tests turn into t-tests?**

The restricted residual sum of squares equals the unrestricted residual sum plus a quadratic mean-contrast term. After dividing by the residual variance, that contrast is exactly \\(t^2\\).

**Why does the multivariate LR test turn into Hotelling \\(T^2\\)?**

The restricted covariance matrix is a rank-one update of the unrestricted residual covariance. The matrix determinant lemma converts the determinant ratio into a quadratic form \\(\bar X^TS^{-1}\bar X\\).

**Why does the union-intersection principle produce the same statistic?**

The strongest projected univariate \\(t\\)-statistic is the Rayleigh quotient whose supremum is the same quadratic form.

**Is “reject for large \\(\lvertX-Y\rvert\\)” exactly the Poisson GLRT?**

It is exact conditional on \\(X+Y\\). Unconditionally, the GLR also depends on the total count.

## 14. Review problems

1. Derive the one-sample normal GLR from the likelihood without using a memorized t-statistic formula.
2. Prove the ANOVA identity
   $$
   A_0=A+\frac{nm}{n+m}(\bar X-\bar Y)^2
   $$
   for the two-sample normal problem.
3. For the Poisson equality problem, show directly that, for fixed \\(s\\), \\(\Lambda(x,s-x)\\) decreases as \\(\lvert2x-s\rvert\\) increases.
4. Prove the matrix determinant lemma for a rank-one update and apply it to the one-sample Hotelling problem.
5. Prove
   $$
   \sup_{\ell\ne0}\frac{(\ell^Tx)^2}{\ell^TS\ell}=x^TS^{-1}x.
   $$
6. Derive the two-sample Hotelling null \\(F\\)-distribution from the standard Wishart result.
7. Implement the covariance-equality simulation algorithm and compare its empirical critical value with a large-sample approximation.

## Lecture summary

The generalized likelihood ratio compares the maximized null likelihood with the unrestricted maximum. In normal models this construction recovers the classical one- and two-sample t-tests and the F-test for variances. Determinant identities extend the same reasoning to Hotelling statistics and covariance-matrix comparisons, while the union–intersection principle supplies an equivalent projection-based interpretation of the multivariate mean test.

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-11-admissibility-equivariance-stein/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }})
</nav>

</div>
