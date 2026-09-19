---
layout: page
title: "Lecture 1: Foundations of Sample Surveys and Representativeness"
course: "Sample Surveys"
lecture: 1
instructor: "Ambarish Chattopadhyay"
institution: "Indian Statistical Institute, Kolkata"
semester: "Fall 2026"
slug: "lecture-01-foundations-and-representativeness"
description: "Motivation, survey terminology, census versus sampling, representativeness, selection bias, and probability versus nonprobability sampling."
math: true
last_updated: "2026-08-06"
status: "published"
author: "Aditya Aryan"
permalink: /notes/sample-surveys/lecture-01-foundations-and-representativeness/
course_slug: sample-surveys
note_kind: lecture
course_order: 1
toc:
  sidebar: right
  collapse: expanded
  collapse_depth: 2
---

<div class="aa-course-note" markdown="1">

> **Source and attribution.** These are unofficial expanded notes based on the Fall 2026 Sample Surveys lectures of Prof. Ambarish Chattopadhyay at the Indian Statistical Institute, Kolkata. The exposition includes additional definitions, derivations, and worked solutions. Any remaining errors belong to the note maintainer, not to the instructor or the Institute.

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Course contents]({{ '/notes/sample-surveys/' | relative_url }}) · [Next lecture →]({{ '/notes/sample-surveys/lecture-02-finite-population-and-srs/' | relative_url }})
</nav>

## Statistics as the science of learning from data

In its modern singular sense, _statistics_ is the collection of principles and methods used to collect, organize, summarize, analyse, and interpret numerical information. Two foundational branches are:

1.  **Design of experiments**: the investigator deliberately assigns treatments or conditions and observes responses.

2.  **Sample surveys**: the investigator selects units from an existing population, measures one or more characteristics, and uses the resulting sample to learn about the whole population.

The common starting point is _data collection_. A sophisticated estimator cannot repair a fundamentally defective data-collection mechanism. This is why survey design is not merely a logistical prelude to analysis; it is part of the statistical argument itself.

## Historical motivation from the ISI tradition

The lectures emphasize that large-scale sample-survey work is deeply connected with the history of the Indian Statistical Institute. P. C. Mahalanobis’s work on agricultural and socioeconomic surveys demonstrated that carefully designed samples could be cheaper, faster, and in many settings more accurate than poorly administered complete censuses. The National Sample Survey, initiated in 1950, institutionalized continuous, multi-subject household surveying on a national scale.

Two methodological themes highlighted in the slides are worth retaining:

- **Theory born from practice.** Real survey constraints lead naturally to optimization, allocation, and variance-estimation problems.

- **Learning while surveying.** Pilot surveys and interpenetrating networks of subsamples anticipate modern ideas of sequential learning, replication, and internal quality assessment.

The story of King Nala and Rtuparna in the _Mahabharata_, used in the slides as an early illustration, captures the core intuition: inspect a small part of a large collection and infer the whole. Modern sampling theory adds what the story does not provide—a probability mechanism and a quantifiable measure of uncertainty.

## Turning practical questions into statistical objects

A survey question becomes mathematically meaningful only after specifying:

1.  the _target population_;

2.  the _observation unit_;

3.  the _study variable_;

4.  the _time reference_; and

5.  the _population parameter_ or _estimand_.

The examples on the first lecture’s “Questions” slide can be formalized as follows.

### Household expenditure

**Question.** How much does a typical family in a district spend each month on food, rent, and basic needs?

**Formalization.**

- Target population: all eligible households ordinarily resident in the district during the reference month.

- Observation unit: a household.

- Variables: monthly household expenditures on food, rent, utilities, and other specified necessities.

- Possible estimands: the population mean expenditure, category-wise means, or a median if “typical” is intended to be robust to extreme values.

A crucial point is that “typical” is not automatically synonymous with “mean.” The mean answers a resource-total question because $N\overline{Y}$ is total expenditure, while the median answers a central-household question and is less sensitive to a few very high-spending households.

### Labour-force participation

