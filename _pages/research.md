---
layout: page
title: Research
permalink: /research/
description: Research questions, methods, evidence, limitations, and release status across theoretical and applied work.
nav: true
nav_order: 2
---

<div class="aa-page-grid aa-index-intro">
  <p class="aa-page-intro">
    My research connects mathematical statistics and the analysis of learning algorithms with scientific modelling and sequential decisions. Each
    record states the question, methods, evidence, limitations, and public-artifact status. Work in progress is not presented as a publication.
  </p>
  <aside class="aa-index-legend" aria-label="Research record guide">
    <h2>Record guide</h2>
    <p><strong>Status</strong> describes the type of work, not publication status.</p>
    <p><strong>Artifacts</strong> are listed only after they are approved for public release.</p>
  </aside>
</div>

{% assign research_projects = site.research | sort: "importance" %}
{% assign research_areas = "Statistical learning and latent-variable models|Battery analytics and energy systems|Multimodal and medical machine learning" | split: "|" %}

{% for area in research_areas %}
{% assign area_projects = research_projects | where: "research_area", area %}
{% if area_projects.size > 0 %}

<section class="aa-section aa-index-group" aria-labelledby="{{ area | slugify }}">
<div class="aa-section-head">
<h2 id="{{ area | slugify }}">{{ area }}</h2>
{% case area %}
{% when "Statistical learning and latent-variable models" %}
<p>EM dynamics, fixed points, local contraction, mixture imbalance, and finite-sample questions.</p>
{% when "Battery analytics and energy systems" %}
<p>Degradation, survival analysis, probabilistic forecasting, and constrained market decisions.</p>
{% when "Multimodal and medical machine learning" %}
<p>Compact visual-language interfaces, reproducible training, preference optimisation, and evaluation.</p>
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
<p>{{ project.research_question }}</p>
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
<a class="aa-row-link" href="{{ project.url | relative_url }}">Record</a>
</article>
{% endfor %}
</div>
</section>
{% endif %}
{% endfor %}
