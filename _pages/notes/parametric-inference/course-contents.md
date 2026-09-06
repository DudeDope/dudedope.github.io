---
layout: page
title: "Parametric Inference — Course Contents"
course: "Parametric Inference"
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Course index for the expanded Parametric Inference notes, covering point estimation, sufficiency and completeness, UMVUE theory, consistency and asymptotic rates, hypothesis testing, Bayesian inference, and minimax decision theory."
last_updated: "2026-09-06"
status: "complete"
math: true
permalink: /notes/parametric-inference/
course_slug: parametric-inference
note_kind: course-index
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Fall 2026 Parametric Inference lectures of Prof. Probal Chaudhuri at the Indian Statistical Institute, Kolkata. Additional exposition and any remaining errors are the responsibility of the note author.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Formula sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }})
</nav>

## Course description

These notes develop the main ideas of parametric inference from point estimation and risk through unbiased estimation, sufficiency, completeness, UMVUE theory, consistency and rates of convergence, hypothesis testing, Bayesian estimation, and minimax decision theory. Examples, proof details, and substantive questions from the handwritten source are kept beside the theory they illustrate so that each lecture remains independently readable without creating separate example-only chapters.

## Lectures

{% assign lecture_01_url = '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url %}
{% assign lecture_02_url = '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url %}
{% assign lecture_03_url = '/notes/parametric-inference/lecture-03-existence-uniqueness-unbiased-estimators/' | relative_url %}
{% assign lecture_04_url = '/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell-ancillarity/' | relative_url %}
{% assign lecture_05_url = '/notes/parametric-inference/lecture-05-completeness-exponential-families-basu/' | relative_url %}
{% assign lecture_06_url = '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-consistency/' | relative_url %}
{% assign lecture_07_url = '/notes/parametric-inference/lecture-07-hypothesis-testing-likelihood-ratio/' | relative_url %}
{% assign lecture_08_url = '/notes/parametric-inference/lecture-08-bayesian-inference-bayes-risk/' | relative_url %}

| Lecture | Title                                                                                                                   | Major topics                                                                                                                                                                                                   | Status   |
| ------: | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
|       1 | [Lecture 1: Point Estimation, Risk, Mean Squared Error, and Estimator Comparison]({{ lecture_01_url }})                 | statistical models, estimators, loss, risk, MSE, bias–variance decomposition, maximum likelihood, Cauchy likelihood equation                                                                                   | Complete |
|       2 | [Lecture 2: Unbiased Estimation, UMVUEs, Fisher Information, and the Cramér–Rao Bound]({{ lecture_02_url }})            | unbiasedness, UMVUE uniqueness, score identities, Fisher information, scalar and matrix CRLB, equality conditions, normal and exponential examples                                                             | Complete |
|       3 | [Lecture 3: Existence and Uniqueness of Unbiased Estimators]({{ lecture_03_url }})                                      | binomial factorial moments, polynomial criterion, Poisson entire power series and coefficient uniqueness, exponential Laplace-transform uniqueness, negative-binomial stopping                                 | Complete |
|       4 | [Lecture 4: Sufficiency, Rao–Blackwell Improvement, and Ancillary Statistics]({{ lecture_04_url }})                     | sufficiency, one-to-one transforms, minimal sufficiency, total variance, Neyman–Fisher factorisation, Rao–Blackwell theorem, normal, beta, Cauchy and uniform examples, ancillarity                            | Complete |
|       5 | [Lecture 5: Completeness, Exponential Families, and Basu’s Theorem]({{ lecture_05_url }})                               | completeness, exponential/Gamma sums, uniform order statistics, one- and multiparameter exponential families, Laplace-transform proof, uniform endpoints, Basu’s theorem                                       | Complete |
|       6 | [Lecture 6: Lehmann–Scheffé Theory, UMVUE Constructions, and Consistency]({{ lecture_06_url }})                         | Lehmann–Scheffé theorem, Rao–Blackwell construction from any unbiased estimator, UMVUE examples, weak/strong/Lp consistency, root-n consistency, asymptotic normality, convergence rates                       | Complete |
|       7 | [Lecture 7: Hypothesis Testing, Power, Sufficiency, and Likelihood-Ratio Tests]({{ lecture_07_url }})                   | test functions, randomization, power and size, sufficient-statistic reduction, two-point likelihood-ratio sufficiency, likelihood-comparison rule, Neyman–Pearson lemma                                        | Complete |
|       8 | [Lecture 8: Bayesian Point Estimation, Conjugate Priors, Bayes Risk, and Generalized Bayes Rules]({{ lecture_08_url }}) | conjugacy procedures, beta–binomial, Poisson and normal examples, Cauchy reciprocal-polynomial family, universal conjugate family, Bayes/generalized Bayes rules, minimax risk, equalizer rules, admissibility | Complete |

## Formula and notation sheet

The cumulative [formula and notation sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) records reusable notation, assumptions, estimator formulas, testing formulas, exponential-family forms, Bayesian updating formulas, and distributional identities, with lecture references.

## How this course is organised

The lecture boundaries follow mathematical dependence rather than the page boundaries of the handwritten source notes. Point-estimation material stays compact; sufficiency is developed before completeness; completeness is paired with exponential-family theory and Basu’s theorem; Lehmann–Scheffé is followed immediately by UMVUE constructions and asymptotic consistency; hypothesis testing and Bayesian inference form separate lectures because they introduce genuinely new frameworks. Decision-theoretic minimaxity is kept with Bayes risk in Lecture 8 because the key minimax lower bound is obtained from Bayes risk.

No standalone examples, summary, workflow, or distribution-identity lectures are used. Examples remain with the results they illustrate, while reusable identities are collected in the formula sheet.

## Editorial policy

Substantive mathematical corrections to source material are marked explicitly as **Editorial note** in the relevant lecture. Additional theory supplied to make an argument self-contained is marked **Additional context**. The source terminology and notation are otherwise preserved as closely as possible.

</div>
