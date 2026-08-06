---
layout: page
title: About
permalink: /about/
description: Statistics, mathematical machine learning, and scientific decision systems.
nav: true
nav_order: 1
---

<div class="aa-page-grid">
  <div class="aa-prose">
    <p class="aa-lede">
      I am a Bachelor of Statistics student at the Indian Statistical Institute, Kolkata, with an expected graduation year of 2027. I work on
      problems that connect mathematical statistics, machine learning, and scientific decision-making.
    </p>

    <h2>Research trajectory</h2>

    <p>
      My theoretical work centres on the geometry and statistics of learning algorithms. With Prof. Xin Bing at the University of Toronto, I study
      population and sample expectation-maximisation for k-component Gaussian mixture-type models, including fixed points, local contraction,
      mixture imbalance, high-dimensional noise, and concentration-style control.
    </p>

    <p>
      Statistical decision theory, dependence modelling, and sequential decisions form a second thread. Projects on James–Stein shrinkage,
      bivariate copulas for extreme air-pollution episodes, and finite-horizon optimal stopping ask how structure and uncertainty should affect an
      estimator or action.
    </p>

    <p>
      Applied work at Ranial Systems brings these concerns to battery degradation, survival modelling, energy-market forecasting, and constrained
      dispatch. Earlier work at Mercity AI examined compact medical vision-language models, visual-token compression, supervised fine-tuning, and
      preference optimisation. Across these settings, I value explicit assumptions, reproducible evaluation, and appropriately limited claims.
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

<section class="aa-section" aria-labelledby="current-questions">
  <div class="aa-section-head">
    <h2 id="current-questions">Current questions</h2>
    <p>Questions I am actively studying or using to connect current work with longer-term research interests.</p>
  </div>
  <ol class="aa-question-list">
    <li>When do population and sample EM updates contract around the target parameter in k-component mixture models?</li>
    <li>How do mixture imbalance, nonconvex geometry, and high-dimensional noise affect the fixed-point landscape?</li>
    <li>How can shrinkage and empirical Bayes methods improve decisions under heterogeneous uncertainty?</li>
    <li>Which copula structures best represent extremal dependence without imposing parametric marginals?</li>
    <li>How should prediction uncertainty and degradation costs affect battery-market decisions?</li>
    <li>How can compact multimodal systems be compressed and evaluated without overstating what automatic metrics establish?</li>
  </ol>
</section>

<section class="aa-section" aria-labelledby="working-style">
  <div class="aa-section-head">
    <h2 id="working-style">Research practice</h2>
    <p>I aim for work whose assumptions, comparisons, numerical evidence, and limits can be inspected.</p>
  </div>
  <div class="aa-topic-list" aria-label="Research principles">
    {% for principle in site.data.profile.principles %}
      <span>{{ principle }}</span>
    {% endfor %}
  </div>
</section>