**Question.** What fraction of young adults in a state are currently working or looking for work?

Define

$$
Y_j=\begin{cases}
1,&\text{if young adult $j$ is employed or actively seeking work},\\
0,&\text{otherwise}.
\end{cases}
$$

Then the population proportion

$$
P=\frac{1}{N}\sum_{j=1}^{N}Y_j
$$

is the labour-force participation rate for the precisely defined age range and reference period. The wording “currently” must be translated into a fixed reference rule, such as status during the previous seven days.

### Mean birth weight

**Question.** What is the average birth weight of newborns delivered in public hospitals across a state?

- Target population: all live births in public hospitals in the state during a specified period.

- Observation unit: a newborn or delivery record.

- Study variable: birth weight, preferably measured using a standardized protocol.

- Estimand: the finite-population mean birth weight.

If only hospitals with digitized records can be sampled, then the sampled population may be smaller than the target population. This is a coverage issue, not a sampling-variance issue.

### Post-outbreak antibody prevalence

**Question.** What portion of a city’s population developed antibodies after a virus outbreak?

The variable is a binary laboratory outcome $Y_j\in\lbrace0,1\rbrace$ for resident $j$. The estimand is the seroprevalence $P$. Imperfect test sensitivity and specificity create measurement error; even a perfectly randomized sample does not by itself correct a defective diagnostic test.

### Wildlife abundance

**Question.** How many tigers or elephants are currently living in a reserve?

The target parameter is a population _total_, but individual animals are difficult to list and detect. Camera-trap locations, transects, or capture occasions may serve as sampling units rather than animals themselves. Because detection probability is less than one, naive counting is generally biased downward. Capture–recapture, distance sampling, or occupancy models are often required. This example shows that the observation unit and sampling unit need not coincide.

### UPI transaction failures

**Question.** What fraction of micro-transactions on a UPI application fail on a given day?

The target population consists of all eligible transaction attempts during the day; a transaction attempt is the observation unit; $Y_j=1$ indicates failure; and $P$ is the failure proportion. One must define whether user cancellations, timeouts, duplicate retries, and bank-side rejections count as failures.

### Distance to school

**Question.** What is the average distance a rural student must travel to the nearest high school?

The observation unit is a rural student, household, or village, depending on policy intent. A student-weighted mean and a village-weighted mean answer different questions. The distance variable must also be defined: straight-line distance, road distance, or actual route length.

### Voting intention

**Question.** Who do voters plan to support in an upcoming election?

For $K$ candidates or parties, define categorical indicators

$$
Y_{jk}=\mathbb{I}\lbrace\text{voter $j$ currently intends to support option $k$}\rbrace,
\qquad k=1,\ldots,K.
$$

The estimand is the vector of support proportions $(P_1,\ldots,P_K)$, together with a separate category for undecided or refusing respondents. The realised election result is not identical to current intention because turnout and late preference changes intervene.

> **Key idea.**
>
> The first answer to a survey question is usually not a number. It is a precise definition of the population, unit, variable, time period, and estimand that the number is supposed to represent.

## The ABCD of sample surveys

Consider the running example from the slides: a state health ministry wants the average monthly out-of-pocket medical expenditure of all adults in West Bengal in order to budget for a health-insurance scheme.

<div class="definition" markdown="1">

**Definition 1.1** (Observation unit). An _observation unit_ is the object on which a measurement is taken. It may be a person, animal, household, hospital, village, agricultural plot, financial record, transaction, or time interval.

</div>

Here, the natural observation unit is an adult resident. If expenditure is reported at household level, the observation unit may instead be a household, and the estimand must be revised accordingly.

<div class="definition" markdown="1">

**Definition 1.2** (Target population). The _target population_ is the complete collection of units, tied to a specified place and time, about which the investigator ultimately wishes to make statements.

</div>

For the running example, the target population might be all persons aged $18$ or older who are usual residents of West Bengal during a stated month.

<div class="definition" markdown="1">

**Definition 1.3** (Census or complete enumeration). A _census_ attempts to collect the study variables for every unit in the target population.

