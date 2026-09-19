---
layout: page
title: Projects
permalink: /projects/
description: Independent and supervised projects in theoretical and applied statistics and machine learning.
nav: true
nav_order: 2
---

<p class="aa-page-intro">
  Independent and supervised projects in theoretical and applied statistics and machine learning. The pages combine mathematical formulation,
  implementation, and evaluation, with ongoing work labelled separately from completed projects.
</p>

{% assign project_slugs = "sequential-testing|stein-shrinkage|copula-air-pollution|nonlinear-mlp|biostat-policyopt|football-probability" | split: "|" %}

<section class="aa-section aa-index-group" aria-labelledby="project-list">
  <div class="aa-section-head aa-section-head-compact">
    <h2 id="project-list">Selected work</h2>
  </div>
  <div class="aa-list">
    {% for slug in project_slugs %}
      {% assign project = site.projects | where_exp: "item", "item.slug == slug" | first %}
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
        <a class="aa-row-link" href="{{ project.url | relative_url }}">Project details</a>
      </article>
    {% endfor %}
  </div>
</section>

{% assign audio_project = site.projects | where_exp: "item", "item.slug == 'audio-denoising'" | first %}

<section class="aa-section aa-index-group" aria-labelledby="earlier-coursework">
  <div class="aa-section-head aa-section-head-compact">
    <h2 id="earlier-coursework">Earlier coursework</h2>
  </div>
  <div class="aa-list">
    <article class="aa-row">
      <div class="aa-row-meta"><span class="aa-status">{{ audio_project.status }}</span></div>
      <div>
        <h3><a href="{{ audio_project.url | relative_url }}">{{ audio_project.title }}</a></h3>
        <p>{{ audio_project.description }}</p>
        <div class="aa-row-context">Supervised by {{ audio_project.supervisor }}</div>
      </div>
      <a class="aa-row-link" href="{{ audio_project.url | relative_url }}">Project details</a>
    </article>
  </div>
</section>
