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
period:
featured: true
importance: 5
tags:
  - optimal stopping
  - dynamic programming
  - Bellman recursion
  - memoisation
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
    A finite-horizon stopping problem with N boxes, C rewards of value V, and a per-observation cost, solved through a Bellman gain recursion.
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
        At each stage, the decision-maker compares the value of stopping with the expected benefit of another observation after paying its cost.
        The finite population and horizon make the value of information depend on the current state and remaining opportunities.
      </p>
    </section>

    <section id="method" class="aa-entry-section">
      <h2>Method</h2>
      <ul>
        <li>Represent the problem using the sufficient state S(x, y).</li>
        <li>Derive a Bellman GAIN recursion comparing stopping and continuation.</li>
        <li>Memoise repeated states to avoid exponential recomputation.</li>
        <li>Recover the stopping policy through backtracking and state-dependent cutoffs.</li>
        <li>Check small instances against direct enumeration.</li>
      </ul>
    </section>

    <section id="result" class="aa-entry-section">
      <h2>Reported result</h2>
      <p>For the specified instance with N = 20 and C = 5, the dynamic program produced an expected gain of 7.6875.</p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations</h2>
      <p>
        The result is tied to the project's reward and cost specification. Exact reproduction requires the complete parameter definition and code.
        Larger or richer state spaces may need structural approximations instead of exact memoisation.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Artifacts</h2>
      <p class="aa-empty">The implementation and full problem specification will be linked when the repository is public.</p>
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
        <dt>Public output</dt>
        <dd>Forthcoming</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#problem">Problem</a>
      <a href="#method">Method</a>
      <a href="#result">Result</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