</div>

A census can eliminate sampling error if it truly covers and measures every unit correctly. It does not eliminate nonresponse, duplication, omission, interviewer error, recording error, or outdated frames.

<div class="definition" markdown="1">

**Definition 1.4** (Sample). A _sample_ is the collection of units actually selected for observation according to a specified procedure.

</div>

<div class="definition" markdown="1">

**Definition 1.5** (Sampled population). The _sampled population_ is the collection of units that can in principle be reached by the implemented sampling mechanism. It is the population represented by the frame and field protocol.

</div>

Ideally, sampled population and target population coincide. In practice, adults living in unregistered households, institutions, temporary shelters, or inaccessible regions may be excluded. The resulting discrepancy is called _undercoverage_; duplicate frame entries create _overcoverage_.

<div class="definition" markdown="1">

**Definition 1.6** (Sampling unit). A _sampling unit_ is a unit that can be directly selected at a particular stage of sampling.

</div>

If no list of adults exists but a list of households does, households may be the first-stage sampling units and adults within selected households may be second-stage sampling units. Observation units remain the adults whose expenditure is measured.

<div class="definition" markdown="1">

**Definition 1.7** (Sampling frame). A _sampling frame_ is the operational list, map, register, database, or rule that identifies the sampling units from which the sample is selected.

</div>

A usable frame should have identifiable units, stable and preferably unique labels, adequate coverage, current information, and enough auxiliary information to support stratification or contact. An electoral roll is a possible frame for adults, but it may exclude eligible non-registered residents and include outdated records.

<div class="definition" markdown="1">

**Definition 1.8** (Sample survey). A _sample survey_ is the complete process of selecting a subset of units, collecting data from the selected units, processing the responses, and using the data to estimate characteristics of a target population with an assessment of uncertainty.

</div>

## Census versus sample survey

A sample survey can offer:

- lower cost and shorter completion time;

- reduced manpower and simpler supervision;

- better-trained investigators and more intensive measurement;

- broader or more detailed questionnaires;

- faster publication and more frequent repetition;

- destructive testing when measuring every unit is impossible.

A census may be preferable when the population is small, unit-level information is legally required, very small geographic domains must be reported, or the consequence of missing a unit is unacceptable.

### Sampling and nonsampling error

The slides present the conceptual decomposition

$$
\text{total error}=\text{sampling error}+\text{nonsampling error}.
$$

Sampling error is variation caused by observing only a subset. Nonsampling error includes frame defects, nonresponse, measurement error, interviewer effects, data-processing mistakes, and model misspecification.

For a numerical estimator $\widehat\theta$, the design-based mean squared error is

$$
\operatorname{MSE}_p(\widehat\theta)
=\mathbb{E}_{p}\bigl[(\widehat\theta-\theta)^2\bigr]
=\operatorname{Var}_{p}(\widehat\theta)+\operatorname{Bias}_p(\widehat\theta)^2.
$$

This formula concerns sampling-design error. Nonsampling errors require additional random variables or bias models and do not always combine as independent additive quantities. The slide’s equality is therefore best read as an organizing principle rather than a universal algebraic identity.

**Question.**

“My opinion has never been asked, so how can the survey results represent me?”

**Answer.**

A probability sample is not intended to ask every person. It represents the population because each frame unit has a known chance of selection and the estimator accounts for that mechanism. Under a valid design, repeated samples are calibrated to the full population in the sense of design unbiasedness or consistency. The guarantee is probabilistic, not a claim that every realised sample visibly resembles the population in every characteristic. Coverage error, nonresponse, and measurement error can still invalidate the result.

## What makes a sample representative?

The word _representative_ is often used vaguely. A more rigorous interpretation has two parts:

1.  The selection mechanism and estimator permit valid reconstruction of specified population quantities.

2.  The design provides a defensible assessment of the reconstruction error.

A random sample can by chance contain imbalances. Randomization does not guarantee exact balance in one sample; it supplies a known sampling distribution and prevents systematic favouring of units before outcomes are observed.

