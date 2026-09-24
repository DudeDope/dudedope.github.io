---
layout: page
permalink: /cv/
title: CV
nav: true
nav_order: 5
description: Two-page academic CV covering education, research and industry experience, selected projects, skills, and academic distinctions.
---

{% assign cv_pdf = '/assets/rendercv/rendercv_output/Aditya_Aryan_CV.pdf' | relative_url %}

<div class="aa-cv-shell">
  <header class="aa-cv-toolbar">
    <nav class="aa-cv-actions" aria-label="CV documents">
      <a class="aa-cv-action aa-cv-action-primary" href="{{ cv_pdf }}" target="_blank" rel="noopener">Open PDF</a>
      <a class="aa-cv-action" href="{{ cv_pdf }}" download>Download PDF</a>
    </nav>
  </header>

  <section class="aa-cv-preview" aria-label="CV PDF preview">
    <object data="{{ cv_pdf }}#view=FitH&navpanes=0" type="application/pdf">
      <div class="aa-cv-fallback">
        <p>Your browser does not display embedded PDFs.</p>
        <a class="aa-cv-action aa-cv-action-primary" href="{{ cv_pdf }}">Open the CV PDF</a>
      </div>
    </object>
  </section>

  <p class="aa-cv-note">For the clearest view on a phone, use <strong>Open PDF</strong> or <strong>Download PDF</strong>.</p>
</div>
