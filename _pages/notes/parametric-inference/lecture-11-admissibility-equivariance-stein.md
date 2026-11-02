---
layout: page
title: "Lecture 11: Bayesian Testing, Admissibility, Karlin's Criterion, Equivariance, and Stein's Phenomenon"
short_title: "Admissibility and equivariance"
course: "Parametric Inference"
lecture: 11
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Connects Bayesian hypothesis testing with likelihood-ratio rules, develops admissibility and Bayes admissibility, states and applies Karlin's one-parameter exponential-family criterion, extends Rao–Blackwell to vector loss, and explains location equivariance and the James–Stein phenomenon."
topics:
  - "Bayesian hypothesis testing"
  - "0-1 loss"
  - "admissibility"
  - "Bayes rules and admissibility"
  - "Karlin theorem"
  - "exponential-family shrinkage"
  - "vector Rao-Blackwell theorem"
  - "multivariate normal mean"
  - "minimaxity"
  - "James-Stein estimator"
  - "location equivariance"
  - "best equivariant estimator"
previous: "lecture-10-consistent-asymptotic-tests"
next: "lecture-12-likelihood-ratio-classical-multivariate-tests"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-11-02"
status: "complete"
math: true
permalink: /notes/parametric-inference/lecture-11-admissibility-equivariance-stein/
course_slug: parametric-inference
note_kind: lecture
course_order: 11
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Bayesian-testing material from 22 September and the admissibility/equivariance classes of 1 October and 6 October 2026 taught by Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata. Additional derivations are included to make every exercise in the handwritten pages exam-ready.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-10-consistent-asymptotic-tests/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-12-likelihood-ratio-classical-multivariate-tests/' | relative_url }})
</nav>

## Learning objectives

After this lecture, you should be able to:

- derive the Bayes test for two simple hypotheses under 0-1 loss;
- define domination, admissibility, and inadmissibility in terms of risk functions;
- prove that a proper Bayes rule with full-support prior is admissible under continuity of risk;
- state and apply Karlin's admissibility criterion for affine rules in one-parameter exponential families;
- classify the shrinkage estimators appearing in the normal, binomial, Poisson, exponential, and geometric examples;
- extend Rao–Blackwell's risk decomposition to vector parameters under Euclidean squared loss;
- prove minimaxity of the usual multivariate-normal estimator;
- understand why the same estimator becomes inadmissible in dimension at least three;
- define location equivariance and derive the best location-equivariant estimator in the normal model.

## 1. Bayesian testing of two simple hypotheses

Consider

$$
H_0:f=f_0
\qquad\text{versus}\qquad
H_1:f=f_1.
$$

Put prior probabilities

$$
P(H_0)=\pi_0,
\qquad
P(H_1)=\pi_1,
\qquad
\pi_0+\pi_1=1.
$$

Under 0-1 loss, an incorrect decision costs one and a correct decision costs zero.

Let \\(A\\) be the acceptance region for \\(H_0\\). Then the Bayes risk of the decision rule is

$$
\begin{aligned}
r(A)
&=
\pi_0P_0(A^c)+\pi_1P_1(A)\\
&=
\int_{A^c}\pi_0f_0(x)\,dx
+
\int_A\pi_1f_1(x)\,dx.
\end{aligned}
$$

For each observed \\(x\\), the contribution to risk is:

- \\(\pi_1f_1(x)\\) if we put \\(x\in A\\) and accept \\(H_0\\);
- \\(\pi_0f_0(x)\\) if we put \\(x\in A^c\\) and reject \\(H_0\\).

Hence choose the smaller one pointwise. The Bayes acceptance region is

$$
A^{\star}
=
\lbracex:\pi_1f_1(x)\le\pi_0f_0(x)\rbrace.
$$

Equivalently, reject \\(H_0\\) when

$$
\boxed{
\frac{f_1(x)}{f_0(x)}>\frac{\pi_0}{\pi_1}.
}
$$

Using Bayes' theorem,

$$
P(H_1\mid x)
=
\frac{\pi_1f_1(x)}{\pi_0f_0(x)+\pi_1f_1(x)}.
$$

Therefore the same rule is

$$
\boxed{
\text{choose }H_1
\iff
P(H_1\mid x)>\frac12.
}
$$

So the Bayes test is a likelihood-ratio test whose threshold is determined by the prior odds.

