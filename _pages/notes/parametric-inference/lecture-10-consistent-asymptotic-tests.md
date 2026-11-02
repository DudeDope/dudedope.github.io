---
layout: page
title: "Lecture 10: Monotone Power, Consistent Tests, and Asymptotic Testing"
short_title: "Consistent and asymptotic tests"
course: "Parametric Inference"
lecture: 10
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Develops monotonicity of power in MLR families, consistency of test sequences, construction of tests from consistent and asymptotically normal estimators, sample-median tests, and MLE consistency and asymptotic normality with location-family examples."
topics:
  - "monotone likelihood ratio"
  - "monotone power"
  - "consistent sequence of tests"
  - "tests from consistent estimators"
  - "asymptotic level"
  - "sample median"
  - "MLE consistency"
  - "MLE asymptotic normality"
  - "Cauchy Fisher information"
previous: "lecture-09-unbiased-similar-neyman-structure-tests"
next: "lecture-11-admissibility-equivariance-stein"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-11-02"
status: "complete"
math: true
permalink: /notes/parametric-inference/lecture-10-consistent-asymptotic-tests/
course_slug: parametric-inference
note_kind: lecture
course_order: 10
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based primarily on the 17 September, 22 September, and 29 September 2026 Parametric Inference classes of Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata. The MLE consistency proof is written in the elementary form used for exam preparation, avoiding KL-divergence terminology. Additional exposition and any remaining errors are the responsibility of the note author.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-09-unbiased-similar-neyman-structure-tests/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-11-admissibility-equivariance-stein/' | relative_url }})
</nav>

## Learning objectives

After this lecture, you should be able to:

- prove that an upper-tail test has nondecreasing power in an MLR family;
- state and verify consistency of a sequence of tests;
- derive consistent tests from consistent estimators and show why the critical radius must shrink to zero;
- obtain asymptotic critical constants from asymptotic normality;
- derive one-sided tests based on the sample median and on an asymptotically normal MLE;
- prove MLE consistency using uniform convergence and the elementary inequality \\(\log x\le x-1\\);
- derive the asymptotic normality of a regular one-dimensional MLE by Taylor expansion of the score;
- compute the Fisher information for the Cauchy location family.

## 1. Monotone likelihood ratio and monotone power

Suppose the family \\(\lbracef\_\theta\rbrace\\) has monotone likelihood ratio in a statistic \\(T(X)\\): for \\(\theta_1>\theta_0\\),

$$
\frac{f_{\theta_1}(x)}{f_{\theta_0}(x)}
$$

is a nondecreasing function of \\(T(x)\\).

Consider an upper-tail test

$$
\phi(X)=\mathbf 1\lbraceT(X)>c\rbrace
$$

with possible randomization at \\(T=c\\).

The lecture notes assert that the power

$$
\beta(\theta)=E_\theta[\phi(X)]
$$

is nondecreasing in \\(\theta\\). Here is a full proof.

<div class="lemma" markdown="1">

**Lemma 10.1 — Covariance of increasing functions.** If \\(U\\) is a real random variable and \\(h_1,h_2\\) are nondecreasing functions for which the expectations exist, then

$$
\operatorname{Cov}(h_1(U),h_2(U))\ge0.
$$

</div>

