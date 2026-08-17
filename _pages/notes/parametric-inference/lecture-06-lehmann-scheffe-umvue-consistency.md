---
layout: page
title: "Lecture 6: Lehmann–Scheffé Theory, UMVUE Constructions, and Consistency"
short_title: "Lehmann–Scheffé and consistency"
course: "Parametric Inference"
lecture: 6
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Proves the Lehmann–Scheffé theorem, constructs UMVUEs across standard models, distinguishes UMVUE and CRLB optimality, and develops weak and mean-square consistency results."
topics:
  - "Lehmann–Scheffé theorem"
  - "complete sufficiency"
  - "UMVUE construction"
  - "CRLB versus UMVUE"
  - "weak consistency"
  - "mean-square consistency"
previous: "lecture-05-completeness-exponential-families-basu"
next: "lecture-07-hypothesis-testing-likelihood-ratio"
contents: "course-contents"
formula_sheet: "formula-sheet"
last_updated: "2026-08-17"
status: "complete"
math: true
permalink: /notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-consistency/
course_slug: parametric-inference
note_kind: lecture
course_order: 6
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Fall 2026 Parametric Inference lectures of Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata. Additional exposition and any remaining errors are the responsibility of the note author.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-05-completeness-exponential-families-basu/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-07-hypothesis-testing-likelihood-ratio/' | relative_url }})
</nav>

## Learning objectives

<div class="intuition" markdown="1">

**Additional context.**
This section was added to make the lecture easier to use as a self-contained study note.

</div>

- Prove the Lehmann–Scheffé theorem from Rao–Blackwellisation and completeness.
- Construct UMVUEs in Bernoulli, binomial, Poisson, exponential, uniform, and normal models.
- Use falling-factorial and gamma moments in UMVUE construction.
- Distinguish unique unbiasedness, UMVUE uniqueness, CRLB attainment, and MSE optimality.
- Define weak consistency and prove a useful consistency theorem for sequences of UMVUEs.

## 1. Lehmann–Scheffé theorem and construction principle

<div class="theorem" markdown="1">

**Theorem 6.1 — Lehmann–Scheffé.**

Let \\(S\\) be a complete sufficient statistic for \\(\theta\\). If \\(h(S)\\) is unbiased for \\(\psi(\theta)\\), then \\(h(S)\\) is the unique UMVUE of \\(\psi(\theta)\\).

</div>

**Proof.**

Let \\(U\\) be any unbiased estimator of \\(\psi(\theta)\\). By Rao–Blackwell,

$$
U^{\ast}=\operatorname{E}[U\mid S]
$$

is a function of \\(S\\), is unbiased, and satisfies

$$
\operatorname{Var}_\theta(U^{\ast})\le \operatorname{Var}_\theta(U).
$$

Both \\(U^{\ast}\\) and \\(h(S)\\) are unbiased functions of the complete statistic \\(S\\). Completeness implies

$$
U^{\ast}=h(S)\quad\text{almost surely}.
$$

Therefore

$$
\operatorname{Var}_\theta(h(S))=\operatorname{Var}_\theta(U^{\ast})\le \operatorname{Var}_\theta(U)
$$

for every unbiased \\(U\\) and every \\(\theta\\). Thus \\(h(S)\\) is a UMVUE. Uniqueness follows from the general uniqueness theorem for UMVUEs.

\\(\square\\)

> **Key point.**
> Practical recipe: find a sufficient statistic \\(S\\); prove it is complete; find any unbiased function \\(h(S)\\). Then \\(h(S)\\) is automatically the unique UMVUE.

## 2. Binomial and Bernoulli models

### Worked Example 6.1 — UMVUE of \\(\theta\\) in a Bernoulli sample

**Problem.**

Work through the source example “UMVUE of \\(\theta\\) in a Bernoulli sample” in full.

**Solution.**

Let \\(X_1,\dots,X_n\overset{\mathrm{iid}}{\sim}\operatorname{Bernoulli}(\theta)\\). Then

$$
S=\sum_{i=1}^nX_i\sim\operatorname{Bin}(n,\theta)
$$

is complete and sufficient. Since

$$
\operatorname{E}_\theta\left[\frac Sn\right]=\theta,
$$

the estimator

