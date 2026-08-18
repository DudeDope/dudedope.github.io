---
layout: page
title: Bivariate Copula Modelling of Extreme Air-Pollution Events
description: Empirical marginals, canonical maximum likelihood, copula selection, upper-tail dependence, and conditional severity estimates.
permalink: /projects/copula-air-pollution/
type: project
project_area: Statistical inference and probabilistic modelling
status: Supervised project
organisation: Indian Statistical Institute
supervisor: Prof. Shyamal Krishna De
period: April 2026
featured: true
importance: 4
math: true
tags:
  - copulas
  - tail dependence
  - environmental statistics
  - canonical maximum likelihood
repository_url:
report_url: /assets/pdf/projects/copula-air-pollution-public.pdf
code_url: /assets/code/projects/copula-gumbel-reference.py
image: /assets/img/projects/copula/marginals-joint.png
pseudo_observations_image: /assets/img/projects/copula/pseudo-observations.png
---

<header class="aa-entry-header">
  <div class="aa-entry-meta">
    <span class="aa-status">{{ page.status }}</span>
    <span>{{ page.organisation }}</span>
    <span>with {{ page.supervisor }}</span>
  </div>
  <p class="aa-entry-subtitle">
    A semiparametric analysis of the duration and cumulative severity of unhealthy Bengaluru air-pollution episodes, with empirical margins and
    explicit upper-tail dependence.
  </p>
  <div class="aa-tags" aria-label="Topics">
    {% for tag in page.tags %}
      <span class="aa-tag">{{ tag }}</span>
    {% endfor %}
  </div>
</header>

<div class="aa-entry-layout">
  <div class="aa-entry-main">
    <section id="question" class="aa-entry-section">
      <h2>Question</h2>
      <p>
        Duration and cumulative exposure describe different aspects of an unhealthy pollution episode. Marginal histograms do not determine how
        their extremes coincide, while Pearson correlation compresses dependence into a symmetric linear summary. The project asks which bivariate
        copula best represents their rank dependence and what the fitted model implies for conditional threshold exceedance.
      </p>
    </section>

    <section id="events" class="aa-entry-section">
      <h2>From hourly observations to events</h2>
      <p>
        The report analyses 87,649 hourly AQI observations for Bengaluru from 1 January 2015 through 31 December 2024. It describes the file as a
        secondary distribution of Central Pollution Control Board monitoring data. An unhealthy episode \(P_j\) is a maximal contiguous run of hours
        satisfying \(\operatorname{AQI}(t)>100\).
      </p>
      <p>Each episode is reduced to two variables:</p>

$$
D_j=\lvert P_j\rvert,
\qquad
S_j=\sum_{t\in P_j}\operatorname{AQI}(t).
$$

      <p>
        This construction yields \(n=13{,}904\) episodes. Duration has median 4 hours, upper quartile 7, and maximum 35. Cumulative severity has median
        1,084.2, upper quartile 2,069.1, and maximum 10,777 AQI-units. Both summaries are strongly right-skewed.
      </p>
    </section>

    <figure class="aa-project-figure">
      <img
        class="img-fluid"
        src="{{ page.image | relative_url }}"
        alt="Histograms of episode duration and cumulative AQI severity beside their joint scatter"
        loading="lazy"
      >
      <figcaption>
        Empirical margins and joint scatter for the extracted episodes. The strong trend partly reflects that cumulative severity sums AQI over
        duration. Source: project report.
      </figcaption>
    </figure>

    <section id="copula" class="aa-entry-section">
      <h2>Separating margins from dependence</h2>
      <p>
        Sklar's theorem writes a bivariate distribution \(H\) with marginals \(F_D\) and \(F_S\) as
      </p>

$$
H(d,s)=C\!\left(F_D(d),F_S(s)\right),
$$

      <p>
        where \(C\) is a copula. The analysis estimates the two margins empirically and puts the parametric structure only on \(C\). For observation
        \(i\), average ranks handle tied integer durations:
      </p>

