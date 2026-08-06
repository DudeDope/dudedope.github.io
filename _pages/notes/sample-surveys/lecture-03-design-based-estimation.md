---
layout: page
title: "Lecture 3: Design-Based Estimation under Simple Random Sampling"
course: "Sample Surveys"
lecture: 3
instructor: "Ambarish Chattopadhyay"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
slug: "lecture-03-design-based-estimation"
description: "Unbiased estimation, sampling variances, finite-population correction, variance estimation, distinct-unit estimators, totals, and proportions."
math: true
last_updated: "2026-08-06"
status: "published"
author: "Aditya Aryan"
permalink: /notes/sample-surveys/lecture-03-design-based-estimation/
course_slug: sample-surveys
note_kind: lecture
course_order: 3
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Fall 2026 Sample Surveys lectures of Prof. Ambarish Chattopadhyay at the Indian Statistical Institute, Kolkata. The exposition includes additional definitions, derivations, and worked solutions. Any remaining errors belong to the note maintainer, not to the instructor or the Institute.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/sample-surveys/lecture-02-finite-population-and-srs/' | relative_url }}) · [Course contents]({{ '/notes/sample-surveys/' | relative_url }}) · [Next lecture →]({{ '/notes/sample-surveys/lecture-04-confidence-intervals-and-sample-size/' | relative_url }})
</nav>

## Sampling distributions and design unbiasedness

An estimator is a random variable because it changes from one possible sample to another. Its _sampling distribution_ is the distribution induced by the sampling design while the population values remain fixed.

<div class="definition" markdown="1">

**Definition 3.1** (Design bias). For an estimator $\widehat\theta$ of a finite-population parameter $\theta$,

$$
\operatorname{Bias}_p(\widehat\theta)=\mathbb{E}_{p}(\widehat\theta)-\theta.
$$

The estimator is _design unbiased_ if $\operatorname{Bias}_p(\widehat\theta)=0$ for every finite population in the stated class.

</div>

<div class="definition" markdown="1">

**Definition 3.2** (Sampling variance). The design or sampling variance of $\widehat\theta$ is

$$
\operatorname{Var}_{p}(\widehat\theta)
=\mathbb{E}_{p}\left[\left\lbrace\widehat\theta-\mathbb{E}_{p}(\widehat\theta)\right\rbrace^2\right].
$$

It measures sample-to-sample variability under the design.

</div>

## Estimating the population mean under SRSWR

Let $J_1,\ldots,J_n$ be independent uniform labels from $\mathcal{U}$, and let $y_i=Y_{J_i}$. The natural estimator of

$$
\overline{Y}=\frac1N\sum_{j=1}^{N}Y_j
$$

is the sample mean

$$
\overline{y}=\frac1n\sum_{i=1}^{n}y_i.
$$

**Question.**

Why is the sample mean a reasonable estimator under SRSWR?

**Answer.**

Every draw has the finite-population empirical distribution:

$$
\mathbb{P}(y_i=Y_j)=\frac1N,
\qquad j=1,\ldots,N.
$$

Therefore each draw has expectation $\overline{Y}$, and averaging independent draws preserves that expectation while reducing variance. The result follows from the design alone; no superpopulation distribution is assumed.

<div class="theorem" markdown="1">

**Theorem 3.3** (Unbiasedness under SRSWR). Under SRSWR,

$$
\mathbb{E}_{p}(\overline{y})=\overline{Y}.
$$

</div>

_Proof._ For each draw,

$$
\mathbb{E}_{p}(y_i)=\sum_{j=1}^{N}Y_j\mathbb{P}(J_i=j)
=\frac1N\sum_{j=1}^{N}Y_j
=\overline{Y}.
$$

Hence, by linearity,

$$
\mathbb{E}_{p}(\overline{y})
=\frac1n\sum_{i=1}^{n}\mathbb{E}_{p}(y_i)
=\overline{Y}.
$$

◻

