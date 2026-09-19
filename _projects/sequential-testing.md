---
layout: page
title: "Sequential Testing: Optimal Stopping under a Reward–Cost Trade-off"
description: A finite-horizon Markov decision problem solved by Bellman recursion, backward induction, memoisation, and stopping cutoffs.
permalink: /projects/sequential-testing/
type: project
project_area: Optimisation and decision-making
status: Supervised project
organisation: Indian Statistical Institute
supervisor: Dr. Arnab Chakraborty
period: March 2024
featured: true
importance: 5
math: true
tags:
  - optimal stopping
  - Markov decision processes
  - dynamic programming
  - Bellman recursion
repository_url:
report_url: /assets/pdf/projects/sequential-testing-public.pdf
code_url: /assets/code/projects/sequential-stopping.cpp
image: /assets/img/projects/sequential/cutoff-growth.png
---

<header class="aa-entry-header">
  <div class="aa-entry-meta">
    <span class="aa-status">{{ page.status }}</span>
    <span>{{ page.organisation }}</span>
    <span>with {{ page.supervisor }}</span>
  </div>
  <p class="aa-entry-subtitle">
    A finite stochastic game reduced to a two-dimensional Markov state, solved exactly through a Bellman recursion and a backward-induction proof of
    optimality.
  </p>
  <div class="aa-tags" aria-label="Topics">
    {% for tag in page.tags %}
      <span class="aa-tag">{{ tag }}</span>
    {% endfor %}
  </div>
</header>

<div class="aa-entry-layout">
  <div class="aa-entry-main">
    <section id="game" class="aa-entry-section">
      <h2>The game</h2>
      <p>
        There are \(N\) closed boxes, exactly \(C\) of which contain a reward worth \(V\). Opening any box costs one unit. Reward locations are
        uniformly distributed over the \(\binom{N}{C}\) possible placements, and the decision-maker may stop after any observation. Stopping keeps all
        reward already collected and incurs no further gain or loss.
      </p>
      <p>
        The reported instance uses \(N=20\), \(C=5\), and \(V=5\). The central question is sequential: after seeing part of the random placement,
        should one pay for another observation or preserve the current gain?
      </p>
    </section>

    <section id="heuristic" class="aa-entry-section">
      <h2>Why the first rule was insufficient</h2>
      <p>
        The initial rule compared observed rewards with their expectation and stopped after realised net gain crossed a hand-built threshold.
        Averaging it over all \(\binom{20}{5}=15{,}504\) reward placements produced expected gain \(6.6393188854\). That is a valid benchmark, but it
        optimises neither the decision at each state nor the complete policy.
      </p>
      <p>
        The key change is to value future information rather than only accumulated profit. Once the past has been summarised correctly, the problem
        becomes a finite-horizon Markov decision process with two actions: stop or continue.
      </p>
    </section>

    <section id="state" class="aa-entry-section">
      <h2>Markov state and transition law</h2>
      <p>
        Let \(S(x,y)\) denote the state after observing \(x\) rewards and \(y\) empty boxes. No other history is needed: conditional on \(x\) and
        \(y\), all unopened boxes remain exchangeable. There are \(C-x\) rewards among \(N-x-y\) unopened boxes, so
      </p>

$$
p_{x,y}
=\Pr\!\left(\text{next box contains a reward}\mid S(x,y)\right)
=\frac{C-x}{N-x-y}.
$$

      <p>
        Continuing moves to \(S(x+1,y)\) with probability \(p_{x,y}\) and gives immediate gain \(V-1\), or to \(S(x,y+1)\) with probability
        \(1-p_{x,y}\) and gives immediate gain \(-1\). This produces an acyclic state graph because every transition increases \(x+y\) by one.
      </p>
    </section>

    <section id="bellman" class="aa-entry-section">
      <h2>Bellman value</h2>
      <p>
        Define \(G(x,y)\) as the maximum expected additional gain available from \(S(x,y)\). Stopping is normalised to zero. The continuation value
        is
      </p>

$$
Q(x,y)
=p_{x,y}\bigl[V-1+G(x+1,y)\bigr]
+(1-p_{x,y})\bigl[-1+G(x,y+1)\bigr].
$$

      <p>The Bellman equation is therefore</p>

