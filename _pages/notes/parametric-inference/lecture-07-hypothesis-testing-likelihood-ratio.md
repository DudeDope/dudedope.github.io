---
layout: page
title: "Lecture 7: Hypothesis Testing, Power, Sufficiency, and Likelihood-Ratio Tests"
short_title: "Hypothesis testing"
course: "Parametric Inference"
lecture: 7
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Develops randomized tests, power and size, sufficient-statistic reduction, the Neyman–Pearson lemma, uniformly most powerful one-sided tests, monotone likelihood ratio families, and normal, binomial, exponential-family, and Cauchy examples."
topics:
  - "hypothesis testing"
  - "randomized tests"
  - "power function"
  - "size and level"
  - "sufficiency in testing"
  - "likelihood ratio"
  - "likelihood-ratio sufficiency"
  - "Neyman–Pearson lemma"
  - "uniformly most powerful tests"
  - "monotone likelihood ratio"
  - "Karlin–Rubin principle"
  - "binomial MLR"
  - "exponential-family MLR"
previous: "lecture-06-lehmann-scheffe-umvue-consistency"
next: "lecture-08-bayesian-inference-bayes-risk"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-09-06"
status: "complete"
math: true
permalink: /notes/parametric-inference/lecture-07-hypothesis-testing-likelihood-ratio/
course_slug: parametric-inference
note_kind: lecture
course_order: 7
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Fall 2026 Parametric Inference lectures of Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata. Additional exposition and any remaining errors are the responsibility of the note author.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-consistency/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-08-bayesian-inference-bayes-risk/' | relative_url }})
</nav>

## Learning objectives

After this lecture, you should be able to:

- formulate a testing problem as a partition of the parameter space;
- distinguish a randomized test from a nonrandomized rejection region;
- define the power function, size, level, Type I error, and Type II error;
- show that conditioning a test on a sufficient statistic preserves its entire power function;
- derive the likelihood ratio for a simple-versus-simple problem;
- prove directly that the likelihood ratio is sufficient when the parameter space contains only the two tested values;
- distinguish the raw likelihood-comparison rule \\(\Lambda>1\\) from a prescribed level-\\(\alpha\\) likelihood-ratio test;
- state and prove the Neyman–Pearson lemma;
- derive the most powerful level-\\(\alpha\\) test for two normal means with known variance.

## 1. Testing problems

Let

$$
\mathcal P=\lbrace P_\theta:\theta\in\Theta\rbrace
$$

be a parametric model. A testing problem divides the parameter space into two disjoint parts,

$$
\Theta=\Theta_0\cup\Theta_1,
\qquad
\Theta_0\cap\Theta_1=\varnothing,
$$

and asks us to distinguish

$$
H_0:\theta\in\Theta_0
\qquad\text{from}\qquad
H_1:\theta\in\Theta_1.
$$

\\(H_0\\) is the null hypothesis and \\(H_1\\) is the alternative hypothesis.

<div class="definition" markdown="1">

**Definition 7.1 — Simple and composite hypotheses.**
A hypothesis is _simple_ if it specifies a single distribution, equivalently a single parameter value. It is _composite_ if it contains more than one parameter value.

</div>

For example,

$$
H_0:\theta=\theta_0
\qquad\text{versus}\qquad
H_1:\theta=\theta_1
$$

is simple versus simple, while

$$
H_0:\theta\le\theta_0
\qquad\text{versus}\qquad
H_1:\theta>\theta_0
$$

is composite versus composite.

## 2. Test functions and randomization

<div class="definition" markdown="1">

**Definition 7.2 — Test function.**
A test is a measurable function

$$
\phi:\mathcal X\to[0,1].
$$

After observing \\(X=x\\), the number \\(\phi(x)\\) is interpreted as the conditional probability of rejecting \\(H_0\\).

</div>

Thus:

- \\(\phi(x)=1\\) means reject \\(H_0\\) with certainty;
- \\(\phi(x)=0\\) means do not reject \\(H_0\\);
- \\(0<\phi(x)<1\\) means randomize.

A nonrandomized test has the form

$$
\phi(x)=\mathbf 1_C(x)
$$

for some rejection region \\(C\subseteq\mathcal X\\).

<div class="remark" markdown="1">

**Remark.**
Modern statistical language usually says “reject” or “fail to reject” \\(H_0\\), rather than “accept \\(H_1\\)”. The mathematical test function is the same.

</div>

## 3. Power, size, and error probabilities

<div class="definition" markdown="1">

