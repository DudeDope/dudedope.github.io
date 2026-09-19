---
layout: page
permalink: /notes/
title: Notes
description: Expanded course notes in parametric inference, sample surveys, and algorithms.
nav: true
nav_order: 3
---

<div class="aa-notes-index">
<p class="aa-page-intro">
  Expanded course notes from ISI, with proofs, worked examples, and formula references. The collections cover parametric inference, sample surveys,
  and algorithms. Sources, added exposition, and substantive corrections are identified within the notes.
</p>

{% for course in site.data.course_notes.courses %}

  <section class="aa-section aa-course-series" aria-labelledby="{{ course.slug }}">
    <div class="aa-section-head">
      <div>
        <h2 id="{{ course.slug }}"><a href="{{ course.contents_url | relative_url }}">{{ course.title }}</a></h2>
        <p class="aa-course-byline">
          <span>{{ course.instructor }}</span>
          <span aria-hidden="true">·</span>
          <span>{{ course.term }}</span>
        </p>
      </div>
      <p>{{ course.landing_description }}</p>
    </div>
    <nav class="aa-course-landing-links" aria-label="{{ course.title }} resources">
      <a href="{{ course.contents_url | relative_url }}">Course contents</a>
      <a href="{{ course.formula_url | relative_url }}">Formula reference</a>
    </nav>
  </section>
{% endfor %}

</div>