$$
\widehat u_i=\frac{\operatorname{rank}_{\mathrm{avg}}(D_i)}{n+1},
\qquad
\widehat v_i=\frac{\operatorname{rank}_{\mathrm{avg}}(S_i)}{n+1}.
$$

      <p>
        Division by \(n+1\) keeps every pseudo-observation strictly inside \((0,1)^2\), avoiding numerical singularities at zero and one. The
        resulting vertical bands are expected: many episodes share the same integer duration but have different cumulative severity.
      </p>
    </section>

    <figure class="aa-project-figure">
      <img
        class="img-fluid"
        src="{{ page.pseudo_observations_image | relative_url }}"
        alt="Rank pseudo-observations in vertical bands with concentration near the upper-right corner"
        loading="lazy"
      >
      <figcaption>
        Average-rank pseudo-observations. Discrete duration creates the bands; upper-corner concentration motivates a model with upper-tail
        dependence. Source: project report.
      </figcaption>
    </figure>

    <section id="families" class="aa-entry-section">
      <h2>Candidate dependence structures</h2>
      <p>Six one-parameter copulas were compared because they encode different symmetry and tail behaviour:</p>
      <table>
        <thead>
          <tr>
            <th>Family</th>
            <th>Dependence emphasis</th>
            <th>Tail behaviour used in interpretation</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>Clayton</td><td>Asymmetric</td><td>Lower-tail dependence</td></tr>
          <tr><td>Ali–Mikhail–Haq</td><td>Limited concordance range</td><td>Tail independent</td></tr>
          <tr><td>Frank</td><td>Radially symmetric</td><td>Tail independent</td></tr>
          <tr><td>Gumbel</td><td>Asymmetric</td><td>Upper-tail dependence</td></tr>
          <tr><td>Joe</td><td>Strong upper-corner concentration</td><td>Upper-tail dependence</td></tr>
          <tr><td>Plackett</td><td>Symmetric odds-ratio association</td><td>Tail independent</td></tr>
        </tbody>
      </table>
      <p>
        For the Gumbel family selected by the data,
      </p>

$$
C_{\theta}^{\mathrm{Gu}}(u,v)
=\exp\!\left(
-\left[(-\log u)^{\theta}+(-\log v)^{\theta}\right]^{1/\theta}
\right),
\qquad \theta\geq1,
$$

      <p>with Kendall's \(\tau=1-\theta^{-1}\) and upper-tail coefficient \(\lambda_U=2-2^{1/\theta}\).</p>
    </section>

    <section id="estimation" class="aa-entry-section">
      <h2>Canonical maximum likelihood</h2>
      <p>For each family, the copula parameter is estimated from the pseudo-observations by</p>

$$
\widehat\theta
=\underset{\theta}{\arg\max}
\sum_{i=1}^{n}\log c_{\theta}(\widehat u_i,\widehat v_i),
\qquad
c_{\theta}(u,v)=\frac{\partial^2 C_{\theta}(u,v)}{\partial u\,\partial v}.
$$

      <p>
        The report evaluates densities through a central finite difference with step \(h=2\times10^{-4}\):
      </p>

$$
\widehat c_{\theta}(u,v)
=\frac{
C_{\theta}(u+h,v+h)-C_{\theta}(u+h,v-h)
-C_{\theta}(u-h,v+h)+C_{\theta}(u-h,v-h)
}{4h^2}.
$$

      <p>
        Bounded numerical optimisation supplies \(\widehat\theta\). Because every candidate has one fitted parameter, minimising
        \(\operatorname{AIC}=2-2\widehat\ell\) gives the same ranking as maximising the fitted pseudo-log-likelihood.
      </p>
    </section>

    <section id="selection" class="aa-entry-section">
      <h2>Model comparison</h2>
      <table>
        <thead>
          <tr>
            <th>Model</th>
            <th>\(\widehat\theta\)</th>
            <th>AIC</th>
            <th>Model \(\widehat\tau\)</th>
            <th>\(\widehat\lambda_U\)</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>Gumbel</td><td>6.1831</td><td>−38,531.2</td><td>0.7954</td><td>0.8814</td></tr>
          <tr><td>Joe</td><td>9.3735</td><td>−37,954.2</td><td>0.7896</td><td>0.9233</td></tr>
          <tr><td>Frank</td><td>22.204</td><td>−36,630.2</td><td>0.7640</td><td>0</td></tr>
          <tr><td>Plackett</td><td>100.00</td><td>−35,708.6</td><td>0.7245</td><td>0</td></tr>
          <tr><td>Ali–Mikhail–Haq</td><td>0.990</td><td>−11,439.6</td><td>0.2745</td><td>0</td></tr>
          <tr><td>Clayton</td><td>14.870</td><td>7,262.5</td><td>0.8137</td><td>0</td></tr>
        </tbody>
      </table>
      <p>
        Empirical Kendall's \(\widehat\tau=0.881\) and Spearman's \(\widehat\rho_S=0.972\) show very strong rank association. Gumbel achieves the
        smallest reported AIC. Its fitted \(\widehat\lambda_U=0.8814\) describes limiting co-exceedance of equally high marginal quantiles; it is not
        the probability that every long episode has a severe outcome.
      </p>
    </section>

    <section id="conditional" class="aa-entry-section">
      <h2>Conditional exceedance derivation</h2>
      <p>
        For duration threshold \(d_0\) and severity threshold \(s_0\), discreteness requires the left limit
        \(F_D(d_0^-)=\Pr(D<d_0)\). Inclusion–exclusion gives
      </p>