## 2. Admissibility

Suppose an estimator \\(\delta\\) has risk

$$
R(\theta,\delta)
=
E_\theta[L(\theta,\delta(X))].
$$

<div class="definition" markdown="1">

**Definition 11.1 — Domination.** An estimator \\(\delta_1\\) dominates \\(\delta_2\\) if

$$
R(\theta,\delta_1)
\le
R(\theta,\delta_2)
\qquad\forall\theta,
$$

with strict inequality for at least one parameter value.

</div>

<div class="definition" markdown="1">

**Definition 11.2 — Admissible estimator.** An estimator is _admissible_ if no other estimator dominates it. Otherwise it is _inadmissible_.

</div>

Admissibility is a pointwise comparison over the **entire risk function**. It is different from minimaxity, which compares only

$$
\sup_\theta R(\theta,\delta).
$$

An estimator can be admissible but not minimax, minimax but inadmissible, both, or neither.

## 3. A fundamental Bayes-admissibility theorem

<div class="theorem" markdown="1">

**Theorem 11.3 — Proper Bayes rule with full-support prior is admissible.** Suppose:

1. \\(\Theta\\) is an open interval (or, more generally, a topological parameter space);
2. \\(\pi\\) is a proper prior assigning positive probability to every nonempty open interval;
3. \\(\delta\_\pi\\) is Bayes under \\(\pi\\);
4. for every estimator under consideration, \\(R(\theta,\delta)\\) is continuous in \\(\theta\\).

Then \\(\delta\_\pi\\) is admissible.

</div>

**Proof.** Suppose, to the contrary, that some \\(\delta_1\\) dominates \\(\delta\_\pi\\). Then

$$
R(\theta,\delta_1)
\le
R(\theta,\delta_\pi)
\qquad\forall\theta,
$$

and at some \\(\theta_0\\),

$$
R(\theta_0,\delta_1)
<
R(\theta_0,\delta_\pi).
$$

Define the continuous difference

$$
D(\theta)
=
R(\theta,\delta_\pi)-R(\theta,\delta_1).
$$

Then \\(D(\theta)\ge0\\) everywhere and \\(D(\theta_0)>0\\). By continuity there is an open interval \\(I\\) around \\(\theta_0\\) and \\(\varepsilon>0\\) such that

$$
D(\theta)>\varepsilon
\qquad\forall\theta\in I.
$$

Because \\(\pi(I)>0\\),

$$
\begin{aligned}
r(\pi,\delta_\pi)-r(\pi,\delta_1)
&=
\int D(\theta)\pi(\theta)\,d\theta\\
&\ge
\int_I D(\theta)\pi(\theta)\,d\theta\\
&>0.
\end{aligned}
$$

Thus \\(\delta_1\\) has smaller Bayes risk than the Bayes rule \\(\delta\_\pi\\), a contradiction. Hence \\(\delta\_\pi\\) is admissible. \\(\square\\)

### 3.1 Exercise: continuity of the risk in a regular exponential family

The handwritten notes ask to verify continuity of the risk. Here is a precise sufficient-condition argument. Suppose

$$
f_\theta(x)=\beta(\theta)e^{\theta T(x)}h(x),
\qquad \theta\in(\underline\theta,\overline\theta),
$$

and let the target be a continuous function \\(g(\theta)\\). Under squared-error loss,

$$
R(\theta,\delta)
=
\int
\lbrace\delta(x)-g(\theta)\rbrace^2
\beta(\theta)e^{\theta T(x)}h(x)\,dx.
$$

Fix an interior point \\(\theta_0\\). Choose \\(\varepsilon>0\\) such that

$$
[\theta_0-\varepsilon,\theta_0+\varepsilon]
\subset(\underline\theta,\overline\theta).
$$

Assume

$$
E_{\theta_0-\varepsilon}[\delta(X)^2]
+
E_{\theta_0+\varepsilon}[\delta(X)^2]
<\infty.
$$

On the compact interval above, \\(\beta(\theta)\\) and \\(g(\theta)\\) are bounded. Also, for every real \\(t\\) and every \\(\theta\\) in this interval,

$$
e^{\theta t}
\le
 e^{(\theta_0-\varepsilon)t}
+e^{(\theta_0+\varepsilon)t}.
$$

Therefore the risk integrand is dominated by an integrable multiple of