$$
\widehat\theta=\frac Sn=\overline X
$$

is the unique UMVUE of \\(\theta\\).

**Final result.**

The conclusion is the final result derived in the solution above.

### Worked Example 6.2 — UMVUE of \\(\theta^k\\)

**Problem.**

Work through the source example “UMVUE of \\(\theta^k\\)” in full.

**Solution.**

For \\(1\le k\le n\\),

$$
\operatorname{E}_\theta[(S)_{k}]=(n)_{k}\theta^k.
$$

Therefore

$$
\widehat{\theta^k}
=\frac{(S)_{k}}{(n)_{k}}
$$

is an unbiased function of the complete sufficient statistic \\(S\\), and is therefore the unique UMVUE of \\(\theta^k\\).

**Final result.**

The conclusion is the final result derived in the solution above.

## 3. Poisson model

### Worked Example 6.3 — UMVUEs from the total count

**Problem.**

Construct UMVUEs of \\(\theta\\) and \\(\theta^k\\) from an iid Poisson sample.

**Solution.**

Let \\(X_1,\dots,X_n\overset{\mathrm{iid}}{\sim}\operatorname{Poisson}(\theta)\\). Then

$$
S=\sum_{i=1}^nX_i\sim\operatorname{Poisson}(n\theta)
$$

is complete and sufficient. Since

$$
\operatorname{E}\left[\frac Sn\right]=\theta,
$$

\\(S/n\\) is the unique UMVUE of \\(\theta\\).

Also,

$$
\operatorname{E}[(S)_{k}]=(n\theta)^k,
$$

so

$$
\frac{(S)_{k}}{n^k}
$$

is the unique UMVUE of \\(\theta^k\\).

**Final result.**

\\(S/n\\) is the UMVUE of \\(\theta\\), and \\((S)\_k/n^k\\) is the UMVUE of \\(\theta^k\\).

## 4. Exponential model

### Worked Example 6.4 — UMVUE of the exponential mean

**Problem.**

Find the UMVUE of the mean of an iid exponential sample and distinguish the cases \\(n=1\\) and \\(n\ge2\\).

**Solution.**

Let \\(X_1,\dots,X_n\\) be iid exponential with mean \\(\theta\\). The sum

$$
S=\sum_{i=1}^nX_i
$$

is complete and sufficient. Since

$$
\operatorname{E}\left[\frac Sn\right]=\theta,
$$

the sample mean

$$
\overline X=\frac Sn
$$

is the unique UMVUE of \\(\theta\\).

For \\(n=1\\), \\(S=X_1\\), so \\(X_1\\) is not merely the UMVUE; it is the unique unbiased estimator of \\(\theta\\). For \\(n\ge2\\), there are many unbiased estimators, but only one UMVUE.

**Final result.**

\\(\overline X=S/n\\) is the unique UMVUE. For \\(n=1\\), it is also the unique unbiased estimator; for \\(n\ge2\\), other unbiased estimators exist.

### Worked Example 6.5 — UMVUE of powers of the exponential mean

**Problem.**

Use gamma moments of the sufficient sum to construct the UMVUE of \\(\theta^k\\) for an exponential sample.

**Solution.**

Since \\(S\sim\operatorname{Gamma}(n,\text{scale }\theta)\\),

$$
\operatorname{E}[S^k]=\theta^k\frac{\Gamma(n+k)}{\Gamma(n)}.
$$

Therefore

$$
\widehat{\theta^k}
=\frac{\Gamma(n)}{\Gamma(n+k)}S^k
$$

is unbiased for \\(\theta^k\\). Being a function of the complete sufficient statistic \\(S\\), it is the unique UMVUE.

**Final result.**

\\(\Gamma(n)S^k/\Gamma(n+k)\\) is the unique UMVUE of \\(\theta^k\\).

## 5. Uniform model

### Worked Example 6.6 — Two unbiased estimators of \\(\theta\\)

**Problem.**

Work through the source example “Two unbiased estimators of \\(\theta\\)” in full.

**Solution.**

Let \\(X_1,\dots,X_n\overset{\mathrm{iid}}{\sim}\operatorname{Uniform}(0,\theta)\\).

Because \\(\operatorname{E}[X\_i]=\theta/2\\),

