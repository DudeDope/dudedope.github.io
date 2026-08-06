---
layout: page
title: Elo-Based Football Probability Modelling and Betting Simulation
description: Elo features, logistic outcome probabilities, calibration metrics, and a retrospective value-betting simulation.
permalink: /projects/football-probability/
type: project
project_area: Applied statistical learning
status: Supervised project
organisation: Indian Statistical Institute
supervisor: Dr. Ayanendranath Basu
period:
featured: false
importance: 5
tags:
  - Elo ratings
  - probabilistic prediction
  - calibration
  - historical simulation
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
    English Premier League outcome probabilities from Elo-derived features and logistic regression, evaluated with proper scoring rules and a
    retrospective value-betting simulation.
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
      <strong>Interpretation.</strong> The bankroll result is a historical simulation under the project's assumptions. It is not evidence of future
      profitability and is not financial or betting advice.
    </p>

    <section id="problem" class="aa-entry-section">
      <h2>Problem</h2>
      <p>
        The project predicts English Premier League match outcomes as probabilities rather than point classifications. This makes calibration and
        proper scoring rules central: confident probabilities should be supported by corresponding long-run frequencies.
      </p>
    </section>

    <section id="data" class="aa-entry-section">
      <h2>Data and method</h2>
      <ul>
        <li>English Premier League match data covering 2014–2024.</li>
        <li>Elo ratings used to summarise changing team strength.</li>
        <li>Logistic regression for match-outcome probabilities.</li>
        <li>Calibration analysis using Brier score and log loss.</li>
        <li>Retrospective value-betting simulation on the held-out test period.</li>
      </ul>
    </section>

    <section id="results" class="aa-entry-section">
      <h2>Reported results</h2>
      <p>
        The evaluated probabilities recorded a Brier score of 0.2176 and log loss of 0.6249. Under the project's historical simulation rules, a
        10,000-unit test bankroll recorded 5,139 units of profit.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations</h2>
      <p>
        A retrospective betting result is sensitive to the split, odds source, staking rule, transaction assumptions, market availability, and
        selection decisions. Football data are nonstationary, and backtests are vulnerable to leakage and overfitting. Public reproduction should
        include chronological splits, baselines, calibration plots, and complete simulation code.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Artifacts</h2>
      <p class="aa-empty">The code, data description, and evaluation notebook will be linked when the repository is public.</p>
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
        <dt>Data period</dt>
        <dd>2014–2024</dd>
      </div>
      <div>
        <dt>Public output</dt>
        <dd>Forthcoming</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#problem">Problem</a>
      <a href="#data">Data and method</a>
      <a href="#results">Results</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
