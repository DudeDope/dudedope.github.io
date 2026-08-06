---
layout: page
permalink: /publications/
title: Publications
description: Publications, preprints, working manuscripts, and public technical reports.
nav: true
nav_order: 3
---

{% if site.data.profile.publications_available %}
{% include bib_search.liquid %}

  <div class="publications">
    {% bibliography %}
  </div>
{% else %}
  <p class="aa-empty">
    I do not currently have any publications or public manuscripts. Future papers, preprints, and technical reports will appear here only after a
    public record is available. Ongoing work is described on the <a href="{{ '/research/' | relative_url }}">Research page</a>.
  </p>
{% endif %}
