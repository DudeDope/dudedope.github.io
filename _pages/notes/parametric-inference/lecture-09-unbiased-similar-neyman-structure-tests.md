---
layout: page
title: "Lecture 9: Unbiased and Similar Tests, Neyman Structures, and Conditional UMPU Tests"
short_title: "Unbiased and similar tests"
course: "Parametric Inference"
lecture: 9
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Develops unbiased and similar tests, boundary arguments, Neyman structures, conditioning on complete sufficient nuisance statistics, and exact UMP unbiased constructions for Poisson, normal, exponential, two-sample normal, and two-binomial problems."
topics:
  - "unbiased tests"
  - "similar tests"
  - "boundary of the null hypothesis"
  - "Neyman structure"
  - "conditional tests"
  - "nuisance parameters"
  - "UMP unbiased tests"
  - "Poisson conditional binomial test"
  - "normal mean comparison"
  - "exponential mean comparison"
  - "unknown nuisance variance"
  - "Fisher exact conditional test"
previous: "lecture-08-bayesian-inference-bayes-risk"
next: "lecture-10-consistent-asymptotic-tests"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-11-02"
status: "complete"
math: true
permalink: /notes/parametric-inference/lecture-09-unbiased-similar-neyman-structure-tests/
course_slug: parametric-inference
note_kind: lecture
course_order: 9
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based primarily on the 15 September and 29 September 2026 Parametric Inference classes of Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata, with the boundary-conditioning arguments developed fully and with the related nuisance-parameter examples from the 22 September class placed beside the same theory. Additional exposition and any remaining errors are the responsibility of the note author.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-08-bayesian-inference-bayes-risk/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-10-consistent-asymptotic-tests/' | relative_url }})
</nav>

## Learning objectives

After this lecture, you should be able to:

- define an unbiased test and explain why its power must equal the level on a regular boundary between the null and alternative;
- define an \\(\alpha\\)-similar test and a Neyman structure;
- explain why conditioning on a complete sufficient statistic for nuisance parameters is the natural way to enforce similarity;
- derive conditional distributions on the boundary of a composite null;
- combine conditional similarity with monotone likelihood ratio to obtain UMP unbiased tests;
- carry out the full Poisson, normal, exponential, unknown-variance normal, two-sample normal, and two-binomial constructions;
- recognize when randomization is unavoidable in discrete conditional tests.

## 1. Why unbiased tests appear

Consider

$$
H_0:\theta\in\Theta_0
\qquad\text{versus}\qquad
H_1:\theta\in\Theta_1,
$$

and a test function \\(\phi\\), with power

$$
\beta_\phi(\theta)=E_\theta[\phi(X)].
$$

A level-\\(\alpha\\) test satisfies

$$
\sup_{\theta\in\Theta_0}\beta_\phi(\theta)\le \alpha.
$$

For a one-sided problem, a good test should not reject _less often_ under an alternative than it does under the null. This motivates unbiasedness.

<div class="definition" markdown="1">

**Definition 9.1 — Unbiased test.** A level-\\(\alpha\\) test \\(\phi\\) is _unbiased_ if

$$
\beta_\phi(\theta)\ge \alpha
\qquad\text{for every }\theta\in\Theta_1.
$$

Equivalently,

$$
E_\theta[\phi(X)]\le \alpha
\quad(\theta\in\Theta_0),
\qquad
E_\theta[\phi(X)]\ge \alpha
\quad(\theta\in\Theta_1).
$$

</div>

The restriction is particularly important for two-sided alternatives, where a UMP test among _all_ level-\\(\alpha\\) tests often does not exist. Restricting attention to unbiased tests can restore an optimal test.

## 2. The boundary argument

Suppose a scalar parameter problem has

$$
\Theta_0=(a,\theta_0]
\qquad\text{and}\qquad
\Theta_1=(\theta_0,b),
$$

or the analogous closed/open variants, and suppose the power function is continuous at \\(\theta_0\\).

