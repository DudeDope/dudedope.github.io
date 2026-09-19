---
layout: page
title: Aditya Aryan
description: Aditya Aryan, B.Stat student at ISI Kolkata. Research, projects, and notes in theoretical and applied statistics and machine learning.
permalink: /
---

<div class="aa-home-grid">
  <div class="aa-home-intro">
    <p class="aa-home-identity">Theoretical and applied statistics and machine learning</p>
    <p class="aa-affiliation">Bachelor of Statistics student <span aria-hidden="true">·</span> Indian Statistical Institute, Kolkata</p>

    <p class="aa-lede">
      I am interested in the mathematical foundations of statistical and machine-learning methods, and in how these methods behave on data. I
      currently work with Prof. Xin Bing on population and sample EM for Gaussian mixture-type models.
    </p>

    <p class="aa-lede">
      My applied work includes statistical modelling and forecasting for energy systems at Ranial Systems, following an internship on medical
      vision-language models at Mercity AI. My projects explore estimation, dependence modelling, optimal stopping, and neural-network experiments.
    </p>

    <nav class="aa-actions" aria-label="Homepage shortcuts">
      <a href="{{ '/research/' | relative_url }}">Research</a>
      <a href="{{ '/projects/' | relative_url }}">Projects</a>
      <a href="{{ '/assets/rendercv/rendercv_output/Aditya_Aryan_CV.pdf' | relative_url }}">CV PDF</a>
      <a href="mailto:{{ site.data.socials.email }}">Email</a>
      <a href="https://github.com/{{ site.data.socials.github_username }}">GitHub</a>
    </nav>

  </div>

  <aside class="aa-academic-rail aa-contact-rail" aria-label="Contact and profile links">
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

<section class="aa-section" aria-labelledby="current-work">
  <div class="aa-section-head aa-section-head-compact">
    <h2 id="current-work">Current research and applied work</h2>
  </div>
  <div class="aa-list">
    <article class="aa-row">
      <div class="aa-row-meta"><span class="aa-status">In progress</span></div>
      <div>
        <h3><a href="{{ '/research/em-convergence/' | relative_url }}">EM Convergence in Gaussian Mixture-Type Models</a></h3>
        <p>Population and sample EM: fixed points, local contraction, and the effects of mixture imbalance and sampling error.</p>
        <div class="aa-row-context">University of Toronto · with Prof. Xin Bing · In progress</div>
      </div>
      <a class="aa-row-link" href="{{ '/research/em-convergence/' | relative_url }}">Research details</a>
    </article>

    <article class="aa-row">
      <div class="aa-row-meta"><span class="aa-status">In progress</span></div>
      <div>
        <h3>Statistical and Machine-Learning Methods for Energy Systems</h3>
        <p>
          Applied work on battery-health modelling and probabilistic forecasting, with separate evaluation of prediction, uncertainty, and
          operational decisions.
        </p>
        <div class="aa-row-context">Ranial Systems · Data Science Intern · In progress</div>
        <nav class="aa-inline-links" aria-label="Energy project details">
          <a href="{{ '/research/battery-life/' | relative_url }}">Battery-health project</a>
          <a href="{{ '/research/battery-dispatch/' | relative_url }}">Forecasting and market decisions</a>
        </nav>
      </div>
    </article>

  </div>
</section>

{% assign project_slugs = "sequential-testing|copula-air-pollution|nonlinear-mlp|biostat-policyopt" | split: "|" %}

<section class="aa-section" aria-labelledby="selected-projects">
  <div class="aa-section-head aa-section-head-compact">
    <h2 id="selected-projects">Selected projects</h2>
  </div>
  <div class="aa-list">
    {% for slug in project_slugs %}
      {% assign project = site.projects | where_exp: "item", "item.slug == slug" | first %}
      <article class="aa-row">
        <div class="aa-row-meta">{{ project.home_label }}</div>
        <div>
          <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
          <p>{{ project.home_summary | default: project.description }}</p>
          <div class="aa-row-context">{{ project.home_context }}</div>
        </div>
        <a class="aa-row-link" href="{{ project.url | relative_url }}">Project details</a>
      </article>
    {% endfor %}
  </div>
  <p class="aa-more-link"><a href="{{ '/projects/' | relative_url }}">All projects</a></p>
</section>

<section class="aa-section" aria-labelledby="selected-notes">
  <div class="aa-section-head">
    <h2 id="selected-notes">Selected notes</h2>
    <p>Expanded course notes with proofs and worked examples.</p>
  </div>
  <div class="aa-list">
    <article class="aa-row aa-row-simple">
      <div>
        <h3>
          <a href="{{ '/notes/parametric-inference/lecture-05-completeness-exponential-families-basu/' | relative_url }}"
            >Completeness, Exponential Families, and Basu’s Theorem</a
          >
        </h3>
      </div>
      <a class="aa-row-link" href="{{ '/notes/parametric-inference/lecture-05-completeness-exponential-families-basu/' | relative_url }}">Read</a>
    </article>
    <article class="aa-row aa-row-simple">
      <div>
        <h3>
          <a href="{{ '/notes/parametric-inference/lecture-08-bayesian-inference-bayes-risk/' | relative_url }}"
            >Bayesian Estimation and Minimax Risk</a
          >
        </h3>
      </div>
      <a class="aa-row-link" href="{{ '/notes/parametric-inference/lecture-08-bayesian-inference-bayes-risk/' | relative_url }}">Read</a>
    </article>
  </div>
  <p class="aa-more-link"><a href="{{ '/notes/' | relative_url }}">All course notes</a></p>
</section>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": {{ site.data.profile.name | jsonify }},
  "url": {{ page.url | absolute_url | jsonify }},
  "description": {{ page.description | jsonify }},
  "email": {{ site.data.socials.email | prepend: "mailto:" | jsonify }},
  "affiliation": { "@type": "CollegeOrUniversity", "name": "Indian Statistical Institute" },
  "sameAs": [
    "https://github.com/{{ site.data.socials.github_username }}",
    "https://www.linkedin.com/in/{{ site.data.socials.linkedin_username }}"
  ],
  "knowsAbout": {{ site.data.profile.research_interests | jsonify }}
}
</script>
