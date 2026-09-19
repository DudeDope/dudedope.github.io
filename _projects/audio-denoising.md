---
layout: page
title: Variance-Gated Suppression of Noise-Dominated Audio
description: An interpretable time-domain speech-pause detector developed after a frequency-domain separation attempt failed on real audio.
permalink: /projects/audio-denoising/
type: project
project_area: Applied statistics and signal processing
status: Supervised project
organisation: Indian Statistical Institute
supervisor: Dr. Arnab Chakraborty
period: November 2023
featured: false
importance: 6
math: true
tags:
  - signal processing
  - local variance
  - voice activity detection
  - R
repository_url:
report_url: /assets/pdf/projects/audio-denoising-public.pdf
code_url: /assets/code/projects/audio-variance-gate.R
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
    An interpretable signal-processing study that moved from an unsuccessful spectral filter to a local-variance rule for detecting and suppressing
    noise-dominated pauses.
  </p>
  <div class="aa-tags" aria-label="Topics">
    {% for tag in page.tags %}
      <span class="aa-tag">{{ tag }}</span>
    {% endfor %}
  </div>
</header>

<div class="aa-entry-layout">
  <div class="aa-entry-main">
    <section id="objective" class="aa-entry-section">
      <h2>Objective and scope</h2>
      <p>
        The input is a speech recording with mild, approximately stationary background noise. The intended operation is deliberately narrower than
        general source separation: detect intervals dominated by background noise during speech pauses, suppress those intervals, and preserve
        clearly active speech.
      </p>
      <p>
        This distinction matters. The method can act as a transparent voice-activity gate, but it cannot remove noise whose frequency and time support
        overlap active speech.
      </p>
    </section>

    <section id="spectral" class="aa-entry-section">
      <h2>The frequency-domain attempt</h2>
      <p>
        The first approach used the discrete Fourier transform. On a synthetic signal made from three sinusoids plus random noise, the power spectrum
        exposed three dominant frequency peaks, so frequency selection appeared promising.
      </p>
      <p>
        Real speech broke that assumption. Speech is broadband and time-varying, while ordinary background noise can occupy the same frequencies. The
        observed power spectrum contained many overlapping peaks rather than a clean separation. A fixed spectral cutoff would therefore remove useful
        speech components together with noise. This negative result motivated a statistic localised in time.
      </p>
    </section>

    <section id="statistic" class="aa-entry-section">
      <h2>Local variance as an activity statistic</h2>
      <p>
        Let \(a_1,\ldots,a_T\) be the waveform amplitudes sampled at rate \(f_s\). The implementation uses windows of roughly \(0.1\) seconds,
        \(m=\lfloor f_s/10\rfloor-1\) samples, with starting points separated by 1,000 samples. For window \(W_j\), it computes
      </p>

$$
v_j
=\frac{1}{m-1}\sum_{t\in W_j}\left(a_t-\bar a_j\right)^2.
$$

      <p>
        At \(f_s=44.1\) kHz, each window contains approximately 4,410 samples. Voice-active windows tend to have larger amplitude variation than
        noise-only pauses, making \(v_j\) a simple, interpretable activity score.
      </p>
    </section>

    <figure class="aa-project-figure">
      <img
        class="img-fluid"
        src="{{ page.image | relative_url }}"
        alt="Audio waveform and sliding-window variance increasing over voice-active intervals"
        loading="lazy"
      >
      <figcaption>Waveform amplitude and the sliding-window variance signal used by the gate. Source: project report.</figcaption>
    </figure>

    <section id="threshold" class="aa-entry-section">
      <h2>Data-derived threshold</h2>
      <p>The window variances are linearly rescaled to \([0,1000]\):</p>