**Definition 7.3 — Power function.**
The power function of a test \\(\phi\\) is

$$
\beta_\phi(\theta)
=
\operatorname{E}_\theta[\phi(X)].
$$

</div>

For a nonrandomized test,

$$
\beta_\phi(\theta)
=
P_\theta(X\in C),
$$

the probability of rejection when the true parameter is \\(\theta\\).

If \\(\theta\in\Theta_0\\), this is a Type I error probability. If \\(\theta\in\Theta_1\\), then

$$
1-\beta_\phi(\theta)
$$

is the Type II error probability.

<div class="definition" markdown="1">

**Definition 7.4 — Size and level.**
The _size_ of \\(\phi\\) is

$$
\alpha(\phi)
=
\sup_{\theta\in\Theta_0}
\beta_\phi(\theta).
$$

The test is of _level \\(\alpha\\)_ if

$$
\sup_{\theta\in\Theta_0}
\beta_\phi(\theta)
\le\alpha.
$$

</div>

For a simple null \\(H_0:\theta=\theta_0\\),

$$
\alpha(\phi)
=
\operatorname{E}_{\theta_0}[\phi(X)].
$$

<div class="warning" markdown="1">

**Common mistake.**
The size is not the probability that \\(H_0\\) is true. Frequentist testing treats \\(\theta\\) as fixed, not random. The size is a probability computed under distributions belonging to \\(H_0\\).

</div>

## 4. Sufficiency is enough for testing

Suppose \\(T=T(X)\\) is sufficient for \\(\theta\\). The handwritten notes point out that no power is lost by restricting attention to tests that are functions of \\(T\\).

<div class="theorem" markdown="1">

**Theorem 7.5 — Rao–Blackwellisation of a test.**
Let \\(\phi(X)\\) be any test and let \\(T\\) be sufficient. Define

$$
\psi(T)
=
\operatorname{E}[\phi(X)\mid T].
$$

Because \\(T\\) is sufficient, the conditional distribution of \\(X\\) given \\(T\\) is independent of \\(\theta\\), so \\(\psi\\) is a single well-defined function of \\(T\\). Then

$$
\operatorname{E}_\theta[\psi(T)]
=
\operatorname{E}_\theta[\phi(X)]
$$

for every \\(\theta\\).

</div>

**Proof.**

By the tower property,

$$
\begin{aligned}
\operatorname{E}_\theta[\psi(T)]
&=
\operatorname{E}_\theta[
\operatorname{E}_\theta[\phi(X)\mid T]
]\\
&=
\operatorname{E}_\theta[\phi(X)].
\end{aligned}
$$

The role of sufficiency is that the conditional expectation can be represented by the same function \\(\psi(T)\\) for every \\(\theta\\).

\\(\square\\)

Therefore \\(\phi\\) and \\(\psi\\) have **exactly the same power function**:

$$
\boxed{
\beta_\psi(\theta)=\beta_\phi(\theta)
\quad\text{for all }\theta.
}
$$

So, for testing as well as estimation, a sufficient statistic contains everything relevant about \\(\theta\\).

## 5. Likelihood ratios in a two-point testing problem

Consider the special case emphasized in the handwritten notes:

$$
H_0:\theta=\theta_0
\qquad\text{versus}\qquad
H_1:\theta=\theta_1.
$$

Assume that \\(f\_{\theta_0}\\) and \\(f\_{\theta_1}\\) are densities or mass functions with respect to a common dominating measure and that they have a common support. On points where \\(f\_{\theta_0}(x)>0\\), define

<div class="definition" markdown="1">

**Definition 7.6 — Likelihood ratio.**

The likelihood ratio in favour of \\(H_1\\) against \\(H_0\\) is

$$
\Lambda(x)
=
\frac{f_{\theta_1}(x)}{f_{\theta_0}(x)}.
$$

</div>

The ratio compares the relative support that the observed value gives to the two simple models:

$$
\Lambda(x)>1
\iff
f_{\theta_1}(x)>f_{\theta_0}(x),
$$

whereas

$$
\Lambda(x)<1
\iff
f_{\theta_0}(x)>f_{\theta_1}(x).
$$

### 5.1 The likelihood ratio itself is sufficient for the two-point family

A detail written explicitly in the source notes is easy to overlook but important: after restricting the parameter space to

$$
\Theta=\lbrace\theta_0,\theta_1\rbrace,
$$

the likelihood ratio itself is a sufficient statistic.

<div class="proposition" markdown="1">

**Proposition 7.7 — Sufficiency of the likelihood ratio for a two-point model.**

