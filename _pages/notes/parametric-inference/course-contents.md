---
layout: page
title: "Parametric Inference — Course Contents"
course: "Parametric Inference"
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
description: "Course index for the expanded Parametric Inference notes, covering estimation, sufficiency and completeness, testing, Bayesian and minimax decision theory, admissibility, asymptotics, and multivariate inference."
last_updated: "2026-11-02"
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

These notes develop parametric inference from point estimation and risk through unbiased estimation, sufficiency, completeness, UMVUE theory, hypothesis testing, Bayesian and minimax decision theory, asymptotic testing, admissibility, equivariance, and multivariate likelihood-ratio methods. Examples, proof details, and substantive questions from the handwritten source are kept beside the theory they illustrate so that each lecture remains independently readable without creating separate example-only chapters.

## Lectures

{% assign lecture_01_url = '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url %}
{% assign lecture_02_url = '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url %}
{% assign lecture_03_url = '/notes/parametric-inference/lecture-03-existence-uniqueness-unbiased-estimators/' | relative_url %}
{% assign lecture_04_url = '/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell-ancillarity/' | relative_url %}
{% assign lecture_05_url = '/notes/parametric-inference/lecture-05-completeness-exponential-families-basu/' | relative_url %}
{% assign lecture_06_url = '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-consistency/' | relative_url %}
{% assign lecture_07_url = '/notes/parametric-inference/lecture-07-hypothesis-testing-likelihood-ratio/' | relative_url %}
{% assign lecture_08_url = '/notes/parametric-inference/lecture-08-bayesian-inference-bayes-risk/' | relative_url %}
{% assign lecture_09_url = '/notes/parametric-inference/lecture-09-unbiased-similar-neyman-structure-tests/' | relative_url %}
{% assign lecture_10_url = '/notes/parametric-inference/lecture-10-consistent-asymptotic-tests/' | relative_url %}
{% assign lecture_11_url = '/notes/parametric-inference/lecture-11-admissibility-equivariance-stein/' | relative_url %}
{% assign lecture_12_url = '/notes/parametric-inference/lecture-12-likelihood-ratio-classical-multivariate-tests/' | relative_url %}

| Lecture | Title                                                                          | Major topics                                                                                                                                                                                                                | Status   |
| ------: | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
|       1 | [Point Estimation, Risk, and Likelihood]({{ lecture_01_url }})                 | statistical models, risk and MSE, maximum likelihood, Cauchy likelihood equation, Newton–Raphson, Fisher scoring, MLE-sufficiency reduction, invariance principle                                                           | Complete |
|       2 | [Unbiased Estimation and the Cramér–Rao Bound]({{ lecture_02_url }})           | unbiasedness, UMVUE uniqueness, score identities, Fisher information, scalar and matrix CRLB, equality conditions, normal and exponential examples                                                                          | Complete |
|       3 | [Existence and Uniqueness of Unbiased Estimators]({{ lecture_03_url }})        | binomial factorial moments, polynomial criterion, Poisson entire power series and coefficient uniqueness, exponential Laplace-transform uniqueness, negative-binomial stopping                                              | Complete |
|       4 | [Sufficiency, Rao–Blackwell, and Ancillarity]({{ lecture_04_url }})            | sufficiency, one-to-one transforms, minimal sufficiency, total variance, Neyman–Fisher factorisation, Rao–Blackwell theorem, normal, beta, Cauchy and uniform examples, ancillarity                                         | Complete |
|       5 | [Completeness, Exponential Families, and Basu’s Theorem]({{ lecture_05_url }}) | completeness, exponential/Gamma sums, uniform order statistics, one- and multiparameter exponential families, Laplace-transform proof, uniform endpoints, Basu’s theorem                                                    | Complete |
|       6 | [Lehmann–Scheffé and Consistency]({{ lecture_06_url }})                        | Lehmann–Scheffé, UMVUE examples, weak/strong/Lp consistency, root-n rates, Slutsky consistency, sample median, fixed-design regression, convergence in distribution, MLE consistency                                        | Complete |
|       7 | [Hypothesis Testing and Likelihood Ratios]({{ lecture_07_url }})               | test functions, power and size, sufficiency reduction, Neyman–Pearson lemma, UMP one-sided tests, monotone likelihood ratio, binomial/exponential-family MLR, Cauchy counterexample                                         | Complete |
|       8 | [Bayesian Estimation and Minimax Risk]({{ lecture_08_url }})                   | conjugacy, Cauchy reciprocal-polynomial family, Bayes/generalized Bayes rules, minimax and admissibility, exact binomial minimax rule, sequence-of-priors theorem, Pareto conjugacy, uniform endpoint infinite maximum risk | Complete |
|       9 | [Unbiased and Similar Tests]({{ lecture_09_url }})                             | unbiased and similar tests, boundary arguments, Neyman structure, conditional UMPU tests, nuisance parameters, Poisson, exponential, normal and two-binomial constructions                                                  | Complete |
|      10 | [Consistent and Asymptotic Tests]({{ lecture_10_url }})                        | monotone power, consistent test sequences, asymptotically normal estimator tests, sample medians, MLE consistency and asymptotic normality                                                                                  | Complete |
|      11 | [Admissibility, Equivariance, and Stein's Phenomenon]({{ lecture_11_url }})    | Bayesian testing, admissibility, Karlin's criterion, vector Rao–Blackwell theory, multivariate normal means, James–Stein shrinkage, and location equivariance                                                               | Complete |
|      12 | [Likelihood-Ratio and Multivariate Tests]({{ lecture_12_url }})                | generalized likelihood ratios, classical t and F tests, Poisson equality, Hotelling statistics, union–intersection tests, and covariance-matrix testing                                                                     | Complete |

## Formula and notation sheet

The cumulative [formula and notation sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}) records reusable notation, assumptions, estimator formulas, testing formulas, exponential-family forms, Bayesian updating formulas, and distributional identities, with lecture references.

## How this course is organised

The lecture boundaries follow mathematical dependence rather than the page boundaries of the handwritten source notes. Point-estimation material stays compact; sufficiency is developed before completeness; completeness is paired with exponential-family theory and Basu’s theorem; and Lehmann–Scheffé is followed by UMVUE constructions and consistency. The testing sequence moves from Neyman–Pearson and MLR theory to conditional UMPU methods and asymptotic tests. Bayesian inference leads into minimaxity and admissibility, followed by equivariant and multivariate procedures.

No standalone examples, summary, workflow, or distribution-identity lectures are used. Examples remain with the results they illustrate, while reusable identities are collected in the formula sheet.

## Editorial policy

Substantive mathematical corrections to source material are marked explicitly as **Editorial note** in the relevant lecture. Additional theory supplied to make an argument self-contained is marked **Additional context**. The source terminology and notation are otherwise preserved as closely as possible.

</div>