$$
z_j
=1000\,
\frac{v_j-\min_k v_k}{\max_k v_k-\min_k v_k}.
$$

      <p>
        The \(z_j\) values are placed into bins of width 25. If \(b^\star\) is the modal bin, the cutoff is set immediately above it,
        \(c=25(b^\star+1)+1\). The modal region is treated as the recording's prevailing low-variance background regime, so the threshold adapts to
        the observed clip instead of being chosen as a fixed amplitude.
      </p>
    </section>

    <section id="algorithm" class="aa-entry-section">
      <h2>Suppression rule</h2>
      <p>For each overlapping window, the documented algorithm applies</p>

$$
\widetilde a_t=
\begin{cases}
0, & z_j<c,\\[3pt]
\frac{1}{2}a_t, & c\leq z_j<1.5c,\\[3pt]
a_t, & z_j\geq1.5c,
\end{cases}
\qquad t\in W_j.
$$

      <p>
        The middle band softens the transition between silence and active speech. Because windows overlap, a sample may be visited more than once:
        any low-variance visit can zero it, while repeated transition-band visits can attenuate it repeatedly. That behaviour is part of the
        reported implementation and is important when interpreting the output.
      </p>
      <ol>
        <li>Read a WAV file and extract the waveform and sampling rate.</li>
        <li>Compute local variance over overlapping 0.1-second windows.</li>
        <li>Scale the variances and estimate the modal-bin cutoff.</li>
        <li>Zero low-variance windows and attenuate the transition band.</li>
        <li>Write the processed amplitudes back to a WAV file.</li>
      </ol>
    </section>

    <figure class="aa-project-figure">
      <img
        class="img-fluid"
        src="{{ page.output_image | relative_url }}"
        alt="Processed speech waveform with pause intervals suppressed near zero amplitude"
        loading="lazy"
      >
      <figcaption>Processed waveform after local-variance suppression and transition-band attenuation. Source: project report.</figcaption>
    </figure>

    <section id="evaluation" class="aa-entry-section">
      <h2>What the experiments establish</h2>
      <p>
        The rule was applied to a primary recording and two additional clips: one with two speakers and one with few clear silence periods. The report
        compares original waveforms, local-variance traces, scaled variance distributions, and processed waveforms. These plots show that the
        algorithm identifies many visibly quiet intervals and makes its decisions traceable to a single statistic.
      </p>
      <p>
        The evidence is qualitative rather than comparative. There is no clean reference signal, signal-to-noise improvement, perceptual score,
        intelligibility test, listening study, or baseline such as spectral subtraction. The experiment therefore demonstrates algorithmic behaviour,
        not superior perceptual denoising.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Failure modes and extensions</h2>
      <ul>
        <li>Noise present during active speech is retained because high-variance windows are preserved.</li>
        <li>Quiet phonemes, breaths, or distant speech may be mistaken for background noise.</li>
        <li>A dominant high-variance noise process can invalidate the modal-bin interpretation.</li>
        <li>Min–max scaling is undefined for constant local variance and sensitive to extreme windows.</li>
        <li>Sequential updates over overlapping windows make attenuation depend on window overlap and processing order.</li>
      </ul>
      <p>
        A stronger extension would aggregate window-level masks before altering samples, smooth the mask in time, compare robust activity statistics,
        and evaluate against labelled voice activity or paired clean/noisy audio.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Report and code</h2>
      <nav class="aa-artifacts" aria-label="Audio variance-gating artifacts">
        <a href="{{ page.report_url | relative_url }}">Read the public report (PDF)</a>
        <a href="{{ page.code_url | relative_url }}">Download the cleaned R implementation</a>
      </nav>
      <p class="aa-empty">
        The public PDF begins after the original identifying cover page. The R file is a cleaned transcription of the documented main algorithm;
        audio samples are not redistributed.
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
        <dt>Public output</dt>
        <dd>Technical record, report, code</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#objective">Objective</a>
      <a href="#spectral">Spectral attempt</a>
      <a href="#statistic">Activity statistic</a>
      <a href="#threshold">Threshold</a>
      <a href="#algorithm">Algorithm</a>
      <a href="#evaluation">Evaluation</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Report and code</a>
    </nav>
  </aside>
</div>
