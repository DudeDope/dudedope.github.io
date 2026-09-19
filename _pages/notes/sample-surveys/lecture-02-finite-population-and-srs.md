---
layout: page
title: "Lecture 2: Finite-Population Framework and Simple Random Sampling"
course: "Sample Surveys"
lecture: 2
instructor: "Ambarish Chattopadhyay"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
slug: "lecture-02-finite-population-and-srs"
description: "Finite-population notation, sampling designs, selection and inclusion probabilities, SRSWR, SRSWOR, and implementation."
math: true
last_updated: "2026-08-06"
status: "published"
author: "Aditya Aryan"
permalink: /notes/sample-surveys/lecture-02-finite-population-and-srs/
course_slug: sample-surveys
note_kind: lecture
course_order: 2
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Fall 2026 Sample Surveys lectures of Prof. Ambarish Chattopadhyay at the Indian Statistical Institute, Kolkata. The exposition includes additional definitions, derivations, and worked solutions. Any remaining errors belong to the note maintainer, not to the instructor or the Institute.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/sample-surveys/lecture-01-foundations-and-representativeness/' | relative_url }}) · [Course contents]({{ '/notes/sample-surveys/' | relative_url }}) · [Next lecture →]({{ '/notes/sample-surveys/lecture-03-design-based-estimation/' | relative_url }})
</nav>

## The finite-population framework

Let the finite population be

$$
\mathcal{U}=\lbrace1,2,\ldots,N\rbrace.
$$

The label $j$ identifies unit $j$ in the sampling frame. For a study variable $Y$, let $Y_j$ be the value attached to unit $j$. The complete vector

$$
\mathbf{Y}=(Y_1,\ldots,Y_N)
$$

is fixed in design-based inference.

Important finite-population parameters include

$$
\begin{aligned}
\text{total:}\qquad T_Y&=\sum_{j=1}^{N}Y_j,\\
\text{mean:}\qquad \overline{Y}&=\frac{1}{N}\sum_{j=1}^{N}Y_j,\\
\text{variance with denominator $N$:}\qquad
\sigma_Y^2&=\frac{1}{N}\sum_{j=1}^{N}(Y_j-\overline{Y})^2,\\
\text{variance with denominator $N-1$:}\qquad
S_Y^2&=\frac{1}{N-1}\sum_{j=1}^{N}(Y_j-\overline{Y})^2.
\end{aligned}
$$

The two variance conventions satisfy

$$
S_Y^2=\frac{N}{N-1}\sigma_Y^2,
\qquad
\sigma_Y^2=\frac{N-1}{N}S_Y^2.
$$

<div class="definition" markdown="1">

**Definition 2.1** (Parameter, estimator, and estimate). A _parameter_ or _estimand_ is a fixed feature of the finite population, such as $\overline{Y}$. An _estimator_ is a random rule computed from the selected sample, such as $\overline{y}$. After a sample is observed, the numerical value of the estimator is an _estimate_.

</div>

## Where does randomness come from?

Let $S$ denote the random sample of population labels, and let $s$ denote a realised sample. The observed values $y_1,\ldots,y_n$ are random because the labels that occupy the sample positions are random, even though all $Y_j$ are fixed.

A useful distinction is:

- **Design-based view:** $Y_1,\ldots,Y_N$ are fixed; the sample is random.

- **Model-based or superpopulation view:** the $Y_j$ may themselves be modelled as random draws from a larger conceptual population.

The lectures use the design-based view. No normality, linear model, or iid superpopulation assumption is required for the unbiasedness results in the next chapters.

## Sample space and sampling design

<div class="definition" markdown="1">

**Definition 2.2** (Sample space). The sample space $\mathcal{S}$ is the collection of all samples that the design may produce. Its elements may be ordered sequences, unordered sets, multisets, or more complex multistage objects, depending on the sampling procedure.

</div>

<div class="definition" markdown="1">

**Definition 2.3** (Sampling design). A sampling design is a probability mass function

$$
p:\mathcal{S}\longrightarrow[0,1],
\qquad
\sum_{s\in\mathcal{S}}p(s)=1.
$$

Here $p(s)$ is the probability that the realised sample equals $s$.

</div>

**Question.**

For $\mathcal{U}=\lbrace1,2,3\rbrace$, what is $\mathcal{S}$ when