The same argument gives, for any known function $h$,

$$
\frac1n\sum_{i=1}^{n}h(y_i)
\quad\text{unbiasedly estimates}\quad
\frac1N\sum_{j=1}^{N}h(Y_j).
$$

This observation will later produce estimators of moments and proportions.

<div class="theorem" markdown="1">

**Theorem 3.4** (Variance under SRSWR). Let

$$
\sigma_Y^2=\frac1N\sum_{j=1}^{N}(Y_j-\overline{Y})^2.
$$

Then

$$
\operatorname{Var}_{p}(\overline{y})=\frac{\sigma_Y^2}{n}.
$$

</div>

_Proof._ For one draw,

$$
\operatorname{Var}_{p}(y_i)
=\frac1N\sum_{j=1}^{N}(Y_j-\overline{Y})^2
=\sigma_Y^2.
$$

The draws are independent, so

$$
\operatorname{Var}_{p}(\overline{y})
=\operatorname{Var}_{p}\left(\frac1n\sum_{i=1}^{n}y_i\right)
=\frac1{n^2}\sum_{i=1}^{n}\operatorname{Var}_{p}(y_i)
=\frac{\sigma_Y^2}{n}.
$$

◻

The variance depends on $N$ only through the finite-population spread $\sigma_Y^2$. Repeated observations do not reveal additional distinct units, but they still enter the iid average.

## Estimating the SRSWR variance

Define the usual sample variance

$$
s^2=\frac1{n-1}\sum_{i=1}^{n}(y_i-\overline{y})^2,
\qquad n\ge2.
$$

**Question.**

Why is $\mathbb{E}_{p}(s^2)=\sigma_Y^2$ under SRSWR?

**Answer.**

Use the decomposition

$$
\sum_{i=1}^{n}(y_i-\overline{y})^2
=\sum_{i=1}^{n}(y_i-\overline{Y})^2-n(\overline{y}-\overline{Y})^2.
$$

Taking design expectation gives

$$
\begin{aligned}
\mathbb{E}_{p}\left[\sum_{i=1}^{n}(y_i-\overline{y})^2\right]
&=n\sigma_Y^2-n\operatorname{Var}_{p}(\overline{y})\\
&=n\sigma_Y^2-n\left(\frac{\sigma_Y^2}{n}\right)\\
&=(n-1)\sigma_Y^2.
\end{aligned}
$$

Dividing by $n-1$ yields $\mathbb{E}_{p}(s^2)=\sigma_Y^2$.

Therefore

$$
\widehat{\operatorname{Var}_{p}}(\overline{y})=\frac{s^2}{n}
$$

is design unbiased for $\operatorname{Var}_{p}(\overline{y})$, and

$$
\widehat{\mathop{\mathrm{SE}}}(\overline{y})=\frac{s}{\sqrt n}
$$

is the standard plug-in standard error. The square root makes $\widehat{\mathop{\mathrm{SE}}}$ generally slightly biased as an estimator of the true standard error, but it is the conventional and consistent measure of uncertainty.

## Estimating the mean under SRSWOR

Let

$$
I_j=\mathbb{I}\lbrace{}j\in S\rbrace,
\qquad j=1,\ldots,N.
$$

For an SRSWOR sample of size $n$,

$$
\sum_{j=1}^{N}I_j=n,
\qquad
\mathbb{E}_{p}(I_j)=\pi_j=\frac nN.
$$

The sample mean can be written as

$$
\overline{y}=\frac1n\sum_{j=1}^{N}I_jY_j.
$$

<div class="theorem" markdown="1">

**Theorem 3.5** (Unbiasedness under SRSWOR). Under SRSWOR,

$$
\mathbb{E}_{p}(\overline{y})=\overline{Y}.
$$

</div>

_Proof._ By linearity and equal inclusion probabilities,

