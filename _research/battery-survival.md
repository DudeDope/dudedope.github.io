---
layout: page
title: Battery Degradation, Alert Prediction, and Survival Modelling
description: Statistical pipelines for early degradation signals, operational alerts, and time-to-event outcomes.
permalink: /research/battery-life/
research_area: Battery analytics and energy systems
status: Industry research
organisation: Ranial Systems
collaborators: []
period: May 2026–Present
featured: true
importance: 2
research_question: How can early operational measurements support defensible degradation, alert, and survival estimates for battery energy storage systems?
tags:
  - battery degradation
  - survival analysis
  - alert prediction
  - evaluation
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
    Applied statistical work on battery performance and degradation, alert prediction, survival modelling, and decision-support outputs for U.S.
    battery energy storage systems.
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
        Battery monitoring combines longitudinal measurements, operational context, rare alerts, and partially observed lifetimes. The work builds
        statistical pipelines that keep target definitions, data splits, preprocessing, and evaluation aligned with the operational question.
      </p>
    </section>

    <section id="question" class="aa-entry-section">
      <h2>Research question</h2>
      <p>{{ page.research_question }}</p>
    </section>

    <section id="methods" class="aa-entry-section">
      <h2>Methods</h2>
      <ul>
        <li>Feature engineering from early and longitudinal performance measurements.</li>
        <li>Degradation and performance modelling with interpretable baselines.</li>
        <li>Alert prediction under class imbalance and time-aware evaluation.</li>
        <li>Survival models with explicit event and censoring definitions.</li>
        <li>Group-aware splitting, reproducible preprocessing, and evaluation dashboards.</li>
      </ul>
    </section>

    <section id="contribution" class="aa-entry-section">
      <h2>Contribution</h2>
      <p>
        My work includes Python data pipelines, model comparisons, evaluation dashboards, and decision-support outputs. A central concern is
        preventing information leakage across time, assets, or operating groups while separating discrimination, calibration, and operational
        usefulness.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations and next questions</h2>
      <p>
        Battery behaviour can shift across chemistries, protocols, equipment, and operating conditions. Models require recalibration and genuinely
        out-of-group evaluation before transfer claims. Public numerical results are omitted because the underlying company artifacts are not
        released.
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
      <a href="#contribution">Contribution</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
