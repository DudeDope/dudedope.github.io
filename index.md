---
layout: page
title: Aditya Aryan
description: Statistics, probabilistic modelling, machine learning, and optimisation under uncertainty.
---

<div class="aa-home-grid">
  <div class="aa-home-intro">
    <span class="aa-kicker">Statistics · Probabilistic Modelling · Machine Learning · Optimisation</span>

    <p class="aa-lede">
      I am a Bachelor of Statistics student at the Indian Statistical Institute, Kolkata. My interests lie in mathematical statistics,
      probabilistic modelling, machine learning, and optimisation under uncertainty.
    </p>

    <p class="aa-lede">
      I am currently a student researcher at the University of Toronto and a data science intern at Ranial Systems, following an earlier
      machine-learning research internship at Mercity AI. Across these roles, I have worked on theoretical analysis, forecasting, anomaly
      detection, decision models, and multimodal learning.
    </p>

    <nav class="aa-actions" aria-label="Homepage shortcuts">
      <a href="{{ '/research/' | relative_url }}">Research</a>
      <a href="{{ '/projects/' | relative_url }}">Projects</a>
      <a href="{{ '/cv/' | relative_url }}">CV</a>
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

<section class="aa-section" aria-labelledby="experience">
  <div class="aa-section-head">
    <h2 id="experience">Experience</h2>
    <p>Research and industry experience spanning statistical learning, probabilistic modelling, machine learning, and optimisation.</p>
  </div>

  <div class="aa-list">
    <article class="aa-row">
      <div class="aa-row-meta">Apr 2026–Present</div>
      <div>
        <h3><a href="{{ '/research/em-convergence/' | relative_url }}">Student Researcher</a></h3>
        <p>Working on theoretical questions in statistical learning through the analysis of population and sample expectation-maximisation algorithms.</p>
        <div class="aa-row-context">University of Toronto · Remote · with Prof. Xin Bing</div>
      </div>
      <a class="aa-row-link" href="{{ '/research/em-convergence/' | relative_url }}">Record</a>
    </article>

    <article class="aa-row">
      <div class="aa-row-meta">May 2026–Present</div>
      <div>
        <h3><a href="{{ '/research/battery-dispatch/' | relative_url }}">Data Science Intern</a></h3>
        <p>
          Working on battery modelling, anomaly detection, probabilistic forecasting, and optimisation for electricity-market and operational
          decisions.
        </p>
        <div class="aa-row-context">Ranial Systems · Remote</div>
      </div>
      <a class="aa-row-link" href="{{ '/research/battery-dispatch/' | relative_url }}">Record</a>
    </article>

    <article class="aa-row">
      <div class="aa-row-meta">Apr–Aug 2025</div>
      <div>
        <h3><a href="{{ '/research/medical-vlm/' | relative_url }}">Machine Learning Research Intern</a></h3>
        <p>Worked on efficient multimodal learning, including representation compression, supervised training, and preference optimisation.</p>
        <div class="aa-row-context">Mercity AI · Bengaluru</div>
      </div>
      <a class="aa-row-link" href="{{ '/research/medical-vlm/' | relative_url }}">Record</a>
    </article>

  </div>
</section>

{% assign selected_research = site.research | where: "featured", true | sort: "importance" %}

<section class="aa-section" aria-labelledby="selected-research">
  <div class="aa-section-head">
    <h2 id="selected-research">Selected research</h2>
    <p>Current and completed work across statistical learning, probabilistic modelling, optimisation, and machine-learning systems.</p>
  </div>

  <div class="aa-list">
    {% for project in selected_research limit: 4 %}
      <article class="aa-row">
        <div class="aa-row-meta">
          <span class="aa-status">{{ project.status }}</span>
          <div>{{ project.period }}</div>
        </div>
        <div>
          <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
          <p>{{ project.summary | default: project.description }}</p>
          <div class="aa-row-context">{{ project.organisation }}</div>
        </div>
        <a class="aa-row-link" href="{{ project.url | relative_url }}">Record</a>
      </article>
    {% endfor %}
  </div>
</section>

{% assign selected_projects = site.projects | where: "type", "project" | sort: "importance" %}

<section class="aa-section" aria-labelledby="selected-projects">
  <div class="aa-section-head">
    <h2 id="selected-projects">Selected projects</h2>
    <p>Supervised projects applying statistical inference, probabilistic modelling, optimisation, and predictive methods to varied problems.</p>
  </div>
  <div class="aa-list">
    {% for project in selected_projects limit: 3 %}
      <article class="aa-row">
        <div class="aa-row-meta">{{ project.project_area }}</div>
        <div>
          <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
          <p>{{ project.description }}</p>
          {% if project.supervisor %}
            <div class="aa-row-context">Supervised by {{ project.supervisor }}</div>
          {% endif %}
        </div>
        <a class="aa-row-link" href="{{ project.url | relative_url }}">Record</a>
      </article>
    {% endfor %}
  </div>
</section>

<section class="aa-section" aria-labelledby="notes-status">
  <div class="aa-section-head">
    <h2 id="notes-status">Course notes</h2>
    <p>Lecture-wise notes with explicit attribution, cumulative formula sheets, and navigable course indexes.</p>
  </div>
  <div class="aa-list">
    {% for course in site.data.course_notes.courses %}
      <article class="aa-row">
        <div class="aa-row-meta">
          {{ course.term }}
          <div>{{ course.lecture_count }} lectures</div>
        </div>
        <div>
          <h3><a href="{{ course.contents_url | relative_url }}">{{ course.title }}</a></h3>
          <p>{{ course.description }}</p>
          <div class="aa-row-context">{{ course.instructor }} · {{ course.institution }}</div>
        </div>
        <a class="aa-row-link" href="{{ course.contents_url | relative_url }}">Browse</a>
      </article>
    {% endfor %}
  </div>
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
