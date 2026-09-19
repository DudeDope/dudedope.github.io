---
layout: page
title: "Sample Surveys: Cumulative Formula Sheet"
course: "Sample Surveys"
instructor: "Ambarish Chattopadhyay"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
description: "Cumulative formula sheet for the Sample Surveys course; update after each lecture."
math: true
last_updated: "2026-08-06"
status: "ongoing"
author: "Aditya Aryan"
permalink: /notes/sample-surveys/formula-sheet/
course_slug: sample-surveys
note_kind: formula-sheet
course_order: 99
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Course contents]({{ '/notes/sample-surveys/' | relative_url }})
</nav>

> This is a **cumulative page**. Add new notation and formulae here after every lecture, while keeping the derivations in the lecture pages.

## Finite-population quantities

$$
\begin{aligned}
T_Y&=\sum_{j=1}^{N}Y_j,
&\overline{Y}&=\frac1N\sum_{j=1}^{N}Y_j,\\
\sigma_Y^2&=\frac1N\sum_{j=1}^{N}(Y_j-\overline{Y})^2,
&S_Y^2&=\frac1{N-1}\sum_{j=1}^{N}(Y_j-\overline{Y})^2,\\
S_Y^2&=\frac{N}{N-1}\sigma_Y^2,
&f&=\frac nN.
\end{aligned}
$$

## SRSWR

$$
\begin{aligned}
p(j_1,\ldots,j_n)&=N^{-n},\\
\pi_j&=1-\left(1-\frac1N\right)^n,\\
\pi_{jk}&=1-2\left(1-\frac1N\right)^n
+\left(1-\frac2N\right)^n,\\
E_p(\overline{y})&=\overline{Y},\\
\operatorname{Var}_{p}(\overline{y})&=\frac{\sigma_Y^2}{n},\\
\widehat{\operatorname{Var}_{p}}(\overline{y})&=\frac{s^2}{n}.
\end{aligned}
$$

## SRSWOR

$$
\begin{aligned}
p(s)&=\binom Nn^{-1},\\
\pi_j&=\frac nN,\\
\pi_{jk}&=\frac{n(n-1)}{N(N-1)},\\
E_p(\overline{y})&=\overline{Y},\\
\operatorname{Var}_{p}(\overline{y})&=(1-f)\frac{S_Y^2}{n}
=\frac{N-n}{N-1}\frac{\sigma_Y^2}{n},\\
E_p(s^2)&=S_Y^2,\\
\widehat{\operatorname{Var}_{p}}(\overline{y})&=(1-f)\frac{s^2}{n},\\
\widehat{\mathop{\mathrm{SE}}}(\overline{y})&=\sqrt{1-f}\frac{s}{\sqrt n}.
\end{aligned}
$$

## Totals and proportions

$$
\begin{aligned}
\widehat T_Y&=N\overline{y},
&\operatorname{Var}_{p}(\widehat T_Y)&=N^2\operatorname{Var}_{p}(\overline{y}),\\
P&=\frac1N\sum_jY_j,\quad Y_j\in\lbrace0,1\rbrace,
&\widehat{P}&=\overline{y},\\
\operatorname{Var}_{p,\mathrm{WR}}(\widehat{P})&=\frac{P(1-P)}{n},\\
\operatorname{Var}_{p,\mathrm{WOR}}(\widehat{P})&=\frac{N-n}{N-1}\frac{P(1-P)}{n},\\
\widehat{\operatorname{Var}_{p}}_{\mathrm{WOR}}(\widehat{P})&=(1-f)\frac{\widehat{P}(1-\widehat{P})}{n-1}.
\end{aligned}
$$

## Confidence intervals

$$
\begin{aligned}
\text{Known-$\sigma$ normal mean:}\quad
&\overline{X}\pm z_{\alpha/2}\frac{\sigma}{\sqrt n},\\
\text{Approximate SRSWOR mean:}\quad
&\overline{y}\pm z_{\alpha/2}\sqrt{1-f}\frac{s}{\sqrt n}.
\end{aligned}
$$

## Sample size

$$
\begin{aligned}
n_{\mathrm{WR,mean}}
&=\frac{z_{\alpha/2}^2\sigma_Y^2}{e^2},\\
n_{\mathrm{WOR,mean}}
&=\frac{z_{\alpha/2}^2S_Y^2}
{e^2+z_{\alpha/2}^2S_Y^2/N},\\
n_{\mathrm{WR,prop}}
&=\frac{z_{\alpha/2}^2P(1-P)}{e^2},\\
n_{\mathrm{WR,prop,worst}}
&=\frac{z_{\alpha/2}^2}{4e^2},\\
n_{\mathrm{WOR,prop}}
&=\frac{Nz_{\alpha/2}^2P(1-P)}
{(N-1)e^2+z_{\alpha/2}^2P(1-P)}.
\end{aligned}
$$

Always round upward and then adjust for expected nonresponse and design effect.

## References

W. G. Cochran. _Sampling Techniques_, 3rd edition. Wiley, 1977.

S. L. Lohr. _Sampling: Design and Analysis_. Chapman and Hall/CRC.

C.-E. Särndal, B. Swensson, and J. Wretman. _Model Assisted Survey Sampling_. Springer, 1992.

P. V. Sukhatme, B. V. Sukhatme, S. Sukhatme, and C. Asok. _Sampling Theory of Surveys with Applications_. Iowa State University Press and Indian Society of Agricultural Statistics.

J. Hájek. Limiting distributions in simple random sampling from a finite population. _Publications of the Mathematical Institute of the Hungarian Academy of Sciences_, 5:361–374, 1960.

X.-L. Meng. Statistical paradises and paradoxes in big data (I): Law of large populations, big data paradox, and the 2016 US presidential election. _The Annals of Applied Statistics_, 12(2):685–726, 2018.

V. C. Bradley et al. Unrepresentative big surveys significantly overestimated US vaccine uptake. _Nature_, 600:695–700, 2021.

</div>