$$
\mathbb{E}_{p}(\overline{y})
=\frac1n\sum_{j=1}^{N}Y_j\mathbb{E}_{p}(I_j)
=\frac1n\sum_{j=1}^{N}Y_j\frac nN
=\overline{Y}.
$$

◻

**Question.**

Why does unbiasedness under SRSWOR not require iid observations?

**Answer.**

The sampled values are dependent because selecting one unit changes the remaining set. Independence is unnecessary: linearity of expectation and the equal inclusion probability $n/N$ are sufficient.

## Variance of the SRSWOR sample mean

Write $d_j=Y_j-\overline{Y}$, so $\sum_jd_j=0$ and

$$
\overline{y}-\overline{Y}=\frac1n\sum_{j=1}^{N}I_jd_j.
$$

For $j\neq k$,

$$
\operatorname{Var}_{p}(I_j)=\pi_j(1-\pi_j),
\qquad
\operatorname{Cov}_{p}(I_j,I_k)=\pi_{jk}-\pi_j\pi_k.
$$

<div class="theorem" markdown="1">

**Theorem 3.6** (SRSWOR variance). Under SRSWOR,

$$
\begin{aligned}
\operatorname{Var}_{p}(\overline{y})
&=\frac{N-n}{N-1}\frac{\sigma_Y^2}{n}\\
&=\left(1-\frac nN\right)\frac{S_Y^2}{n}.
\end{aligned}
$$

If $f=n/N$ is the sampling fraction, then

$$
\operatorname{Var}_{p}(\overline{y})=(1-f)\frac{S_Y^2}{n}.
$$

</div>

_Proof._ Using the centered values,

$$
\begin{aligned}
\operatorname{Var}_{p}(\overline{y})
&=\frac1{n^2}\left[
\sum_{j=1}^{N}d_j^2\operatorname{Var}_{p}(I_j)
+2\sum_{j<k}d_jd_k\operatorname{Cov}_{p}(I_j,I_k)
\right].
\end{aligned}
$$

Because $\sum_jd_j=0$,

$$
2\sum_{j<k}d_jd_k
=\left(\sum_jd_j\right)^2-\sum_jd_j^2
=-\sum_jd_j^2.
$$

Let $\pi=n/N$ and $\pi_2=n(n-1)/\lbrace{}N(N-1)\rbrace$. Then

$$
\begin{aligned}
\operatorname{Var}_{p}(\overline{y})
&=\frac1{n^2}
\left[\pi(1-\pi)-(\pi_2-\pi^2)\right]
\sum_{j=1}^{N}d_j^2\\
&=\frac1{n^2}(\pi-\pi_2)\sum_{j=1}^{N}d_j^2\\
&=\frac1{n^2}
\left\lbrace\frac{n(N-n)}{N(N-1)}\right\rbrace
\sum_{j=1}^{N}d_j^2\\
&=\frac{N-n}{Nn}\,S_Y^2
=\left(1-\frac nN\right)\frac{S_Y^2}{n}.
\end{aligned}
$$

Substituting $S_Y^2=N\sigma_Y^2/(N-1)$ gives the other form. ◻

<div class="definition" markdown="1">

**Definition 3.7** (Finite population correction). The factor

$$
1-f=1-\frac nN
$$

in the variance, or its square root $\sqrt{1-f}$ in the standard error, is the _finite population correction_ (FPC).

</div>

As $n$ approaches $N$, uncertainty vanishes because the sample approaches a census. When $f$ is very small, $1-f\approx1$ and SRSWOR behaves approximately like SRSWR.

## Why the sample variance estimates $S_Y^2$ under SRSWOR

For the selected values, define

$$
s^2=\frac1{n-1}\sum_{j\in S}(Y_j-\overline{y})^2.
$$

<div class="lemma" markdown="1">

**Lemma 3.8** (Pairwise identity). For any numbers $a_1,\ldots,a_m$ with mean $\bar a$,

$$
\sum_{i=1}^{m}(a_i-\bar a)^2
=\frac1m\sum_{i<k}(a_i-a_k)^2.
$$

