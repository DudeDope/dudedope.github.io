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
        Renewable generation, weather, market prices, and battery state interact across different time scales. This work separates forecasting,
        decision optimisation, and historical market replay so that uncertainty estimates can inform bids and dispatch without using information
        that would have been unavailable at the original decision time.
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
      <p>
        The modelling stack distinguishes a forecast from a control action. Forecasts describe plausible future generation or price paths; an
        optimiser values stored energy and constructs a contingent policy; only then does a later market replay determine which bid or offer blocks
        would clear under realised prices.
      </p>
    </section>

    <section id="methods" class="aa-entry-section">
      <h2>Methods</h2>
      <ul>
        <li>Leakage-safe machine-learning and deep-learning forecasts for solar generation, weather-dependent quantities, and market prices.</li>
        <li>Quantile forecasts, tail-event probabilities, and vine-copula models for multivariate dependence and probabilistic scenarios.</li>
        <li>Stochastic modelling of day-ahead and real-time market-clearing prices, with residual-based path generation.</li>
        <li>Rolling model-predictive control with a dynamic program for the marginal opportunity value of stored energy.</li>
        <li>Quantile-based and opportunity-value bidding policies translated into finite price–quantity bid and offer curves.</li>
        <li>Physical replay under power, energy, efficiency, state-of-charge, cycle-budget, and degradation-cost assumptions.</li>
      </ul>
    </section>

    <section id="evaluation" class="aa-entry-section">
      <h2>Backtesting and evaluation</h2>
      <p>
        Evaluation uses chronological train, validation, and test periods and freezes each decision before revealing the prices used for clearing and
        settlement. Forecast quality is assessed separately from decision quality: point and quantile errors do not automatically imply trading
        value. Policy comparisons therefore track gross and degradation-adjusted margin, equivalent full cycles, value per cycle, negative days,
        drawdown, tail risk, stress scenarios, and perfect-foresight opportunity benchmarks.
      </p>
    </section>

    <section id="contribution" class="aa-entry-section">
      <h2>Contribution</h2>
      <p>
        My contribution spans time-aligned data and feature pipelines, deterministic and probabilistic forecasts, scenario construction, constrained
        optimisation, bid-policy design, market replay, and risk-aware evaluation. A recurring design goal is to preserve an auditable boundary
        between information available at the bid cutoff, the policy selected at that time, and the outcomes observed later. Exact company strategies
        and numerical performance remain outside the public record.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations and next questions</h2>
      <p>
        Historical conditions may not represent future weather regimes, generation patterns, price spikes, equipment behaviour, or market-rule
        changes. Decision quality depends on forecast calibration, scenario construction, market timing, bid-clearing approximations, settlement
        rules, operating limits, degradation valuation, and terminal inventory treatment. Historical backtests are evidence about a specified replay,
        not bankable revenue forecasts or proof of production feasibility.
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
      <a href="#evaluation">Evaluation</a>
      <a href="#contribution">Contribution</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
