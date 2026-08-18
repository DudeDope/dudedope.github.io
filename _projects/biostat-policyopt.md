---
layout: page
title: "BioStat-PO: Policy Selection for Causal Survival Analysis"
description: An integrated Python–R research framework for selecting causal RMST analysis pipelines under missingness, censoring, and statistical-validity constraints.
permalink: /projects/biostat-policyopt/
type: project
project_area: Statistical inference and probabilistic modelling
status: Independent research software
organisation: Independent project
featured: true
importance: 1
tags:
  - causal inference
  - survival analysis
  - missing data
  - simulation studies
  - policy optimisation
repository_url: https://github.com/DudeDope/biostat-policyopt
benchmark_repository_url: https://github.com/DudeDope/biostat-simbench
notebook_url: https://colab.research.google.com/github/DudeDope/biostat-policyopt/blob/main/notebooks/biostat_po_all_experiments_colab.ipynb
technical_note_url: https://github.com/DudeDope/biostat-policyopt/blob/main/docs/RESEARCH_PROSPECTUS.md
image:
---

<header class="aa-entry-header">
  <div class="aa-entry-meta">
    <span class="aa-status">{{ page.status }}</span>
    <span>{{ page.organisation }}</span>
  </div>
  <p class="aa-entry-subtitle">
    A paired Python and R system for studying how a policy can select among causal survival-analysis pipelines while accounting for missing
    covariates, censoring, inferential validity, failures, and computational cost.
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
      <strong>Current scope.</strong> This is public research software under active development. The repositories contain implemented simulation,
      estimation, policy, testing, and evaluation components, but do not claim a trained final model, a completed confirmatory benchmark, a
      convergence theorem, or performance on real biomedical data. The current benchmark uses synthetic data only.
    </p>

    <section id="problem" class="aa-entry-section">
      <h2>Problem</h2>
      <p>
        Estimating a causal difference in restricted mean survival time can require choices about adjustment, missing-data handling, censoring,
        interval construction, and computational budget. A method that works well under one data-generating process may have poor bias, coverage,
        stability, or failure behaviour under another. BioStat-PO treats analysis-pipeline selection as a constrained decision problem rather than
        assuming that one procedure is uniformly best.
      </p>
    </section>

    <section id="architecture" class="aa-entry-section">
      <h2>Two-repository architecture</h2>
      <ul>
        <li>
          <strong>biostat-simbench (R)</strong> owns synthetic data-generating processes, causal RMST estimators, bootstrap inference, calibration,
          and repeated-sampling evaluation.
        </li>
        <li>
          <strong>biostat-policyopt (Python)</strong> owns structured actions, observable task representations, baseline policies, constraint-aware
          rewards, sequential allocation, training interfaces, and held-out policy evaluation.
        </li>
        <li>A versioned JSON contract separates statistical computation from policy learning, while cached reward tables keep large R simulations outside GPU training loops.</li>
      </ul>
    </section>

    <section id="statistical-benchmark" class="aa-entry-section">
      <h2>Statistical benchmark</h2>
      <p>
        The R environment generates Weibull proportional-hazards studies with observed confounding, binary treatment, right censoring,
        administrative truncation, and missing-at-random baseline covariates. Implemented analysis templates include unadjusted and weighted
        Kaplan–Meier procedures, complete-case and median-imputed workflows, Cox standardisation, substantive-model-compatible multiple imputation,
        and doubly robust adjusted-RMST estimation.
      </p>
      <p>
        Candidate pipelines are compared using bias, root mean squared error, confidence-interval coverage, interval-production and outer-pipeline
        failures, Monte Carlo uncertainty, and computational cost. Selection and evaluation replicates are separated to reduce reuse of the same
        simulation noise.
      </p>
    </section>

    <section id="policy-system" class="aa-entry-section">
      <h2>Policy system</h2>
      <p>
        The Python repository implements a strict action parser and task representation together with random, rule-based, and multinomial-classifier
        baselines. It also contains group-relative advantages, fixed constraint multipliers with an offline update, a sequential ranking and
        elimination prototype, dependency-gated supervised and GRPO/DAPO trainer factories, policy-stability diagnostics, and paired held-out
        evaluation utilities.
      </p>
    </section>

    <section id="evaluation" class="aa-entry-section">
      <h2>Evaluation design</h2>
      <ul>
        <li>Independent outer-replicate halves for oracle selection and reward evaluation.</li>
        <li>Coverage, type-I-error, failure, and interval-production constraints with explicit denominators.</li>
        <li>Paired data-generating-process comparisons, Monte Carlo standard errors, and sample-size planning.</li>
        <li>Held-out policy evaluation using a paired data-generating-process cluster bootstrap.</li>
        <li>Repeated observable contexts to detect policies that react to diagnostic noise rather than stable scenario structure.</li>
      </ul>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Current limitations</h2>
      <p>
        The expensive confirmatory simulation catalogue and full calibration of several advanced estimator arms remain unfinished. The framework
        does not yet cover MNAR missingness, competing risks, recurrent events, time-varying treatment, or arbitrary model-generated analysis code.
        Software tests and small smoke runs establish implementation behaviour, not scientific superiority of a learned policy.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Public artifacts</h2>
      <nav class="aa-artifacts" aria-label="BioStat-PO artifacts">
        <a href="{{ page.repository_url }}">Python policy repository</a>
        <a href="{{ page.benchmark_repository_url }}">R simulation repository</a>
        <a href="{{ page.notebook_url }}">Colab experiment runner</a>
        <a href="{{ page.technical_note_url }}">Research prospectus</a>
      </nav>
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
        <dt>Scope</dt>
        <dd>Causal RMST pipeline selection</dd>
      </div>
      <div>
        <dt>Implementation</dt>
        <dd>Python and R</dd>
      </div>
      <div>
        <dt>Data</dt>
        <dd>Synthetic simulation studies</dd>
      </div>
      <div>
        <dt>Public output</dt>
        <dd>Code, protocols, tests, and notebooks</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#problem">Problem</a>
      <a href="#architecture">Architecture</a>
      <a href="#statistical-benchmark">Statistical benchmark</a>
      <a href="#policy-system">Policy system</a>
      <a href="#evaluation">Evaluation</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
