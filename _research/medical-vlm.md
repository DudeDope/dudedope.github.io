---
layout: page
title: Compact Medical Vision-Language Modelling
description: Visual-token compression, reproducible training, preference optimisation, and calibrated caption generation.
permalink: /research/medical-vlm/
research_area: Machine-learning systems
status: Completed internship
organisation: Mercity AI
collaborators: []
period: Apr–Aug 2025
featured: true
importance: 4
research_question: How can a compact visual-language interface reduce training memory while preserving useful caption-generation behaviour?
summary: Efficient multimodal learning through representation compression and targeted training.
tags:
  - vision-language models
  - Q-Former
  - preference optimisation
  - evaluation
paper_url:
code_url:
technical_note_url:
image:
---

<header class="aa-entry-header">
  <div class="aa-entry-meta">
    <span class="aa-status">{{ page.status }}</span>
    <span>{{ page.period }}</span>
    <span>{{ page.organisation }}</span>
  </div>
  <p class="aa-entry-subtitle">
    A medSigLIP-to-Qwen-2.5-7B pipeline using a Q-Former visual bottleneck, followed by supervised and preference-optimisation experiments for
    medical image caption generation.
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
      <strong>Scope.</strong> These were research experiments, not a clinical system. Automatic caption metrics do not establish diagnostic validity
      or fitness for patient care.
    </p>

    <section id="abstract" class="aa-entry-section">
      <h2>Abstract</h2>
      <p>
        The project connected a medical vision encoder to a frozen large language model through a trainable Q-Former. The bottleneck compressed image
        representations before caption generation, reducing the memory cost of the visual prefix while keeping the language model frozen.
      </p>
    </section>

    <section id="question" class="aa-entry-section">
      <h2>Research question</h2>
      <p>{{ page.research_question }}</p>
    </section>

    <section id="setup" class="aa-entry-section">
      <h2>Model and training setup</h2>
      <p>
        medSigLIP supplied visual features and Qwen-2.5-7B supplied the language model. A Q-Former compressed 256 image tokens into 32 latent queries.
        The Q-Former was trained with cross-entropy on MIMIC captions while the encoder and language model remained frozen.
      </p>
    </section>

    <section id="methods" class="aa-entry-section">
      <h2>Methods</h2>
      <ul>
        <li>Q-Former visual bottleneck and frozen-LLM caption generation.</li>
        <li>Supervised fine-tuning and experiments with PPO, DPO, and GRPO.</li>
        <li>Hugging Face trl, Accelerate, bitsandbytes, and PEFT workflows.</li>
        <li>Extension of a DeepSeek-R1 GRPO workflow to multimodal inputs.</li>
        <li>Reproducible configurations and metric-based comparisons.</li>
      </ul>
    </section>

    <section id="results" class="aa-entry-section">
      <h2>Reported results</h2>
      <ul>
        <li>8× visual-token compression, from 256 tokens to 32 latent queries.</li>
        <li>Approximately 70% memory reduction in the reported frozen-language-model setup.</li>
        <li>Probabilistic calibration was preserved in the reported caption-generation experiments.</li>
        <li>The multimodal GRPO experiments improved BLEU and reduced perplexity relative to their recorded comparisons.</li>
      </ul>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations</h2>
      <p>
        BLEU, perplexity, and calibration summaries do not establish factual correctness or clinical reliability. The results are specific to the
        recorded experimental setup and require task-specific error analysis, data-governance review, and stronger human evaluation before broader
        claims.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>References and artifacts</h2>
      <p class="aa-empty">Public code and write-ups will be linked later. No private data or model artifact is distributed from this site.</p>
    </section>

  </div>

  <aside class="aa-entry-rail" aria-label="Research record metadata">
    <h2>Record</h2>
    <dl class="aa-fact-list">
      <div>
        <dt>Status</dt>
        <dd>{{ page.status }}</dd>
      </div>
      <div>
        <dt>Period</dt>
        <dd>{{ page.period }}</dd>
      </div>
      <div>
        <dt>Organisation</dt>
        <dd>{{ page.organisation }}</dd>
      </div>
      <div>
        <dt>Role</dt>
        <dd>ML Research Intern</dd>
      </div>
      <div>
        <dt>Public output</dt>
        <dd>Not published</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#abstract">Abstract</a>
      <a href="#question">Question</a>
      <a href="#setup">Setup</a>
      <a href="#methods">Methods</a>
      <a href="#results">Results</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
