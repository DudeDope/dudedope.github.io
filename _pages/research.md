---
layout: page
title: Research
permalink: /research/
description: Research and technical work in statistical learning, probabilistic modelling, machine learning, and optimisation.
nav: true
nav_order: 2
---

<div class="aa-page-grid aa-index-intro">
  <p class="aa-page-intro">
    This page presents current and completed research experience across statistical learning, probabilistic modelling, machine learning, and
    optimisation. Each record describes the problem, methodology, contributions, and limitations of the work.
  </p>
  <aside class="aa-index-legend" aria-label="Research record guide">
    <h2>Record guide</h2>
    <p><strong>Status</strong> describes the type of work, not publication status.</p>
    <p><strong>Artifacts</strong> are listed only after they are approved for public release.</p>
  </aside>
</div>

{% assign research_projects = site.research | sort: "importance" %}
{% assign research_areas = "Statistical learning and inference|Probabilistic modelling and decision-making|Machine-learning systems" | split: "|" %}

{% for area in research_areas %}
{% assign area_projects = research_projects | where: "research_area", area %}
{% if area_projects.size > 0 %}

<section class="aa-section aa-index-group" aria-labelledby="{{ area | slugify }}">
<div class="aa-section-head">
<h2 id="{{ area | slugify }}">{{ area }}</h2>
{% case area %}
{% when "Statistical learning and inference" %}
<p>Theoretical and computational questions in estimation, latent-variable models, and finite-sample behaviour.</p>
{% when "Probabilistic modelling and decision-making" %}
<p>Forecasting, uncertainty quantification, anomaly detection, and optimisation for sequential and market decisions.</p>
{% when "Machine-learning systems" %}
<p>Efficient representation learning, multimodal modelling, training methods, and evaluation.</p>
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
<a class="aa-row-link" href="{{ project.url | relative_url }}">Record</a>
</article>
{% endfor %}
</div>
</section>
{% endif %}
{% endfor %}

<section class="aa-section" aria-labelledby="publication-status">
  <div class="aa-section-head">
    <h2 id="publication-status">Publication status</h2>
    <p>No publications or public manuscripts at present. Public research outputs will be listed here when they become available.</p>
  </div>
</section>