$$
(1+\delta(x)^2)
\left[
 e^{(\theta_0-\varepsilon)T(x)}
+e^{(\theta_0+\varepsilon)T(x)}
\right]h(x).
$$

For each fixed \\(x\\), the integrand is continuous in \\(\theta\\). Dominated convergence therefore gives

$$
\boxed{R(\theta,\delta)\to R(\theta_0,\delta)
\quad\text{as }\theta\to\theta_0.}
$$

Thus the risk is continuous under these standard local square-integrability conditions. This is the continuity input used in Theorem 11.3.

## 4. Karlin's theorem for affine shrinkage in a one-parameter exponential family

Consider the natural exponential family

$$
f_\theta(x)
=
\beta(\theta)e^{\theta T(x)}h(x),
\qquad
\underline\theta<\theta<\overline\theta,
$$

and suppose the target is

$$
g(\theta)=E_\theta[T(X)].
$$

Consider affine estimators

$$
\delta_{\lambda,\gamma}(X)
=
\frac{T(X)+\gamma\lambda}{1+\lambda},
\qquad \lambda\ge0.
$$

The class notes use mainly \\(\gamma=0\\):

$$
\delta_\lambda(X)=\frac{T(X)}{1+\lambda}.
$$

<div class="theorem" markdown="1">

**Theorem 11.4 — Karlin's admissibility criterion.** Fix an interior point \\(\theta_0\\). A sufficient condition for \\(\delta\_{\lambda,\gamma}\\) to be admissible under squared-error loss for estimating \\(g(\theta)\\) is that both integrals

$$
\int_{\underline\theta}^{\theta_0}
\frac{e^{-\gamma\lambda\theta}}{\beta(\theta)^\lambda}\,d\theta
$$

and

$$
\int_{\theta_0}^{\overline\theta}
\frac{e^{-\gamma\lambda\theta}}{\beta(\theta)^\lambda}\,d\theta
$$

diverge to infinity.

</div>

The criterion is sufficient, not generally necessary. It is especially useful because admissibility can be reduced to endpoint behavior of two ordinary integrals.

<div class="remark" markdown="1">

**Additional context on the proof.** Karlin's proof is a one-dimensional complete-class/recurrence argument. The displayed integrals are the recurrence integrals for the diffusion associated with the risk-difference equation for affine rules. Divergence at both ends prevents a nonzero improvement from satisfying the boundary conditions required to dominate \\(\delta\_{\lambda,\gamma}\\). The full recurrence proof is substantially beyond the calculations used elsewhere in this course; for exam use, the theorem is applied by checking the two endpoint integrals exactly as in the handwritten notes.

</div>

## 5. Karlin theorem: normal example

Let

$$
X\sim N(\mu,1),
\qquad -\infty<\mu<\infty.
$$

Write

$$
f_\mu(x)
=
\frac1{\sqrt{2\pi}}e^{-x^2/2}
\cdot e^{-\mu^2/2}e^{\mu x}.
$$

Thus

$$
T(X)=X,
\qquad
\beta(\mu)=e^{-\mu^2/2}
$$

(up to a parameter-free constant), and

$$
E_\mu[X]=\mu.
$$

For \\(\gamma=0\\),

$$
\beta(\mu)^{-\lambda}
=e^{\lambda\mu^2/2}.
$$

Both endpoint integrals diverge for every \\(\lambda\ge0\\). Hence

$$
\boxed{\frac{X}{1+\lambda}\text{ is admissible for every }\lambda\ge0.}
$$

For \\(\lambda>0\\), this also follows from Theorem 11.3 because

$$
\frac{X}{1+\lambda}
$$

is the posterior mean under the proper prior

$$
\mu\sim N\left(0,\frac1\lambda\right).
$$

### 5.1 Which of these rules are minimax?

Let

$$
c=\frac1{1+\lambda}.
$$

Then

$$
R(\mu,cX)
=c^2+(1-c)^2\mu^2.
$$

If \\(c<1\\), equivalently \\(\lambda>0\\), then

$$
\sup_\mu R(\mu,cX)=\infty.
$$

For \\(c=1\\),

$$
R(\mu,X)=1
$$

for every \\(\mu\\), and the diffuse-normal-prior lower-bound argument gives minimax risk one. Therefore