</div>

_Proof._ Expand the right-hand side:

$$
\begin{aligned}
\sum_{i<k}(a_i-a_k)^2
&=m\sum_{i=1}^{m}a_i^2-\left(\sum_{i=1}^{m}a_i\right)^2\\
&=m\sum_{i=1}^{m}(a_i-\bar a)^2.
\end{aligned}
$$

Divide by $m$. ◻

Hence, for the sample,

$$
s^2=\frac1{n(n-1)}\sum_{j<k}I_jI_k(Y_j-Y_k)^2.
$$

Taking expectations and using $\mathbb{E}_{p}(I_jI_k)=\pi_{jk}$,

$$
\begin{aligned}
\mathbb{E}_{p}(s^2)
&=\frac{\pi_{jk}}{n(n-1)}
\sum_{j<k}(Y_j-Y_k)^2\\
&=\frac1{N(N-1)}
\sum_{j<k}(Y_j-Y_k)^2.
\end{aligned}
$$

The population pairwise identity gives

$$
\sum_{j<k}(Y_j-Y_k)^2
=N\sum_{j=1}^{N}(Y_j-\overline{Y})^2.
$$

Therefore

$$
\mathbb{E}_{p}(s^2)
=\frac1{N-1}\sum_{j=1}^{N}(Y_j-\overline{Y})^2
=S_Y^2.
$$

Thus an unbiased estimator of the sampling variance is

$$
\widehat{\operatorname{Var}_{p}}(\overline{y})
=(1-f)\frac{s^2}{n},
$$

and the estimated standard error is

$$
\widehat{\mathop{\mathrm{SE}}}(\overline{y})
=\sqrt{1-f}\frac{s}{\sqrt n}.
$$

## A complete finite-population example

**Example 3.9** (Enumerating every SRSWOR sample). Let

$$
N=4,\qquad (Y_1,Y_2,Y_3,Y_4)=(2,4,6,8),\qquad n=2.
$$

First compute the population quantities:

$$
\overline{Y}=\frac{2+4+6+8}{4}=5,
$$

$$
\sigma_Y^2
=\frac{(-3)^2+(-1)^2+1^2+3^2}{4}
=5,
$$

$$
S_Y^2=\frac{20}{3}.
$$

There are $\binom42=6$ equally likely samples:

$$
\lbrace1,2\rbrace,\lbrace1,3\rbrace,\lbrace1,4\rbrace,\lbrace2,3\rbrace,\lbrace2,4\rbrace,\lbrace3,4\rbrace.
$$

Their sample means are

$$
3,4,5,5,6,7.
$$

Therefore the exact sampling mean is

$$
\mathbb{E}_{p}(\overline{y})=\frac{3+4+5+5+6+7}{6}=5=\overline{Y}.
$$

The exact sampling variance is

$$
\operatorname{Var}_{p}(\overline{y})
=\frac{(3-5)^2+(4-5)^2+0+0+(6-5)^2+(7-5)^2}{6}
=\frac{10}{6}=\frac53.
$$

The formula gives the same answer:

$$
(1-f)\frac{S_Y^2}{n}
=\left(1-\frac24\right)\frac{20/3}{2}
=\frac53.
$$

For a two-unit sample, $s^2=(a-b)^2/2$. The six sample variances are

$$
2,8,18,2,8,2,
$$

whose mean is

$$
\frac{40}{6}=\frac{20}{3}=S_Y^2.
$$

This verifies both unbiasedness results by complete enumeration.

## SRSWR versus SRSWOR

For the same $N,n$, compare

$$
\operatorname{Var}_{p,\mathrm{WR}}(\overline{y})=\frac{\sigma_Y^2}{n}
$$

with

$$
\operatorname{Var}_{p,\mathrm{WOR}}(\overline{y})
=\frac{N-n}{N-1}\frac{\sigma_Y^2}{n}.
$$

Thus

