---
layout: page
title: Variance-Based Audio Denoising via Amplitude Thresholding
description: Sliding-window variance, modal threshold selection, time-domain suppression, and FFT-based diagnostics.
permalink: /projects/audio-denoising/
type: project
project_area: Applied statistical learning
status: Supervised project
organisation: Indian Statistical Institute
supervisor: Dr. Arnab Chakraborty
period:
featured: false
importance: 4
tags:
  - signal processing
  - variance thresholding
  - audio denoising
  - R
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
    An R-based audio denoising study using short-window variance to choose an amplitude-suppression rule, with time-domain and frequency-domain
    diagnostics.
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
        The project asks whether locally quiet and active portions of an audio signal can be separated using an interpretable variance-derived
        threshold, then selectively suppressed or rescaled to reduce background noise.
      </p>
    </section>

    <section id="method" class="aa-entry-section">
      <h2>Method</h2>
      <ul>
        <li>Estimate local variance over windows of approximately 0.1 seconds.</li>
        <li>Bin variance values and use the modal region to construct a cutoff.</li>
        <li>Suppress or rescale amplitudes according to the derived rule.</li>
        <li>Implement the pipeline in R.</li>
        <li>Inspect waveforms and fast Fourier transform summaries before and after processing.</li>
      </ul>
    </section>

    <section id="evaluation" class="aa-entry-section">
      <h2>Evaluation</h2>
      <p>
        The method was explored on the audio samples described in the project report. Its main benefit is transparency: the threshold has a direct
        connection to the empirical distribution of local variance, and each processing step can be visualised.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations</h2>
      <p>
        A single modal cutoff can remove low-amplitude signal as well as noise, and FFT summaries do not alone measure perceptual quality.
        Reproducible evaluation should add signal-to-noise measures, listening tests, stronger filtering baselines, and a precise description of
        every audio source.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Artifacts</h2>
      <p class="aa-empty">The R implementation and example outputs will be linked when the repository is public.</p>
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
        <dt>Implementation</dt>
        <dd>R</dd>
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
      <a href="#evaluation">Evaluation</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
