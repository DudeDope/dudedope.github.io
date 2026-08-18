---
layout: page
title: Bivariate Copula Modelling of Extreme Air-Pollution Events
description: Nonparametric marginals, copula selection, upper-tail dependence, and conditional severity estimates for Bengaluru AQI episodes.
permalink: /projects/copula-air-pollution/
type: project
project_area: Statistical inference and probabilistic modelling
status: Supervised project
organisation: Indian Statistical Institute
supervisor: Prof. Shyamal Krishna De
period: April 2026
featured: true
importance: 4
tags:
  - copulas
  - tail dependence
  - environmental statistics
  - AQI
repository_url:
image: /assets/img/projects/copula/marginals-joint.png
pseudo_observations_image: /assets/img/projects/copula/pseudo-observations.png
---

<header class="aa-entry-header">
  <div class="aa-entry-meta">
    <span class="aa-status">{{ page.status }}</span>
    <span>{{ page.organisation }}</span>
    <span>with {{ page.supervisor }}</span>
  </div>
  <p class="aa-entry-subtitle">
    A bivariate dependence analysis of the duration and cumulative severity of unhealthy air-pollution episodes in Bengaluru from 2015–2024, using
    empirical marginals and six candidate copula families.
  </p>
  <div class="aa-tags" aria-label="Topics">
    {% for tag in page.tags %}
      <span class="aa-tag">{{ tag }}</span>
    {% endfor %}
  </div>
</header>

<div class="aa-entry-layout">
  <div class="aa-entry-main">
    <section id="problem" class="aa-entry-section">
      <h2>Problem</h2>
      <p>
        A long pollution episode and a severe pollution episode are not interchangeable risk descriptions. The project asks how their joint upper
        tail behaves and whether a copula can represent that dependence without forcing Gaussian marginal distributions or reducing the analysis to
        Pearson correlation.
      </p>
    </section>

    <section id="data" class="aa-entry-section">
      <h2>Data and definitions</h2>
      <p>
        The study uses 87,649 hourly Bengaluru AQI observations from 1 January 2015 through 31 December 2024. An unhealthy event is a maximal
        contiguous run of hours with AQI &gt; 100. Duration D is the number of hours in the run; cumulative severity S is the sum of its hourly AQI
        values. This produces 13,904 events.
      </p>
      <p>
        Both event summaries are strongly right-skewed. Duration has median 4 hours and maximum 35 hours, while cumulative severity has median
        1,084.2 and maximum 10,777 AQI-units in the report's data construction.
      </p>
    </section>

    <figure>
      <img
        class="img-fluid rounded"
        src="{{ page.image | relative_url }}"
        alt="Histograms of event duration and cumulative AQI severity alongside their strongly increasing joint scatter plot"
        loading="lazy"
      >
      <figcaption>
        Marginal distributions and joint scatter for the extracted unhealthy events. The strong trend partly reflects that cumulative severity sums
        AQI over the event duration. Source: project report.
      </figcaption>
    </figure>

    <section id="methods" class="aa-entry-section">
      <h2>Methods</h2>
      <ul>
        <li>Empirical marginal CDFs and rescaled rank pseudo-observations, with average ranks for tied integer durations.</li>
        <li>Clayton, Ali–Mikhail–Haq, Frank, Gumbel, Joe, and Plackett copulas fitted by canonical maximum likelihood.</li>
        <li>Akaike information criterion for model comparison across the six one-parameter families.</li>
        <li>Empirical Kendall's τ and Spearman's ρ together with model-implied tail-dependence coefficients.</li>
        <li>Conditional exceedance probabilities derived from the fitted copula and empirical marginals.</li>
      </ul>
    </section>

    <figure>
      <img
        class="img-fluid rounded"
        src="{{ page.pseudo_observations_image | relative_url }}"
        alt="Rank-based pseudo-observations forming vertical columns and concentrating near the upper-right corner"
        loading="lazy"
      >
      <figcaption>
        Rank-based pseudo-observations. Vertical columns arise from tied integer durations; upper-corner concentration motivates an upper-tail model.
        Source: project report.
      </figcaption>
    </figure>

    <section id="results" class="aa-entry-section">
      <h2>Reported results</h2>
      <p>
        The data produced empirical Kendall's τ = 0.881 and Spearman's ρ = 0.972. Gumbel achieved the lowest reported AIC, −38,531.2, with estimated
        parameter θ = 6.1831, model-implied Kendall's τ = 0.7954, and upper-tail-dependence coefficient 0.8814. Under the project's definitions, the
        fitted conditional estimate P(S &gt; 2000 | D ≥ 12) was approximately 0.9998; the corresponding empirical estimate was 1.0000.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Interpretation and limitations</h2>
      <p>
        Cumulative severity mechanically grows with duration because it is defined as a sum over event hours. The very strong dependence therefore
        should not be interpreted as an independent causal effect of duration. Likewise, the conditional probability is an illustrative
        model-derived estimate, not a validated clinical or regulatory threshold.
      </p>
      <p>
        Results depend on the AQI &gt; 100 event definition, dataset coverage and provenance, station aggregation, ties in duration, finite-difference
        density evaluation, and the six-family candidate set. The analysis treats extracted events as independent and does not yet model temporal
        dependence, seasonality, meteorology, alternative thresholds, or time-varying copula parameters.
      </p>
    </section>

    <section id="team" class="aa-entry-section">
      <h2>Project team</h2>
      <p>
        This work was completed as a three-student course project under the supervision of {{ page.supervisor }} at the Indian Statistical
        Institute.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Artifacts</h2>
      <p class="aa-empty">
        A reproducible analysis repository or sanitised report will be linked after the code, data provenance, and collaborator permissions are
        cleared for public release.
      </p>
    </section>

  </div>

  <aside class="aa-entry-rail" aria-label="Project metadata">
    <h2>Project record</h2>
    <dl class="aa-fact-list">
      <div>
        <dt>Type</dt>
        <dd>{{ page.status }}</dd>
      </div>
      <div>
        <dt>Institution</dt>
        <dd>{{ page.organisation }}</dd>
      </div>
      <div>
        <dt>Supervisor</dt>
        <dd>{{ page.supervisor }}</dd>
      </div>
      <div>
        <dt>Study period</dt>
        <dd>AQI data, 2015–2024</dd>
      </div>
      <div>
        <dt>Completed</dt>
        <dd>{{ page.period }}</dd>
      </div>
      <div>
        <dt>Team</dt>
        <dd>Three students</dd>
      </div>
      <div>
        <dt>Public output</dt>
        <dd>Web project record</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#problem">Problem</a>
      <a href="#data">Data</a>
      <a href="#methods">Methods</a>
      <a href="#results">Results</a>
      <a href="#limitations">Limitations</a>
      <a href="#team">Team</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
