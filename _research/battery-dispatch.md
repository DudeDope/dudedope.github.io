---
layout: page
title: Battery Forecasting and Energy-Market Optimisation
description: Uncertainty-aware forecasting and operational optimisation for battery energy storage systems.
permalink: /research/battery-dispatch/
research_area: Battery analytics and energy systems
status: Industry research
organisation: Ranial Systems
collaborators: []
period: May 2026–Present
featured: true
importance: 3
research_question: How should battery monitoring and trading decisions combine uncertain market information with operational and degradation constraints?
tags:
  - energy markets
  - battery optimisation
  - probabilistic forecasting
  - decision support
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
    Machine-learning and optimisation work for operational decision support, monitoring, and trading in U.S. battery energy storage systems.
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
      <strong>Confidentiality.</strong> This record stays at the level of general statistical and optimisation methods. Private datasets, company
      logic, customer information, and internal performance are not published.
    </p>

    <section id="abstract" class="aa-entry-section">
      <h2>Abstract</h2>
      <p>
        Battery decisions couple forecasts with physical state: an action changes available energy, future flexibility, and degradation exposure.
        The work develops forecasting and optimisation components that respect information timing and translate model outputs into inspectable
        decision support.
      </p>
    </section>

    <section id="question" class="aa-entry-section">
      <h2>Research question</h2>
      <p>{{ page.research_question }}</p>
    </section>

    <section id="setup" class="aa-entry-section">
      <h2>Decision setup</h2>
      <p>
        Market and operational signals arrive on different timelines. Feasible actions depend on power, energy, efficiency, state of charge, and
        degradation considerations, so forecast evaluation and policy evaluation must be aligned with the information available at each decision.
      </p>
    </section>

    <section id="methods" class="aa-entry-section">
      <h2>Methods</h2>
      <ul>
        <li>Probabilistic and uncertainty-aware electricity-market forecasting.</li>
        <li>Scenario-based analysis and time-consistent feature construction.</li>
        <li>Operational optimisation under power, energy, and state constraints.</li>
        <li>Degradation-aware objectives and sensitivity analysis.</li>
        <li>Python pipelines, model evaluation, and decision-support dashboards.</li>
      </ul>
    </section>

    <section id="contribution" class="aa-entry-section">
      <h2>Contribution</h2>
      <p>
        My contribution spans data and modelling pipelines, evaluation outputs, and the connection between forecast uncertainty and operational
        choices. Exact strategies and numerical performance are intentionally omitted from the public record.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations and next questions</h2>
      <p>
        Historical conditions may not represent future price spikes, equipment behaviour, or market-rule changes. Policy quality also depends on
        forecast calibration and cost assumptions. Current questions include tail scenarios, distribution shift, degradation sensitivity, and
        scalable representations of operational state.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>References and artifacts</h2>
      <p class="aa-empty">No public code or report is attached. Links will be added only after confidentiality review.</p>
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
      <a href="#setup">Setup</a>
      <a href="#methods">Methods</a>
      <a href="#contribution">Contribution</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