$$
p(\lbrace1,2\rbrace)=p(\lbrace1,3\rbrace)=p(\lbrace2,3\rbrace)=\frac13
$$

and $p(s)=0$ otherwise?

**Answer.**

The support of the design is

$$
\mathcal{S}=\bigl\lbrace\lbrace1,2\rbrace,\lbrace1,3\rbrace,\lbrace2,3\rbrace\bigr\rbrace.
$$

It is the set of all unordered samples of size two from $\mathcal{U}$. Equivalently, one may declare a larger mathematical sample space, such as the full power set of $\mathcal{U}$, and assign probability zero to every other subset; the effective sample space is the support above. This is SRSWOR with $N=3$ and $n=2$.

## Sampling scheme versus sampling design

A _sampling scheme_ is the algorithm used to generate a sample. A _sampling design_ is the probability law induced by the scheme. Different algorithms can induce the same design. For example, a lottery with thoroughly mixed slips and a software pseudorandom generator can both produce the uniform distribution over all $n$-subsets.

This distinction matters because inference depends on the induced probabilities, not on the physical appearance of the randomization device.

## Selection and inclusion probabilities

<div class="definition" markdown="1">

**Definition 2.4** (Selection probability). In a sequential design, the stage-$k$ selection probability of unit $j$ is

$$
\mathbb{P}(\text{unit $j$ is selected at draw $k$}).
$$

One must distinguish an unconditional or marginal probability from a conditional probability given earlier draws.

</div>

<div class="definition" markdown="1">

**Definition 2.5** (First-order inclusion probability). The first-order inclusion probability of unit $j$ is

$$
\pi_j=\mathbb{P}(j\in S).
$$

</div>

<div class="definition" markdown="1">

**Definition 2.6** (Second-order inclusion probability). For distinct units $j\neq k$,

$$
\pi_{jk}=\mathbb{P}(j\in S,\ k\in S).
$$

</div>

Selection probability concerns a particular draw. Inclusion probability concerns presence anywhere in the final sample. Under sampling with replacement, a unit can be selected multiple times but is included at least once only once.

## Simple random sampling with replacement

### Sampling scheme

Under SRSWR of size $n$:

1.  select one of the $N$ units with probability $1/N$ each;

2.  record the selected unit and return it to the population;

3.  repeat independently until $n$ draws have been made.

Let $J_i$ be the label selected at draw $i$. Then

$$
\mathbb{P}(J_i=j)=\frac1N,
\qquad
J_1,\ldots,J_n\text{ are independent}.
$$

The observed value at draw $i$ is $y_i=Y_{J_i}$.

### Induced design

An ordered sample is

$$
s=(j_1,\ldots,j_n)\in\mathcal{U}^n.
$$

There are $N^n$ ordered samples, and independence gives

$$
p(s)=\prod_{i=1}^{n}\frac1N=\frac1{N^n}.
$$

Thus SRSWR is uniform over ordered samples of size $n$ with repetition allowed.

**Question.**

What is the sampling design induced by SRSWR?

**Answer.**

The sample space is $\mathcal{S}=\mathcal{U}^n$, the set of all ordered $n$-tuples of population labels, and

$$
p(j_1,\ldots,j_n)=N^{-n}
$$

for every tuple. If order or multiplicity is discarded, the resulting objects are not equally likely; therefore the natural uniform formulation retains both.

### Inclusion probabilities under SRSWR

For a fixed unit $j$, the probability that it is not selected on one draw is $1-1/N$. Hence

$$
\pi_j
=1-\mathbb{P}(\text{$j$ is never selected})
=1-\left(1-\frac1N\right)^n.
$$

For distinct $j,k$, inclusion–exclusion yields

$$
\pi_{jk}
=1-2\left(1-\frac1N\right)^n
+\left(1-\frac2N\right)^n.
$$

Let $M_j=\sum_{i=1}^{n}\mathbb{I}(J_i=j)$ be the number of times unit $j$ is selected. Then

$$
M_j\sim\operatorname{Binomial}\left(n,\frac1N\right),
\qquad
\mathbb{E}_{p}(M_j)=\frac nN.
$$

The vector $(M_1,\ldots,M_N)$ has a multinomial distribution with total $n$ and equal cell probabilities $1/N$.