$$
\frac{\operatorname{Var}_{p,\mathrm{WOR}}(\overline{y})}
{\operatorname{Var}_{p,\mathrm{WR}}(\overline{y})}
=\frac{N-n}{N-1}.
$$

For $n\ge2$ and $n\le N$, this ratio is below one unless the population variance is zero. SRSWOR is more efficient because it avoids duplicate labels and induces negative dependence between inclusion indicators.

**Question.**

Is SRSWR ever used?

**Answer.**

Yes, though direct survey selection with replacement is uncommon.

- When $N$ is enormous and $n/N$ is tiny, the difference from SRSWOR is negligible.
- Sampling with replacement can simplify computation or storage.
- Bootstrap resampling deliberately samples observations with replacement.
- Some unequal-probability multistage designs are formulated with replacement because their variance theory is simple.

For ordinary finite-population unit sampling, SRSWOR usually uses information more efficiently.

## The number of distinct units in SRSWR

Let

$$
K=n_{\mathrm{eff}}=\#\lbrace{}J_1,\ldots,J_n\rbrace
$$

be the number of distinct population units observed in an SRSWR sample. Define

$$
A_j=\mathbb{I}\lbrace\text{unit $j$ appears at least once}\rbrace.
$$

Then $K=\sum_jA_j$ and

$$
\mathbb{E}_{p}(A_j)=1-\left(1-\frac1N\right)^n.
$$

Therefore

<div class="theorem" markdown="1">

**Theorem 3.10** (Expected number of distinct units).

$$
\mathbb{E}_{p}(K)
=N\left[1-\left(1-\frac1N\right)^n\right].
$$

</div>

For $n\ll N$, a binomial expansion gives

$$
\mathbb{E}_{p}(K)
=n-\binom n2\frac1N+O\left(\frac{n^3}{N^2}\right),
$$

so expected duplicate loss is approximately $\binom n2/N$.

The exact distribution is

$$
\mathbb{P}(K=k)
=\frac{(N)_k\,\left\lbrace\begin{matrix}n\\k\end{matrix}\right\rbrace}{N^n},
\qquad
k=1,\ldots,\min(n,N),
$$

where $\left\lbrace\begin{matrix}n\\k\end{matrix}\right\rbrace$ is a Stirling number of the second kind. Choose the $k$ distinct labels, partition the $n$ draw positions into $k$ nonempty groups, and assign the groups to the labels.

## The distinct-units estimator

Let $D=\lbrace{}J_1,\ldots,J_n\rbrace$ be the set of distinct labels and $K=\lvert{}D\rvert$. Define

$$
\overline{y}_{\mathrm{eff}}
=\frac1K\sum_{j\in D}Y_j.
$$

**Question.**

Why is $\mathbb{E}_{p}(\overline{y}_{\mathrm{eff}})=\overline{Y}$?

**Answer.**

Conditional on $K=k$, symmetry implies that $D$ is a uniformly selected $k$-subset of $\mathcal{U}$; that is, $D\mid K=k$ is SRSWOR of size $k$. Therefore

$$
\mathbb{E}_{p}(\overline{y}_{\mathrm{eff}}\mid K=k)=\overline{Y}
$$

for every possible $k$. The law of iterated expectation gives

$$
\mathbb{E}_{p}(\overline{y}_{\mathrm{eff}})=\overline{Y}.
$$

There is a stronger explanation. Conditional on the distinct set $D$, all labels in $D$ are symmetric with respect to their multiplicities. Since the multiplicities sum to $n$, the expected multiplicity of each observed label is $n/K$. Hence

$$
\begin{aligned}
\mathbb{E}_{p}(\overline{y}\mid D)
&=\mathbb{E}_{p}\left(\frac1n\sum_{j\in D}M_jY_j\,\middle|\,D\right)\\
&=\frac1n\sum_{j\in D}\frac nK Y_j\\
&=\overline{y}_{\mathrm{eff}}.
\end{aligned}
$$