$$
T_1=2\overline X
$$

is unbiased. Its variance is

$$
\operatorname{Var}(T_1)=4\operatorname{Var}(\overline X)
=4\frac{\theta^2/12}{n}
=\frac{\theta^2}{3n}.
$$

Let \\(M=X\_{(n)}\\). Its distribution function is

$$
\mathbb{P}(M\le m)
=\left(\frac m\theta\right)^n,
\qquad 0<m<\theta.
$$

Thus

$$
f_M(m)=\frac{n m^{n-1}}{\theta^n},
\qquad 0<m<\theta.
$$

Its first two moments are

$$
\begin{aligned}
\operatorname{E}[M]
&=\int_0^\theta m\frac{n m^{n-1}}{\theta^n}\,\mathrm{d}m
=\frac{n}{\theta^n}\frac{\theta^{n+1}}{n+1}
=\frac{n}{n+1}\theta,\\
\operatorname{E}[M^2]
&=\int_0^\theta m^2\frac{n m^{n-1}}{\theta^n}\,\mathrm{d}m
=\frac{n}{n+2}\theta^2.
\end{aligned}
$$

Hence

$$
\begin{aligned}
\operatorname{Var}(M)
&=\frac{n}{n+2}\theta^2-\frac{n^2}{(n+1)^2}\theta^2\\
&=\frac{n}{(n+1)^2(n+2)}\theta^2.
\end{aligned}
$$

Therefore

$$
T_2=\frac{n+1}{n}M
$$

is unbiased and

$$
\operatorname{Var}(T_2)
=\left(\frac{n+1}{n}\right)^2\operatorname{Var}(M)
=\frac{\theta^2}{n(n+2)}.
$$

For \\(n>1\\),

$$
\frac{\theta^2}{n(n+2)}<\frac{\theta^2}{3n},
$$

so \\(T_2\\) has strictly smaller variance than \\(T_1\\).

**Final result.**

The conclusion is the final result derived in the solution above.

### Worked Example 6.7 — UMVUE in the uniform model

**Problem.**

Use completeness and sufficiency of the sample maximum to identify the UMVUE of the uniform endpoint.

**Solution.**

The maximum \\(M=X\_{(n)}\\) is complete and sufficient for \\(\theta\\). Since

$$
\frac{n+1}{n}M
$$

is unbiased, the Lehmann–Scheffé theorem implies that

$$
\boxed{\widehat\theta_{\mathrm{UMVUE}}=\frac{n+1}{n}X_{(n)}}
$$

is the unique UMVUE of \\(\theta\\).

The ordinary CRLB is not applicable because the support \\((0,\theta)\\) depends on \\(\theta\\).

**Final result.**

\\(\widehat\theta\_{\mathrm{UMVUE}}=((n+1)/n)X\_{(n)}\\).

## 6. Normal variance revisited

### Worked Example 6.8 — UMVUE of \\(\sigma^2\\) in the normal family

**Problem.**

Work through the source example “UMVUE of \\(\sigma^2\\) in the normal family” in full.

**Solution.**

For the normal family with both \\(\mu\\) and \\(\sigma^2\\) unknown, the statistic

$$
\left(\sum_{i=1}^nX_i,\ \sum_{i=1}^nX_i^2\right)
$$

is sufficient by factorisation. This is a full-rank exponential family whose natural parameter space

$$
\left\lbrace \left(\frac\mu{\sigma^2},-\frac1{2\sigma^2}\right):\mu\in\mathbb{R},\sigma^2>0\right\rbrace =\mathbb{R}\times(-\infty,0)
$$

contains an open subset of \\(\mathbb{R}^2\\); hence the statistic is complete. Since

$$
S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\overline X)^2
$$

is an unbiased function of this complete sufficient statistic, it is the unique UMVUE of \\(\sigma^2\\).

This does not contradict the earlier fact that the biased estimator \\(Q/(n+1)\\) has smaller MSE. The UMVUE is optimal only within the class of unbiased estimators.

**Final result.**

The conclusion is the final result derived in the solution above.

## 7. Unique unbiased estimator versus unique UMVUE

These two claims are different.

1.  If an estimator is the _only_ unbiased estimator of \\(\psi(\theta)\\), then it is automatically the UMVUE.