$$
\boxed{X\text{ is minimax, whereas }X/(1+\lambda),\ \lambda>0,\text{ is not minimax}.}
$$

## 6. Binomial example

Let

$$
X\sim\operatorname{Bin}(n,p),
\qquad 0<p<1,
$$

and estimate

$$
g(p)=E_p[X]=np.
$$

Use the natural parameter

$$
\eta=\log\frac{p}{1-p}\in\mathbb R.
$$

Then

$$
P_\eta(X=x)
=
\binom nx
(1+e^\eta)^{-n}e^{\eta x}.
$$

Hence

$$
\beta(\eta)=(1+e^\eta)^{-n}.
$$

Karlin's integrand is

$$
\beta(\eta)^{-\lambda}
=(1+e^\eta)^{n\lambda}.
$$

As \\(\eta\to-\infty\\), it tends to one, so the left integral diverges. As \\(\eta\to+\infty\\), it either equals one when \\(\lambda=0\\) or grows exponentially when \\(\lambda>0\\), so the right integral also diverges. Therefore

$$
\boxed{\frac{X}{1+\lambda}\text{ is admissible for all }\lambda\ge0.}
$$

The unshrunk estimator \\(X\\) is not minimax. The exact minimax rule for estimating \\(np\\) under squared error is the scaled version of the symmetric Beta-prior equalizer rule discussed earlier:

$$
\boxed{
\delta^{\star}(X)
=
\frac{n}{n+\sqrt n}
\left(X+\frac{\sqrt n}{2}\right).
}
$$

Thus admissibility does not imply minimaxity. Moreover, none of the pure shrinkage rules \\(X/(1+\lambda)\\) is the global minimax rule: the exact minimax rule above has a strictly positive intercept, whereas \\(X/(1+\lambda)\\) always passes through zero.

## 7. Poisson example

Let

$$
X\sim\operatorname{Poisson}(\mu),
\qquad \mu>0,
$$

and estimate \\(E[X]=\mu\\). Put

$$
\eta=\log\mu\in\mathbb R.
$$

Then

$$
P_\eta(X=x)
=
\frac1{x!}e^{-e^\eta}e^{\eta x},
$$

so

$$
\beta(\eta)=e^{-e^\eta}.
$$

Thus

$$
\beta(\eta)^{-\lambda}=e^{\lambda e^\eta}.
$$

At \\(-\infty\\) this tends to one, giving an infinite left integral; at \\(+\infty\\) it diverges rapidly, giving an infinite right integral. Hence

$$
\boxed{X/(1+\lambda)\text{ is admissible for every }\lambda\ge0.}
$$

Under ordinary squared-error loss on \\((0,\infty)\\), every estimator has infinite maximum risk, as proved in the earlier minimax discussion by Gamma-prior Bayes-risk lower bounds. Consequently the ordinary minimax criterion is degenerate here.

## 8. Exponential example: Karlin singles out the half-sample estimator

Let

$$
X\sim\operatorname{Exp}(\text{rate }\mu),
\qquad f_\mu(x)=\mu e^{-\mu x},
\qquad \mu>0,
$$

and estimate

$$
g(\mu)=E_\mu[X]=\frac1\mu.
$$

Take the natural parameter

$$
\theta=-\mu\in(-\infty,0).
$$

Then

$$
f_\theta(x)=(-\theta)e^{\theta x},
$$

so

$$
\beta(\theta)=-\theta.
$$

Karlin's integrand for \\(\gamma=0\\) is

$$
(-\theta)^{-\lambda}.
$$

At \\(-\infty\\),

$$
\int^\infty u^{-\lambda}\,du
$$

diverges iff \\(\lambda\le1\\). Near zero,

$$
\int_0 u^{-\lambda}\,du
$$

diverges iff \\(\lambda\ge1\\). Both diverge exactly when

$$
\lambda=1.
$$

Therefore Karlin's theorem proves

$$
\boxed{X/2\text{ is admissible for estimating }1/\mu.}
$$

Now check the entire class \\(cX\\). Since

$$
E[X]=\frac1\mu,
\qquad
\operatorname{Var}(X)=\frac1{\mu^2},
$$

we have

$$
R\left(\mu,cX\right)
=
\frac{c^2+(c-1)^2}{\mu^2}.
$$

The coefficient

$$
c^2+(c-1)^2
=2\left(c-\frac12\right)^2+\frac12
$$

