---
layout: page
title: Research
permalink: /research/
description: Theoretical and applied work in statistics and machine learning.
nav: true
nav_order: 1
---

<div class="aa-page-grid aa-index-intro">
  <div>
    <p class="aa-page-intro">
      My research interests connect the mathematical analysis of statistical and machine-learning methods with their behaviour on data. I currently
      study population and sample EM with Prof. Xin Bing and work on statistical modelling and forecasting at Ranial Systems. My previous internship
      explored compact medical vision-language models.
    </p>
    <p class="aa-page-intro aa-page-intro-secondary">
      My interests span theoretical and applied statistics and machine learning. I am particularly interested in estimation, the behaviour of
      learning algorithms, and the relationship between model assumptions and empirical performance. My current work includes EM convergence and
      statistical modelling for energy systems; my independent projects explore analysis-pipeline selection and neural-network nonlinearity.
    </p>
  </div>
  <aside class="aa-index-legend" aria-label="Research status note">
    <h2>Status</h2>
    <p>Status labels distinguish ongoing work, completed projects, and available public artifacts.</p>
  </aside>
</div>

{% assign research_projects = site.research | sort: "importance" %}
{% assign research_areas = "Statistical learning and inference|Probabilistic modelling and decision-making|Machine-learning systems" | split: "|" %}

{% for area in research_areas %}
{% assign area_projects = research_projects | where: "research_area", area %}
{% if area_projects.size > 0 %}

<section class="aa-section aa-index-group" aria-labelledby="{{ area | slugify }}">
<div class="aa-section-head aa-section-head-compact">
{% case area %}
{% when "Statistical learning and inference" %}
<h2 id="{{ area | slugify }}">Academic research</h2>
{% when "Probabilistic modelling and decision-making" %}
<h2 id="{{ area | slugify }}">Industry projects</h2>
{% when "Machine-learning systems" %}
<h2 id="{{ area | slugify }}">Previous ML research internship</h2>
{% endcase %}
</div>
<div class="aa-list">
{% for project in area_projects %}
<article class="aa-row">
<div class="aa-row-meta">
<span class="aa-status">{{ project.status }}</span>
<div>{{ project.period }}</div>
</div>
<div>
<h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
<p>{{ project.summary | default: project.description }}</p>
<div class="aa-row-context">
{{ project.organisation }}
{% if project.collaborators.size > 0 %}
· with {{ project.collaborators | join: ", " }}
{% endif %}
</div>
<div class="aa-tags" aria-label="Topics">
{% for tag in project.tags limit: 4 %}
<span class="aa-tag">{{ tag }}</span>
{% endfor %}
</div>
</div>
<a class="aa-row-link" href="{{ project.url | relative_url }}">Project details</a>
</article>
{% endfor %}
</div>
</section>
{% endif %}
{% endfor %}

<section id="publications" class="aa-section" aria-labelledby="publication-status">
  <div class="aa-section-head">
    <h2 id="publication-status">Publications</h2>
    <p>No publications or public manuscripts are currently listed. Research summaries and available project artifacts are linked above.</p>
  </div>
</section>