Because \\(\phi\\) is level \\(\alpha\\),

$$
\beta_\phi(\theta_0)\le \alpha.
$$

Because \\(\phi\\) is unbiased, for \\(\theta>\theta_0\\),

$$
\beta_\phi(\theta)\ge \alpha.
$$

Letting \\(\theta\downarrow\theta_0\\) and using continuity gives

$$
\beta_\phi(\theta_0)\ge \alpha.
$$

Hence

$$
\boxed{\beta_\phi(\theta_0)=\alpha.}
$$

<div class="proposition" markdown="1">

**Proposition 9.2 — Exact size on a regular boundary.** If the power function is continuous and a boundary point \\(\theta_0\\) is approached by both null and alternative parameter values, every unbiased level-\\(\alpha\\) test must satisfy

$$
E_{\theta_0}[\phi(X)]=\alpha.
$$

</div>

This equality is the starting point for the conditional constructions below.

## 3. Similarity and Neyman structure

When the boundary itself contains nuisance parameters, one equality at a single point is not enough. Let \\(\Omega\subseteq\Theta_0\\) be the relevant boundary set.

<div class="definition" markdown="1">

**Definition 9.3 — \\(\alpha\\)-similarity on a set.** A test \\(\phi\\) is \\(\alpha\\)-similar on \\(\Omega\\) if

$$
E_\theta[\phi(X)]=\alpha
\qquad\text{for every }\theta\in\Omega.
$$

</div>

Suppose that, under \\(\theta\in\Omega\\), a statistic \\(S\\) is complete and sufficient for the nuisance parameter. A common way to guarantee similarity is to require

$$
\boxed{E_\theta[\phi(X)\mid S]=\alpha\quad\text{a.s. on }\Omega.}
$$

This is called a **Neyman structure**.

Why does it work? By iterated expectation,

$$
E_\theta[\phi(X)]
=
E_\theta\!\left[E_\theta\lbrace\phi(X)\mid S\rbrace\right]
=
E_\theta[\alpha]
=
\alpha.
$$

So conditional level \\(\alpha\\) implies unconditional similarity.

The converse uses completeness.

<div class="theorem" markdown="1">

**Theorem 9.4 — Similarity implies Neyman structure under completeness.** Suppose \\(S\\) is complete sufficient for the nuisance parameter on \\(\Omega\\), and \\(\phi\\) is \\(\alpha\\)-similar on \\(\Omega\\). Then

$$
E_\theta[\phi(X)\mid S]=\alpha
\qquad\text{a.s. for every }\theta\in\Omega.
$$

</div>

**Proof.** Define

$$
h(S)=E_\theta[\phi(X)\mid S]-\alpha.
$$

Sufficiency makes the conditional distribution of the sample given \\(S\\), and therefore the conditional expectation above, independent of the nuisance parameter indexing \\(\Omega\\). Similarity gives

$$
E_\theta[h(S)]
=
E_\theta[\phi(X)]-\alpha
=0
\qquad\forall\theta\in\Omega.
$$

By completeness of \\(S\\),

$$
h(S)=0\quad\text{a.s.}
$$

Hence

$$
E[\phi(X)\mid S]=\alpha\quad\text{a.s.}
$$

as claimed. \\(\square\\)

This theorem explains the method used repeatedly in the handwritten notes: **go to the boundary, condition on a complete sufficient statistic for the nuisance parameter, and solve a one-parameter conditional testing problem.**

## 4. General conditional route to a UMP unbiased test

The standard pattern is:

1. identify the boundary \\(\Omega\\) separating \\(H_0\\) from \\(H_1\\);
2. find a complete sufficient statistic \\(S\\) for the nuisance parameter on \\(\Omega\\);
3. condition on \\(S=s\\);
4. identify a scalar statistic \\(T\\) whose conditional distribution has MLR in the parameter of interest;
5. choose the conditional critical region so that
   $$
   E[\phi\mid S=s]=\alpha;
   $$
