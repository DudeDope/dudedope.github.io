---
layout: page
title: Projects
permalink: /projects/
description: Supervised technical work in statistical methodology, algorithms, signal processing, and applied statistical learning.
nav: true
nav_order: 4
---

<div class="aa-page-grid aa-index-intro">
  <p class="aa-page-intro">
    These are supervised technical studies rather than formal publications. Each record identifies the problem, method, reported result, and
    limitations. Repository and note links will be added when the supporting material is ready for public release.
  </p>
  <aside class="aa-index-legend" aria-label="Project record guide">
    <h2>Coverage</h2>
    <p>Five projects · four supervisors listed by name · no publication claims.</p>
    <p>Numerical results are those reported in the reviewed CV.</p>
  </aside>
</div>

{% assign project_areas = "Statistical methodology|Optimisation and algorithms|Applied statistical learning" | split: "|" %}
{% assign portfolio_projects = site.projects | where: "type", "project" | sort: "importance" %}

{% for area in project_areas %}
{% assign area_projects = portfolio_projects | where: "project_area", area %}
{% if area_projects.size > 0 %}

<section class="aa-section aa-index-group" aria-labelledby="{{ area | slugify }}">
<div class="aa-section-head">
<h2 id="{{ area | slugify }}">{{ area }}</h2>
{% case area %}
{% when "Statistical methodology" %}
<p>Risk, shrinkage, empirical Bayes reasoning, copulas, and extremal dependence.</p>
{% when "Optimisation and algorithms" %}
<p>Finite-horizon decisions, Bellman recursions, memoisation, and stopping rules.</p>
{% when "Applied statistical learning" %}
<p>Signal processing, probability calibration, chronological evaluation, and retrospective simulation.</p>
{% endcase %}
</div>
<div class="aa-list">
{% for project in area_projects %}
<article class="aa-row">
<div class="aa-row-meta"><span class="aa-status">{{ project.status }}</span></div>
<div>
<h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
<p>{{ project.description }}</p>
<div class="aa-row-context">Supervised by {{ project.supervisor }}</div>
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