is uniquely minimized at \\(c=1/2\\). Hence

$$
\boxed{X/2\text{ strictly dominates every }cX\text{ with }c\ne1/2.}
$$

In particular, the usual unbiased estimator \\(X\\) is inadmissible.

## 9. Geometric example from the 6 October notes

Let

$$
P_p(X=x)=p(1-p)^x,
\qquad x=0,1,2,\ldots,
\qquad 0<p<1.
$$

Then

$$
E_p[X]=\frac{1-p}{p}=:m.
$$

Put

$$
\theta=\log(1-p)\in(-\infty,0),
\qquad p=1-e^\theta.
$$

Then

$$
P_\theta(X=x)
=(1-e^\theta)e^{\theta x},
$$

so

$$
\beta(\theta)=1-e^\theta.
$$

For \\(\delta\_\lambda=X/(1+\lambda)\\), Karlin's integrand is

$$
(1-e^\theta)^{-\lambda}.
$$

As \\(\theta\to-\infty\\), the integrand tends to one, so the left integral always diverges. As \\(\theta\uparrow0\\),

$$
1-e^\theta\sim-\theta,
$$

so the right integral behaves like

$$
\int_0 u^{-\lambda}\,du,
$$

which diverges iff \\(\lambda\ge1\\). Hence

$$
\boxed{X/(1+\lambda)\text{ is admissible for }\lambda\ge1.}
$$

What about \\(0\le\lambda<1\\), where Karlin's theorem is inconclusive? Let \\(c=1/(1+\lambda)>1/2\\). Since

$$
\operatorname{Var}(X)=m(m+1),
$$

we get

$$
R(cX,m)
=c^2m(m+1)+(c-1)^2m^2.
$$

For \\(c=1/2\\),

$$
R\left(\frac X2,m\right)
=
\frac14m+\frac12m^2.
$$

For any \\(c>1/2\\), both

$$
c^2>\frac14
$$

and

$$
c^2+(c-1)^2>\frac12.
$$

Therefore

$$
R(cX,m)>R(X/2,m)
\qquad\forall m>0.
$$

Thus

$$
\boxed{X/(1+\lambda)\text{ is inadmissible for }0\le\lambda<1.}
$$

Combining both arguments gives the complete classification within the class:

$$
\boxed{
X/(1+\lambda)\text{ is admissible iff }\lambda\ge1.
}
$$

### 9.1 Can there be a finite-risk minimax estimator for the geometric mean?

The answer under ordinary squared-error loss is no: the minimax value is infinite. A useful two-point argument makes this precise. Write the mean as

$$
m(p)=\frac{1-p}{p}.
$$

Take

$$
p_M=\frac1M,
\qquad
q_M=\frac1{2M}.
$$

Then

$$
\lvertm(p_M)-m(q_M)\rvert=M.
$$

For any estimator \\(\delta\\), we first derive the two-point squared-loss bound. Let \\(m_1=m(p_M)\\), \\(m_2=m(q_M)\\), and \\(\Delta=\lvertm_1-m_2\rvert=M\\). Define

$$
A=\left\lbrace\lvert\delta-m_1\rvert<\frac{\Delta}{2}\right\rbrace.
$$

On \\(A^c\\), the squared error under the first parameter is at least \\(\Delta^2/4\\); on \\(A\\), the triangle inequality gives \\(\lvert\delta-m_2\rvert\ge\Delta/2\\), so the squared error under the second parameter is at least \\(\Delta^2/4\\). Hence

$$
R(p_M,\delta)+R(q_M,\delta)
\ge
\frac{\Delta^2}{4}
\lbraceP_{p_M}(A^c)+P_{q_M}(A)\rbrace.
$$

But

$$
P_{p_M}(A^c)+P_{q_M}(A)
=
1-\lbraceP_{p_M}(A)-P_{q_M}(A)\rbrace
\ge
1-\operatorname{TV}(P_{p_M},P_{q_M}).
$$

Therefore

$$
\boxed{
\max\lbraceR(p_M,\delta),R(q_M,\delta)\rbrace
\ge
\frac{M^2}{8}
\lbrace1-\operatorname{TV}(P_{p_M},P_{q_M})\rbrace.
}
$$

The Hellinger affinity of two geometric laws is