Let

$$
T(x)
=
\frac{f_{\theta_1}(x)}{f_{\theta_0}(x)}.
$$

Then \\(T\\) is sufficient for \\(\theta\\) in the restricted model

$$
\Theta=\lbrace\theta_0,\theta_1\rbrace.
$$

</div>

**Proof.**

Take

$$
h(x)=f_{\theta_0}(x).
$$

Define

$$
g_{\theta_0}(t)=1,
\qquad
g_{\theta_1}(t)=t.
$$

If \\(\theta=\theta_0\\), then

$$
f_{\theta_0}(x)
=
g_{\theta_0}(T(x))h(x).
$$

If \\(\theta=\theta_1\\), then

$$
\begin{aligned}
f_{\theta_1}(x)
&=
\frac{f_{\theta_1}(x)}{f_{\theta_0}(x)}
f_{\theta_0}(x)\\
&=
T(x)h(x)\\
&=
g_{\theta_1}(T(x))h(x).
\end{aligned}
$$

Thus, for both possible parameter values,

$$
f_\theta(x)=g_\theta(T(x))h(x).
$$

By the Neyman–Fisher factorisation criterion, \\(T\\) is sufficient.

\\(\square\\)

This gives a concrete version of the general sufficiency principle from Section 4: for a simple-versus-simple problem, all information in the sample relevant to deciding between the two parameter values can be compressed into the single scalar \\(\Lambda(X)\\).

### 5.2 The source rule \\(\Lambda>1\\): what it does and what it does not do

The handwritten notes suggest the following direct comparison rule. First compute the likelihood ratio

$$
\Lambda(x)
=
\frac{f_{\theta_1}(x)}{f_{\theta_0}(x)}.
$$

Then reject \\(H_0\\) when \\(\Lambda(x)>1\\), and retain \\(H_0\\) when \\(\Lambda(x)<1\\).

If additionally

$$
P_\theta\bigl(\Lambda(X)=1\bigr)=0
$$

for the parameter values under consideration, then ties occur with probability zero and no boundary randomisation is needed for this particular rule.

This rule has a clear interpretation: choose the hypothesis under which the observed data have the larger likelihood. It is therefore a natural _likelihood-comparison rule_.

However, it is not automatically a level-\\(\alpha\\) frequentist test. Its Type I error probability is whatever value

$$
P_{\theta_0}(\Lambda(X)>1)
$$

happens to have. If we require a prescribed level \\(\alpha\\), the threshold must generally be changed from \\(1\\) to a constant \\(k\\) chosen from the null distribution of the likelihood ratio.

> **Key distinction.** The threshold \\(1\\) compares which simple model gives the larger likelihood. The Neyman–Pearson threshold \\(k\\) is chosen to satisfy a frequentist Type I error constraint.

Under equal prior probabilities on \\(\theta_0\\) and \\(\theta_1\\) and equal 0–1 losses, the threshold-1 rule is also the Bayes classification rule. That is a different optimality criterion from fixing a frequentist level.

### 5.3 Relation with an arbitrary sufficient statistic

Suppose more generally that \\(S(X)\\) is sufficient and

$$
f_\theta(x)
=
g_\theta(S(x))h(x).
$$

Then

$$
\Lambda(x)
=
\frac{g_{\theta_1}(S(x))}{g_{\theta_0}(S(x))}.
$$

Hence the likelihood ratio is a function of every sufficient statistic. Combining this observation with Proposition 7.7 gives two complementary facts:

- in the two-point model, \\(\Lambda(X)\\) is itself sufficient;
- if we already know a sufficient statistic \\(S(X)\\), then \\(\Lambda(X)\\) can be computed from \\(S(X)\\) alone.

## 6. The Neyman–Pearson lemma

<div class="intuition" markdown="1">

**Additional context.**
The handwritten notes introduce the simple-versus-simple likelihood ratio. The Neyman–Pearson lemma is the precise theorem explaining why thresholding that ratio is optimal.

</div>

<div class="theorem" markdown="1">

**Theorem 7.8 — Neyman–Pearson lemma.**
For testing

$$
H_0:\theta=\theta_0
\qquad\text{versus}\qquad
H_1:\theta=\theta_1,
$$

suppose there exist \\(k\ge0\\) and \\(0\le\gamma\le1\\) such that

$$
\phi^{\ast}(x)
=
\begin{cases}
1, & \Lambda(x)>k,\\
\gamma, & \Lambda(x)=k,\\
0, & \Lambda(x)<k,
\end{cases}
$$