> **Caution.**
>
> A very large sample can have a tiny reported standard error while remaining badly biased if its frame or response mechanism systematically excludes parts of the population. Standard errors quantify variation under the assumed design; they do not automatically diagnose coverage or nonresponse bias.

## The Literary Digest failure

In the 1936 United States presidential election, the _Literary Digest_ mailed roughly ten million questionnaires and received about 2.3 million responses. Its poll predicted a victory for Alfred Landon; Franklin D. Roosevelt instead won overwhelmingly.

**Question.**

What went wrong despite the enormous sample size?

**Answer.**

Two interacting mechanisms produced bias.

1.  **Coverage bias.** The mailing list relied heavily on telephone directories and vehicle-registration lists. In 1936 these lists disproportionately represented wealthier citizens, who were more likely to support Landon.
2.  **Nonresponse bias.** Only a fraction of contacted persons returned the questionnaire, and response propensity was associated with candidate preference. Landon supporters were more likely to respond.

The nominal sample size was huge, but the respondents were not a probability-like cross-section of the electorate. Increasing the number of observations from the same biased mechanism cannot remove systematic bias.

The poll had performed well in several earlier elections. That history did not validate the mechanism forever: the relationship between frame membership, response, and political preference changed. Past predictive success is not a substitute for a sound design.

## The Delphi–Facebook vaccine survey and the big-data paradox

The slides discuss a 2021 survey conducted through Facebook in partnership with the Delphi Research Group. It collected about $250{,}000$ weekly responses but overestimated adult COVID-19 vaccine uptake by about 17 percentage points. Facebook users who opted into the health survey differed systematically from the target adult population.

A useful mathematical identity clarifies how selection bias can dominate sample size. Let $R_j=1$ if population unit $j$ enters the responding sample and $R_j=0$ otherwise. Let $f=n/N$ be the response fraction, $\sigma_Y$ the finite-population standard deviation, and $\rho_{Y,R}$ the finite-population correlation between the outcome and the response indicator. Then

$$
\overline{Y}_{R}-\overline{Y}
=\rho_{Y,R}\sqrt{\frac{1-f}{f}}\,\sigma_Y.
$$

The three factors are sometimes called data quality, data quantity, and problem difficulty. If $\rho_{Y,R}$ is not close to zero, a huge respondent count can still produce a large error.

**Question.**

What percentage of the US adult population was vaccinated?

**Answer.**

The slides do not supply a single benchmark percentage. They supply the discrepancy: the Facebook-based survey overestimated the benchmark uptake by approximately 17 percentage points. Without the benchmark series and reference date, an exact percentage cannot be recovered from the slides alone.

## Probability and nonprobability sampling

<div class="definition" markdown="1">

**Definition 1.9** (Probability sampling). A design is a _probability sampling design_ when sample selection is governed by a known randomization mechanism and every unit intended to be represented has a known, strictly positive inclusion probability.

</div>

Known inclusion probabilities make design-based inference possible. Equal probabilities are not required; unequal-probability designs are common when units differ greatly in size or importance.

<div class="definition" markdown="1">

**Definition 1.10** (Nonprobability sampling). A design is a _nonprobability sampling design_ when selection probabilities are unknown, zero for some relevant units, or not generated by a controlled probability mechanism.

</div>

Nonprobability samples may be useful for exploration, qualitative inquiry, rare-population access, questionnaire testing, or rapid feedback. They generally do not support design-based margins of error for the target population.

### Convenience sampling

Units are selected because they are cheap and immediately accessible. Surveying people in a university canteen to test draft wording is useful as a pilot; using the same group to estimate all students’ opinions is usually unjustified.

### Judgment or purposive sampling

The investigator deliberately selects units believed to be especially informative. Expert interviews and case studies may benefit, but the investigator’s judgement replaces a known probability mechanism.

### Self-selection sampling

People volunteer entirely on their own initiative, as in online polls or feedback forms. Response propensity is often related to strong opinions or unusual experiences, so the resulting percentages should not be presented as population estimates without strong adjustment assumptions.

### Snowball sampling

