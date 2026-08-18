---
layout: page
title: "Nonlinear-MLP: Controlled Studies of Neural-Network Nonlinearity"
description: A reproducible PyTorch framework for testing how fixed, learned, removed, and structurally controlled nonlinearities affect neural-network accuracy and efficiency.
permalink: /projects/nonlinear-mlp/
type: project
project_area: Applied machine learning
status: Independent research software
organisation: Independent project
featured: true
importance: 2
tags:
  - neural networks
  - activation functions
  - ablation studies
  - efficiency
  - PyTorch
repository_url: https://github.com/DudeDope/Nonlinear-MLP
technical_note_url:
image:
---

<header class="aa-entry-header">
  <div class="aa-entry-meta">
    <span class="aa-status">{{ page.status }}</span>
    <span>{{ page.organisation }}</span>
  </div>
  <p class="aa-entry-subtitle">
    An experimentation and analysis toolkit for asking how much nonlinearity a neural network needs, where nonlinear units matter, and how predictive
    performance changes when nonlinear computation is reduced or learned.
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
      <strong>Evidence status.</strong> The public repository provides the experimental framework, controls, metrics, sweep scripts, and analysis
      pipeline. This record does not present a universal empirical conclusion: stable cross-seed and cross-architecture findings still require the
      planned experiments and final comparative report.
    </p>

    <section id="question" class="aa-entry-section">
      <h2>Research questions</h2>
      <ul>
        <li>How much nonlinear computation is necessary for useful predictive performance?</li>
        <li>Does the answer persist across MLPs, convolutional networks, residual-network heads, and tabular models?</li>
        <li>Which units or channels should remain nonlinear, and can that assignment be learned?</li>
        <li>How does reduced nonlinearity trade off against accuracy, calibration, latency, throughput, memory, and model size?</li>
      </ul>
    </section>

    <section id="design" class="aa-entry-section">
      <h2>Experimental design</h2>
      <p>The framework separates several interventions that can otherwise be conflated:</p>
      <ul>
        <li><strong>Fixed mixtures</strong> assign selected MLP units or convolutional channels to identity instead of ReLU.</li>
        <li><strong>Learned gates</strong> interpolate between identity and ReLU before a hardening step.</li>
        <li><strong>Deterministic zeroing</strong> removes a fixed fraction of unit outputs.</li>
        <li><strong>Structural controls</strong> reduce layer width to compare mixed activations with parameter-matched smaller networks.</li>
        <li><strong>Post-training analysis</strong> uses activation statistics to propose linearisation or pruning candidates.</li>
      </ul>
    </section>

    <section id="coverage" class="aa-entry-section">
      <h2>Models and datasets</h2>
      <p>
        The code supports MLP experiments on MNIST and tabular data, a nine-layer channel-controlled CNN for CIFAR-10, ResNet-18 heads for CIFAR-10
        and CIFAR-100, and an ImageNet head baseline. Sweep scripts cover fixed-ratio, learned-gating, deterministic-zeroing, structural-control, and
        post-training evaluation settings.
      </p>
    </section>

    <section id="measurement" class="aa-entry-section">
      <h2>Measurement and analysis</h2>
      <ul>
        <li>Accuracy, negative log likelihood, expected calibration error, and clean-versus-noisy evaluation.</li>
        <li>Parameter counts, approximate linear operations, latency, throughput, memory, and training-time summaries.</li>
        <li>Layerwise positive and negative activation fractions together with a score for how strongly ReLU changes preactivations.</li>
        <li>Run collection, checkpoint re-evaluation, merged analysis tables, Pareto plots, train–validation gaps, and gate-hardening comparisons.</li>
        <li>Reproducible configuration metadata and optional Weights & Biases logging.</li>
      </ul>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations and next checks</h2>
      <p>
        Apparent gains can depend on optimisation settings, random seeds, architecture, dataset difficulty, and whether controls truly match
        parameter count and computation. Approximate operation counts do not guarantee realised speedups on hardware. Final conclusions therefore
        require repeated seeds, consistent latency protocols, representative activation samples, robustness checks, and comparisons across the
        supported model families.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Public artifact</h2>
      <nav class="aa-artifacts" aria-label="Nonlinear-MLP artifacts">
        <a href="{{ page.repository_url }}">Code and experiment guide</a>
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
        <dt>Question</dt>
        <dd>How much nonlinearity is necessary?</dd>
      </div>
      <div>
        <dt>Implementation</dt>
        <dd>Python and PyTorch</dd>
      </div>
      <div>
        <dt>Coverage</dt>
        <dd>MLPs, CNNs, and residual-network heads</dd>
      </div>
      <div>
        <dt>Public output</dt>
        <dd>Code and experiment guide</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#question">Questions</a>
      <a href="#design">Experimental design</a>
      <a href="#coverage">Models and datasets</a>
      <a href="#measurement">Measurement</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Artifact</a>
    </nav>
  </aside>
</div>
