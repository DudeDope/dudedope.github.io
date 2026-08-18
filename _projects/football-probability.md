---
layout: page
title: Elo-Based Football Probability Modelling and Betting Simulation
description: A chronological Elo state model, logistic probability calibration, proper scoring rules, and a retrospective value-betting simulation.
permalink: /projects/football-probability/
type: project
project_area: Applied machine learning
status: Supervised project
organisation: Indian Statistical Institute
supervisor: Dr. Ayanendranath Basu
period: May 2025
featured: false
importance: 7
math: true
tags:
  - Elo ratings
  - probabilistic prediction
  - calibration
  - historical simulation
repository_url:
report_url: /assets/pdf/projects/football-elo-logistic-public.pdf
code_url: /assets/code/projects/football-elo-reference.py
image: /assets/img/projects/football/elo-top-five.png
---

<header class="aa-entry-header">
  <div class="aa-entry-meta">
    <span class="aa-status">{{ page.status }}</span>
    <span>{{ page.organisation }}</span>
    <span>with {{ page.supervisor }}</span>
  </div>
  <p class="aa-entry-subtitle">
    A chronological probability pipeline in which match results update latent club strength, logistic regression maps rating differences to
    home-win probabilities, and quoted odds define a retrospective decision rule.
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
      <strong>Interpretation.</strong> The bankroll figures are outputs of one historical simulation under incompletely documented market assumptions.
      They do not establish future profitability and are not financial or betting advice.
    </p>

    <section id="question" class="aa-entry-section">
      <h2>Statistical question</h2>
      <p>
        Can a low-dimensional, recursively updated measure of club strength produce useful home-win probabilities, and can those probabilities be
        compared with bookmaker odds without confusing predictive accuracy with historical trading performance?
      </p>
      <p>
        The project separates three objects: an Elo state updated after each match, a logistic probability model estimated from historical results,
        and a threshold rule that decides whether the difference between model and market probabilities is large enough to act on.
      </p>
    </section>

    <section id="data" class="aa-entry-section">
      <h2>Chronological data design</h2>
      <p>
        The report uses English Premier League match results and quoted decimal odds. Ten completed seasons, 2014–15 through 2023–24, provide 3,800
        historical matches; the 2024–25 season is reported as the evaluation period. Each row supplies date, home and away clubs, goals, full-time
        result, and average or maximum quoted odds.
      </p>
      <p>
        Chronology is essential because every pre-match rating must depend only on earlier results. The intended order is: read the current ratings,
        construct the feature and prediction, record the decision, observe the result, and only then update both ratings.
      </p>
    </section>

    <section id="elo" class="aa-entry-section">
      <h2>Elo as a Markov strength state</h2>
      <p>
        Every club begins at rating \(R_0=1000\). For a home side with rating \(R_h\), an away side with rating \(R_a\), and home-advantage offset
        \(H\), the reported expected home score is
      </p>

$$
E_h
=\frac{1}{1+10^{\left(R_a-(R_h+H)\right)/400}},
\qquad
E_a=1-E_h.
$$

      <p>The observed score is \(S_h=1\) for a home win, \(S_h=\tfrac12\) for a draw, and \(S_h=0\) for a home loss, with \(S_a=1-S_h\). Ratings then move by</p>

$$
\begin{aligned}
R_h'&=R_h+K(S_h-E_h),\\
R_a'&=R_a+K(S_a-E_a).
\end{aligned}
$$

      <p>
        The update is zero-sum: an unexpectedly strong result transfers rating mass toward the better-than-expected side. The factor \(K\) controls
        responsiveness; \(H\) shifts the pre-match expectation for home advantage. The current rating vector is a compact state summarising the
        result history used by the model.
      </p>
    </section>

    <section id="calibration" class="aa-entry-section">
      <h2>Logistic probability layer</h2>
      <p>
        Raw Elo expected scores need not be calibrated home-win probabilities. The report therefore uses the pre-match rating difference
        \(x_i=R_{h,i}-R_{a,i}\) in a binary logistic model:
      </p>

$$
\widehat p_i
=\Pr(Y_i=1\mid x_i)
=\frac{1}{1+\exp\!\left[-(\beta_0+\beta_1x_i)\right]}.
$$

      <p>
        Here \(Y_i=1\) denotes a home win. The coefficients are estimated by maximum likelihood on historical matches, and \(\widehat p_i\) is the
        probability passed to scoring and decision layers. The report does not fully specify whether draws are encoded as non-wins or removed during
        this binary fit; that ambiguity is retained as a reproducibility limitation rather than silently resolved.
      </p>
    </section>

    <section id="decision" class="aa-entry-section">
      <h2>From probabilities to a decision</h2>
      <p>For decimal odds \(o_i\), the naive implied probability and reported model edge are</p>