**Proof.** Let \\(U'\\) be an independent copy of \\(U\\). Then

$$
\begin{aligned}
& E\left[(h_1(U)-h_1(U'))(h_2(U)-h_2(U'))\right]\\
&\qquad =
2E[h_1(U)h_2(U)]-2E[h_1(U)]E[h_2(U)]\\
&\qquad =2\operatorname{Cov}(h_1(U),h_2(U)).
\end{aligned}
$$

Because both functions are nondecreasing,

$$
(h_1(u)-h_1(v))(h_2(u)-h_2(v))\ge0
$$

for every \\(u,v\\). Therefore the expectation is nonnegative and the covariance is nonnegative. \\(\square\\)

Now take \\(\theta_1>\theta_0\\). Write

$$
r(X)=\frac{f_{\theta_1}(X)}{f_{\theta_0}(X)}.
$$

Under \\(P\_{\theta_0}\\),

$$
\begin{aligned}
\beta(\theta_1)-\beta(\theta_0)
&=
E_{\theta_0}[\phi(X)r(X)]-E_{\theta_0}[\phi(X)]\\
&=
E_{\theta_0}[\phi(X)r(X)]
-
E_{\theta_0}[\phi(X)]E_{\theta_0}[r(X)],
\end{aligned}
$$

because

$$
E_{\theta_0}[r(X)]=\int f_{\theta_1}(x)\,dx=1.
$$

Thus

$$
\boxed{
\beta(\theta_1)-\beta(\theta_0)
=
\operatorname{Cov}_{\theta_0}(\phi(X),r(X)).
}
$$

Both \\(\phi\\) and \\(r\\) are nondecreasing functions of \\(T\\), so Lemma 10.1 gives

$$
\boxed{\beta(\theta_1)\ge\beta(\theta_0).}
$$

This supplies the monotonicity statement used in Karlin–Rubin one-sided UMP tests.

## 2. Examples of monotone power

### 2.1 Normal location

If

$$
X\sim N(\theta,1)
$$

and we reject for \\(X>c\\), then

$$
\beta(\theta)
=P_\theta(X>c)
=1-\Phi(c-\theta),
$$

which is increasing in \\(\theta\\).

For the level-\\(\alpha\\) test of

$$
H_0:\theta\le\theta_0
\qquad\text{versus}\qquad
H_1:\theta>\theta_0,
$$

choose

$$
c=\theta_0+z_{1-\alpha}.
$$

Then

$$
\beta(\theta)
=1-\Phi(\theta_0+z_{1-\alpha}-\theta),
$$

and \\(\beta(\theta)\uparrow1\\) as \\(\theta\to\infty\\).

### 2.2 Poisson

If

$$
X\sim\operatorname{Poisson}(\theta)
$$

and the test rejects for \\(X\ge c\\), then

$$
\beta(\theta)=P_\theta(X\ge c)
=1-e^{-\theta}\sum_{x=0}^{c-1}\frac{\theta^x}{x!}.
$$

The handwritten notes explicitly ask to check monotonicity by differentiation. Differentiate the lower-tail expression:

$$
\begin{aligned}
\beta'(\theta)
&=-\frac{d}{d\theta}
\left[e^{-\theta}\sum_{x=0}^{c-1}\frac{\theta^x}{x!}\right]\\
&=e^{-\theta}\sum_{x=0}^{c-1}\frac{\theta^x}{x!}
-e^{-\theta}\sum_{x=1}^{c-1}\frac{\theta^{x-1}}{(x-1)!}\\
&=e^{-\theta}\frac{\theta^{c-1}}{(c-1)!}>0.
\end{aligned}
$$

Thus

$$
\boxed{\beta'(\theta)>0,}
$$

so the power is strictly increasing. This direct computation agrees with the general MLR argument.

## 3. Consistent sequences of tests

<div class="definition" markdown="1">

**Definition 10.2 — Consistent sequence of tests.** Let \\(\phi\_{n}\\) be a sequence of tests for the same testing problem. The sequence is **consistent** if, for every fixed \\(\theta\in\Theta\_{1}\\),

$$
\beta_n(\theta)=E_\theta[\phi_n(X_1,\ldots,X_n)]\longrightarrow1.
$$

Usually the tests are required to have level at most a fixed \\(0<\alpha<1\\) for every \\(n\\).

</div>

Consistency means that every fixed false null is eventually detected with probability approaching one.

## 4. Normal one-sided test is consistent

Let

$$
X_1,\ldots,X_n\overset{\text{iid}}\sim N(\theta,1)
$$

and test

$$
H_0:\theta\le0
\qquad\text{versus}\qquad
H_1:\theta>0.
$$

The UMP level-\\(\alpha\\) test rejects when

$$
\sqrt n\,\bar X>z_{1-\alpha}.
$$

At a fixed alternative \\(\theta>0\\),

$$
\sqrt n\,\bar X\sim N(\sqrt n\,\theta,1).
$$

Therefore

$$
\begin{aligned}
\beta_n(\theta)
&=P_\theta(\sqrt n\,\bar X>z_{1-\alpha})\\
&=1-\Phi(z_{1-\alpha}-\sqrt n\,\theta).
\end{aligned}
$$

Since \\(\sqrt n\theta\to\infty\\),

$$
\boxed{\beta_n(\theta)\to1.}
$$

Hence the sequence is consistent.

## 5. Exponential mean test: exact test and consistency

Let

$$
X_1,\ldots,X_n\overset{\text{iid}}\sim\operatorname{Exp}(\text{mean }\theta),
\qquad \theta>0,
$$

and test

$$
H_0:\theta\le1
\qquad\text{versus}\qquad
H_1:\theta>1.
$$

The family has MLR in

$$
S_n=\sum_{i=1}^nX_i.
$$

Hence the UMP test rejects for large \\(S_n\\). Under \\(\theta=1\\),

$$
S_n\sim\operatorname{Gamma}(n,\text{scale }1),
$$

so choose \\(c\_{n,\alpha}\\) such that

$$
P_{\theta=1}(S_n>c_{n,\alpha})=\alpha.
$$

Equivalently,

$$
2S_n\sim\chi^2_{2n}
$$

under the boundary, and

$$
c_{n,\alpha}=\frac12\chi^2_{2n,1-\alpha}.
$$

To show consistency, divide by \\(n\\). By the law of large numbers,

$$
\frac{S_n}{n}=\bar X\xrightarrow{P}\theta.
$$

Also, under \\(\theta=1\\), the critical value satisfies

$$
\frac{c_{n,\alpha}}n\to1,
$$

which follows, for example, from the CLT quantile approximation

$$
c_{n,\alpha}=n+z_{1-\alpha}\sqrt n+o(\sqrt n).
$$

For fixed \\(\theta>1\\), choose \\(\varepsilon>0\\) with \\(1+\varepsilon<\theta\\). Eventually

$$
\frac{c_{n,\alpha}}n<1+\varepsilon.
$$

Thus

$$
P_\theta(S_n>c_{n,\alpha})
\ge
P_\theta\!\left(\bar X>1+\varepsilon\right)
\to1.
$$

Hence the UMP test sequence is consistent.

## 6. Constructing a consistent test from a consistent estimator

Suppose \\(T_n\\) is consistent for \\(\theta\\):

$$
T_n\xrightarrow{P_\theta}\theta
\qquad\text{for every }\theta.
$$

Consider

$$
H_0:\theta=\theta_0
\qquad\text{versus}\qquad
H_1:\theta\ne\theta_0.
$$

Construct a size-\\(\alpha\\) test that rejects when

$$
\lvertT_n-\theta_0\rvert>c_n,
$$

where \\(c_n\\) is chosen so that

$$
P_{\theta_0}(\lvertT_n-\theta_0\rvert>c_n)=\alpha.
$$

### 6.1 Why the critical radius must vanish

Suppose not. Then for some \\(\varepsilon>0\\) there is a subsequence \\(n_k\\) such that

$$
c_{n_k}\ge\varepsilon.
$$

Hence

$$
\alpha
=P_{\theta_0}(\lvertT_{n_k}-\theta_0\rvert>c_{n_k})
\le
P_{\theta_0}(\lvertT_{n_k}-\theta_0\rvert>\varepsilon).
$$

But consistency at \\(\theta_0\\) makes the right side tend to zero, contradicting \\(\alpha>0\\). Therefore

$$
\boxed{c_n\to0.}
$$

### 6.2 Power at a fixed alternative

Take \\(\theta\ne\theta_0\\). Then

$$
T_n-\theta_0
=
(T_n-\theta)+(\theta-\theta_0)
\xrightarrow{P}
\theta-\theta_0.
$$

Therefore

$$
\lvertT_n-\theta_0\rvert
\xrightarrow{P}
\lvert\theta-\theta_0\rvert>0.
$$

Because \\(c_n\to0\\),

$$
P_\theta(\lvertT_n-\theta_0\rvert>c_n)\to1.
$$

Thus:

<div class="theorem" markdown="1">

**Theorem 10.3 — Consistent estimator gives a consistent two-sided test.** If \\(T_n\\) is consistent for \\(\theta\\) and exact critical radii \\(c_n\\) are chosen to give fixed size \\(\alpha\\), then the test rejecting for \\(\lvertT_n-\theta_0\rvert>c_n\\) is consistent, provided the relevant critical values exist.

</div>

## 7. If the estimator is asymptotically normal

Suppose, more strongly,

$$
\frac{\sqrt n\,(T_n-\theta_0)}{\tau(\theta_0)}
\xrightarrow{d}N(0,1)
$$

under \\(H_0\\), where \\(\tau(\theta_0)>0\\).

A natural asymptotic level-\\(\alpha\\) test rejects when

$$
\left\lvert
\frac{\sqrt n\,(T_n-\theta_0)}{\tau(\theta_0)}
\right\rvert
>
z_{1-\alpha/2}.
$$

Equivalently,

$$
\lvertT_n-\theta_0\rvert
>
\frac{\tau(\theta_0)}{\sqrt n}z_{1-\alpha/2}.
$$

Thus the unscaled critical radius is of order \\(n^{-1/2}\\), and in the scaled statistic the critical constant converges to the standard normal quantile:

$$
\boxed{c_n^{\mathrm{scaled}}\to z_{1-\alpha/2}.}
$$

The continuity of the normal cdf is what allows convergence of the null distribution to translate into convergence of the critical quantile.

## 8. Sample median as an asymptotic test statistic

Suppose

$$
X_1,\ldots,X_n\overset{\text{iid}}\sim F_\theta,
$$

where \\(F\_\theta(x)=F_0(x-\theta)\\) is a continuous location family, \\(F_0(0)=1/2\\), and the density \\(f_0\\) is continuous and positive at zero.

Let \\(M_n\\) be the sample median. Then

$$
\boxed{
\sqrt n(M_n-\theta)
\xrightarrow{d}
N\!\left(0,\frac1{4f_0(0)^2}\right).
}
$$

### 8.1 Why this variance appears

For a population median \\(\theta\\),

$$
F_\theta(\theta)=\frac12.
$$

The empirical cdf at \\(\theta\\) satisfies

$$
\sqrt n\left(F_n(\theta)-\frac12\right)
\xrightarrow{d}
N\left(0,\frac14\right).
$$

Locally,

$$
F_\theta(\theta+h)
=
\frac12+f_0(0)h+o(h).
$$

Inverting this local relation gives

$$
M_n-\theta
\approx
-\frac{F_n(\theta)-1/2}{f_0(0)},
$$

which yields variance

$$
\frac{1/4}{f_0(0)^2}
=
\frac1{4f_0(0)^2}.
$$

### 8.2 A direct proof of the asymptotic median distribution

For completeness, here is a standard proof using only a binomial CLT. Take \\(n=2m+1\\) for simplicity and let

$$
M_n=X_{(m+1)}.
$$

Fix \\(t\in\mathbb R\\) and put

$$
x_n=\theta+\frac{t}{\sqrt n}.
$$

Then

$$
\lbraceM_n\le x_n\rbrace
=
\left\lbrace\sum_{i=1}^n\mathbf 1\lbraceX_i\le x_n\rbrace\ge m+1\right\rbrace.
$$

Let

$$
B_n=\sum_{i=1}^n\mathbf 1\lbraceX_i\le x_n\rbrace.
$$

Then

$$
B_n\sim\operatorname{Bin}(n,p_n),
\qquad
p_n=F_\theta(x_n).
$$

Because \\(F\_\theta(\theta)=1/2\\) and the density is continuous at \\(\theta\\),

$$
\begin{aligned}
p_n
&=F_\theta\left(\theta+\frac{t}{\sqrt n}\right)\\
&=\frac12+f_0(0)\frac{t}{\sqrt n}+o(n^{-1/2}).
\end{aligned}
$$

Now standardize the binomial. Since \\(np_n(1-p_n)\sim n/4\\),

$$
\frac{(m+1)-np_n}{\sqrt{np_n(1-p_n)}}
\longrightarrow
-2f_0(0)t.
$$

Therefore, by the CLT,

$$
\begin{aligned}
P_\theta\lbrace\sqrt n(M_n-\theta)\le t\rbrace
&=P(B_n\ge m+1)\\
&\longrightarrow
1-\Phi\lbrace-2f_0(0)t\rbrace\\
&=\Phi\lbrace2f_0(0)t\rbrace.
\end{aligned}
$$

But \\(\Phi(2f_0(0)t)\\) is the cdf of

$$
N\!\left(0,\frac1{4f_0(0)^2}\right).
$$

Hence

$$
\boxed{
\sqrt n(M_n-\theta)
\xrightarrow{d}
N\!\left(0,\frac1{4f_0(0)^2}\right).
}
$$

For even \\(n\\), any standard definition of the sample median gives the same limit.

### 8.3 One-sided median test

For

$$
H_0:\theta\le0
\qquad\text{versus}\qquad
H_1:\theta>0,
$$

reject for large \\(M_n\\). At the boundary \\(\theta=0\\),

$$
2f_0(0)\sqrt n\,M_n
\xrightarrow{d}N(0,1).
$$

Hence an asymptotic level-\\(\alpha\\) critical value is

$$
\boxed{
C_n
=
\frac{z_{1-\alpha}}{2f_0(0)\sqrt n}.
}
$$

So reject when \\(M_n>C_n\\).

For any fixed \\(\theta>0\\), consistency of the sample median gives \\(M_n\xrightarrow{P}\theta\\), while \\(C_n\to0\\). Therefore the test is consistent.

## 9. MLE-based asymptotic tests in a location model

Suppose

$$
X_1,\ldots,X_n\overset{\text{iid}}\sim f(x-\theta),
$$

where \\(f\\) is known and regular, and test

$$
H_0:\theta\le0
\qquad\text{versus}\qquad
H_1:\theta>0.
$$

If the MLE \\(\widehat\theta_n\\) is regular, then

$$
\sqrt n(\widehat\theta_n-\theta)
\xrightarrow{d}
N\!\left(0,\frac1{I(\theta)}\right).
$$

For a location family, Fisher information is independent of \\(\theta\\); write it simply as \\(I\\). At the boundary \\(\theta=0\\),

$$
\sqrt{nI}\,\widehat\theta_n
\xrightarrow{d}N(0,1).
$$

Hence the asymptotic level-\\(\alpha\\) test rejects when

$$
\boxed{
\widehat\theta_n
>
\frac{z_{1-\alpha}}{\sqrt{nI}}.
}
$$

## 10. Cauchy location: calculate the Fisher information

For the standard Cauchy location family,

$$
f_\theta(x)
=
\frac1{\pi\lbrace1+(x-\theta)^2\rbrace}.
$$

The log-density is

$$
\ell(\theta;x)
=-\log\pi-\log\lbrace1+(x-\theta)^2\rbrace.
$$

Differentiate:

$$
U_\theta(x)
=
\frac{\partial}{\partial\theta}\ell(\theta;x)
=
\frac{2(x-\theta)}{1+(x-\theta)^2}.
$$

Therefore

$$
I(\theta)
=
E_\theta\left[
\frac{4(X-\theta)^2}{\lbrace1+(X-\theta)^2\rbrace^2}
\right].
$$

Let \\(Z=X-\theta\sim\operatorname{Cauchy}(0,1)\\). Then

$$
\begin{aligned}
I
&=
\frac4\pi
\int_{-\infty}^{\infty}
\frac{z^2}{(1+z^2)^3}\,dz.
\end{aligned}
$$

Use

$$
\frac{z^2}{(1+z^2)^3}
=
\frac1{(1+z^2)^2}-\frac1{(1+z^2)^3}.
$$

The standard integrals are

$$
\int_{-\infty}^{\infty}\frac{dz}{(1+z^2)^2}=\frac\pi2,
$$

and

$$
\int_{-\infty}^{\infty}\frac{dz}{(1+z^2)^3}=\frac{3\pi}{8}.
$$

Hence

$$
\int_{-\infty}^{\infty}
\frac{z^2}{(1+z^2)^3}\,dz
=
\frac\pi8,
$$

so

$$
\boxed{I=\frac12.}
$$

Therefore the Cauchy-location MLE, when the regular asymptotic result applies to the selected consistent root, satisfies

$$
\boxed{
\sqrt n(\widehat\theta_n-\theta)
\xrightarrow{d}N(0,2).
}
$$

The one-sided asymptotic critical value at \\(\theta=0\\) is therefore

$$
\widehat\theta_n>
\sqrt{\frac2n}\,z_{1-\alpha}.
$$

## 11. Consistency of the MLE: rigorous exam proof

Let

$$
X_1,\ldots,X_n\overset{\text{iid}}\sim f(x;\theta_0),
$$

where \\(\theta_0\\) is the true parameter. Define

$$
M_n(\theta)
=
\frac1n\sum_{i=1}^n\log f(X_i;\theta).
$$

The MLE maximizes \\(M_n\\).

Assume conditions sufficient for the uniform law of large numbers, so

$$
\boxed{
\sup_{\theta\in\Theta}\lvertM_n(\theta)-M(\theta)\rvert
\xrightarrow{P}0,
}
$$

where

$$
M(\theta)=E_{\theta_0}[\log f(X;\theta)].
$$

Also assume identifiability and that \\(M\\) has the regular continuity/compactness properties needed below.

### 11.1 Show that the limiting objective is uniquely maximized at the true parameter

Use the elementary inequality

$$
\log y\le y-1,
\qquad y>0,
$$

with equality iff \\(y=1\\). Then

$$
\begin{aligned}
M(\theta)-M(\theta_0)
&=
E_{\theta_0}\left[
\log\frac{f(X;\theta)}{f(X;\theta_0)}
\right]\\
&\le
E_{\theta_0}\left[
\frac{f(X;\theta)}{f(X;\theta_0)}-1
\right]\\
&=
\int
\left[
\frac{f(x;\theta)}{f(x;\theta_0)}-1
\right]
f(x;\theta_0)\,dx\\
&=
\int f(x;\theta)\,dx-1\\
&=0.
\end{aligned}
$$

Thus

$$
M(\theta)\le M(\theta_0).
$$

If equality holds, equality in \\(\log y\le y-1\\) forces

$$
f(x;\theta)=f(x;\theta_0)
$$

almost everywhere; identifiability then gives \\(\theta=\theta_0\\). Hence \\(\theta_0\\) is the unique maximizer.

### 11.2 Convert uniform convergence into consistency

Fix \\(\varepsilon>0\\) and let

$$
A_\varepsilon
=
\lbrace\theta:\lvert\theta-\theta_0\rvert\ge\varepsilon\rbrace.
$$

Under compactness/continuity,

$$
\sup_{\theta\in A_\varepsilon}M(\theta)
<
M(\theta_0).
$$

Define the positive separation

$$
\Delta_\varepsilon
=
M(\theta_0)-
\sup_{\theta\in A_\varepsilon}M(\theta)>0.
$$

On the event

$$
\sup_\theta\lvertM_n(\theta)-M(\theta)\rvert<\frac{\Delta_\varepsilon}{3},
$$

we have

$$
M_n(\theta_0)
>
M(\theta_0)-\frac{\Delta_\varepsilon}{3},
$$

while

$$
\sup_{\theta\in A_\varepsilon}M_n(\theta)
<
M(\theta_0)-\frac{2\Delta_\varepsilon}{3}.
$$

Thus no maximizer of \\(M_n\\) can lie in \\(A\_\varepsilon\\). Hence

$$
P_{\theta_0}(\lvert\widehat\theta_n-\theta_0\rvert\ge\varepsilon)
\to0.
$$

Therefore

$$
\boxed{\widehat\theta_n\xrightarrow{P}\theta_0.}
$$

<div class="remark" markdown="1">

**Editorial note.** The statement “a unique solution of the likelihood equation is consistent” is not true without further assumptions. The argument above makes explicit what is actually needed: identifiability and sufficient uniform control of the normalized log-likelihood.

</div>

## 12. Asymptotic normality of the MLE

Let

$$
U_n(\theta)
=
\ell_n'(\theta)
=
\sum_{i=1}^nU_i(\theta)
$$

be the score. For an interior MLE,

$$
U_n(\widehat\theta_n)=0.
$$

Taylor-expand around \\(\theta_0\\):

$$
0
=
U_n(\theta_0)
+
(\widehat\theta_n-\theta_0)
U_n'(\widetilde\theta_n),
$$

where \\(\widetilde\theta_n\\) lies between \\(\widehat\theta_n\\) and \\(\theta_0\\). Therefore

$$
\sqrt n(\widehat\theta_n-\theta_0)
=
-
\frac{U_n(\theta_0)/\sqrt n}
{U_n'(\widetilde\theta_n)/n}.
$$

Under the regular score identities,

$$
E_{\theta_0}[U_i(\theta_0)]=0,
\qquad
\operatorname{Var}_{\theta_0}[U_i(\theta_0)]=I(\theta_0).
$$

Hence the CLT gives

$$
\frac{U_n(\theta_0)}{\sqrt n}
\xrightarrow{d}
N(0,I(\theta_0)).
$$

Consistency gives \\(\widetilde\theta_n\xrightarrow{P}\theta_0\\), and a uniform LLN for the second derivative gives

$$
\frac{U_n'(\widetilde\theta_n)}n
\xrightarrow{P}
E_{\theta_0}[\ell_1''(\theta_0)]
=-I(\theta_0).
$$

By Slutsky's theorem,

$$
\boxed{
\sqrt n(\widehat\theta_n-\theta_0)
\xrightarrow{d}
N\!\left(0,\frac1{I(\theta_0)}\right).
}
$$

This is the standard asymptotic normality theorem used for Wald-type tests and approximate confidence intervals.

## 13. Questions answered in this lecture

**Why is power increasing in an MLR family?**

Because the upper-tail indicator and the likelihood ratio are both increasing functions of the same statistic, making their covariance nonnegative.

**Why must the critical radius of a fixed-size test built from a consistent estimator go to zero?**

Otherwise a positive subsequential lower bound would force the null rejection probability to go to zero, contradicting the fixed size \\(\alpha\\).

**Why does consistency of an estimator imply consistency of the associated two-sided test?**

At an alternative, the estimator converges to a point a positive distance from \\(\theta_0\\), whereas the critical radius shrinks to zero.

**Why is pointwise convergence of the normalized log-likelihood not enough for MLE consistency?**

Because maximizers can move erratically under pointwise convergence. Uniform convergence is what prevents a false maximizer far from \\(\theta_0\\) from overtaking the true neighborhood.

## 14. Review problems

1. Prove consistency of the Poisson upper-tail UMP test of \\(H_0:\theta\le\theta_0\\) against \\(\theta>\theta_0\\).
2. Derive the asymptotic size and power of the sample-median test under local alternatives \\(\theta_n=h/\sqrt n\\).
3. Verify the Cauchy Fisher-information integral by the substitution \\(z=\tan u\\).
4. Starting from the score equation, reproduce the MLE asymptotic-normality proof without skipping the intermediate point \\(\widetilde\theta_n\\).
5. Give an example showing that pointwise convergence of objective functions does not necessarily imply convergence of their maximizers.

## Lecture summary

Monotone likelihood ratios yield monotone power for upper-tail tests. A sequence of tests is consistent when its power tends to one at every fixed alternative, and consistent or asymptotically normal estimators provide general constructions. The sample-median and likelihood examples show how exact finite-sample arguments connect to MLE consistency, Fisher information, and asymptotic normality.

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-09-unbiased-similar-neyman-structure-tests/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-11-admissibility-equivariance-stein/' | relative_url }})
</nav>

</div>