2.  A UMVUE can be unique even though many other unbiased estimators exist. This happens because the UMVUE is the unique unbiased estimator with uniformly minimum variance.

3.  Completeness of the _entire sample statistic_ can force uniqueness of all unbiased estimators. More commonly, completeness of a sufficient statistic gives uniqueness among functions of that statistic, while Rao–Blackwell shows that the optimal unbiased estimator must be such a function.

### Worked Example 6.9 — Exponential distinction

**Problem.**

Use the exponential model to distinguish uniqueness of an unbiased estimator from uniqueness of a UMVUE.

**Solution.**

For one observation \\(X\sim\operatorname{Exp}(\text{mean }\theta)\\), \\(X\\) is the unique unbiased estimator of \\(\theta\\).

For \\(n\ge2\\), both \\(X_1\\) and \\(\overline X\\) are unbiased, so unbiased estimators are not unique. Nevertheless, \\(\overline X\\) is the unique UMVUE.

**Final result.**

For \\(n=1\\), \\(X\\) is the unique unbiased estimator of \\(\theta\\); for \\(n\ge2\\), unbiased estimators are not unique, but \\(\overline X\\) is the unique UMVUE.

## 8. CRLB attainment versus UMVUE

1.  If an unbiased estimator attains the CRLB for every parameter value, it is a UMVUE, because no unbiased estimator can have smaller variance.

2.  The converse need not hold: a UMVUE may fail to attain the CRLB when the bound is not attainable.

3.  In nonregular models, such as \\(\operatorname{Uniform}(0,\theta)\\), the usual CRLB may not apply at all, while Lehmann–Scheffé remains valid.

## 9. Consistency of a sequence of UMVUEs

The new notes introduce weak consistency and give a useful sufficient condition for consistency of UMVUEs.

<div class="definition" markdown="1">

**Definition 6.2 — Weak consistency.**
Let

$$
T_n=T_n(X_1,\ldots,X_n)
$$

estimate \\(\psi(\theta)\\) for each \\(n\\). The sequence \\(\lbrace T_n\rbrace\\) is weakly consistent for \\(\psi(\theta)\\) if

$$
T_n\xrightarrow{P_\theta}\psi(\theta)
\qquad
\text{for every }\theta.
$$

</div>

That is, for every \\(\varepsilon>0\\),

$$
\Pr_\theta\left(
\lvert T_n-\psi(\theta)\rvert>\varepsilon
\right)
\longrightarrow0.
$$

<div class="theorem" markdown="1">

**Theorem 6.3 — A finite-variance unbiased estimator forces UMVUE consistency.**
Let \\(X_1,X_2,\ldots\\) be iid from \\(P\_\theta\\). Suppose there exists a one-observation estimator \\(U(X_1)\\) such that

$$
\operatorname{E}_\theta[U(X_1)]
=
\psi(\theta),
\qquad
\operatorname{Var}_\theta(U(X_1))<\infty.
$$

For each \\(n\\), suppose \\(T_n(X_1,\ldots,X_n)\\) is a UMVUE of \\(\psi(\theta)\\). Then

$$
T_n\xrightarrow{P_\theta}\psi(\theta).
$$

</div>

**Proof.**

Form the sample average

$$
\bar U_n
=
\frac1n\sum_{i=1}^nU(X_i).
$$

Because the observations are iid,

$$
\operatorname{E}_\theta[\bar U_n]
=
\psi(\theta),
$$

so \\(\bar U_n\\) is an unbiased estimator based on \\(n\\) observations.

Its variance is

$$
\begin{aligned}
\operatorname{Var}_\theta(\bar U_n)
&=
\frac1{n^2}
\sum_{i=1}^n
\operatorname{Var}_\theta(U(X_i))\\
&=
\frac1n
\operatorname{Var}_\theta(U(X_1)).
\end{aligned}
$$

Since \\(T_n\\) is the UMVUE,

$$
\operatorname{Var}_\theta(T_n)
\le
\operatorname{Var}_\theta(\bar U_n)
=
\frac{\operatorname{Var}_\theta(U(X_1))}{n}.
$$

Therefore

$$
\operatorname{Var}_\theta(T_n)\longrightarrow0.
$$