6. use conditional Neyman–Pearson/Karlin–Rubin optimality for each fixed \\(s\\);
7. integrate over \\(S\\) to obtain an unconditional UMP unbiased test.

<div class="remark" markdown="1">

**Additional context.** The phrase “UMP unbiased” means uniformly most powerful **within the class of unbiased level-\\(\alpha\\) tests**. The conditioning step is what encodes the unbiasedness/similarity restriction in nuisance-parameter problems.

</div>

## 5. Poisson means: conditioning gives a binomial test

Let

$$
X\sim\operatorname{Poisson}(\lambda),
\qquad
Y\sim\operatorname{Poisson}(\mu),
$$

independently. Consider

$$
H_0:\lambda\le \mu
\qquad\text{versus}\qquad
H_1:\lambda>\mu.
$$

The boundary is

$$
\Omega=\lbrace(\lambda,\mu):\lambda=\mu>0\rbrace.
$$

### 5.1 Conditional distribution

Set

$$
S=X+Y.
$$

A standard calculation gives

$$
S\sim\operatorname{Poisson}(\lambda+\mu),
$$

and, conditional on \\(S=s\\),

$$
\boxed{X\mid S=s\sim\operatorname{Bin}\!\left(s,\frac{\lambda}{\lambda+\mu}\right).}
$$

Indeed,

$$
\begin{aligned}
P(X=x\mid S=s)
&=
\frac{P(X=x,Y=s-x)}{P(S=s)}\\
&=
\frac{e^{-\lambda}\lambda^x/x!\;e^{-\mu}\mu^{s-x}/(s-x)!}
{e^{-(\lambda+\mu)}(\lambda+\mu)^s/s!}\\
&=
\binom{s}{x}
\left(\frac{\lambda}{\lambda+\mu}\right)^x
\left(\frac{\mu}{\lambda+\mu}\right)^{s-x}.
\end{aligned}
$$

On the boundary \\(\lambda=\mu\\),

$$
X\mid S=s\sim\operatorname{Bin}(s,1/2).
$$

Also, on the boundary,

$$
S\sim\operatorname{Poisson}(2\lambda),
$$

and the Poisson family in \\(S\\) is complete. Therefore every unbiased test must have the Neyman structure

$$
E[\phi(X,Y)\mid S]=\alpha.
$$

### 5.2 Conditional MLR

Let

$$
p=\frac{\lambda}{\lambda+\mu}.
$$

Then

$$
\lambda>\mu
\iff
p>\frac12.
$$

For fixed \\(s\\), the binomial family has MLR in \\(X\\). Therefore the most powerful conditional test rejects for large \\(X\\).

For each \\(s\\), choose an integer \\(c_s\\) and, if needed, a randomization probability \\(\gamma_s\in[0,1]\\) so that under \\(p=1/2\\),

$$
P(X>c_s\mid S=s)
+
\gamma_sP(X=c_s\mid S=s)
=
\alpha.
$$

Then

$$
\phi(x,y)=
\begin{cases}
1,&x>c_{x+y},\\
\gamma_{x+y},&x=c_{x+y},\\
0,&x<c_{x+y}
\end{cases}
$$

is the conditional UMP test at every \\(S=s\\), and hence the UMP unbiased test of level \\(\alpha\\).

### 5.3 Equality null

For

$$
H_0:\lambda=\mu
\qquad\text{versus}\qquad
H_1:\lambda>\mu,
$$

the same conditional construction applies. For a two-sided alternative \\(\lambda\ne\mu\\), an unbiased conditional test rejects in both tails of the \\(\operatorname{Bin}(s,1/2)\\) distribution, with tail randomization chosen to give conditional size \\(\alpha\\).

## 6. Two normal observations: mean comparison

Let

$$
X\sim N(\mu,1),
\qquad
Y\sim N(\nu,1),
$$

independently. Test