$$
\rho(p,q)
=
\sum_{x=0}^{\infty}
\sqrt{pq}
\lbrace(1-p)(1-q)\rbrace^{x/2}
=
\frac{\sqrt{pq}}{1-\sqrt{(1-p)(1-q)}}.
$$

For the choices above,

$$
\rho(p_M,q_M)\longrightarrow \frac{4}{3\sqrt2}.
$$

Since

$$
\operatorname{TV}(P,Q)
\le
\sqrt{1-\rho(P,Q)^2},
$$

the total variation distance stays bounded strictly below one. Hence the lower bound is a positive constant times \\(M^2\\), which tends to infinity. Therefore

$$
\boxed{
\inf_\delta\sup_{0<p<1}R(p,\delta)=\infty.
}
$$

So, as in the Poisson and unbounded-scale examples, ordinary squared-error minimaxity is degenerate.

## 10. Rao–Blackwell for vector parameters

Suppose now

$$
\theta\in\mathbb R^k,
$$

and estimate \\(\theta\\) under Euclidean squared loss

$$
L(\theta,T)=\lVertT-\theta\rVert^2.
$$

Let \\(S\\) be sufficient and define

$$
T^{\star}=E[T\mid S]
$$

componentwise.

Then

$$
T-\theta=(T-T^{\star})+(T^{\star}-\theta).
$$

Squaring the Euclidean norm,

$$
\lVertT-\theta\rVert^2
=
\lVertT-T^{\star}\rVert^2
+
\lVertT^{\star}-\theta\rVert^2
+
2(T-T^{\star})^T(T^{\star}-\theta).
$$

Conditional on \\(S\\),

$$
E[T-T^{\star}\mid S]=0,
$$

while \\(T^{\star}-\theta\\) is \\(S\\)-measurable. Therefore the cross term has expectation zero, and

$$
\boxed{
R(\theta,T)
=
E_\theta\lVertT-T^{\star}\rVert^2
+
R(\theta,T^{\star}).
}
$$

Hence

$$
\boxed{R(\theta,T^{\star})\le R(\theta,T)\quad\forall\theta.}
$$

So Rao–Blackwellization extends unchanged to vector estimation under squared Euclidean loss.

## 11. Multivariate normal mean: the usual estimator

Let

$$
X\sim N_k(\theta,I_k),
\qquad \theta\in\mathbb R^k,
$$

and estimate \\(\theta\\) under

$$
L(\theta,\delta)=\lVert\delta-\theta\rVert^2.
$$

The natural estimator is

$$
\delta_0(X)=X.
$$

It has several important properties.

### 11.1 Unbiasedness

$$
E_\theta[X]=\theta.
$$

### 11.2 Risk

$$
\begin{aligned}
R(\theta,X)
&=E_\theta\lVertX-\theta\rVert^2\\
&=\operatorname{tr}(I_k)\\
&=k.
\end{aligned}
$$

Thus \\(X\\) is an equalizer rule.

### 11.3 Minimum risk among unbiased estimators

The 6 October notes also describe \\(X\\) as the unbiased estimator with minimum risk. The precise statement is **minimum risk within the class of unbiased estimators**.

The normal family

$$
X\sim N_k(\theta,I_k)
$$

is a full \\(k\\)-parameter exponential family with natural statistic \\(X\\) and natural parameter space \\(\mathbb R^k\\). Hence \\(X\\) is complete sufficient for \\(\theta\\). Each coordinate \\(X_j\\) is therefore the UMVUE of \\(\theta_j\\).

If \\(\delta=(\delta_1,\ldots,\delta_k)^T\\) is any unbiased estimator of \\(\theta\\), then

$$
E_\theta[\delta_j]=\theta_j
$$

for every \\(j\\). Since \\(X_j\\) is UMVUE,

$$
\operatorname{Var}_\theta(\delta_j)
\ge
\operatorname{Var}_\theta(X_j)=1.
$$

Under Euclidean squared loss, unbiasedness makes the risk

$$
\begin{aligned}
R(\theta,\delta)
&=E_\theta\lVert\delta-\theta\rVert^2\\
&=\sum_{j=1}^k\operatorname{Var}_\theta(\delta_j)\\
&\ge k.
\end{aligned}
$$

But

$$
R(\theta,X)=k.
$$

Therefore

$$
\boxed{
X\text{ has minimum risk among all unbiased estimators of }\theta.
}
$$