Since \\(T_n\\) is unbiased,

$$
\operatorname{E}_\theta[T_n]=\psi(\theta).
$$

Chebyshev's inequality gives

$$
\begin{aligned}
\Pr_\theta\left(
\lvert T_n-\psi(\theta)\rvert>\varepsilon
\right)
&\le
\frac{
\operatorname{Var}_\theta(T_n)
}{\varepsilon^2}\\
&\le
\frac{
\operatorname{Var}_\theta(U(X_1))
}{
n\varepsilon^2
}
\longrightarrow0.
\end{aligned}
$$

Hence \\(T_n\\) is weakly consistent.

\\(\square\\)

<div class="remark" markdown="1">

**Remark.**
The theorem is not saying that every UMVUE sequence is automatically consistent. The argument uses the existence of a finite-variance unbiased estimator from a single observation, which produces a benchmark estimator with variance of order \\(1/n\\).

</div>

<div class="intuition" markdown="1">

**Additional context.**
Since

$$
\operatorname{MSE}_\theta(T_n)
=
\operatorname{Var}_\theta(T_n)
$$

for an unbiased estimator, the proof actually gives mean-square consistency:

$$
\operatorname{E}_\theta[
(T_n-\psi(\theta))^2
]
\to0.
$$

Mean-square convergence implies convergence in probability.

</div>

## Questions answered in this lecture

**Question.**
Why is sufficiency alone not enough for uniqueness?

**Answer.**

Rao-Blackwellisation produces an unbiased function of the sufficient statistic, but without completeness there may be several different unbiased functions of that statistic.

**Question.**
What is the practical Lehmann-Scheffe recipe?

**Answer.**

Find a sufficient statistic, prove it is complete, and then find an unbiased function of it for the target. That function is the unique UMVUE.

**Question.**
What is the UMVUE of \\(\theta^k\\) in a Bernoulli sample?

**Answer.**

If \\(S=\sum_iX_i\\), it is \\((S)\_k/(n)\_k\\) for \\(1\le k\le n\\).

**Question.**
Why is \\((n+1)X\_{(n)}/n\\) the UMVUE of the uniform endpoint?

**Answer.**

The maximum is complete and sufficient, and its mean is \\(n\theta/(n+1)\\), so the scaled maximum is unbiased and Lehmann-Scheffe applies.

**Question.**
Why can the unbiased normal sample variance be a UMVUE even though a biased estimator has smaller MSE?

**Answer.**

UMVUE optimality is restricted to unbiased estimators; it does not minimise MSE over all estimators.

**Question.**
Is “unique unbiased estimator” the same statement as “unique UMVUE”?

**Answer.**

No. The first excludes every other unbiased estimator; the second excludes only any other unbiased estimator with uniformly minimum variance.

**Question.**
Does every UMVUE attain the CRLB?

**Answer.**

No. CRLB attainment is sufficient but not necessary, and the ordinary bound may be unattainable or invalid under nonregular support.

**Question.**
What happens for exponential data with one versus several observations?

**Answer.**

With one observation, \\(X\\) is the unique unbiased estimator of the mean. With \\(n\ge2\\), many unbiased estimators exist, but \\(\overline X\\) is the unique UMVUE.

**Question.**
Why does a finite-variance one-observation unbiased estimator imply consistency of the sequence of UMVUEs?

**Answer.**

Averaging independent copies of the one-observation estimator gives an unbiased benchmark with variance proportional to \\(1/n\\). The UMVUE has no larger variance, so its variance tends to zero; unbiasedness plus Chebyshev's inequality then gives convergence in probability.

## References and further reading

- Primary source: lectures of Probal Chaudhuri, Indian Statistical Institute, Kolkata, together with the handwritten/source material supplied for these notes.
- Expanded source: the complete LaTeX notes and compiled PDF used for this Markdown conversion.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Previous lecture]({{ '/notes/parametric-inference/lecture-05-completeness-exponential-families-basu/' | relative_url }}) · [Course contents]({{ '/notes/parametric-inference/' | relative_url }}) · [Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) · [Next lecture]({{ '/notes/parametric-inference/lecture-07-hypothesis-testing-likelihood-ratio/' | relative_url }})
</nav>

</div>
