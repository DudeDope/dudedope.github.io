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
description: "Introduces randomized tests, power and size, shows that sufficient-statistic conditioning preserves the power function, and proves the Neyman–Pearson lemma for simple hypotheses."
topics:
  - "hypothesis testing"
  - "randomized tests"
  - "power function"
  - "size and level"
  - "sufficiency in testing"
  - "likelihood ratio"
  - "Neyman–Pearson lemma"
previous: "lecture-06-lehmann-scheffe-umvue-consistency"
next: "lecture-08-bayesian-inference-bayes-risk"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-17"
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
Modern statistical language usually says “reject” or “fail to reject” \\(H_0\\), rather than “accept \\(H_1\\).” The mathematical test function is the same.

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

## 5. Likelihood ratio for simple hypotheses

Consider

$$
H_0:\theta=\theta_0
\qquad\text{versus}\qquad
H_1:\theta=\theta_1,
$$

with densities or mass functions \\(f\_{\theta_0}\\) and \\(f\_{\theta_1}\\) with respect to a common dominating measure.

<div class="definition" markdown="1">

**Definition 7.6 — Likelihood ratio.**
The likelihood ratio in favour of \\(H_1\\) against \\(H_0\\) is

$$
\Lambda(x)
=
\frac{f_{\theta_1}(x)}
{f_{\theta_0}(x)}
$$

whenever the denominator is positive.

</div>

Large values of \\(\Lambda(x)\\) mean that the observed data are relatively more plausible under \\(H_1\\) than under \\(H_0\\).

If

$$
f_\theta(x)=g_\theta(T(x))h(x)
$$

by factorisation, then

$$
\Lambda(x)
=
\frac{g_{\theta_1}(T(x))}
{g_{\theta_0}(T(x))},
$$

so the likelihood ratio is automatically a function of the sufficient statistic.

<div class="remark" markdown="1">

**Editorial note.**
One handwritten page suggests rejecting whenever \\(\Lambda(x)>1\\). That threshold is meaningful for some equal-prior/equal-loss classification problems, but it does **not** in general produce a prescribed frequentist size. In a level-\\(\alpha\\) test the threshold must be chosen so that the null rejection probability is \\(\alpha\\) (or at most \\(\alpha\\)).

</div>

## 6. The Neyman–Pearson lemma

<div class="intuition" markdown="1">

**Additional context.**
The handwritten notes introduce the simple-versus-simple likelihood ratio. The Neyman–Pearson lemma is the precise theorem explaining why thresholding that ratio is optimal.

</div>

<div class="theorem" markdown="1">

**Theorem 7.7 — Neyman–Pearson lemma.**
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

### Worked Example 7.1 — Most powerful test for two normal means

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

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.
- Additional theorem included for completeness: the Neyman–Pearson lemma for simple hypotheses.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-consistency/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-08-bayesian-inference-bayes-risk/' | relative_url }})
</nav>

</div>
