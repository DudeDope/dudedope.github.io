---
layout: page
title: Bivariate Copula Modelling of Extreme Air-Pollution Events
description: Nonparametric marginals, copula selection, upper-tail dependence, and conditional severity estimates for Bengaluru AQI episodes.
permalink: /projects/copula-air-pollution/
type: project
project_area: Statistical inference and probabilistic modelling
status: Supervised project
organisation: Indian Statistical Institute
supervisor: Dr. Shyamal Krishna De
period:
featured: true
importance: 2
tags:
  - copulas
  - tail dependence
  - environmental statistics
  - AQI
repository_url:
technical_note_url:
image:
---

<header class="aa-entry-header">
  <div class="aa-entry-meta">
    <span class="aa-status">{{ page.status }}</span>
    <span>{{ page.organisation }}</span>
    <span>with {{ page.supervisor }}</span>
  </div>
  <p class="aa-entry-subtitle">
    A bivariate dependence analysis of the duration and severity of extreme air-pollution episodes in Bengaluru from 2015–2024, using empirical
    marginals and six candidate copula families.
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
        Duration and severity are strongly related during extended pollution episodes, but the dependence in their upper tail is not fully
        described by a linear correlation. The project models their joint behaviour without imposing parametric marginal distributions.
      </p>
    </section>

    <section id="data" class="aa-entry-section">
      <h2>Data and definitions</h2>
      <p>
        The study used Bengaluru AQI observations from 2015–2024. Episodes were defined using AQI &gt; 100, with project-specific variables for
        duration D and severity S. Pseudo-observations were constructed from the empirical marginals, including explicit handling of discrete
        duration values.
      </p>
    </section>

    <section id="methods" class="aa-entry-section">
      <h2>Methods</h2>
      <ul>
        <li>Empirical marginal distributions and rank-based pseudo-observations.</li>
        <li>Six candidate copula families fitted by canonical maximum likelihood.</li>
        <li>Model selection using Akaike information criterion.</li>
        <li>Kendall's τ, Spearman's ρ, and upper-tail-dependence summaries.</li>
        <li>Conditional exceedance probabilities under the selected copula model.</li>
      </ul>
    </section>

    <section id="results" class="aa-entry-section">
      <h2>Reported results</h2>
      <p>
        The data produced Kendall's τ = 0.881 and Spearman's ρ = 0.972. The selected Gumbel copula had θ = 6.183 and upper-tail-dependence coefficient
        0.881. Under the project's definitions and fitted model, the conditional estimate
        P(S &gt; 2000 | D ≥ 12) was approximately 0.9998.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Interpretation and limitations</h2>
      <p>
        The conditional probability is a model-derived estimate, not a universal public-health threshold or causal claim. Results depend on episode
        definitions, data coverage and quality, station aggregation, ties in duration, and the adequacy of the selected copula family. Temporal
        nonstationarity and seasonal structure require additional study.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Artifacts</h2>
      <p class="aa-empty">The repository and copula note will be added later, after the public materials are organised.</p>
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
        <dt>Public output</dt>
        <dd>Forthcoming</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#problem">Problem</a>
      <a href="#data">Data</a>
      <a href="#methods">Methods</a>
      <a href="#results">Results</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