Thus $\overline{y}_{\mathrm{eff}}$ is the Rao–Blackwell improvement of the ordinary SRSWR mean based on the distinct-set information.

<div class="theorem" markdown="1">

**Theorem 3.11** (Variance of the distinct-units estimator).

$$
\operatorname{Var}_{p}(\overline{y}_{\mathrm{eff}})
=S_Y^2\left\lbrace\mathbb{E}_{p}\left(\frac1K\right)-\frac1N\right\rbrace.
$$

Moreover,

$$
\operatorname{Var}_{p}(\overline{y}_{\mathrm{eff}})
\le \operatorname{Var}_{p}(\overline{y}).
$$

</div>

_Proof._ Conditional on $K=k$, the distinct set is SRSWOR of size $k$, so

$$
\operatorname{Var}_{p}(\overline{y}_{\mathrm{eff}}\mid K=k)
=\left(1-\frac kN\right)\frac{S_Y^2}{k}
=S_Y^2\left(\frac1k-\frac1N\right).
$$

Its conditional mean is always $\overline{Y}$, so the law of total variance yields the stated formula. The inequality follows from

$$
\overline{y}_{\mathrm{eff}}=\mathbb{E}_{p}(\overline{y}\mid D)
$$

and the variance-reduction property of conditional expectation. ◻

**Question.**

Is the distinct-units estimator better than the ordinary SRSWR mean? How does it compare with SRSWOR of fixed size $n$?

**Answer.**

It is never worse than the ordinary SRSWR mean in variance because it is a Rao–Blackwellization; it is usually strictly better for $n\ge3$ when the population is nonconstant. However, it is generally worse than drawing $n$ distinct units directly by SRSWOR. Since $K\le n$,

$$
\mathbb{E}_{p}\left(\frac1K\right)\ge\frac1n,
$$

so

$$
\operatorname{Var}_{p}(\overline{y}_{\mathrm{eff}})
\ge S_Y^2\left(\frac1n-\frac1N\right)
=\operatorname{Var}_{p,\mathrm{SRSWOR},n}(\overline{y}).
$$

The ranking is therefore

$$
\begin{aligned}
\text{SRSWOR of fixed size $n$}
&\preceq \text{distinct-units SRSWR estimator}\\
&\preceq \text{ordinary SRSWR mean}.
\end{aligned}
$$

where $\preceq$ means “has no larger variance.”

## Other finite-population parameters

### Population total

Since $T_Y=N\overline{Y}$, use

$$
\widehat{T}_Y=N\overline{y}.
$$

It is unbiased under both SRSWR and SRSWOR. Its variance is

$$
\operatorname{Var}_{p}(\widehat{T}_Y)=N^2\operatorname{Var}_{p}(\overline{y}).
$$

Under SRSWOR,

$$
\widehat{\operatorname{Var}_{p}}(\widehat{T}_Y)
=N^2(1-f)\frac{s^2}{n}.
$$

### Population variance

Under SRSWR, $s^2$ is unbiased for $\sigma_Y^2$ because draws follow the empirical population distribution.

Under SRSWOR, $s^2$ is unbiased for $S_Y^2$. Therefore

$$
\widehat{\sigma_Y^2}=\frac{N-1}{N}s^2
$$

is unbiased for the denominator-$N$ variance $\sigma_Y^2$.

### Population covariance

For two fixed variables $X$ and $Y$, define

$$
\begin{aligned}
C_{XY}&=\frac1N\sum_{j=1}^{N}(X_j-\overline{X})(Y_j-\overline{Y}),\\
S_{XY}&=\frac1{N-1}\sum_{j=1}^{N}(X_j-\overline{X})(Y_j-\overline{Y}).
\end{aligned}
$$

They satisfy $S_{XY}=NC_{XY}/(N-1)$. The sample covariance

$$
s_{xy}=\frac1{n-1}\sum_{j\in S}(X_j-\overline{x})(Y_j-\overline{y})
$$