Initial participants recruit others from their personal networks. This can reach hidden or stigmatized populations for which no frame exists. However, network structure and initial seeds heavily influence who is observed.

### Quota sampling

The investigator fixes target counts for categories, such as equal numbers of men and women, and fills each quota nonrandomly. Matching a few margins does not make the sample representative on unmeasured variables. Quota sampling is therefore not equivalent to stratified random sampling.

> **Lecture summary.**
>
> - Survey validity begins with a precise target population, unit, variable, time frame, and estimand.
> - Sample size is not a substitute for coverage, response, and measurement quality.
> - Probability sampling provides a known randomization distribution; nonprobability sampling does not.
> - Sampling units, observation units, and target units can differ.
> - A census can still have substantial nonsampling error, while a carefully managed sample can be more accurate.

---

## Answers to questions posed in the slides

### 1. How much does a typical family spend each month?

No numerical answer is possible without data. Define the district household population and reference month, sample households, measure category-wise expenditure, and estimate a mean or median. The word “typical” must be operationally defined.

### 2. What fraction of young adults are working or looking for work?

Code $Y_j=1$ for employed or actively job-seeking young adult $j$ and 0 otherwise. The target is $P=N^{-1}\sum_jY_j$. A precise age range and reference period are required.

### 3. What is the average birth weight in public hospitals?

Define all live births in public hospitals during the reference period as the population, each newborn as a unit, and birth weight as $Y$. Estimate $\overline{Y}$ using a probability sample or complete hospital records, while checking coverage and measurement quality.

### 4. What portion of a city developed antibodies?

Define a binary seropositivity indicator and estimate its population mean. Correct interpretation may require adjustment for imperfect test sensitivity and specificity.

### 5. How many tigers or elephants live in a reserve?

The parameter is an abundance total. Because animals are not fully detectable or listable, spatial sampling plus capture–recapture, distance sampling, or related detection models is normally required; a raw observed count is generally an underestimate.

### 6. What fraction of UPI micro-transactions fail?

Define the transaction-attempt population for the day, code failure as 1, and estimate the resulting proportion. The operational definition of failure must be fixed in advance.

### 7. What is the average distance to the nearest high school?

Choose whether the estimand is student-weighted, household-weighted, or village-weighted; define distance as route or straight-line distance; then estimate the corresponding finite-population mean.

### 8. Who do voters plan to support?

Estimate one population proportion per candidate or party, with explicit categories for undecided and nonresponse. Current intention is not identical to the final vote because turnout and later changes intervene.

### 9. Who won the 1936 US presidential election?

Franklin D. Roosevelt defeated Alfred Landon. The _Literary Digest_ prediction of a Landon victory failed because of coverage and nonresponse bias.

### 10. What went wrong in the Literary Digest survey?

Telephone and automobile lists overrepresented wealthier Landon-leaning voters, and response propensity was also related to preference. A large biased respondent set remained biased.

### 11. What percentage of US adults was vaccinated in the Delphi–Facebook example?

The slides do not provide a single date-specific benchmark percentage. They state that the survey overestimated uptake by about 17 percentage points. The exact benchmark cannot be reconstructed from the slides alone.

### 12. What can sampling buy us?

Lower cost, time, and manpower; easier supervision; more highly trained investigators; broader measurement; and sometimes greater total accuracy than a census because nonsampling error can be better controlled.

### 13. How can a survey represent someone who was not personally asked?

Through a known probability design. Every frame unit has a known chance of selection, and the estimator is calibrated to that design. Representation is a probabilistic property of the procedure, not a requirement that every person be interviewed.

### 14. Google Classroom?

This is an administrative prompt. The slides contain no answer, and statistical theory cannot determine the instructor’s course-management choice.

---

<nav class="aa-note-nav" aria-label="Course navigation" markdown="1">
[Course contents]({{ '/notes/sample-surveys/' | relative_url }}) · [Next lecture →]({{ '/notes/sample-surveys/lecture-02-finite-population-and-srs/' | relative_url }})
</nav>

</div>
