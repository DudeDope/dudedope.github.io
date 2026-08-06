---
layout: page
title: "Stein's Paradox: Inadmissibility and Risk-Optimal Shrinkage"
description: Decision-theoretic risk, James–Stein shrinkage, heteroscedastic extensions, empirical Bayes estimation, and SURE.
permalink: /projects/stein-shrinkage/
type: project
project_area: Statistical inference and probabilistic modelling
status: Supervised project
organisation: Indian Statistical Institute
supervisor: Dr. Ayanendranath Basu
period:
featured: true
importance: 1
tags:
  - decision theory
  - James–Stein estimation
  - empirical Bayes
  - SURE
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
    A decision-theoretic study of why the usual estimator of a multivariate normal mean is inadmissible for d ≥ 3 and how shrinkage changes
    squared-error risk.
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
        Estimating normal means coordinate by coordinate appears natural, but in three or more dimensions a joint shrinkage estimator can uniformly
        improve total squared-error risk. The project connects this result to bias–variance trade-offs, empirical Bayes reasoning, and practical risk
        estimation.
      </p>
    </section>

    <section id="methods" class="aa-entry-section">
      <h2>Methods</h2>
      <ul>
        <li>Risk comparison between the usual estimator and James–Stein shrinkage.</li>
        <li>James–Stein and mean-centred shrinkage estimators.</li>
        <li>Heteroscedastic extensions through whitening.</li>
        <li>Normal–Normal empirical Bayes with method-of-moments and marginal maximum-likelihood estimates.</li>
        <li>Monte Carlo risk estimation and Stein's unbiased risk estimate (SURE).</li>
      </ul>
    </section>

    <section id="results" class="aa-entry-section">
      <h2>Reported results</h2>
      <p>
        The analysis recovered uniform James–Stein dominance over the usual estimator in the classical setting. In the heteroscedastic simulation
        study, the marginal maximum-likelihood empirical Bayes estimator produced the lowest recorded risk among the compared procedures.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations</h2>
      <p>
        Simulation rankings depend on the chosen signal and variance regimes. A complete public artifact should provide the parameter grid, random
        seeds, baselines, uncertainty around estimated risks, and code needed to reproduce every figure.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Artifacts</h2>
      <p class="aa-empty">The repository and technical note will be linked when they are ready for public release.</p>
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
        <dt>Public output</dt>
        <dd>Forthcoming</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#problem">Problem</a>
      <a href="#methods">Methods</a>
      <a href="#results">Results</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
