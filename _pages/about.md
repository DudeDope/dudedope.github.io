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
      I am a Bachelor of Statistics student at the Indian Statistical Institute, Kolkata, with an expected graduation year of 2027. I am interested
      in mathematical statistics, probabilistic modelling, machine learning, and optimisation.
    </p>

    <h2>Interests and experience</h2>

    <p>
      My interests centre on methods for learning and decision-making under uncertainty. I am particularly drawn to problems where statistical
      structure, predictive models, and optimisation must work together.
    </p>

    <p>
      My current academic research examines the behaviour of expectation-maximisation algorithms for latent-variable models. My applied experience
      includes battery degradation and survival modelling, machine-learning and deep-learning methods for anomaly detection, probabilistic
      forecasting, stochastic price modelling, bidding optimisation, and efficient multimodal learning.
    </p>

    <p>
      I have worked across academic and industry settings at the University of Toronto, Ranial Systems, and Mercity AI. Although these projects
      arise in different application areas, they share a common emphasis on uncertainty, reliable modelling, careful evaluation, and data-informed
      decisions.
    </p>

    <p>
      I value explicit assumptions, reproducible analysis, well-chosen comparisons, and conclusions that reflect the strength of the available
      evidence.
    </p>

  </div>

  <aside class="aa-academic-rail aa-profile-rail" aria-label="Profile facts">
    <h2>Profile</h2>
    <dl class="aa-fact-list">
      <div>
        <dt>Institution</dt>
        <dd>Indian Statistical Institute, Kolkata</dd>
      </div>
      <div>
        <dt>Programme</dt>
        <dd>B.Stat (Hons.), expected 2027</dd>
      </div>
      <div>
        <dt>Current roles</dt>
        <dd>Student Researcher, University of Toronto<br />Data Science Intern, Ranial Systems</dd>
      </div>
      <div>
        <dt>Previously</dt>
        <dd>ML Research Intern, Mercity AI</dd>
      </div>
      <div>
        <dt>Contact</dt>
        <dd><a href="mailto:{{ site.data.socials.email }}">{{ site.data.socials.email }}</a></dd>
      </div>
    </dl>
    <nav class="aa-rail-nav" aria-label="Profile links">
      <a href="https://github.com/{{ site.data.socials.github_username }}">GitHub</a>
      <a href="https://www.linkedin.com/in/{{ site.data.socials.linkedin_username }}">LinkedIn</a>
      <a href="{{ '/assets/rendercv/rendercv_output/Aditya_Aryan_CV.pdf' | relative_url }}">CV PDF</a>
    </nav>
  </aside>
</div>

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