satisfies

$$
\operatorname{E}_{\theta_0}[\phi^{\ast}(X)]
=
\alpha.
$$

Then \\(\phi^{\ast}\\) is most powerful among all tests of level \\(\alpha\\):

$$
\operatorname{E}_{\theta_1}[\phi(X)]
\le
\operatorname{E}_{\theta_1}[\phi^{\ast}(X)]
$$

for every \\(\phi\\) with

$$
\operatorname{E}_{\theta_0}[\phi(X)]\le\alpha.
$$

</div>

**Proof.**

Write

$$
f_0=f_{\theta_0},
\qquad
f_1=f_{\theta_1},
\qquad
\Lambda=\frac{f_1}{f_0}.
$$

For any competing level-\\(\alpha\\) test \\(\phi\\),

$$
\begin{aligned}
\operatorname{E}_{\theta_1}[\phi^{\ast}-\phi]
&=
\int(\phi^{\ast}-\phi)f_1\,\mathrm d\mu\\
&=
\int(\phi^{\ast}-\phi)\Lambda f_0\,\mathrm d\mu\\
&=
\int(\phi^{\ast}-\phi)(\Lambda-k)f_0\,\mathrm d\mu
+
k\int(\phi^{\ast}-\phi)f_0\,\mathrm d\mu.
\end{aligned}
$$

The second term is nonnegative because

$$
\int\phi^{\ast}f_0\,\mathrm d\mu
=
\alpha
\ge
\int\phi f_0\,\mathrm d\mu.
$$

For the first term, consider the three likelihood-ratio regions:

- if \\(\Lambda>k\\), then \\(\phi^{\ast}=1\\), so \\(\phi^{\ast}-\phi\ge0\\) and \\(\Lambda-k>0\\);
- if \\(\Lambda<k\\), then \\(\phi^{\ast}=0\\), so \\(\phi^{\ast}-\phi=-\phi\le0\\) and \\(\Lambda-k<0\\);
- if \\(\Lambda=k\\), the product is zero.

Thus

$$
(\phi^{\ast}-\phi)(\Lambda-k)\ge0
$$

pointwise. Therefore

$$
\operatorname{E}_{\theta_1}[\phi^{\ast}-\phi]\ge0,
$$

which proves the result.

\\(\square\\)

<div class="intuition" markdown="1">

**Why randomization appears.**
In a discrete model it may be impossible to choose a nonrandomized rejection region whose null probability is exactly \\(\alpha\\). Randomizing on the boundary \\(\lbrace \Lambda=k\rbrace \\) fills the gap.

</div>

## 7. Worked normal example

### Worked Example 7.1 — Likelihood-ratio reduction and the most powerful test for two normal means

**Problem.**

Let

$$
X\sim N(\theta,1),
$$

and test

$$
H_0:\theta=\theta_0
\qquad\text{versus}\qquad
H_1:\theta=\theta_1,
$$

where \\(\theta_1>\theta_0\\). Find the most powerful level-\\(\alpha\\) test.

**Solution.**

Because the restricted parameter space is \\(\lbrace\theta_0,\theta_1\rbrace\\), Proposition 7.7 first tells us that the likelihood ratio itself is sufficient for this two-point model.

The likelihood ratio is

$$
\begin{aligned}
\Lambda(x)
&=
\frac{
\exp\lbrace -(x-\theta_1)^2/2\rbrace }{
\exp\lbrace -(x-\theta_0)^2/2\rbrace }\\
&=
\exp\left\lbrace -\frac12(x-\theta_1)^2
+
\frac12(x-\theta_0)^2
\right\rbrace .
\end{aligned}
$$

Expand:

$$
\begin{aligned}
\log\Lambda(x)
&=
-\frac12(x^2-2x\theta_1+\theta_1^2)
+
\frac12(x^2-2x\theta_0+\theta_0^2)\\
&=
(\theta_1-\theta_0)x
-\frac12(\theta_1^2-\theta_0^2).
\end{aligned}
$$

Since \\(\theta_1-\theta_0>0\\), \\(\Lambda(x)\\) is strictly increasing in \\(x\\). By Neyman–Pearson, the most powerful test rejects for large \\(X\\):

$$
\phi^{\ast}(x)=\mathbf 1_{\lbrace x>c\rbrace }
$$

for a threshold \\(c\\) chosen to have size \\(\alpha\\).

Under \\(H_0\\),

$$
X-\theta_0\sim N(0,1).
$$

Let \\(\Phi\\) denote the standard normal cdf and let