$$
\Pr(S>s_0,D\geq d_0)
=1-F_D(d_0^-)-F_S(s_0)
+C\!\left(F_D(d_0^-),F_S(s_0)\right).
$$

      <p>Dividing by \(\Pr(D\geq d_0)=1-F_D(d_0^-)\) yields</p>

$$
\Pr(S>s_0\mid D\geq d_0)
=\frac{
1-F_D(d_0^-)-F_S(s_0)
+C\!\left(F_D(d_0^-),F_S(s_0)\right)
}{
1-F_D(d_0^-)
}.
$$

      <p>
        At \(d_0=12\) hours and \(s_0=2000\), the fitted estimate is 0.9998 and the empirical estimate is 1.0000 under the report's event definition.
      </p>
    </section>

    <section id="interpretation" class="aa-entry-section">
      <h2>Interpretation before application</h2>
      <p>
        Cumulative severity contains duration by construction: \(S_j=D_j\bar A_j\), where \(\bar A_j\) is mean AQI during episode \(j\). Much of the
        near-monotone relationship is therefore mechanical, and the threshold result is partly explained by arithmetic. It must not be described as
        an independent causal effect of duration or as a clinically validated alert threshold.
      </p>
      <p>
        The copula still provides a coherent description of the joint ranks and a reusable conditional-probability calculation. A stronger scientific
        question would compare duration with mean intensity, peak intensity, or excess above the threshold, then test whether upper-tail dependence
        persists without embedding duration in both variables.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations and robustness checks</h2>
      <ul>
        <li>The secondary dataset needs a durable provenance record, station-aggregation description, and missingness audit.</li>
        <li>Average ranks accommodate ties computationally, but continuous-copula likelihood theory is not exact for discrete duration.</li>
        <li>The finite-difference density can depend on step size and boundary clipping.</li>
        <li>Extracted episodes may retain temporal, seasonal, and meteorological dependence.</li>
        <li>A fixed AQI threshold of 100 has not been compared with alternative episode definitions.</li>
        <li>AIC selects within the six fitted families; it does not establish absolute goodness of fit.</li>
      </ul>
      <p>
        Useful extensions include checkerboard or interval-censored copulas for ties, bootstrap uncertainty, goodness-of-fit diagnostics, threshold
        sensitivity, seasonal stratification, and conditional models with meteorological covariates.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Report and code</h2>
      <nav class="aa-artifacts" aria-label="Copula project artifacts">
        <a href="{{ page.report_url | relative_url }}">Read the public report (PDF)</a>
        <a href="{{ page.code_url | relative_url }}">Download the Gumbel-workflow Python reference</a>
      </nav>
      <p class="aa-empty">
        The public PDF begins after the original identifying cover page. The Python file reconstructs event extraction, pseudo-observations, the
        selected Gumbel fit, and conditional exceedance; it is not presented as the unavailable original six-family source.
      </p>
    </section>

  </div>

  <aside class="aa-entry-rail" aria-label="Project metadata">
    <h2>Project record</h2>
    <dl class="aa-fact-list">
      <div>
        <dt>Type</dt>
        <dd>{{ page.status }}</dd>
      </div>
      <div>
        <dt>Institution</dt>
        <dd>{{ page.organisation }}</dd>
      </div>
      <div>
        <dt>Supervisor</dt>
        <dd>{{ page.supervisor }}</dd>
      </div>
      <div>
        <dt>Study period</dt>
        <dd>AQI data, 2015–2024</dd>
      </div>
      <div>
        <dt>Completed</dt>
        <dd>{{ page.period }}</dd>
      </div>
      <div>
        <dt>Public output</dt>
        <dd>Technical record, report, reference code</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#question">Question</a>
      <a href="#events">Event construction</a>
      <a href="#copula">Copula setup</a>
      <a href="#families">Families</a>
      <a href="#estimation">Estimation</a>
      <a href="#selection">Selection</a>
      <a href="#conditional">Conditional risk</a>
      <a href="#interpretation">Interpretation</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Report and code</a>
    </nav>
  </aside>
</div>
