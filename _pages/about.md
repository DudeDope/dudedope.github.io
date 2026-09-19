---
layout: page
title: About
permalink: /about/
description: A concise biography and links to Aditya Aryan's research, projects, notes, and CV.
nav: false
nav_order: 1
---

<div class="aa-page-grid">
  <div class="aa-prose">
    <p class="aa-lede">I am a Bachelor of Statistics student at the Indian Statistical Institute, Kolkata. My interests span theoretical and applied statistics and machine learning.</p>

    <p>
      My coursework projects introduced me to estimation, dependence modelling, and sequential decisions. My current work includes the analysis of
      EM algorithms, statistical modelling for energy systems, and independent experiments with machine-learning methods. Earlier, I worked on
      medical vision-language modelling at Mercity AI.
    </p>

    <p>This site collects research summaries, project analyses, code, and expanded course notes.</p>

    <nav class="aa-actions" aria-label="About page links">
      <a href="{{ '/research/' | relative_url }}">Research</a>
      <a href="{{ '/projects/' | relative_url }}">Projects</a>
      <a href="{{ '/notes/' | relative_url }}">Notes</a>
      <a href="{{ '/cv/' | relative_url }}">CV</a>
    </nav>

  </div>

  <aside class="aa-academic-rail aa-profile-rail aa-contact-rail" aria-label="Contact and profile links">
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
