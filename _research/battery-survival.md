---
layout: page
title: Battery Degradation, Alert Prediction, and Survival Modelling
description: Statistical pipelines for early degradation signals, operational alerts, and time-to-event outcomes.
permalink: /research/battery-life/
research_area: Probabilistic modelling and decision-making
status: Industry research
organisation: Ranial Systems
collaborators: []
period: May 2026–Present
featured: true
importance: 2
research_question: How can early operational measurements support defensible degradation, alert, and survival estimates for battery energy storage systems?
summary: Machine-learning and statistical methods for battery degradation, anomaly detection, alert prediction, and survival modelling.
tags:
  - battery degradation
  - survival analysis
  - alert prediction
  - anomaly detection
  - remaining useful life
  - out-of-distribution detection
paper_url:
code_url:
technical_note_url:
image:
---

<header class="aa-entry-header">
  <div class="aa-entry-meta">
    <span class="aa-status">{{ page.status }}</span>
    <span>{{ page.period }}</span>
    <span>{{ page.organisation }}</span>
  </div>
  <p class="aa-entry-subtitle">
    Applied statistical and machine-learning work on battery performance and degradation, anomaly detection, alert prediction, survival modelling,
    and decision-support outputs for U.S. battery energy storage systems.
  </p>
  <div class="aa-tags" aria-label="Topics">
    {% for tag in page.tags %}
      <span class="aa-tag">{{ tag }}</span>
    {% endfor %}
  </div>
</header>

<div class="aa-entry-layout">
  <div class="aa-entry-main">
    <p class="aa-notice">
      <strong>Confidentiality.</strong> This record describes public-level statistical methods only. It does not expose company data, customer
      information, internal reports, or proprietary implementation details.
    </p>

    <section id="abstract" class="aa-entry-section">
      <h2>Abstract</h2>
      <p>
        Battery-health modelling combines longitudinal electrochemical measurements, operational context, rare alerts, and partially observed
        lifetimes. This work develops leakage-aware pipelines for early degradation signals, cycle-life and horizon-risk prediction, unusualness
        detection, and time-to-end-of-life ranking, while keeping each output tied to a clearly defined decision problem.
      </p>
    </section>

    <section id="question" class="aa-entry-section">
      <h2>Research question</h2>
      <p>{{ page.research_question }}</p>
    </section>

    <section id="methods" class="aa-entry-section">
      <h2>Methods</h2>
      <ul>
        <li>Early-cycle features from voltage-curve change, capacity, internal resistance, temperature, charge time, and operating protocol.</li>
        <li>Regression and fixed-horizon classification for cycle life and early risk, with interpretable scientific baselines.</li>
        <li>Checkpoint-based remaining-useful-life prototypes and survival-style ranking with Cox proportional-hazards and Weibull AFT models.</li>
        <li>Robust-distance, reconstruction, covariance, and isolation-based scores for out-of-distribution review.</li>
        <li>Group-aware splitting, train-only preprocessing, feature-family ablations, and reproducible diagnostic tables.</li>
      </ul>
    </section>

    <section id="evaluation" class="aa-entry-section">
      <h2>Evaluation principles</h2>
      <p>
        Regression, classification, risk ranking, and anomaly review answer different questions and are evaluated separately. Cycle-life models use
        held-out errors and feature-family comparisons; survival-style models emphasize concordance ranking; classifiers require discrimination and
        calibration checks. Unsupervised unusualness is not relabelled as failure severity: an unusual cell can be better, worse, or simply exposed
        to a rare protocol.
      </p>
    </section>

    <section id="contribution" class="aa-entry-section">
      <h2>Contribution</h2>
      <p>
        My work includes Python data and feature pipelines, purpose-specific model comparisons, survival and RUL prototypes, unusualness diagnostics,
        and evaluation outputs. A central concern is preventing information leakage across time, cells, batches, or operating groups while keeping
        ranking, probability calibration, and operational usefulness conceptually separate.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations and next questions</h2>
      <p>
        Early development uses cell-level laboratory cycling data, which are not equivalent to full BESS site telemetry or a naturally censored
        fleet-lifetime dataset. Small sample sizes, batch and protocol effects, correlated features, and missing maintenance or system-failure labels
        limit transfer claims. Checkpoint RUL and survival probabilities remain prototypes; relative risk ranking is more defensible than exact
        lifetime calibration. External validation across chemistries, protocols, equipment, and operating regimes is required.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>References and artifacts</h2>
      <p class="aa-empty">No public dataset, code, or report is attached. Links will be added only after confidentiality review.</p>
    </section>

  </div>

  <aside class="aa-entry-rail" aria-label="Research record metadata">
    <h2>Record</h2>
    <dl class="aa-fact-list">
      <div>
        <dt>Status</dt>
        <dd>{{ page.status }}</dd>
      </div>
      <div>
        <dt>Period</dt>
        <dd>{{ page.period }}</dd>
      </div>
      <div>
        <dt>Organisation</dt>
        <dd>{{ page.organisation }}</dd>
      </div>
      <div>
        <dt>Role</dt>
        <dd>Data Science Intern</dd>
      </div>
      <div>
        <dt>Public output</dt>
        <dd>Not released</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#abstract">Abstract</a>
      <a href="#question">Question</a>
      <a href="#methods">Methods</a>
      <a href="#evaluation">Evaluation</a>
      <a href="#contribution">Contribution</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
