---
layout: page
title: Compact Medical Vision-Language Modelling
description: A Q-Former interface for compact medical image-caption modelling and related training experiments.
permalink: /research/medical-vlm/
research_area: Machine-learning systems
status: Completed internship
organisation: Mercity AI
collaborators: []
period: Apr–Aug 2025
featured: true
importance: 4
research_question: How can a compact visual-language interface connect a medical vision encoder to a frozen language model for caption generation?
summary: A Q-Former interface between medSigLIP and frozen Qwen-2.5-7B, with supervised and reward-based training experiments.
tags:
  - vision-language models
  - Q-Former
  - reward-based training
  - evaluation
synapse_repository_url: https://github.com/DudeDope/VisionLM-synapse
grpo_repository_url: https://github.com/DudeDope/VisionLM-GRPO
---

<header class="aa-entry-header">
  <div class="aa-entry-meta">
    <span class="aa-status">{{ page.status }}</span>
    <span>{{ page.period }}</span>
    <span>{{ page.organisation }}</span>
  </div>
  <p class="aa-entry-subtitle">
    This project connected medSigLIP to frozen Qwen-2.5-7B through a trainable Q-Former, compressing 256 visual tokens into 32 latent queries for
    medical caption generation. It also explored supervised and reward-based training for multimodal models.
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

    <section id="overview" class="aa-entry-section">
      <h2>Overview</h2>
      <p>
        During the internship, I worked on the Q-Former interface and on supervised and reward-based training experiments. The 256-to-32 reduction
        describes the architecture; it is not presented here as a measured memory, latency, calibration, or clinical-performance result.
      </p>
    </section>

    <section id="question" class="aa-entry-section">
      <h2>Research question</h2>
      <p>{{ page.research_question }}</p>
    </section>

    <section id="setup" class="aa-entry-section">
      <h2>Model and training setup</h2>
      <p>
        medSigLIP supplied visual features and Qwen-2.5-7B supplied the language model. A Q-Former compressed 256 image tokens into 32 latent queries,
        while the vision encoder and language model remained frozen in this setup.
      </p>
    </section>

    <section id="methods" class="aa-entry-section">
      <h2>Work explored</h2>
      <ul>
        <li>A Q-Former visual bottleneck and frozen-language-model caption generation.</li>
        <li>Supervised training and experiments with reward-based optimisation for multimodal models.</li>
        <li>Hugging Face trl, Accelerate, bitsandbytes, and PEFT workflows.</li>
        <li>Adaptation of language-model training workflows to multimodal inputs.</li>
      </ul>
    </section>

    <section id="evidence" class="aa-entry-section">
      <h2>Current public evidence</h2>
      <p>
        The public evidence supports the architectural description—256 visual tokens mapped to 32 latent queries—and documents related experimental
        code. It does not currently support a public quantitative claim about memory reduction, calibration, BLEU, perplexity, or clinical utility.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations</h2>
      <p>
        Token compression alone does not determine memory or latency savings. Caption metrics alone would not establish factual correctness or
        clinical reliability. Any quantitative comparison requires a named dataset and split, baseline, trainable components, hardware and precision,
        metric definition, and a recorded configuration.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Related public experiments</h2>
      <p>
        These repositories document related experiments, not interchangeable evidence for every internship result. VisionLM-synapse is a public
        medSigLIP/Qwen alignment variant using ROCO; VisionLM-GRPO explores SmolVLM2 on Path-VQA. Neither is labelled as a reproduction of an
        unlinked MIMIC experiment.
      </p>
      <nav class="aa-artifacts" aria-label="Related medical vision-language repositories">
        <a href="{{ page.synapse_repository_url }}">VisionLM-synapse code</a>
        <a href="{{ page.grpo_repository_url }}">VisionLM-GRPO code</a>
      </nav>
    </section>

  </div>

  <aside class="aa-entry-rail" aria-label="Research project metadata">
    <h2>Project</h2>
    <dl class="aa-fact-list">
      <div><dt>Status</dt><dd>{{ page.status }}</dd></div>
      <div><dt>Period</dt><dd>{{ page.period }}</dd></div>
      <div><dt>Organisation</dt><dd>{{ page.organisation }}</dd></div>
      <div><dt>Role</dt><dd>Machine Learning Research Intern</dd></div>
      <div><dt>Public output</dt><dd>Related experiment repositories</dd></div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#overview">Overview</a>
      <a href="#question">Question</a>
      <a href="#setup">Setup</a>
      <a href="#methods">Work explored</a>
      <a href="#evidence">Public evidence</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Related experiments</a>
    </nav>
  </aside>
</div>