$$
z_q=\Phi^{-1}(q)
$$

denote its \\(q\\)th quantile.
Hence

$$
\alpha
=
P_{\theta_0}(X>c)
=
1-\Phi(c-\theta_0).
$$

Therefore

$$
c-\theta_0=z_{1-\alpha},
$$

so

$$
\boxed{
c=\theta_0+z_{1-\alpha}.
}
$$

The power at \\(\theta_1\\) is

$$
\begin{aligned}
\beta(\theta_1)
&=
P_{\theta_1}(X>c)\\
&=
1-\Phi(c-\theta_1)\\
&=
1-\Phi(
\theta_0+z_{1-\alpha}-\theta_1
).
\end{aligned}
$$

**Final result.**

Reject \\(H_0\\) when

$$
\boxed{
X>\theta_0+z_{1-\alpha}.
}
$$

Its power against \\(\theta_1\\) is

$$
\boxed{
1-\Phi(
\theta_0+z_{1-\alpha}-\theta_1
).
}
$$

**Interpretation.**

When the alternative mean is larger, unusually large observations provide evidence against \\(H_0\\). If \\(\theta_1<\theta_0\\), the likelihood ratio is decreasing in \\(x\\) and the optimal rejection region is in the lower tail.

## 8. Extension to an iid normal sample

<div class="intuition" markdown="1">

**Additional context.**
The one-observation example extends immediately to a sample and illustrates the role of sufficiency.

</div>

If

$$
X_1,\ldots,X_n
\overset{\mathrm{iid}}{\sim}
N(\theta,\sigma^2),
$$

with known \\(\sigma^2\\), then the likelihood ratio between \\(\theta_1\\) and \\(\theta_0\\) depends on the data only through

$$
\sum_{i=1}^nX_i
\quad\text{or equivalently}\quad
\bar X.
$$

When \\(\theta_1>\theta_0\\), the most powerful level-\\(\alpha\\) test rejects when

$$
\boxed{
\bar X
>
\theta_0
+
\frac{\sigma}{\sqrt n}
z_{1-\alpha}.
}
$$

The power at any \\(\theta\\) is

$$
\beta(\theta)
=
1-\Phi\left(
z_{1-\alpha}
-
\frac{\sqrt n(\theta-\theta_0)}{\sigma}
\right).
$$

This is a direct example of the principle that a sufficient statistic is enough for testing.

## 9. From most powerful to uniformly most powerful tests

The 25 August notes make an important observation in the normal example: the critical value chosen from the null distribution does **not** depend on the particular simple alternative \\(\theta_1>\theta_0\\).

For

$$
X\sim N(\theta,1),
$$

consider testing

$$
H_0:\theta=\theta_0
\qquad\text{against}\qquad
H_1:\theta=\theta_1,
$$

where \\(\theta_1>\theta_0\\). Section 7 showed that the Neyman–Pearson most powerful level-\\(\alpha\\) test rejects when

$$
X>c_\alpha,
$$

where

$$
P_{\theta_0}(X>c_\alpha)=\alpha.
$$

Thus

$$
c_\alpha=\theta_0+z_{1-\alpha}.
$$

The striking point is that \\(c\_\alpha\\) contains \\(\theta_0\\) and \\(\alpha\\), but not \\(\theta_1\\). Therefore the **same** rejection region is most powerful against every fixed \\(\theta_1>\theta_0\\).

<div class="definition" markdown="1">

**Definition 7.9 — Uniformly most powerful test.**

A level-\\(\alpha\\) test \\(\phi^{\ast}\\) for

$$
H_0:\theta\in\Theta_0
\qquad\text{versus}\qquad
H_1:\theta\in\Theta_1
$$

is _uniformly most powerful_ (UMP) if, for every other level-\\(\alpha\\) test \\(\phi\\),

$$
\operatorname{E}_\theta[\phi(X)]
\le
\operatorname{E}_\theta[\phi^{\ast}(X)]
\qquad
\text{for every }\theta\in\Theta_1.
$$

</div>

### Worked Example 7.2 — UMP upper-tail test in the normal location family

Consider

$$
H_0:\theta\le\theta_0
\qquad\text{versus}\qquad
H_1:\theta>\theta_0.
$$

Take

$$
\phi^{\ast}(x)
=
\mathbf 1_{\lbrace x>\theta_0+z_{1-\alpha}\rbrace }.
$$

First check the level. Since \\(P\_\theta(X>c)\\) is increasing in \\(\theta\\),

