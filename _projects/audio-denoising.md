---
layout: page
title: Variance-Based Audio Denoising via Amplitude Thresholding
description: Sliding-window variance, modal threshold selection, time-domain suppression, and FFT-based diagnostics.
permalink: /projects/audio-denoising/
type: project
project_area: Applied machine learning
status: Supervised project
organisation: Indian Statistical Institute
supervisor: Dr. Arnab Chakraborty
period: November 2023
featured: false
importance: 6
tags:
  - signal processing
  - variance thresholding
  - audio denoising
  - R
repository_url:
image: /assets/img/projects/audio/amplitude-variance.png
output_image: /assets/img/projects/audio/denoised-waveform.png
---

<header class="aa-entry-header">
  <div class="aa-entry-meta">
    <span class="aa-status">{{ page.status }}</span>
    <span>{{ page.organisation }}</span>
    <span>with {{ page.supervisor }}</span>
  </div>
  <p class="aa-entry-subtitle">
    An interpretable R-based speech-pause detector that grew from an unsuccessful frequency-domain approach into a local-variance gating rule.
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
        The project considers speech recorded with mild, approximately steady background noise. Its practical target is narrower than general audio
        denoising: identify intervals dominated by background noise during pauses, then suppress those intervals without erasing clearly active
        speech.
      </p>
    </section>

    <section id="initial" class="aa-entry-section">
      <h2>Why the first approach failed</h2>
      <p>
        The initial idea used the fast Fourier transform to isolate stable frequencies. It worked on a synthetic mixture of three sinusoids and
        random noise, but real speech produced many overlapping spectral peaks. Because speech and background noise occupied overlapping frequency
        ranges, a simple frequency cutoff could not separate them reliably. That failure motivated a return to the time domain.
      </p>
    </section>

    <section id="method" class="aa-entry-section">
      <h2>Variance-gating method</h2>
      <p>
        Voice-active windows showed larger amplitude variation than noise-only pauses. The implementation therefore estimates local variance and
        derives its threshold from the empirical variance distribution rather than choosing one by hand.
      </p>
      <ul>
        <li>Read the waveform amplitudes in R and use windows of approximately 0.1 seconds—4,410 samples at 44.1 kHz—with a 1,000-sample step.</li>
        <li>Linearly scale the window variances, divide them into 40 bins of width 25, and place the cutoff just above the modal bin.</li>
        <li>Set amplitudes to zero for windows below the cutoff.</li>
        <li>Halve amplitudes in the transition band from the cutoff to 1.5 times the cutoff, cushioning the boundary between pauses and speech.</li>
      </ul>
    </section>

    <figure>
      <img
        class="img-fluid rounded"
        src="{{ page.image | relative_url }}"
        alt="Audio waveform with a local variance trace rising during voice-active intervals"
        loading="lazy"
      >
      <figcaption>Audio amplitude and the sliding-window variance signal used by the gating rule. Source: project report.</figcaption>
    </figure>

    <section id="evaluation" class="aa-entry-section">
      <h2>Evaluation</h2>
      <p>
        The report applies the rule to a primary clip and two additional samples, including a two-speaker recording and a clip with few clear silence
        periods. Evaluation is qualitative, using the original waveform, variance trace, scaled variance distribution, and processed waveform.
        The strongest evidence is interpretability: every suppressed interval is traceable to the observed local-variance threshold.
      </p>
    </section>

    <figure>
      <img
        class="img-fluid rounded"
        src="{{ page.output_image | relative_url }}"
        alt="Processed speech waveform with noise-dominated pause intervals suppressed near zero amplitude"
        loading="lazy"
      >
      <figcaption>Processed waveform after variance-based suppression and transition-band scaling. Source: project report.</figcaption>
    </figure>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations</h2>
      <p>
        The method suppresses noise mainly when speech is absent; it does not separate overlapping speech and noise. A single modal cutoff can erase
        weak phonemes, breaths, or low-amplitude speech, and it relies on relatively steady, mild background noise. The report does not include
        signal-to-noise improvement, intelligibility metrics, listening tests, or modern denoising baselines, so the figures demonstrate algorithmic
        behaviour rather than perceptual superiority.
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
      <p class="aa-empty">
        The audio samples and standalone implementation will be linked only if their redistribution status and collaborator permissions are
        confirmed.
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
        <dt>Implementation</dt>
        <dd>R</dd>
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
      <a href="#initial">Initial approach</a>
      <a href="#method">Method</a>
      <a href="#evaluation">Evaluation</a>
      <a href="#limitations">Limitations</a>
      <a href="#team">Team</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