$$
H_0:\mu\le\nu
\qquad\text{versus}\qquad
H_1:\mu>\nu.
$$

Introduce

$$
U=X+Y,
\qquad
V=X-Y.
$$

Because \\((X,Y)\\) is jointly normal,

$$
U\sim N(\mu+\nu,2),
\qquad
V\sim N(\mu-\nu,2).
$$

Moreover,

$$
\operatorname{Cov}(U,V)
=
\operatorname{Var}(X)-\operatorname{Var}(Y)
=0,
$$

so \\(U\\) and \\(V\\) are independent.

On the boundary \\(\mu=\nu\\), \\(U\\) contains the nuisance mean and is complete sufficient for it, while

$$
V\mid U\sim N(0,2).
$$

The same fact can be written in the exact conditional form used in the handwritten notes. Since \\((X,U)\\) is jointly normal,

$$
X\mid U=u
\sim
N\!\left(
\mu+\frac{1}{2}(u-\mu-\nu),\,
1-\frac{1^2}{2}
\right).
$$

Hence, on the boundary \\(\mu=\nu\\),

$$
\boxed{
X\mid X+Y=u
\sim
N\!\left(\frac u2,\frac12\right).
}
$$

Because \\(V=2X-U\\), this is exactly equivalent to \\(V\mid U\sim N(0,2)\\). The conditional distribution is free of the nuisance common mean, which is the key Neyman-structure step.

Independence means the conditioning is especially simple. To obtain level \\(\alpha\\), choose \\(c\\) from

$$
P_{\mu=\nu}(V>c)=\alpha.
$$

Hence

$$
c=\sqrt2\,z_{1-\alpha}.
$$

Therefore

$$
\boxed{\text{Reject }H_0\text{ iff }X-Y>\sqrt2\,z_{1-\alpha}.}
$$

Since the distribution of \\(V\\) shifts to the right as \\(\mu-\nu\\) increases, the power is increasing in the alternative direction. This is the UMP unbiased level-\\(\alpha\\) test.

## 7. Exponential samples: conditioning on the sum and the scaled-F representation

The handwritten 15/17 September derivation writes the exponential density in **rate** form. We therefore take

$$
X\sim\operatorname{Exp}(\text{rate }\lambda),
\qquad
Y\sim\operatorname{Exp}(\text{rate }\mu),
$$

independently, so that

$$
f(x,y)=\lambda\mu e^{-\lambda x-\mu y},
\qquad x,y>0.
$$

Consider

$$
H_0:\lambda\le\mu
\qquad\text{versus}\qquad
H_1:\lambda>\mu.
$$

The boundary is \\(\lambda=\mu\\). Put

$$
S=X+Y.
$$

For fixed \\(S=s\\), the conditional density of \\(X\\) is

$$
\begin{aligned}
f_{X\mid S}(x\mid s)
&=
\frac{\lambda\mu e^{-\lambda x-\mu(s-x)}}
{\int_0^s\lambda\mu e^{-\lambda u-\mu(s-u)}\,du}\\
&=
\frac{(\lambda-\mu)e^{-(\lambda-\mu)x}}
{1-e^{-(\lambda-\mu)s}},
\qquad 0<x<s,
\end{aligned}
$$

when \\(\lambda\ne\mu\\). If we write

$$
\delta=\lambda-\mu,
$$

then

$$
\boxed{
f_{X\mid S}(x\mid s;\delta)
=
\frac{\delta e^{-\delta x}}{1-e^{-\delta s}},
\qquad 0<x<s.
}
$$

For \\(\delta_1>\delta_0\\),

$$
\frac{f_{\delta_1}(x\mid s)}{f_{\delta_0}(x\mid s)}
=
C(\delta_0,\delta_1,s)e^{-(\delta_1-\delta_0)x},
$$

which is decreasing in \\(x\\). Thus the conditional family has MLR in \\(-X\\), or equivalently it has a monotone likelihood ratio favouring **small** \\(X\\) as \\(\lambda-\mu\\) increases.