is unbiased for $S_{XY}$ under SRSWOR. One proof applies the sample-variance result to $X+Y$ and $X-Y$ and uses polarization. Consequently,

$$
\frac{N-1}{N}s_{xy}
$$

is unbiased for $C_{XY}$.

## Population proportions as means of indicators

Suppose a characteristic is coded as

$$
Y_j=\begin{cases}
1,&\text{unit $j$ possesses the characteristic},\\
0,&\text{otherwise}.
\end{cases}
$$

Then

$$
P=\frac1N\sum_{j=1}^{N}Y_j=\overline{Y}
$$

is the population proportion. The estimator is

$$
\widehat{P}=\overline{y}
=\frac1n\sum_{j\in S}Y_j
=\frac{\text{number of sampled successes}}{n}.
$$

**Question.**

How are questions about unemployment, digital-payment adoption, moneylender dependence, or medicine stock-outs formalized?

**Answer.**

Define one binary indicator per unit and one precise reference period. For example, $Y_j=1$ if clinic $j$ experienced at least one complete stock-out of the specified antibiotics during the previous three months, and $Y_j=0$ otherwise. The target proportion is the finite-population mean of these indicators. Estimation and inference then reduce to the theory for a population mean.

For binary $Y$,

$$
\sigma_Y^2=P(1-P),
\qquad
S_Y^2=\frac{N}{N-1}P(1-P).
$$

Therefore

$$
\begin{aligned}
\operatorname{Var}_{p,\mathrm{WR}}(\widehat{P})
&=\frac{P(1-P)}{n},\\
\operatorname{Var}_{p,\mathrm{WOR}}(\widehat{P})
&=\frac{N-n}{N-1}\frac{P(1-P)}{n}.
\end{aligned}
$$

For a binary sample,

$$
s^2=\frac{n}{n-1}\widehat{P}(1-\widehat{P}).
$$

Hence the unbiased SRSWOR variance estimator is

$$
\widehat{\operatorname{Var}_{p}}(\widehat{P})
=(1-f)\frac{\widehat{P}(1-\widehat{P})}{n-1}.
$$

## Measures of accuracy

### Standard error

The standard error is

$$
\mathop{\mathrm{SE}}(\widehat\theta)=\sqrt{\operatorname{Var}_{p}(\widehat\theta)}.
$$

Under SRSWOR,

$$
\mathop{\mathrm{SE}}(\overline{y})=\sqrt{1-f}\frac{S_Y}{\sqrt n},
\qquad
\widehat{\mathop{\mathrm{SE}}}(\overline{y})=\sqrt{1-f}\frac{s}{\sqrt n}.
$$

It has the same units as the estimator.

### Coefficient of variation or relative standard deviation

For a nonzero parameter,

$$
\mathop{\mathrm{CV}}(\widehat\theta)
=\frac{\mathop{\mathrm{SE}}(\widehat\theta)}{|\theta|}.
$$

The plug-in estimate is

$$
\widehat{\mathop{\mathrm{CV}}}(\widehat\theta)
=\frac{\widehat{\mathop{\mathrm{SE}}}(\widehat\theta)}{|\widehat\theta|}.
$$

Multiplying by 100 expresses the CV as a percentage.

The slides report the following operational Statistics Canada-style categories:

| Estimated CV                  | Reporting interpretation |
| :---------------------------- | :----------------------- |
| $\le16.6\%$                   | reliable                 |
| $16.6\%<\mathrm{CV}\le33.3\%$ | report with a warning    |
| $>33.3\%$                     | unreliable or suppress   |

These thresholds are agency guidelines, not universal mathematical laws.

> **Caution.**
>
> CV is unstable or meaningless when the true parameter is zero or close to zero, and it is awkward for parameters that can be negative. In such cases, report an absolute standard error, confidence interval, or another scale-appropriate measure.

### Estimation versus inference