$$
\sup_{\theta\le\theta_0}
P_\theta(X>c_\alpha)
=
P_{\theta_0}(X>c_\alpha)
=
\alpha.
$$

Now fix any \\(\theta_1>\theta_0\\). By the Neyman–Pearson lemma, this same upper-tail test is most powerful of level \\(\alpha\\) for testing \\(\theta_0\\) against \\(\theta_1\\). Since the argument holds for **every** \\(\theta_1>\theta_0\\), the test is UMP for the one-sided composite alternative.

**Final result.**

$$
\boxed{
\text{Reject }H_0
\text{ when }
X>\theta_0+z_{1-\alpha}.
}
$$

For an iid sample from \\(N(\theta,\sigma^2)\\), the corresponding UMP test rejects when

$$
\boxed{
\bar X
>
\theta_0+
\frac{\sigma}{\sqrt n}z_{1-\alpha}.
}
$$

## 10. Monotone likelihood ratio families

The preceding normal argument is not accidental. It is a special case of the monotone likelihood ratio structure introduced in the 25 August notes.

<div class="definition" markdown="1">

**Definition 7.10 — Monotone likelihood ratio in a statistic.**

A one-parameter family \\(\lbrace f\_\theta:\theta\in\Theta\rbrace\\) has a _monotone likelihood ratio_ (MLR) in a statistic \\(T(X)\\) if, whenever \\(\theta_1>\theta_0\\), the ratio

$$
\frac{f_{\theta_1}(x)}{f_{\theta_0}(x)}
$$

is a nondecreasing function of \\(T(x)\\).

If the ratio is nonincreasing instead, one obtains the analogous lower-tail theory after reversing the direction of \\(T\\).

</div>

The definition says that larger values of \\(T\\) systematically favour larger parameter values.

### 10.1 Why MLR leads to one-sided UMP tests

<div class="theorem" markdown="1">

**Theorem 7.11 — One-sided UMP principle for an MLR family.**

Suppose the family has MLR in \\(T(X)\\). Consider

$$
H_0:\theta\le\theta_0
\qquad\text{versus}\qquad
H_1:\theta>\theta_0.
$$

If a threshold \\(c\_\alpha\\), together with boundary randomization if needed, is chosen so that

$$
P_{\theta_0}(T>c_\alpha)
+\gamma P_{\theta_0}(T=c_\alpha)
=
\alpha,
$$

then the resulting upper-tail test is UMP of level \\(\alpha\\), under the standard stochastic-monotonicity consequence of MLR.

</div>

**Reasoning.**

Fix any simple alternative \\(\theta_1>\theta_0\\). Since

$$
\frac{f_{\theta_1}(x)}{f_{\theta_0}(x)}
$$

is nondecreasing in \\(T(x)\\), the Neyman–Pearson rejection region \\(\lbrace f\_{\theta_1}/f\_{\theta_0}>k\rbrace\\) can be written as an upper-tail region in \\(T\\). The size condition is determined under \\(\theta_0\\), so the same threshold is usable for all \\(\theta_1>\theta_0\\). MLR also implies that upper-tail probabilities of \\(T\\) increase with \\(\theta\\), hence the largest Type I error over \\(\theta\le\theta_0\\) occurs at the boundary \\(\theta_0\\). Therefore the same test is most powerful against every \\(\theta_1>\theta_0\\), which is exactly the UMP property.

<div class="remark" markdown="1">

**Remark.**
This result is often presented as the one-parameter Karlin–Rubin theorem. For the exam, the key proof idea is Neyman–Pearson plus monotonicity of the likelihood ratio in a common statistic.

</div>

### Worked Example 7.3 — The binomial family has MLR in \\(X\\)

Let

$$
X\sim\operatorname{Bin}(n,\theta),
\qquad 0<\theta<1.
$$

Take \\(\theta_1>\theta_0\\). The likelihood ratio is

$$
\begin{aligned}
\frac{f_{\theta_1}(x)}{f_{\theta_0}(x)}
&=
\frac{
\binom nx\theta_1^x(1-\theta_1)^{n-x}
}{
\binom nx\theta_0^x(1-\theta_0)^{n-x}
}\\
&=
\left(
\frac{1-\theta_1}{1-\theta_0}
\right)^n
\left[
\frac{\theta_1(1-\theta_0)}
{\theta_0(1-\theta_1)}
\right]^x.
\end{aligned}
$$

Because \\(\theta_1>\theta_0\\),

$$
\frac{\theta_1(1-\theta_0)}
{\theta_0(1-\theta_1)}
>1.
$$