The same conclusion follows from the multivariate Cramér--Rao inequality, since the Fisher information matrix for one observation is \\(I_k\\).

### 11.4 MLE

The likelihood is proportional to

$$
\exp\left\lbrace-\frac12\lVertx-\theta\rVert^2\right\rbrace,
$$

which is maximized at

$$
\widehat\theta=X.
$$

### 11.5 Generalized Bayes under the flat prior

Under the improper prior

$$
\pi(\theta)\equiv1,
$$

the posterior is

$$
\theta\mid X=x\sim N_k(x,I_k).
$$

Hence the generalized Bayes estimator is \\(x\\).

### 11.6 Minimaxity

Take the proper prior

$$
\theta\sim N_k(0,\tau^2I_k).
$$

The Bayes estimator is

$$
\delta_\tau(X)
=
\frac{\tau^2}{1+\tau^2}X,
$$

and the posterior covariance is

$$
\frac{\tau^2}{1+\tau^2}I_k.
$$

Therefore the minimum Bayes risk is

$$
r_\tau
=
\frac{k\tau^2}{1+\tau^2}.
$$

Every Bayes risk is a lower bound on minimax risk, so

$$
R^{\star}\ge \frac{k\tau^2}{1+\tau^2}.
$$

Let \\(\tau\to\infty\\):

$$
R^{\star}\ge k.
$$

But \\(X\\) has maximum risk \\(k\\), so

$$
\boxed{X\text{ is minimax with minimax risk }k.}
$$

## 12. Stein's phenomenon

The surprising result in the notes is:

<div class="theorem" markdown="1">

**Theorem 11.5 — Stein phenomenon.** For estimating \\(\theta\\) in

$$
X\sim N_k(\theta,I_k)
$$

under total squared-error loss:

- \\(X\\) is admissible for \\(k=1,2\\);
- \\(X\\) is inadmissible for every \\(k\ge3\\).

</div>

For \\(k\ge3\\), the James–Stein estimator

$$
\boxed{
\delta_{JS}(X)
=
\left(1-\frac{k-2}{\lVertX\rVert^2}\right)X
}
$$

dominates \\(X\\).

### 12.1 Risk calculation

Write

$$
\delta(X)=X+g(X).
$$

Then

$$
\begin{aligned}
R(\theta,\delta)
&=E\lVertX-\theta+g(X)\rVert^2\\
&=k+E\lVertg(X)\rVert^2
+2E[(X-\theta)^Tg(X)].
\end{aligned}
$$

Stein's identity states, under suitable differentiability/integrability,

$$
E[(X_i-\theta_i)g_i(X)]
=
E\left[\frac{\partial g_i}{\partial x_i}(X)\right].
$$

Take

$$
g(x)=-a\frac{x}{\lVertx\rVert^2}.
$$

Then

$$
\lVertg(x)\rVert^2
=
\frac{a^2}{\lVertx\rVert^2}.
$$

Also

$$
\sum_{i=1}^k
\frac{\partial}{\partial x_i}
\left(-a\frac{x_i}{\lVertx\rVert^2}\right)
=
-a\frac{k-2}{\lVertx\rVert^2}.
$$

Hence

$$
R(\theta,\delta)
=
k+
E_\theta\left[
\frac{a^2-2a(k-2)}{\lVertX\rVert^2}
\right].
$$

The quadratic in \\(a\\) is minimized at

$$
a=k-2.
$$

Therefore

$$
\boxed{
R(\theta,\delta_{JS})
=
k-(k-2)^2
E_\theta\left[\frac1{\lVertX\rVert^2}\right]
<k
}
$$

for \\(k\ge3\\), where the inverse moment is finite. Thus \\(\delta\_{JS}\\) strictly dominates \\(X\\).

<div class="remark" markdown="1">

The positive-part estimator

$$
\delta_{JS}^+(X)
=
\left(1-\frac{k-2}{\lVertX\rVert^2}\right)_+X
$$

improves further on the original James–Stein rule, although that refinement was not needed in the handwritten class notes.

</div>

The central lesson is striking: \\(X\\) is unbiased, MLE, generalized Bayes, and minimax in every dimension, yet for \\(k\ge3\\) it is still inadmissible.

## 13. Location equivariance

Consider a location family

$$
X_1,\ldots,X_n\overset{\text{iid}}\sim f(x-\theta),
\qquad \theta\in\mathbb R.
$$