$$
G(x,y)=
\begin{cases}
0, & x=C\ \text{or}\ x+y=N,\\[4pt]
\max\!\left\{0,Q(x,y)\right\}, & \text{otherwise}.
\end{cases}
$$

      <p>
        The optimal action is explicit: continue exactly when \(Q(x,y)>0\), and stop when \(Q(x,y)\leq 0\). Memoisation evaluates each reachable
        state once, requiring \(O\!\left(C(N-C)\right)\) time and storage.
      </p>
    </section>

    <section id="proof" class="aa-entry-section">
      <h2>Why this strategy is optimal</h2>
      <div class="theorem">
        <p><strong>Proposition — Bellman optimality.</strong> For every feasible state \(S(x,y)\), \(G(x,y)\) equals the supremum of expected future
        gain over all admissible stopping strategies beginning at that state.</p>
      </div>
      <p><strong>Proof.</strong> Use backward induction on the number \(r=N-x-y\) of unopened boxes.</p>
      <p>
        If \(r=0\), or if \(x=C\), no uncollected reward remains and stopping gives value zero. Thus the claim holds at every terminal state.
      </p>
      <p>
        Assume it holds for every state with fewer than \(r\) unopened boxes. At a state with \(r\) unopened boxes, the first action of any admissible
        strategy is either stop or continue. Stopping has value zero. If it continues, exchangeability gives the two successor states and
        probabilities above. By the induction hypothesis, no continuation after either successor can exceed \(G(x+1,y)\) or \(G(x,y+1)\), so every
        continue-first strategy has expected value at most \(Q(x,y)\).
      </p>
      <p>
        Conversely, choosing an optimal continuation at each successor attains \(Q(x,y)\). Selecting the better of stopping and continuing therefore
        attains \(\max\{0,Q(x,y)\}=G(x,y)\). The claim follows for horizon \(r\), and hence for all states by backward induction. \(\square\)
      </p>
    </section>

    <section id="policy" class="aa-entry-section">
      <h2>Cutoff representation of the policy</h2>
      <p>
        A state with \(\alpha=C-x\) rewards among \(n=N-x-y\) unopened boxes is equivalent to a fresh subproblem with \(\alpha\) rewards and \(n\)
        boxes. For reward value \(V=5\), the report computed the largest \(n\) for which the initial continuation value remains positive:
      </p>

      <table>
        <thead>
          <tr>
            <th>Rewards remaining \(\alpha\)</th>
            <th>Largest profitable box count \(n_{\alpha}\)</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>8</td></tr>
          <tr><td>2</td><td>15</td></tr>
          <tr><td>3</td><td>21</td></tr>
          <tr><td>4</td><td>27</td></tr>
          <tr><td>5</td><td>33</td></tr>
        </tbody>
      </table>

      <p>
        Thus the policy continues when \(n\leq n_{\alpha}\). In the 20-box instance it necessarily searches for the first three rewards, because the
        relevant cutoffs exceed the available horizon. After the third and fourth rewards, the 15-box and 8-box cutoffs determine whether another
        search is worth its cost.
      </p>
    </section>

    <figure class="aa-project-figure">
      <img
        class="img-fluid"
        src="{{ page.image | relative_url }}"
        alt="Computed stopping cutoffs increasing with the number of rewards"
        loading="lazy"
      >
      <figcaption>
        Computed cutoffs over a wider parameter range. The near-linear pattern is empirical for these calculations; it is not a proved asymptotic
        law. Source: project report.
      </figcaption>
    </figure>

    <section id="result" class="aa-entry-section">
      <h2>Exact result and verification</h2>
      <p>
        Evaluating the recursion at the initial state gives
      </p>

$$
G(0,0;C=5,V=5,N=20)=7.6875644995.
$$

      <p>
        The derived cutoff policy was independently averaged over all \(15{,}504\) reward placements and produced the same expected gain. Agreement
        between exhaustive enumeration and the Bellman value verifies the implementation for the reported instance; the backward-induction
        proposition supplies the general optimality argument.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Scope and limitations</h2>
      <p>
        The proof relies on known \(N\), \(C\), and \(V\); uniformly random reward placement; exchangeable unopened boxes; unit opening cost; perfect
        observation; and a risk-neutral expected-gain objective. Unknown reward prevalence, non-exchangeable boxes, learning across rounds, discounting,
        or risk constraints would enlarge the state and change the Bellman equation. The observed cutoff trend does not establish convergence or
        linearity beyond the computed parameter range.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Report and code</h2>
      <nav class="aa-artifacts" aria-label="Sequential testing artifacts">
        <a href="{{ page.report_url | relative_url }}">Read the public report (PDF)</a>
        <a href="{{ page.code_url | relative_url }}">Download the memoised C++ implementation</a>
      </nav>
      <p class="aa-empty">The public PDF begins after the original identifying cover page. Its analysis, proof, algorithms, and appendices are unchanged.</p>
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
        <dd>\(N=20,\ C=5,\ V=5\)</dd>
      </div>
      <div>
        <dt>Completed</dt>
        <dd>{{ page.period }}</dd>
      </div>
      <div>
        <dt>Public output</dt>
        <dd>Technical record, report, code</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#game">Game</a>
      <a href="#heuristic">Initial rule</a>
      <a href="#state">Markov state</a>
      <a href="#bellman">Bellman value</a>
      <a href="#proof">Optimality proof</a>
      <a href="#policy">Policy</a>
      <a href="#result">Result</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Report and code</a>
    </nav>
  </aside>
</div>