$$
\pi_i=\frac{1}{o_i},
\qquad
e_i=\widehat p_i-\pi_i.
$$

      <p>
        A candidate bet is triggered when \(e_i>\delta\). With flat stake \(B\), its realised profit is \((o_i-1)B\) after a win and \(-B\) after a
        loss. This decision rule is deliberately downstream of probability estimation: a probability model can score well but fail to clear prices,
        while a noisy backtest can appear profitable by chance despite weak calibration.
      </p>
      <p>
        The report also considers a rolling mean of the last \(n=10\) club ratings,
      </p>

$$
\bar R_i^{(t)}
=\frac{1}{n}\sum_{j=t-n+1}^{t}R_i^{(j)},
$$

      <p>as a lower-variance alternative to the latest Elo state.</p>
    </section>

    <section id="metrics" class="aa-entry-section">
      <h2>Probability metrics</h2>
      <p>The reported evaluation uses two proper scoring rules for binary outcomes:</p>

$$
\operatorname{Brier}
=\frac{1}{m}\sum_{i=1}^{m}(\widehat p_i-y_i)^2,
$$

$$
\operatorname{LogLoss}
=-\frac{1}{m}\sum_{i=1}^{m}
\left[y_i\log\widehat p_i+(1-y_i)\log(1-\widehat p_i)\right].
$$

      <p>
        Both reward accurate probability assignment rather than only correct classifications. They should ultimately be accompanied by reliability
        curves and reference models, because a raw score has limited meaning without a baseline.
      </p>
    </section>

    <section id="results" class="aa-entry-section">
      <h2>Reported configuration and outcomes</h2>
      <p>
        The reported grid search selected \(K=38\), \(H=25\), and edge threshold \(\delta=0.11\). The evaluation records a Brier score of 0.2176 and
        log loss of 0.6249. The historical simulation placed 277 bets, recorded a 46.21% win rate, and states total profit of 5,139 units from a
        10,000-unit starting bankroll.
      </p>
      <p>
        The report separately gives ROI as 18.76%. Those quantities can use different denominators—starting bankroll versus total amount staked—but
        the wager ledger needed to reconcile them is not included. They are therefore presented as reported outputs rather than recomputed claims.
      </p>
    </section>

    <figure class="aa-project-figure">
      <img
        class="img-fluid"
        src="{{ page.image | relative_url }}"
        alt="Elo trajectories for Liverpool, Arsenal, Manchester City, Aston Villa, and Newcastle"
        loading="lazy"
      >
      <figcaption>Reported Elo trajectories for the five highest-rated clubs at the end of the study period. Source: project report.</figcaption>
    </figure>

    <section id="audit" class="aa-entry-section">
      <h2>Backtest audit</h2>
      <p>
        A defensible replication needs a decision-time table containing the match date, pre-match ratings, fitted probability, exact bookmaker and
        odds timestamp, quoted price, edge, decision, stake, result, and bankroll update. Model fitting and selection must be frozen before the final
        season is revealed.
      </p>
      <ul>
        <li>Convert all outcome odds to normalised market probabilities to account for bookmaker margin.</li>
        <li>Document draw handling and whether decisions are home-only or span multiple outcomes.</li>
        <li>Separate training, parameter selection, calibration, and final testing chronologically.</li>
        <li>Compare against constant home-win frequency, raw Elo probability, and market-implied probability baselines.</li>
        <li>Add reliability diagrams, uncertainty intervals, maximum drawdown, and sensitivity to the edge threshold.</li>
      </ul>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations</h2>
      <p>
        Historical football strength is nonstationary; injuries, transfers, line-ups, managerial changes, and closing-market information are absent.
        Grid-searching \(K\), \(H\), and \(\delta\) on data later used for performance reporting would create selection leakage. Odds availability,
        limits, timing, margin, rejected wagers, and transaction frictions are not modelled. The reported season is a single realisation, so the
        profit path cannot by itself distinguish a persistent edge from variance.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Report and code</h2>
      <nav class="aa-artifacts" aria-label="Football probability artifacts">
        <a href="{{ page.report_url | relative_url }}">Read the public report (PDF)</a>
        <a href="{{ page.code_url | relative_url }}">Download the equation-level Python reference</a>
      </nav>
      <p class="aa-empty">
        The public PDF begins after the original identifying cover page. The Python file implements the documented equations and metrics; it is not
        presented as the unavailable original backtest pipeline.
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
        <dt>Data period</dt>
        <dd>2014–15 to 2024–25</dd>
      </div>
      <div>
        <dt>Completed</dt>
        <dd>{{ page.period }}</dd>
      </div>
      <div>
        <dt>Public output</dt>
        <dd>Technical record, report, reference code</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#question">Question</a>
      <a href="#data">Data design</a>
      <a href="#elo">Elo state</a>
      <a href="#calibration">Calibration</a>
      <a href="#decision">Decision rule</a>
      <a href="#metrics">Metrics</a>
      <a href="#results">Results</a>
      <a href="#audit">Backtest audit</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Report and code</a>
    </nav>
  </aside>
</div>