### 7.1 Boundary distribution

At \\(\lambda=\mu\\), i.e. \\(\delta=0\\), take the limit

$$
\lim_{\delta\to0}
\frac{\delta e^{-\delta x}}{1-e^{-\delta s}}
=
\frac1s,
$$

because \\(1-e^{-\delta s}\sim\delta s\\). Hence

$$
\boxed{X\mid S=s,\ \lambda=\mu\sim U(0,s).}
$$

Equivalently,

$$
W=\frac{X}{X+Y}\mid S
\sim U(0,1)
$$

on the boundary. The exact conditional level-\\(\alpha\\) test for the upper-rate alternative \\(\lambda>\mu\\) therefore rejects for

$$
\boxed{
\frac{X}{X+Y}<\alpha.
}
$$

Equivalently,

$$
\boxed{
\frac{X}{Y}<\frac{\alpha}{1-\alpha}.
}
$$

This direction is important: with **rate** parameters, larger \\(\lambda\\) makes \\(X\\) stochastically smaller.

### 7.2 Why the source notes call this a scaled F distribution

Since

$$
\lambda X\sim\operatorname{Exp}(1),
\qquad
\mu Y\sim\operatorname{Exp}(1),
$$

independently, and \\(2\lambda X,2\mu Y\\) are independent \\(\chi^2_2\\) variables,

$$
\frac{\lambda X}{\mu Y}\sim F_{2,2}.
$$

Therefore

$$
\boxed{
\frac XY
=\frac{\mu}{\lambda}F_{2,2}.
}
$$

At the boundary \\(\lambda=\mu\\), \\(X/Y\sim F\_{2,2}\\); away from the boundary it is a **scaled \\(F\\)** variable, exactly as indicated in the 15 September notes.

> **Parameterization note.** If instead \\(\lambda,\mu\\) denote exponential **means**, the rates are \\(1/\lambda,1/\mu\\), so all inequality directions reverse. For the mean-parameter problem \\(H_0:\lambda\le\mu\\) versus \\(H_1:\lambda>\mu\\), the corresponding rejection region is
>
> $$
> \frac{X}{X+Y}>1-\alpha
> \quad\Longleftrightarrow\quad
> \frac XY>\frac{1-\alpha}{\alpha}.
> $$
>
> The underlying conditional argument is identical; only the parameterization changes the direction of the tail.

## 8. Testing a normal variance with unknown mean

Let

$$
X_1,\ldots,X_n\overset{\text{iid}}\sim N(\mu,\sigma^2),
$$

with both parameters unknown, and test

$$
H_0:\sigma^2\le\sigma_0^2
\qquad\text{versus}\qquad
H_1:\sigma^2>\sigma_0^2.
$$

The boundary is \\(\sigma^2=\sigma_0^2\\), with nuisance parameter \\(\mu\\).

Under that boundary model, \\(\bar X\\) is complete sufficient for \\(\mu\\). The residual sum of squares

$$
Q=\sum_{i=1}^n(X_i-\bar X)^2
$$

is independent of \\(\bar X\\), and

$$
\frac{Q}{\sigma_0^2}\sim\chi^2_{n-1}.
$$

Hence the Neyman-structure condition can be enforced by a test depending only on \\(Q\\). More explicitly, with \\(\nu=n-1\\),

$$
f_Q(q;\sigma^2)
=
\frac{q^{\nu/2-1}e^{-q/(2\sigma^2)}}
{2^{\nu/2}\Gamma(\nu/2)(\sigma^2)^{\nu/2}},
\qquad q>0.
$$

For \\(\sigma_1^2>\sigma_0^2\\),

$$
\frac{f_Q(q;\sigma_1^2)}{f_Q(q;\sigma_0^2)}
=
C\exp\left\lbrace
\frac q2\left(\frac1{\sigma_0^2}-\frac1{\sigma_1^2}\right)
\right\rbrace,
$$

