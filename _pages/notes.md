---
layout: page
permalink: /notes/
title: Notes
description: Expanded course notes in parametric inference, sample surveys, and algorithms.
nav: true
nav_order: 4
---

<p class="aa-page-intro">
  Expanded course notes from ISI, with proofs, worked examples, and formula references. Sources, added exposition, and substantive corrections are
  identified within the notes.
</p>

{% for course in site.data.course_notes.courses %}
{% assign course_lectures = site.pages | where: "course_slug", course.slug | where: "note_kind", "lecture" | sort: "course_order" %}

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
      <nav class="aa-course-resources" aria-label="{{ course.title }} resources">
        <a href="{{ course.contents_url | relative_url }}">All lectures</a>
        <a href="{{ course.formula_url | relative_url }}">Formula sheet</a>
      </nav>
    </div>

    <div class="aa-list aa-lecture-list">
      {% for note in course_lectures %}
        <article class="aa-row">
          <div class="aa-row-meta">Lecture {{ note.lecture }}</div>
          <div>
            <h3><a href="{{ note.url | relative_url }}">{{ note.short_title | default: note.title }}</a></h3>
            <p>{{ note.description }}</p>
          </div>
          <a class="aa-row-link" href="{{ note.url | relative_url }}">Read</a>
        </article>
      {% endfor %}
    </div>

  </section>
{% endfor %}