## Simple random sampling without replacement

### Sampling scheme

Under SRSWOR of size $n$:

1.  choose one of the $N$ units uniformly;

2.  remove it;

3.  choose one of the remaining units uniformly;

4.  continue until $n$ distinct units are selected.

At draw $k$, exactly $N-k+1$ units remain. Conditional on the history, each remaining unit has probability $1/(N-k+1)$ of being selected next.

**Question.**

Why does every unit have marginal probability $1/N$ of being selected at every stage, even though the conditional probability at draw $k$ is $1/(N-k+1)$?

**Answer.**

Fix unit $j$. For it to be selected at draw $k$, it must survive the first $k-1$ draws and then be chosen. By symmetry,

$$
\mathbb{P}(\text{$j$ survives the first $k-1$ draws})
=\frac{N-k+1}{N}.
$$

Given survival, its probability of being selected at draw $k$ is $1/(N-k+1)$. Therefore

$$
\mathbb{P}(J_k=j)
=\frac{N-k+1}{N}\cdot\frac1{N-k+1}
=\frac1N.
$$

The value $1/N$ is marginal. Conditional on $j$ still being available, the probability is $1/(N-k+1)$.

### Ordered and unordered designs

An ordered sequence of $n$ distinct units has probability

$$
\frac1N\cdot\frac1{N-1}\cdots\frac1{N-n+1}
=\frac1{(N)_n},
$$

where $(N)_n=N(N-1)\cdots(N-n+1)$ is the falling factorial.

A fixed unordered set $s$ of size $n$ can arise in $n!$ orders. Therefore

$$
p(s)=\frac{n!}{(N)_n}=\frac1{\binom Nn}.
$$

Hence SRSWOR is uniform over all unordered $n$-subsets.

**Question.**

What is the sampling design induced by SRSWOR?

**Answer.**

The natural unordered sample space is

$$
\mathcal{S}=\lbrace{}s\subseteq\mathcal{U}:\lvert s\rvert=n\rbrace,
$$

and

$$
p(s)=\binom{N}{n}^{-1}
$$

for every $s\in\mathcal{S}$. There are $\binom Nn$ possible samples, all equally likely.

### First- and second-order inclusion probabilities

For unit $j$,

$$
\pi_j
=\frac{\binom{N-1}{n-1}}{\binom Nn}
=\frac nN.
$$

For distinct $j,k$,

$$
\pi_{jk}
=\frac{\binom{N-2}{n-2}}{\binom Nn}
=\frac{n(n-1)}{N(N-1)}.
$$

The covariance of inclusion indicators is negative:

$$
\begin{aligned}
\operatorname{Cov}_p(I_j,I_k)
&=\pi_{jk}-\pi_j\pi_k\\
&=\frac{n(n-1)}{N(N-1)}-\frac{n^2}{N^2}\\
&=-\frac{n(N-n)}{N^2(N-1)}<0
\end{aligned}
$$

for $0<n<N$. Selecting one unit slightly reduces the chance of selecting another because the sample size is fixed.

## Implementing SRS

### Lottery method

Write the unique labels on identical slips, mix thoroughly, and draw. Replacement or nonreplacement is implemented literally. This method is transparent for small populations but becomes cumbersome for large frames.

### Random-number tables

A random-number table is a fixed printed sequence designed to behave like independent uniform digits. The investigator chooses a starting position and direction by a rule fixed before examining convenient outcomes.

#### Example: $N=10$, $n=4$, SRSWR

Using row 07 from the slide’s table and reading single digits from left to right gives

$$
1,7,7,8.
$$

The resulting ordered sample is $(1,7,7,8)$. If digit 0 appears, map it to unit 10.

#### Example: $N=17$, $n=4$, direct rejection

Read two-digit groups from row 07:

$$
17,78,30,00,15,10,80,68,30,91,91,53,03,\ldots
$$

Accept values $01$ through $17$ and reject $00$ or values above 17. The first four accepted labels are

$$
17,15,10,03.
$$

The acceptance probability is only $17/100$, so many groups are wasted.

#### Remainder method

Let $d$ be the number of digits used, and define

$$
M=N\left\lfloor \frac{10^d}{N}\right\rfloor.
$$