which is increasing in \\(q\\). Thus the conditional family has MLR in \\(Q\\). This supplies the optimality step, not merely the size calculation. Therefore the UMP unbiased test rejects for large residual sums of squares:

$$
\boxed{
\text{Reject }H_0
\iff
Q>\sigma_0^2\chi^2_{n-1,1-\alpha}.
}
$$

This is the standard one-sided chi-square variance test, now understood as a conditional UMP unbiased construction in the presence of nuisance mean \\(\mu\\).

## 9. Testing a normal mean with unknown variance

Let

$$
X_1,\ldots,X_n\overset{\text{iid}}\sim N(\mu,\sigma^2),
$$

and test

$$
H_0:\mu\le0
\qquad\text{versus}\qquad
H_1:\mu>0,
$$

with \\(\sigma^2\\) unknown.

The joint density can be written

$$
f(\mathbf x;\mu,\sigma^2)
=
(2\pi\sigma^2)^{-n/2}
\exp\!\left
\lbrace
\frac{\mu}{\sigma^2}\sum_i x_i
-
\frac1{2\sigma^2}\sum_i x_i^2
-
\frac{n\mu^2}{2\sigma^2}
\right\rbrace.
$$

Define

$$
T_1=\sum_iX_i,
\qquad
T_2=\sum_iX_i^2,
$$

and natural parameters

$$
\eta_1=\frac{\mu}{\sigma^2},
\qquad
\eta_2=-\frac1{2\sigma^2}.
$$

On the boundary \\(\mu=0\\), \\(T_2\\) is complete sufficient for \\(\sigma^2\\). Conditional on \\(T_2=q\\), the conditional density of \\(T_1=t\\) has the form

$$
f_{T_1\mid T_2}(t\mid q)
\propto
h_q(t)e^{\eta_1 t}.
$$

Therefore it has MLR in \\(T_1\\) as \\(\eta_1\\) increases. Since \\(\eta_1>0\\) is equivalent to \\(\mu>0\\), the conditional UMP test rejects for large \\(T_1\\), with a critical value depending on \\(T_2\\).

By scale invariance the conditional statistic can be written as

$$
\frac{T_1}{\sqrt{T_2}}.
$$

This is a monotone transformation of the usual one-sample \\(t\\)-statistic. Indeed, with

$$
S^2=\frac1{n-1}\sum_i(X_i-\bar X)^2,
$$

we have

$$
t
=
\frac{\sqrt n\,\bar X}{S}
=
\frac{T_1\sqrt{n-1}}{\sqrt{nT_2-T_1^2}},
$$

which is strictly increasing in \\(T_1/\sqrt{T_2}\\) on the positive side.

Hence the conditional UMP unbiased test is exactly the standard one-sided \\(t\\)-test:

$$
\boxed{
\text{Reject }H_0
\iff
\frac{\sqrt n\,\bar X}{S}>t_{n-1,1-\alpha}.
}
$$

## 10. Two normal means with common unknown variance

Let

$$
X_1,\ldots,X_n\overset{\text{iid}}\sim N(\mu_1,\sigma^2),
$$

$$
Y_1,\ldots,Y_m\overset{\text{iid}}\sim N(\mu_2,\sigma^2),
$$

independently, with \\(\mu_1,\mu_2,\sigma^2\\) unknown. Test

$$
H_0:\mu_1\le\mu_2
\qquad\text{versus}\qquad
H_1:\mu_1>\mu_2.
$$

The boundary is \\(\mu_1=\mu_2\\). The class notes explicitly identify the contrast

$$
\delta=\mu_1-\mu_2
$$

and the associated natural parameter

$$
\boxed{\eta=\frac{\mu_1-\mu_2}{\sigma^2}.}
$$

To see the exponential-family structure cleanly, put \\(N=n+m\\) and define the weighted common-location parameter

