---
layout: page
title: Aditya Aryan
description: Statistics, learning theory, and machine learning for scientific systems.
---

<div class="aa-home-grid">
  <div class="aa-home-intro">
    <span class="aa-kicker">Statistics · learning theory · scientific systems</span>

    <p class="aa-lede">
      I am a Bachelor of Statistics student at the Indian Statistical Institute, Kolkata. I work across mathematical statistics, machine learning,
      and scientific decision systems, with current interests in expectation-maximisation, high-dimensional inference, battery analytics, and
      reliable multimodal learning.
    </p>

    <p class="aa-lede">
      I am currently a student researcher with Prof. Xin Bing at the University of Toronto and a data science intern at Ranial Systems. Previously,
      I worked on compact medical vision-language models at Mercity AI.
    </p>

    <nav class="aa-actions" aria-label="Homepage shortcuts">
      <a href="{{ '/research/' | relative_url }}">Research</a>
      <a href="{{ '/projects/' | relative_url }}">Projects</a>
      <a href="{{ '/cv/' | relative_url }}">CV</a>
    </nav>

  </div>

  <aside class="aa-academic-rail" aria-label="Academic profile">
    <h2>Academic profile</h2>
    <dl class="aa-fact-list">
      <div>
        <dt>Education</dt>
        <dd>B.Stat (Hons.), Indian Statistical Institute</dd>
      </div>
      <div>
        <dt>Expected</dt>
        <dd>2027</dd>
      </div>
      <div>
        <dt>Current</dt>
        <dd>University of Toronto · Ranial Systems</dd>
      </div>
      <div>
        <dt>Location</dt>
        <dd>Kolkata, India</dd>
      </div>
      <div>
        <dt>Contact</dt>
        <dd><a href="mailto:{{ site.data.socials.email }}">{{ site.data.socials.email }}</a></dd>
      </div>
    </dl>
    <div class="aa-rail-links">{% social_links %}</div>
    <nav class="aa-rail-nav" aria-label="Document links">
      <a href="{{ '/assets/rendercv/rendercv_output/Aditya_Aryan_CV.pdf' | relative_url }}">CV PDF</a>
    </nav>
  </aside>
</div>

<section class="aa-section" aria-labelledby="experience">
  <div class="aa-section-head">
    <h2 id="experience">Experience</h2>
    <p>Research and industry roles spanning statistical theory, scientific machine learning, and decision systems.</p>
  </div>

  <div class="aa-list">
    <article class="aa-row">
      <div class="aa-row-meta">Apr 2026–Present</div>
      <div>
        <h3><a href="{{ '/research/em-convergence/' | relative_url }}">Student Researcher</a></h3>
        <p>Studying population and sample EM for k-component Gaussian mixture-type models under nonconvex geometry and sampling noise.</p>
        <div class="aa-row-context">University of Toronto · Remote · with Prof. Xin Bing</div>
      </div>
      <a class="aa-row-link" href="{{ '/research/em-convergence/' | relative_url }}">Record</a>
    </article>

    <article class="aa-row">
      <div class="aa-row-meta">May 2026–Present</div>
      <div>
        <h3><a href="{{ '/research/battery-dispatch/' | relative_url }}">Data Science Intern</a></h3>
        <p>Developing battery degradation, forecasting, survival-modelling, and operational decision-support workflows.</p>
        <div class="aa-row-context">Ranial Systems · Remote</div>
      </div>
      <a class="aa-row-link" href="{{ '/research/battery-dispatch/' | relative_url }}">Record</a>
    </article>

    <article class="aa-row">
      <div class="aa-row-meta">Apr–Aug 2025</div>
      <div>
        <h3><a href="{{ '/research/medical-vlm/' | relative_url }}">Machine Learning Research Intern</a></h3>
        <p>Worked on compact medical vision-language modelling, visual-token compression, supervised fine-tuning, and preference optimisation.</p>
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
    <p>Ongoing theoretical and applied work. Each record separates methods and evidence from limitations and release status.</p>
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
          <p>{{ project.research_question }}</p>
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
    <p>Course and supervised technical work in statistical methodology, dependence modelling, algorithms, signal processing, and calibration.</p>
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