If every observation is shifted by \\(a\\), the parameter becomes \\(\theta+a\\). A natural estimator should transform in the same way.

<div class="definition" markdown="1">

**Definition 11.6 — Location equivariant estimator.** An estimator \\(T\\) is location equivariant if

$$
T(x_1+a,\ldots,x_n+a)
=
T(x_1,\ldots,x_n)+a
$$

for every real \\(a\\).

</div>

### 13.1 Risk of an equivariant estimator is constant

Write

$$
X_i=\theta+Z_i,
$$

where \\(Z_i\sim f(z)\\). By equivariance,

$$
T(X_1,\ldots,X_n)-\theta
=
T(Z_1,\ldots,Z_n).
$$

Therefore under squared-error loss,

$$
R(\theta,T)
=E[T(Z_1,\ldots,Z_n)^2],
$$

which does not depend on \\(\theta\\).

Thus every equivariant rule is an equalizer rule in a location problem.

### 13.2 Best equivariant estimator and flat-prior generalized Bayes rule

The generalized Bayes estimator under the flat prior \\(\pi(\theta)\equiv1\\) is

$$
\boxed{
\delta^{\star}(x)
=
\frac{
\int_{-\infty}^{\infty}
\theta\prod_{i=1}^n f(x_i-\theta)\,d\theta
}{
\int_{-\infty}^{\infty}
\prod_{i=1}^n f(x_i-\theta)\,d\theta
},
}
$$

when these integrals are well defined. This is the **Pitman estimator** and is the best location-equivariant estimator under squared-error loss.

For the normal location model with known variance,

$$
X_i\sim N(\theta,\sigma^2),
$$

the flat-prior posterior is

$$
\theta\mid\mathbf X
\sim
N\left(\bar X,\frac{\sigma^2}{n}\right).
$$

Hence

$$
\boxed{\delta^{\star}(X)=\bar X.}
$$

For one observation, this reduces to \\(\delta^{\star}(X)=X\\), matching the class note that the natural estimator is the best location-equivariant rule in the normal model.

## 14. Questions answered in this lecture

**Does Bayes imply admissible?**

A proper Bayes rule is admissible under the full-support and continuity conditions of Theorem 11.3. Generalized Bayes status alone does not guarantee admissibility.

**Why can a minimax estimator be inadmissible?**

Minimaxity only controls the largest risk. Another estimator can lower risk everywhere while retaining the same maximum-risk bound; James–Stein provides exactly such a phenomenon.

**Why was Karlin's theorem inconclusive for the unshrunk geometric estimator?**

For \\(\lambda=0\\), the right endpoint interval has finite length and the corresponding integral does not diverge. Direct risk comparison is then needed; \\(X/2\\) dominates \\(X\\).

**Why is \\(X/2\\) special in the exponential-rate example?**

It uniquely minimizes the coefficient \\(c^2+(c-1)^2\\) in the risk of \\(cX\\), and Karlin's two endpoint conditions meet exactly at \\(\lambda=1\\).

## 15. Review problems

1. Verify directly that \\(X/(1+\lambda)\\) is the Bayes estimator for \\(N(\mu,1)\\) under the prior \\(N(0,1/\lambda)\\).
2. Apply Karlin's theorem to the Poisson natural exponential family and check both endpoint integrals explicitly.
3. Reproduce the geometric risk comparison proving that \\(X/2\\) dominates every \\(cX\\) with \\(c>1/2\\).
4. Prove the vector Rao–Blackwell identity componentwise.
5. Derive the James–Stein risk formula using Stein's identity.
6. Show that the normal sample mean is location equivariant and has constant risk \\(\sigma^2/n\\).

## Lecture summary

Bayesian testing produces likelihood-ratio rules, while proper full-support Bayes rules provide an important route to admissibility. Karlin's criterion gives endpoint conditions for affine shrinkage rules in one-parameter exponential families. In vector problems, Rao–Blackwellisation remains valid under squared Euclidean loss, but the usual multivariate normal estimator becomes inadmissible in dimension at least three through the James–Stein phenomenon. Equivariance then identifies natural constant-risk rules within transformation classes.

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-10-consistent-asymptotic-tests/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-12-likelihood-ratio-classical-multivariate-tests/' | relative_url }})
</nav>

</div>