$$
a=\frac{n\mu_1+m\mu_2}{N}.
$$

Then

$$
\mu_1=a+\frac mN\delta,
\qquad
\mu_2=a-\frac nN\delta.
$$

The joint log-likelihood can be written, up to data-only terms, as

$$
\frac{a}{\sigma^2}U
+
\frac{\delta}{\sigma^2}C
-
\frac1{2\sigma^2}V
-
A(a,\delta,\sigma^2),
$$

where

$$
U=\sum_{i=1}^nX_i+\sum_{j=1}^mY_j,
$$

$$
C=\frac mN\sum_{i=1}^nX_i-\frac nN\sum_{j=1}^mY_j
=\frac{nm}{N}(\bar X-\bar Y),
$$

and

$$
V=\sum_{i=1}^nX_i^2+\sum_{j=1}^mY_j^2.
$$

On the boundary \\(\delta=0\\), the nuisance parameters are \\(a\\) and \\(\sigma^2\\), and

$$
\boxed{(U,V)\text{ is complete sufficient for }(a,\sigma^2)}
$$

because the boundary model is a full two-parameter normal exponential family. Thus every unbiased test must satisfy the Neyman structure after conditioning on \\((U,V)\\).

Conditional on \\((U,V)\\), the density of the contrast statistic \\(C\\) has the form

$$
f_{C\mid U,V}(c\mid u,v;\eta)
\propto
h_{u,v}(c)e^{\eta c}.
$$

Hence it has MLR in \\(C\\) as \\(\eta\\) increases. Since

$$
\eta>0\iff\mu_1>\mu_2,
$$

the conditional MP test rejects for large \\(C\\), equivalently large \\(\bar X-\bar Y\\).

To identify the familiar statistic, let

$$
Q
=
\sum_{i=1}^n(X_i-\bar X)^2
+
\sum_{j=1}^m(Y_j-\bar Y)^2,
$$

and

$$
S_p^2=\frac{Q}{N-2}.
$$

The total centered sum of squares satisfies

$$
V-\frac{U^2}{N}
=
Q+\frac{nm}{N}(\bar X-\bar Y)^2.
$$

Thus, after conditioning on \\((U,V)\\), increasing the positive contrast \\(\bar X-\bar Y\\) is equivalent to increasing

$$
T
=
\frac{\bar X-\bar Y}
{S_p\sqrt{1/n+1/m}}.
$$

Under the boundary \\(\mu_1=\mu_2\\),

$$
\boxed{T\sim t_{N-2}.}
$$

Therefore the exact level-\\(\alpha\\) UMP unbiased test is

$$
\boxed{
\text{Reject }H_0
\iff
T>t_{N-2,1-\alpha}.
}
$$

> **Editorial clarification.** A shorthand boundary statistic written in the class page uses the pooled within-group sum of squares. For sufficiency for both the common mean and the common variance on the boundary, the exact complete sufficient pair is \\((U,V)\\), equivalently the grand mean together with the **total** sum of squares about the grand mean. The pooled within-group quantity \\(Q\\) enters after the contrast decomposition above and produces the usual pooled \\(t\\)-statistic.

## 11. Two binomial proportions: hypergeometric conditioning

Let

$$
X\sim\operatorname{Bin}(n,p_1),
\qquad
Y\sim\operatorname{Bin}(m,p_2),
$$

independently. Test

$$
H_0:p_1\le p_2
\qquad\text{versus}\qquad
H_1:p_1>p_2.
$$

The boundary is \\(p_1=p_2=p\\). Let

$$
S=X+Y.
$$

On the boundary, \\(S\sim\operatorname{Bin}(n+m,p)\\), a complete family in \\(S\\). Conditional on \\(S=s\\),

$$
\boxed{
P(X=x\mid S=s)
=
\frac{\binom nx\binom m{s-x}}{\binom{n+m}s},
}
$$

