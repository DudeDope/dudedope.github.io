---
layout: page
title: About
permalink: /about/
description: Mathematical statistics, probabilistic modelling, machine learning, and optimisation under uncertainty.
nav: true
nav_order: 1
---

<div class="aa-page-grid">
  <div class="aa-prose">
    <p class="aa-lede">
      I am a Bachelor of Statistics student at the Indian Statistical Institute, Kolkata, graduating in 2027. I work across statistical inference,
      probabilistic modelling, machine learning, and optimisation, with a broader interest in reliable learning and decision-making under
      uncertainty.
    </p>

    <h2>Interests and experience</h2>

    <p>
      My interests centre on methods for learning and decision-making under uncertainty. I am particularly drawn to problems where statistical
      structure, predictive models, and optimisation must work together.
    </p>

    <p>
      At the University of Toronto, my current academic research examines statistical learning for latent-variable models. At Ranial Systems, I work
      on probabilistic modelling, forecasting, anomaly detection, and optimisation for energy systems, alongside battery degradation and survival
      modelling. Earlier, at Mercity AI, I worked on efficient multimodal learning for medical AI.
    </p>

    <p>
      Although these projects arise in different application areas, they share a common emphasis on uncertainty, reliable modelling, careful
      evaluation, and data-informed decisions.
    </p>

    <p>
      I value explicit assumptions, reproducible analysis, well-chosen comparisons, and conclusions that reflect the strength of the available
      evidence.
    </p>

  </div>

  <aside class="aa-academic-rail aa-profile-rail aa-contact-rail" aria-label="Contact and profile links">
    <h2>Contact</h2>
    <a class="aa-contact-email" href="mailto:{{ site.data.socials.email }}">{{ site.data.socials.email }}</a>
    <nav class="aa-contact-links" aria-label="Profile and document links">
      <a
        class="aa-social-link"
        href="https://github.com/{{ site.data.socials.github_username }}"
        aria-label="GitHub profile"
        title="GitHub"
        rel="me"
      >
        <i class="fa-brands fa-github" aria-hidden="true"></i>
      </a>
      <a
        class="aa-social-link"
        href="https://www.linkedin.com/in/{{ site.data.socials.linkedin_username }}"
        aria-label="LinkedIn profile"
        title="LinkedIn"
        rel="me"
      >
        <i class="fa-brands fa-linkedin" aria-hidden="true"></i>
      </a>
      <a class="aa-cv-link" href="{{ '/assets/rendercv/rendercv_output/Aditya_Aryan_CV.pdf' | relative_url }}">CV PDF</a>
    </nav>
  </aside>
</div>

<section class="aa-section" aria-labelledby="academic-highlights">
  <div class="aa-section-head">
    <h2 id="academic-highlights">Academic highlights</h2>
    <p>Selected distinctions in mathematics, science, and national entrance examinations.</p>
  </div>
  <div class="aa-list">
    <article class="aa-row">
      <div class="aa-row-meta">2023</div>
      <div>
        <h3>University entrance examinations</h3>
        <p>All India Rank 90 in the Indian Statistical Institute entrance examination; 98.9 percentile in JEE Main; 331/390 in BITSAT.</p>
      </div>
    </article>
    <article class="aa-row">
      <div class="aa-row-meta">2022</div>
      <div>
        <h3>Mathematics and science</h3>
        <p>Indian National Mathematical Olympiad merit list; Karnataka top 20 in IOQM; All India Rank 1,034 in KVPY (SA stream).</p>
      </div>
    </article>
    <article class="aa-row">
      <div class="aa-row-meta">2021</div>
      <div>
        <h3>National Talent Search Examination</h3>
        <p>National scholarship as a top-1,000 candidate among approximately two million students; Stage I Rank 72.</p>
      </div>
    </article>
  </div>
</section>

<section class="aa-section" aria-labelledby="areas-of-interest">
  <div class="aa-section-head">
    <h2 id="areas-of-interest">Areas of interest</h2>
    <p>Broad methodological directions connecting my current research, technical projects, and industry experience.</p>
  </div>
  <ul class="aa-question-list">
    <li>Statistical learning and inference for complex and latent-variable models.</li>
    <li>Probabilistic modelling of dependent, high-dimensional, and time-varying data.</li>
    <li>Machine-learning methods for forecasting, anomaly detection, and representation learning.</li>
    <li>Optimisation and sequential decision-making under uncertainty.</li>
  </ul>
</section>

<section class="aa-section" aria-labelledby="working-style">
  <div class="aa-section-head">
    <h2 id="working-style">Research practice</h2>
    <p>I value explicit assumptions, reproducible analysis, well-chosen baselines, and conclusions supported by the available evidence.</p>
  </div>
  <div class="aa-topic-list" aria-label="Research principles">
    {% for principle in site.data.profile.principles %}
      <span>{{ principle }}</span>
    {% endfor %}
  </div>
</section>
