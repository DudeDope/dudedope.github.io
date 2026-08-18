---
layout: page
title: "Sequential Testing: Optimal Stopping under a Reward–Cost Trade-off"
description: A finite-horizon Bellman recursion, memoised dynamic programming, backtracking, and stopping cutoffs.
permalink: /projects/sequential-testing/
type: project
project_area: Optimisation and decision-making
status: Supervised project
organisation: Indian Statistical Institute
supervisor: Dr. Arnab Chakraborty
period: March 2024
featured: true
importance: 5
tags:
  - optimal stopping
  - dynamic programming
  - Bellman recursion
  - memoisation
repository_url:
image: /assets/img/projects/sequential/cutoff-growth.png
---

<header class="aa-entry-header">
  <div class="aa-entry-meta">
    <span class="aa-status">{{ page.status }}</span>
    <span>{{ page.organisation }}</span>
    <span>with {{ page.supervisor }}</span>
  </div>
  <p class="aa-entry-subtitle">
    From an intuitive stopping heuristic to an exact finite-horizon policy: a Bellman recursion for deciding whether another observation is worth
    its cost.
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
        Twenty closed boxes contain exactly five five-rupee coins. Opening a box costs one rupee, and the decision-maker may stop at any time. Because
        the five reward locations are assumed uniformly distributed, unopened boxes are exchangeable: the useful decision is not which box to open,
        but whether the expected value of one more observation justifies its cost.
      </p>
      <p>The report generalises the game to N boxes, C rewards of value V, and unit opening cost.</p>
    </section>

    <section id="heuristic" class="aa-entry-section">
      <h2>From a heuristic to a value function</h2>
      <p>
        The first strategy compared realised reward counts with their expectation and stopped only after the accumulated gain crossed an intuitive
        threshold. Exhaustive averaging over the possible reward placements gave an expected gain of approximately 6.6393. This provided a useful
        benchmark, but not a proof of optimality.
      </p>
      <p>
        The exact approach represents a state as S(x, y), where x rewards and y empty boxes have been observed. From that state, the probability that
        the next box contains a reward is (C − x)/(N − x − y). The value function compares immediate stopping, worth zero additional gain, with the
        expected reward and continuation value after paying for one more box.
      </p>
    </section>

    <section id="method" class="aa-entry-section">
      <h2>Dynamic-programming solution</h2>
      <ul>
        <li>Use backward induction to show that the Bellman value equals the maximum expected future gain at every state.</li>
        <li>Memoise repeated states so the recursive calculation does not recompute the same subproblems.</li>
        <li>Stop whenever continuation value is non-positive; otherwise open the next exchangeable box.</li>
        <li>Translate the state values into cutoffs indexed by the number of rewards still being sought.</li>
        <li>Check the derived strategy by averaging over all reward-box permutations for the reported instance.</li>
      </ul>
    </section>

    <section id="result" class="aa-entry-section">
      <h2>Reported result</h2>
      <p>
        For N = 20, C = 5, V = 5, and unit opening cost, the dynamic program gives an expected gain of 7.6875644995. The reported cutoffs for one
        through five remaining reward boxes are 8, 15, 21, 27, and 33 boxes. In the 20-box game, these cutoffs produce a state-dependent policy that
        continues aggressively while several rewards remain and becomes more selective as opportunities are exhausted.
      </p>
    </section>

    <figure>
      <img
        class="img-fluid rounded"
        src="{{ page.image | relative_url }}"
        alt="Scatter plot showing computed stopping cutoffs increasing with the number of reward boxes"
        loading="lazy"
      >
      <figcaption>
        Exploratory cutoff calculations over a wider parameter range. The near-linear pattern is empirical for the computed cases, not a proved
        asymptotic law. Source: project report.
      </figcaption>
    </figure>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations</h2>
      <p>
        Optimality depends on uniformly random reward placement, known N, C, and V, unit observation cost, and risk-neutral expected gain. The cutoff
        pattern does not establish convergence or linearity in general. Larger state spaces or non-exchangeable observations may require structural
        approximations rather than exact memoisation.
      </p>
    </section>

    <section id="team" class="aa-entry-section">
      <h2>Project team</h2>
      <p>
        This work was completed as a six-student course project supervised by {{ page.supervisor }} at the Indian Statistical Institute.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Artifacts</h2>
      <p class="aa-empty">A standalone implementation or sanitised report will be linked if it is released.</p>
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
        <dt>Reported instance</dt>
        <dd>N = 20, C = 5</dd>
      </div>
      <div>
        <dt>Completed</dt>
        <dd>{{ page.period }}</dd>
      </div>
      <div>
        <dt>Team</dt>
        <dd>Six students</dd>
      </div>
      <div>
        <dt>Public output</dt>
        <dd>Web project record</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#problem">Problem</a>
      <a href="#heuristic">Heuristic</a>
      <a href="#method">Method</a>
      <a href="#result">Result</a>
      <a href="#limitations">Limitations</a>
      <a href="#team">Team</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
