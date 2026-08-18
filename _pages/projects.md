---
layout: page
title: Projects
permalink: /projects/
description: Independent and supervised projects in statistical inference, probabilistic modelling, optimisation, and machine learning.
nav: true
nav_order: 3
---

<p class="aa-page-intro">
  Selected independent and supervised projects in statistical inference, probabilistic modelling, optimisation, and machine learning. Each record
  summarises the problem, methodology, current evidence, and limitations.
</p>

{% assign project_areas = "Statistical inference and probabilistic modelling|Optimisation and decision-making|Applied machine learning" | split: "|" %}
{% assign portfolio_projects = site.projects | where: "type", "project" | sort: "importance" %}

{% for area in project_areas %}
{% assign area_projects = portfolio_projects | where: "project_area", area %}
{% if area_projects.size > 0 %}

<section class="aa-section aa-index-group" aria-labelledby="{{ area | slugify }}">
<div class="aa-section-head">
<h2 id="{{ area | slugify }}">{{ area }}</h2>
{% case area %}
{% when "Statistical inference and probabilistic modelling" %}
<p>Estimation, shrinkage, dependence modelling, and uncertainty quantification.</p>
{% when "Optimisation and decision-making" %}
<p>Dynamic programming, optimal stopping, and computational decision methods.</p>
{% when "Applied machine learning" %}
<p>Predictive modelling, signal processing, calibration, and evaluation.</p>
{% endcase %}
</div>
<div class="aa-list">
{% for project in area_projects %}
<article class="aa-row">
<div class="aa-row-meta"><span class="aa-status">{{ project.status }}</span></div>
<div>
<h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
<p>{{ project.description }}</p>
{% if project.supervisor %}
<div class="aa-row-context">Supervised by {{ project.supervisor }}</div>
{% else %}
<div class="aa-row-context">{{ project.organisation }}</div>
{% endif %}
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