Accept integers $x\in\lbrace1,\ldots,M\rbrace$ and reject $0$ or $x>M$. Map an accepted $x$ to

$$
g(x)=1+((x-1)\bmod N).
$$

Every unit label has exactly $M/N$ preimages, so $g(x)$ is uniform on $\lbrace1,\ldots,N\rbrace$.

For $N=17$ and $d=2$, $M=17\times5=85$. Using the sequence above:

$$
17\mapsto17,
\qquad
78\mapsto10,
\qquad
30\mapsto13,
\qquad
00\text{ is rejected},
\qquad
15\mapsto15.
$$

Thus the sample is $(17,10,13,15)$.

> **Caution.**
>
> Writing “take $x\bmod17$” requires a convention for remainder 0. A multiple of 17 must map to unit 17, not to a nonexistent unit 0. The formula $1+((x-1)\bmod17)$ handles this automatically.

For SRSWOR, ignore repeated accepted labels and continue until $n$ distinct labels have been obtained.

### Software implementation in R

```r
N <- 17
n <- 4

srswr_draw <- sample(1:N, size = n, replace = TRUE)

srswor_draw <- sample(1:N, size = n, replace = FALSE)

selected_indices <- sample(
  1:nrow(pop_data),
  size = n,
  replace = FALSE
)
sample_data <- pop_data[selected_indices, ]
```

For reproducibility, record the software version, frame version, sample code, and random seed. A seed reproduces pseudorandom output; it does not repair a biased frame.

> **Lecture summary.**
>
> - A sampling design is a probability distribution over possible samples.
> - Under SRSWR, ordered samples are uniform over $\mathcal{U}^n$ and repeats are allowed.
> - Under SRSWOR, unordered $n$-subsets are uniform with probability $1/\binom Nn$.
> - Under SRSWOR, $\pi_j=n/N$ and $\pi_{jk}=n(n-1)/\lbrace{}N(N-1)\rbrace$.
> - Stagewise conditional probabilities under SRSWOR differ from stagewise marginal probabilities.
> - Random-number mappings must preserve uniformity; careless modular reduction can introduce bias.

---

## Answers to questions posed in the slides

### 15. For $\mathcal{U}=\lbrace1,2,3\rbrace$, what is the sample space in the example?

$$
\mathcal{S}=\lbrace\lbrace1,2\rbrace,\lbrace1,3\rbrace,\lbrace2,3\rbrace\rbrace,
\qquad p(s)=1/3.
$$

It is SRSWOR of size 2.

### 16. Why is the marginal stage-$k$ probability $1/N$ under SRSWOR?

A fixed unit survives the first $k-1$ draws with probability $(N-k+1)/N$ and, conditional on survival, is chosen with probability $1/(N-k+1)$. Their product is $1/N$.

### 17. What design is induced by SRSWR?

The sample space is $\mathcal{U}^n$ of ordered tuples, repeats allowed, and every tuple has probability $N^{-n}$.

### 18. What is a reasonable estimator of $\overline{Y}$ under SRSWR?

The sample mean $\overline{y}=n^{-1}\sum_i y_i$. Each draw has expectation $\overline{Y}$, so $\overline{y}$ is design unbiased and has variance $\sigma_Y^2/n$.

### 19. Why is $E_p(s^2)=\sigma_Y^2$ under SRSWR?

Use

$$
\sum_i(y_i-\overline{y})^2
=\sum_i(y_i-\overline{Y})^2-n(\overline{y}-\overline{Y})^2.
$$

The expectation of the right side is $n\sigma_Y^2-\sigma_Y^2=(n-1)\sigma_Y^2$, and division by $n-1$ gives the result.

### 20. What design is induced by SRSWOR?

The sample space consists of all unordered subsets of size $n$, and each has probability $1/\binom Nn$. First-order inclusion probability is $n/N$; second-order inclusion probability is $n(n-1)/\lbrace{}N(N-1)\rbrace$.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[← Previous lecture]({{ '/notes/sample-surveys/lecture-01-foundations-and-representativeness/' | relative_url }}) · [Course contents]({{ '/notes/sample-surveys/' | relative_url }}) · [Next lecture →]({{ '/notes/sample-surveys/lecture-03-design-based-estimation/' | relative_url }})
</nav>

</div>
