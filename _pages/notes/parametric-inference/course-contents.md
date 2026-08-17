---
layout: page
title: "Parametric Inference — Course Contents"
course: "Parametric Inference"
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Course index for the expanded Parametric Inference notes, covering point estimation, sufficiency and completeness, UMVUE theory, hypothesis testing, and Bayesian inference."
last_updated: "2026-08-17"
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

## Lectures

{% assign lecture_01_url = '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url %}
{% assign lecture_02_url = '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url %}
{% assign lecture_03_url = '/notes/parametric-inference/lecture-03-existence-uniqueness-unbiased-estimators/' | relative_url %}
{% assign lecture_04_url = '/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell-ancillarity/' | relative_url %}
{% assign lecture_05_url = '/notes/parametric-inference/lecture-05-completeness-exponential-families-basu/' | relative_url %}
{% assign lecture_06_url = '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-consistency/' | relative_url %}
{% assign lecture_07_url = '/notes/parametric-inference/lecture-07-hypothesis-testing-likelihood-ratio/' | relative_url %}
{% assign lecture_08_url = '/notes/parametric-inference/lecture-08-bayesian-inference-bayes-risk/' | relative_url %}

| Lecture | Title                                                                                                                   | Major topics                                                                                                                                    | Status   |
| ------: | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
|       1 | [Lecture 1: Point Estimation, Risk, Mean Squared Error, and Estimator Comparison]({{ lecture_01_url }})                 | statistical models, estimators, loss, risk, MSE, bias–variance decomposition, maximum likelihood, Cauchy likelihood equation                    | Complete |
|       2 | [Lecture 2: Unbiased Estimation, UMVUEs, Fisher Information, and the Cramér–Rao Bound]({{ lecture_02_url }})            | unbiasedness, UMVUE, Fisher information, scalar and matrix CRLB, efficiency, normal and exponential examples                                    | Complete |
|       3 | [Lecture 3: Existence and Uniqueness of Unbiased Estimators]({{ lecture_03_url }})                                      | binomial polynomial criterion, Poisson power series, analytic functions, Laplace transforms, exponential uniqueness, negative-binomial stopping | Complete |
|       4 | [Lecture 4: Sufficiency, Rao–Blackwell Improvement, and Ancillary Statistics]({{ lecture_04_url }})                     | sufficiency, Neyman–Fisher factorisation, Rao–Blackwell theorem, normal, beta, Cauchy and uniform examples, ancillarity                         | Complete |
|       5 | [Lecture 5: Completeness, Exponential Families, and Basu’s Theorem]({{ lecture_05_url }})                               | completeness, one- and multiparameter exponential families, natural parameter spaces, uniform endpoints, Basu’s theorem                         | Complete |
|       6 | [Lecture 6: Lehmann–Scheffé Theory, UMVUE Constructions, and Consistency]({{ lecture_06_url }})                         | Lehmann–Scheffé theorem, UMVUE constructions, CRLB distinctions, weak and mean-square consistency                                               | Complete |
|       7 | [Lecture 7: Hypothesis Testing, Power, Sufficiency, and Likelihood-Ratio Tests]({{ lecture_07_url }})                   | test functions, randomization, power, size, sufficient-statistic reduction, likelihood-ratio sufficiency, Neyman–Pearson lemma                  | Complete |
|       8 | [Lecture 8: Bayesian Point Estimation, Conjugate Priors, Bayes Risk, and Generalized Bayes Rules]({{ lecture_08_url }}) | beta–binomial, gamma–Poisson, normal–normal and Cauchy conjugacy, Bayes risk, sufficient statistics, improper priors, generalized Bayes rules   | Complete |

## Formula and notation sheet

[Open the cumulative formula and notation sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}).

</div>