for feasible \\(x\\). This is the hypergeometric distribution and contains no nuisance parameter \\(p\\).

Away from the boundary, conditional on \\(S=s\\),

$$
P(X=x\mid S=s)
\propto
\binom nx\binom m{s-x}\omega^x,
$$

where

$$
\omega
=
\frac{p_1(1-p_2)}{p_2(1-p_1)}.
$$

Since

$$
p_1>p_2
\iff
\omega>1,
$$

the conditional family has MLR in \\(X\\). Therefore the UMP unbiased test rejects for large \\(X\\), conditional on \\(S=s\\).

For every \\(s\\), choose \\(c_s\\) and \\(\gamma_s\\) such that

$$
P_{H_0}(X>c_s\mid S=s)
+
\gamma_sP_{H_0}(X=c_s\mid S=s)
=
\alpha.
$$

Then the resulting test is UMP unbiased. This is the one-sided conditional test underlying Fisher's exact test.

## 12. Questions answered in this lecture

**Why does an unbiased test have power exactly \\(\alpha\\) on the boundary?**

Because the level condition approaches the boundary from the null side and unbiasedness approaches it from the alternative side. Continuity squeezes the boundary power to \\(\alpha\\).

**Why do we condition on a complete sufficient statistic on the boundary?**

Because it removes the nuisance parameter while completeness forces every similar test to satisfy the conditional size condition. The conditional problem therefore contains exactly the freedom available to unbiased tests.

**Why is randomization needed in Poisson/binomial examples?**

The conditional distributions are discrete. A tail probability will usually jump over \\(\alpha\\), so randomization at one boundary point is required to obtain exact conditional size.

**Why do the normal problems reduce to familiar \\(t\\)- and chi-square tests?**

The conditional Neyman-structure argument removes the nuisance parameters, and the remaining scale-free statistics are monotone transformations of the classical pivots.

## 13. Common mistakes

- Unbiasedness of a test is not the same as unbiasedness of an estimator. For tests it is a statement about the power function.
- Similarity is stronger than merely having size \\(\alpha\\): it requires rejection probability exactly \\(\alpha\\) throughout a specified null subset.
- Conditioning must be done on a statistic sufficient for the nuisance parameter **under the boundary family**.
- In discrete tests, writing “reject for \\(X\ge c\\)” without checking exact size can be wrong; a randomized boundary point may be necessary.
- In the exponential example, the parameterization matters. Here \\(\lambda\\) and \\(\mu\\) are means, so \\(\lambda>\mu\\) corresponds to larger \\(X/Y\\).

## 14. Review problems

1. For independent \\(X\sim\operatorname{Poisson}(\lambda)\\) and \\(Y\sim\operatorname{Poisson}(\mu)\\), derive the two-sided UMP unbiased conditional test of \\(H_0:\lambda=\mu\\) against \\(H_1:\lambda\ne\mu\\).
2. Derive the exact randomization probability \\(\gamma_s\\) in the one-sided Poisson test for a given \\(s\\) and \\(\alpha\\).
3. Starting from the joint normal density, verify directly that conditioning on \\(\sum X_i^2\\) gives a conditional family with MLR in \\(\sum X_i\\).
4. Show algebraically that \\(T_1/\sqrt{T_2}\\) is a strictly increasing function of the usual one-sample \\(t\\)-statistic on the upper-tail rejection region.
5. Derive the hypergeometric conditional distribution for the two-binomial problem from first principles.

## Lecture summary

Unbiasedness constrains power on both sides of a null boundary, while similarity fixes rejection probability on that boundary. Conditioning on a complete sufficient statistic removes nuisance parameters and turns the remaining problem into a one-parameter Neyman–Pearson or MLR construction. This gives exact conditional UMP unbiased tests for the Poisson, exponential, normal, and two-binomial examples developed here.

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-08-bayesian-inference-bayes-risk/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-10-consistent-asymptotic-tests/' | relative_url }})
</nav>

</div>
