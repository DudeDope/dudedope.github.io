---
layout: page
title: "Parametric Inference — Course Contents"
description: "Lecture-wise notes on point estimation, unbiased estimation, sufficiency, completeness, and UMVUE theory."
course: "Parametric Inference"
instructor: "Probal Chaudhuri"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
author: "Aditya Aryan"
last_updated: "2026-08-11"
status: "living"
math: true
permalink: /notes/parametric-inference/
course_slug: parametric-inference
note_kind: course-index
course_order: 0
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

## Lecture notes

{% assign lecture_1_url = '/notes/parametric-inference/lecture-01-point-estimation-risk-mse/' | relative_url %}
{% assign lecture_2_url = '/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/' | relative_url %}
{% assign lecture_3_url = '/notes/parametric-inference/lecture-03-existence-uniqueness-unbiased-estimators/' | relative_url %}
{% assign lecture_4_url = '/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell/' | relative_url %}
{% assign lecture_5_url = '/notes/parametric-inference/lecture-05-completeness-standard-exponential-families/' | relative_url %}
{% assign lecture_6_url = '/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-examples/' | relative_url %}

| Lecture | Topic                                                                                            | Main coverage                                                                      | Status   |
| ------: | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | -------- |
|       1 | [Point Estimation, Risk, Mean Squared Error, and Estimator Comparison]({{ lecture_1_url }})      | Parametric models; loss and risk; mean squared error; bias–variance decomposition  | Complete |
|       2 | [Unbiased Estimation, UMVUEs, Fisher Information, and the Cramér–Rao Bound]({{ lecture_2_url }}) | Unbiased estimation; UMVUEs; Fisher information; CRLB; efficiency                  | Complete |
|       3 | [Existence and Uniqueness of Unbiased Estimators]({{ lecture_3_url }})                           | Binomial polynomials; Poisson power series; analytic functions; Laplace transforms | Complete |
|       4 | [Sufficient Statistics, Factorisation, and Rao–Blackwell Improvement]({{ lecture_4_url }})       | Sufficiency; factorisation theorem; standard models; Rao–Blackwell theorem         | Complete |
|       5 | [Completeness in Standard Models and Full Exponential Families]({{ lecture_5_url }})             | Completeness; standard families; Laplace-transform arguments; exponential families | Complete |
|       6 | [Lehmann–Scheffé Theory and Detailed UMVUE Constructions]({{ lecture_6_url }})                   | Complete sufficiency; Lehmann–Scheffé theorem; UMVUE constructions                 | Complete |

## Formula and notation sheet

[Open the cumulative formula and notation sheet]({{ '/notes/parametric-inference/formula-sheet/' | relative_url }}).

</div>
