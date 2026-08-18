---
layout: page
title: Elo-Based Football Probability Modelling and Betting Simulation
description: Elo features, logistic outcome probabilities, calibration metrics, and a retrospective value-betting simulation.
permalink: /projects/football-probability/
type: project
project_area: Applied machine learning
status: Supervised project
organisation: Indian Statistical Institute
supervisor: Dr. Ayanendranath Basu
period: May 2025
featured: false
importance: 7
tags:
  - Elo ratings
  - probabilistic prediction
  - calibration
  - historical simulation
repository_url:
image: /assets/img/projects/football/elo-top-five.png
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
        The project asks whether a compact measure of changing team strength can support useful match probabilities and a transparent historical
        betting rule. Elo ratings supply the evolving strength signal; logistic regression maps rating differences to empirical home-win
        probabilities; bookmaker odds provide the comparison required to define a candidate value bet.
      </p>
    </section>

    <section id="data" class="aa-entry-section">
      <h2>Data and evaluation design</h2>
      <p>
        The report uses English Premier League results and bookmaker odds. Ten completed seasons, 2014–15 through 2023–24, form the training period;
        the 2024–25 season is treated as the test period. The training data contain 3,800 matches, with home and away teams, goals, full-time result,
        and average or maximum quoted odds.
      </p>
      <ul>
        <li>Chronological separation between the historical rating/model period and the reported test season.</li>
        <li>Proper scoring rules—Brier score and log loss—for the predicted probabilities.</li>
        <li>A flat-stake retrospective simulation for bets passing the selected edge threshold.</li>
      </ul>
    </section>

    <section id="method" class="aa-entry-section">
      <h2>Model and decision rule</h2>
      <p>
        Every team begins at Elo 1,000. After a match, ratings move according to the gap between the observed score—one for a win, one-half for a
        draw, and zero for a loss—and the Elo expectation, with a tunable update factor and home-advantage adjustment. A binary logistic calibration
        layer then estimates home-win probability from the home–away rating difference.
      </p>
      <p>
        Decimal odds are converted to implied probabilities. A candidate bet is placed only when the model probability exceeds the corresponding
        implied probability by more than a chosen edge threshold. The report also explores a ten-match moving average of Elo ratings to reduce
        short-run volatility.
      </p>
    </section>

    <section id="results" class="aa-entry-section">
      <h2>Reported results</h2>
      <p>
        The reported grid search selected an Elo update factor of 38, a 25-point home advantage, and an edge threshold of 0.11. On the reported
        evaluation, the probabilities recorded a Brier score of 0.2176 and log loss of 0.6249. The simulation placed 277 bets with a 46.21% win
        rate. The report states an aggregate profit of 5,139 units from a 10,000-unit starting bankroll and separately reports 18.76% ROI under its
        staking and ROI definitions.
      </p>
    </section>

    <figure>
      <img
        class="img-fluid rounded"
        src="{{ page.image | relative_url }}"
        alt="Line chart of Elo ratings over time for Liverpool, Arsenal, Manchester City, Aston Villa, and Newcastle"
        loading="lazy"
      >
      <figcaption>Reported Elo trajectories for the five highest-rated teams at the end of the study period. Source: project report.</figcaption>
    </figure>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations</h2>
      <p>
        This is a historical simulation, not evidence of future profitability. The result is sensitive to parameter search, the precise odds
        timestamp and source, bookmaker margin, the treatment of draws, staking rules, market availability, and possible selection leakage.
        Football strength is nonstationary, while injuries, transfers, and line-up information are absent. A stronger replication would freeze all
        tuning before the test season and add calibration curves, simple probability baselines, uncertainty intervals, and a fully specified
        bankroll ledger.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Artifacts</h2>
      <p class="aa-empty">The implementation, a reproducible data pipeline, and a sanitised report will be linked if they are released.</p>
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
        <dd>2014–15 to 2024–25</dd>
      </div>
      <div>
        <dt>Completed</dt>
        <dd>{{ page.period }}</dd>
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
      <a href="#method">Model</a>
      <a href="#results">Results</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
