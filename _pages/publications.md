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
    No publications or public manuscripts at present. Current work is described on the
    <a href="{{ '/research/' | relative_url }}">Research page</a>.
  </p>
{% endif %}
