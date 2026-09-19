---
layout: page
permalink: /publications/
title: Publications
description: Publication status and public research artifacts.
nav: false
---

{% if site.data.profile.publications_available %}
{% include bib_search.liquid %}

  <div class="publications">
    {% bibliography %}
  </div>
{% else %}
  <p class="aa-empty">
    No publications or public manuscripts are currently listed. Research summaries and available public artifacts appear on the
    <a href="{{ '/research/' | relative_url }}">Research page</a>.
  </p>
{% endif %}