Hence the likelihood ratio is strictly increasing in \\(x\\). Therefore

$$
\boxed{
\operatorname{Bin}(n,\theta)
\text{ has MLR in }X.
}
$$

Consequently, upper-tail tests in \\(X\\) are the natural UMP tests for one-sided alternatives of the form \\(\theta>\theta_0\\).

### 10.2 One-parameter exponential families have MLR under monotone natural parameter

<div class="proposition" markdown="1">

**Proposition 7.12 — Exponential-family MLR criterion.**

Suppose

$$
f_\theta(x)
=
h(x)c(\theta)
\exp\lbrace \eta(\theta)T(x)\rbrace,
$$

where \\(\eta(\theta)\\) is nondecreasing in \\(\theta\\). Then the family has MLR in \\(T(X)\\).

</div>

**Proof.**

For \\(\theta_1>\theta_0\\),

$$
\begin{aligned}
\frac{f_{\theta_1}(x)}{f_{\theta_0}(x)}
&=
\frac{c(\theta_1)}{c(\theta_0)}
\exp\left\lbrace
[\eta(\theta_1)-\eta(\theta_0)]T(x)
\right\rbrace .
\end{aligned}
$$

The prefactor does not depend on \\(x\\). Since

$$
\eta(\theta_1)-\eta(\theta_0)\ge0,
$$

the exponential factor is nondecreasing in \\(T(x)\\). Therefore the likelihood ratio is nondecreasing in \\(T(x)\\).

\\(\square\\)

This result explains at once why many standard one-parameter exponential families—binomial, Poisson, and normal location with known variance—have MLR in their canonical sufficient statistics.

### Worked Example 7.4 — Normal location as an MLR family

For \\(X\sim N(\theta,1)\\),

$$
\frac{f_{\theta_1}(x)}{f_{\theta_0}(x)}
=
\exp\left\lbrace
(\theta_1-\theta_0)x
-
\frac12(\theta_1^2-\theta_0^2)
\right\rbrace .
$$

If \\(\theta_1>\theta_0\\), this is strictly increasing in \\(x\\). Hence the normal location family has MLR in \\(X\\), which is precisely why the upper-tail critical value does not depend on which \\(\theta_1>\theta_0\\) is chosen.

### Worked Example 7.5 — Why the Cauchy location family is not MLR in \\(X\\)

Let

$$
f_\theta(x)
=
\frac{1}{\pi\lbrace 1+(x-\theta)^2\rbrace }.
$$

For \\(\theta_1\ne\theta_0\\),

$$
\frac{f_{\theta_1}(x)}{f_{\theta_0}(x)}
=
\frac{1+(x-\theta_0)^2}
{1+(x-\theta_1)^2}.
$$

As \\(x\to\infty\\),

$$
\frac{f_{\theta_1}(x)}{f_{\theta_0}(x)}
\to1,
$$

and as \\(x\to-\infty\\), the same limit holds:

$$
\frac{f_{\theta_1}(x)}{f_{\theta_0}(x)}
\to1.
$$

But the ratio is not identically equal to \\(1\\) when \\(\theta_1\ne\theta_0\\). A nonconstant monotone function on the whole real line cannot have the same finite limit at both \\(-\infty\\) and \\(+\infty\\). Therefore the ratio is not monotone in \\(x\\).

**Final result.**

$$
\boxed{
\text{The Cauchy location family is not MLR in the observation }X.
}
$$

## Questions answered in this lecture

**Question.**
What does a test function taking values between \\(0\\) and \\(1\\) mean?

**Answer.**

It specifies a randomized decision: after observing \\(x\\), reject \\(H_0\\) with probability \\(\phi(x)\\).

**Question.**
What is the difference between power and size?

**Answer.**

The power function is \\(\beta\_\phi(\theta)=\operatorname{E}\_\theta[\phi(X)]\\) for every parameter value. The size is the largest rejection probability under the null:

$$
\sup_{\theta\in\Theta_0}\beta_\phi(\theta).
$$

**Question.**
Why can we restrict attention to tests based on a sufficient statistic?

**Answer.**

Conditioning any test on the sufficient statistic gives a new test with exactly the same expectation under every \\(\theta\\), hence exactly the same power function.

**Question.**
Why do likelihood-ratio tests reject for large ratios?

**Answer.**

The Neyman–Pearson proof shows that, subject to a fixed Type I error budget, placing rejection probability on outcomes with largest \\(f_1/f_0\\) maximizes power under \\(H_1\\).

