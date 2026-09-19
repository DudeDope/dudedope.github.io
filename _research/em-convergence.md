---
layout: page
title: EM in k-Component Gaussian Mixture-Type Models
description: Population and sample EM under nonconvex geometry, mixture imbalance, and high-dimensional noise.
permalink: /research/em-convergence/
research_area: Statistical learning and inference
status: Research in progress
organisation: University of Toronto
collaborators:
  - Prof. Xin Bing
period: Apr 2026–Present
featured: true
importance: 1
research_question: When do population and sample EM updates contract toward the target parameters in k-component Gaussian mixture-type models?
summary: Theoretical analysis of expectation-maximisation algorithms for latent-variable models.
tags:
  - EM algorithm
  - Gaussian mixtures
  - convergence
  - high-dimensional statistics
paper_url:
code_url:
slides_url:
poster_url:
technical_note_url:
image:
---

<header class="aa-entry-header">
  <div class="aa-entry-meta">
    <span class="aa-status">{{ page.status }}</span>
    <span>{{ page.period }}</span>
    <span>{{ page.organisation }}</span>
  </div>
  <p class="aa-entry-subtitle">
    A theoretical study of population and sample expectation-maximisation for k-component Gaussian mixture-type models, with emphasis on fixed
    points, local contraction, mixture imbalance, nonconvex geometry, and high-dimensional sampling error.
  </p>
  <div class="aa-tags" aria-label="Topics">
    {% for tag in page.tags %}
      <span class="aa-tag">{{ tag }}</span>
    {% endfor %}
  </div>
</header>

<div class="aa-entry-layout">
  <div class="aa-entry-main">
    <section id="abstract" class="aa-entry-section">
      <h2>Abstract</h2>
      <p>
        EM is easy to state but its behaviour can depend delicately on component separation, weights, initialisation, dimension, and sampling noise.
        The project first isolates the deterministic population map, then studies how finite-sample updates deviate from that map.
      </p>
    </section>

    <section id="question" class="aa-entry-section">
      <h2>Research question</h2>
      <p>{{ page.research_question }}</p>
    </section>

    <section id="setup" class="aa-entry-section">
      <h2>Setup</h2>
      <p>
        The analysis begins from conditional latent assignments and the resulting population update. Candidate parameters are organised relative to
        the signal geometry so that fixed-point and contraction questions can be reduced to interpretable components without discarding the
        high-dimensional structure.
      </p>
    </section>

    <section id="methods" class="aa-entry-section">
      <h2>Methods</h2>
      <ul>
        <li>Derivation and analysis of population and sample EM maps.</li>
        <li>Fixed-point identities and local Jacobian/operator-norm bounds.</li>
        <li>Stein's lemma for expectations involving Gaussian covariates.</li>
        <li>Fisher and missing-information decompositions for local rate analysis.</li>
        <li>Concentration-style bounds connecting population geometry with empirical updates.</li>
      </ul>
    </section>

    <section id="progress" class="aa-entry-section">
      <h2>Contribution and current progress</h2>
      <p>
        My work focuses on organising the update map, checking fixed-point structure, and identifying the terms that control a local contraction
        argument under imbalance and high-dimensional noise. Population and sample analyses are being developed together; no paper or theorem claim
        is presented as public or complete here.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations</h2>
      <p>
        Local contraction does not establish a global basin of attraction, and population behaviour alone does not determine finite-sample
        convergence. Results may depend on the mixture specification, separation regime, initialisation, and how component labels are handled.
      </p>
    </section>

    <section id="next" class="aa-entry-section">
      <h2>Next questions</h2>
      <ul>
        <li>How do component imbalance and separation change the local rate and basin size?</li>
        <li>Which concentration terms can remain dimension-light?</li>
        <li>How tightly can sample iterates be coupled to population dynamics?</li>
        <li>Which geometric arguments extend beyond the current mixture family?</li>
      </ul>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>References and artifacts</h2>
      <p class="aa-empty">A public technical note and code link will be added after they are ready for release.</p>
    </section>

  </div>

  <aside class="aa-entry-rail" aria-label="Research record metadata">
    <h2>Record</h2>
    <dl class="aa-fact-list">
      <div>
        <dt>Status</dt>
        <dd>{{ page.status }}</dd>
      </div>
      <div>
        <dt>Period</dt>
        <dd>{{ page.period }}</dd>
      </div>
      <div>
        <dt>Institution</dt>
        <dd>{{ page.organisation }}</dd>
      </div>
      <div>
        <dt>Advisor</dt>
        <dd>{{ page.collaborators | join: ", " }}</dd>
      </div>
      <div>
        <dt>Public output</dt>
        <dd>Not yet published</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#abstract">Abstract</a>
      <a href="#question">Question</a>
      <a href="#setup">Setup</a>
      <a href="#methods">Methods</a>
      <a href="#progress">Progress</a>
      <a href="#limitations">Limitations</a>
      <a href="#next">Next questions</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ResearchProject",
  "name": {{ page.title | jsonify }},
  "description": {{ page.description | jsonify }},
  "url": {{ page.url | absolute_url | jsonify }},
  "member": { "@type": "Person", "name": {{ site.data.profile.name | jsonify }} },
  "keywords": {{ page.tags | jsonify }}
}
</script>