**Estimation** produces a point estimate such as $\widehat{P}$. **Inference** additionally quantifies uncertainty or tests claims, for example through a standard error, confidence interval, or hypothesis test. A reported proportion without its design and uncertainty is incomplete statistical evidence.

> **Lecture summary.**
>
> - $\overline{y}$ is design unbiased for $\overline{Y}$ under both SRSWR and SRSWOR.
> - Under SRSWR, $\operatorname{Var}_{p}(\overline{y})=\sigma_Y^2/n$.
> - Under SRSWOR, $\operatorname{Var}_{p}(\overline{y})=(1-f)S_Y^2/n$.
> - Under SRSWOR, $s^2$ is unbiased for $S_Y^2$.
> - SRSWOR is more efficient than SRSWR at the same nominal $n$.
> - The mean across distinct SRSWR units is a Rao–Blackwell improvement, but direct SRSWOR is still at least as efficient.
> - Proportions are means of binary variables, so all mean-estimation formulae apply.

---

## Answers to questions posed in the slides

### 21. How do we draw an SRS?

Use a lottery, a correctly implemented random-number table, or software such as `sample()` in R. The mapping from random digits to labels must preserve uniformity, and replacement must match the intended design.

### 22. Why is $E_p(\overline{y})=\overline{Y}$ under SRSWOR?

Write $\overline{y}=n^{-1}\sum_jI_jY_j$ and use $E_p(I_j)=n/N$:

$$
E_p(\overline{y})=\frac1n\sum_jY_j\frac nN=\overline{Y}.
$$

### 23. What is the sampling variance under SRSWOR?

$$
\operatorname{Var}_{p}(\overline{y})
=\frac{N-n}{N-1}\frac{\sigma_Y^2}{n}
=(1-f)\frac{S_Y^2}{n}.
$$

The proof uses first- and second-order inclusion probabilities and the negative covariance of inclusion indicators.

### 24. How is that variance estimated?

Since $E_p(s^2)=S_Y^2$ under SRSWOR,

$$
\widehat{\operatorname{Var}_{p}}(\overline{y})=(1-f)\frac{s^2}{n}.
$$

### 25. Which design is more efficient for fixed $n$?

For $n\ge2$,

$$
\operatorname{Var}_{p,\mathrm{WOR}}(\overline{y})
=\frac{N-n}{N-1}\operatorname{Var}_{p,\mathrm{WR}}(\overline{y})
<\operatorname{Var}_{p,\mathrm{WR}}(\overline{y})
$$

for a nonconstant population. SRSWOR is more efficient.

### 26. Is SRSWR ever used?

Yes: when $N$ is huge relative to $n$, for computational simplicity, in some unequal-probability designs, and especially in bootstrap resampling. It is uncommon for ordinary direct finite-population surveys.

### 27. What is $E_p(n_{\mathrm{eff}})$?

If $n_{\mathrm{eff}}$ is the number of distinct labels in $n$ SRSWR draws,

$$
E_p(n_{\mathrm{eff}})
=N\left[1-\left(1-\frac1N\right)^n\right].
$$

### 28. Why is the distinct-units mean unbiased?

Conditional on observing $k$ distinct units, their set is an SRSWOR sample of size $k$. Its mean has conditional expectation $\overline{Y}$, so the unconditional expectation is also $\overline{Y}$.

### 29. How are population proportions estimated and inferred?

Code the characteristic as a binary $Y$. Then $P=\overline{Y}$ and $\widehat{P}=\overline{y}$. Report $\widehat{P}$ with a design-appropriate standard error or confidence interval, not as an isolated percentage.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/sample-surveys/lecture-02-finite-population-and-srs/' | relative_url }}) · [Course contents]({{ '/notes/sample-surveys/' | relative_url }}) · [Next lecture →]({{ '/notes/sample-surveys/lecture-04-confidence-intervals-and-sample-size/' | relative_url }})
</nav>

</div>