**Question.**
Why is the likelihood ratio itself a sufficient statistic in a simple-versus-simple problem?

**Answer.**

With \\(T=f\_{\theta_1}/f\_{\theta_0}\\), take \\(h=f\_{\theta_0}\\), \\(g\_{\theta_0}(t)=1\\), and \\(g\_{\theta_1}(t)=t\\). Then

$$
f_\theta(x)=g_\theta(T(x))h(x)
$$

for both possible values of \\(\theta\\), so factorisation gives sufficiency.

**Question.**
Why do the source notes compare the likelihood ratio with \\(1\\), while the Neyman–Pearson lemma uses a threshold \\(k\\)?

**Answer.**

The threshold \\(1\\) simply chooses the model assigning the larger likelihood to the observation. A frequentist level-\\(\alpha\\) test instead chooses \\(k\\) so that the null rejection probability is \\(\alpha\\), with randomisation on the boundary if necessary. The two thresholds coincide only in special circumstances.

**Question.**
Why does the normal critical value become independent of the particular alternative \\(\theta_1>\theta_0\\)?

**Answer.**

For every \\(\theta_1>\theta_0\\), the likelihood ratio is increasing in \\(X\\), so Neyman–Pearson always gives an upper-tail region. The level condition is imposed under \\(\theta_0\\), hence the threshold is determined only by \\(\theta_0\\) and \\(\alpha\\), not by \\(\theta_1\\). This is what makes the same test UMP for the one-sided alternative.

**Question.**
Does the binomial family have the MLR property?

**Answer.**

Yes. For \\(\theta_1>\theta_0\\), the ratio is a positive constant times

$$
\left[
\frac{\theta_1(1-\theta_0)}
{\theta_0(1-\theta_1)}
\right]^X,
$$

and the bracketed base exceeds \\(1\\), so the ratio increases with \\(X\\).

**Question.**
Why does a one-parameter exponential family often have MLR?

**Answer.**

If

$$
f_\theta(x)=h(x)c(\theta)e^{\eta(\theta)T(x)}
$$

with \\(\eta(\theta)\\) increasing, then for \\(\theta_1>\theta_0\\) the likelihood ratio is a positive constant times

$$
e^{[\eta(\theta_1)-\eta(\theta_0)]T(x)},
$$

which is increasing in \\(T(x)\\).

**Question.**
Why is the Cauchy location family not MLR in \\(X\\)?

**Answer.**

Its likelihood ratio for two different locations is a nonconstant ratio of quadratics that tends to \\(1\\) at both \\(-\infty\\) and \\(+\infty\\). Such a function cannot be monotone on all of \\(\mathbb R\\).

## Lecture summary

The essential objects are

$$
\phi(X)\in[0,1],
\qquad
\beta_\phi(\theta)=\operatorname{E}_\theta[\phi(X)],
\qquad
\alpha(\phi)=\sup_{\Theta_0}\beta_\phi(\theta).
$$

Sufficiency preserves the complete power function. For simple-versus-simple testing, the Neyman–Pearson lemma proves that the most powerful level-\\(\alpha\\) test rejects for large values of

$$
\frac{f_{\theta_1}(X)}{f_{\theta_0}(X)}.
$$

## Review problems

1. For \\(X\sim\operatorname{Bernoulli}(\theta)\\), construct the most powerful level-\\(\alpha\\) randomized test of \\(\theta=\theta_0\\) versus \\(\theta=\theta_1>\theta_0\\).
2. For \\(X_1,\ldots,X_n\sim\operatorname{Poisson}(\theta)\\), show that the simple-versus-simple likelihood ratio is a monotone function of \\(\sum_iX_i\\).
3. Prove directly that Rao–Blackwellising a randomized test with respect to a sufficient statistic preserves both Type I and Type II error probabilities.
4. In the normal example, derive the corresponding lower-tail test when \\(\theta_1<\theta_0\\).
5. Prove directly that the binomial likelihood ratio is increasing in \\(X\\) when \\(\theta_1>\theta_0\\).
6. For a Poisson family, verify MLR in \\(X\\) and derive the form of a UMP upper-tail test.
7. Show that a nonconstant function on \\(\mathbb R\\) with the same finite limits at \\(-\infty\\) and \\(+\infty\\) cannot be monotone, and apply this to the Cauchy likelihood ratio.

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.
- Additional theorem included for completeness: the Neyman–Pearson lemma for simple hypotheses.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-consistency/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-08-bayesian-inference-bayes-risk/' | relative_url }})
</nav>

</div>
