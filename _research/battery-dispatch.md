---
layout: page
title: Probabilistic Forecasting and Electricity-Market Bidding
description: Probabilistic forecasting, stochastic price modelling, and optimisation for renewable generation and electricity-market decisions.
permalink: /research/battery-dispatch/
research_area: Probabilistic modelling and decision-making
status: Industry research
organisation: Ranial Systems
collaborators: []
period: May 2026–Present
featured: true
importance: 3
research_question: How can probabilistic forecasts of generation, weather, and market prices support bidding and battery-operation decisions under uncertainty?
summary: Probabilistic forecasting and optimisation for renewable generation and electricity-market decisions.
tags:
  - energy markets
  - vine copulas
  - probabilistic forecasting
  - bidding optimisation
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
    Probabilistic forecasting and decision modelling for renewable generation and electricity markets, including vine-copula dependence models,
    stochastic market-clearing-price models, quantile-based bidding, and battery-constrained optimisation.
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
        Renewable generation, weather, market prices, and battery conditions interact across different time scales. This work develops probabilistic
        models for those uncertainties and connects their outputs to bidding and operational decisions while respecting information timing and
        physical constraints.
      </p>
    </section>

    <section id="question" class="aa-entry-section">
      <h2>Research question</h2>
      <p>{{ page.research_question }}</p>
    </section>

    <section id="setup" class="aa-entry-section">
      <h2>Decision setup</h2>
      <p>
        Weather, solar-generation, market, and operational signals arrive on different timelines. Feasible battery actions depend on power, energy,
        efficiency, state of charge, and degradation considerations, so forecast and bidding-policy evaluation must use only the information
        available at each decision.
      </p>
    </section>

    <section id="methods" class="aa-entry-section">
      <h2>Methods</h2>
      <ul>
        <li>Machine-learning and deep-learning forecasting of solar generation and weather-dependent quantities.</li>
        <li>Vine-copula models for multivariate dependence and probabilistic forecasting.</li>
        <li>Stochastic modelling of market-clearing prices (MCP) for electricity-market decisions.</li>
        <li>Quantile-based bidding strategies and time-aware backtesting.</li>
        <li>Operational optimisation under battery power, energy, state, and degradation constraints.</li>
      </ul>
    </section>

    <section id="contribution" class="aa-entry-section">
      <h2>Contribution</h2>
      <p>
        My contribution spans data and modelling pipelines, probabilistic forecasts, time-aware evaluation, and the connection between uncertainty,
        bidding strategies, and battery-operational choices. Exact strategies and numerical performance are intentionally omitted from the public
        record.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations and next questions</h2>
      <p>
        Historical conditions may not represent future weather regimes, generation patterns, price spikes, equipment behaviour, or market-rule
        changes. Decision quality also depends on forecast calibration, dependence assumptions, bid construction, and operating costs. Evaluation
        therefore needs time-aware backtesting, tail-scenario analysis, and sensitivity checks.
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
