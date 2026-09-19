---
layout: page
title: "Stein's Paradox: Inadmissibility and Risk-Optimal Shrinkage"
description: Decision-theoretic risk, James–Stein shrinkage, heteroscedastic extensions, empirical Bayes estimation, and SURE.
permalink: /projects/stein-shrinkage/
type: project
project_area: Statistical inference and probabilistic modelling
status: Supervised project
organisation: Indian Statistical Institute
supervisor: Dr. Ayanendranath Basu
period:
featured: false
importance: 3
math: true
tags:
  - decision theory
  - James–Stein estimation
  - empirical Bayes
  - SURE
repository_url:
technical_note_url:
image:
---

<header class="aa-entry-header">
  <div class="aa-entry-meta">
    <span class="aa-status">{{ page.status }}</span>
    <span>{{ page.organisation }}</span>
    <span>with {{ page.supervisor }}</span>
  </div>
  <p class="aa-entry-subtitle">
    A decision-theoretic study of how biased joint estimation can dominate coordinate-wise maximum likelihood under multivariate squared-error risk.
  </p>
  <div class="aa-tags" aria-label="Topics">
    {% for tag in page.tags %}
      <span class="aa-tag">{{ tag }}</span>
    {% endfor %}
  </div>
</header>

<div class="aa-entry-layout">
  <div class="aa-entry-main">
    <section id="model" class="aa-entry-section">
      <h2>Normal-means decision problem</h2>
      <p>In the classical model,</p>

$$
X\sim\mathcal N_d(\theta,\sigma^2 I_d),
\qquad
L(\theta,\delta)=\lVert\delta-\theta\rVert_2^2.
$$

      <p>
        The usual estimator \(\delta_0(X)=X\) is unbiased, equivariant, and has constant risk
        \(R(\theta,\delta_0)=d\sigma^2\). Coordinate-wise reasoning therefore makes it look canonical. Stein's paradox is that for \(d\geq3\), this
        estimator is inadmissible: another estimator has no larger risk for any \(\theta\) and strictly smaller risk somewhere.
      </p>
    </section>

    <section id="estimator" class="aa-entry-section">
      <h2>James–Stein shrinkage</h2>
      <p>The classical estimator shrinks the observed vector toward the origin:</p>

$$
\delta_{\mathrm{JS}}(X)
=\left(
1-\frac{(d-2)\sigma^2}{\lVert X\rVert_2^2}
\right)X.
$$

      <p>
        When the observed norm is small, the common multiplier pools the coordinates strongly; when it is large, the estimate approaches \(X\).
        The positive-part modification
      </p>

$$
\delta_{\mathrm{JS}}^{+}(X)
=\max\!\left\{
0,\,
1-\frac{(d-2)\sigma^2}{\lVert X\rVert_2^2}
\right\}X
$$

      <p>avoids reversing the direction of \(X\) when the unconstrained multiplier becomes negative.</p>
    </section>

    <section id="risk" class="aa-entry-section">
      <h2>Risk calculation through Stein's identity</h2>
      <p>
        Write \(\delta(X)=X+g(X)\). Under the regularity conditions for Stein's identity, the risk difference from the usual estimator is
      </p>

$$
R(\theta,\delta)-R(\theta,X)
=\operatorname E_{\theta}\!\left[
\lVert g(X)\rVert_2^2
+2\sigma^2\operatorname{div}g(X)
\right].
$$

      <p>For \(g(x)=-a x/\lVert x\rVert_2^2\),</p>

$$
\lVert g(x)\rVert_2^2=\frac{a^2}{\lVert x\rVert_2^2},
\qquad
\operatorname{div}g(x)=-\frac{a(d-2)}{\lVert x\rVert_2^2}.
$$

      <p>Consequently,</p>

$$
R(\theta,\delta)-R(\theta,X)
=
\left[a^2-2a\sigma^2(d-2)\right]
\operatorname E_{\theta}\!\left[\frac{1}{\lVert X\rVert_2^2}\right].
$$

      <p>
        Choosing \(a=(d-2)\sigma^2\) makes the coefficient negative for \(d\geq3\), yielding the James–Stein rule and its uniform risk improvement in
        the classical setting. This argument explains both the threshold dimension and the exact shrinkage constant.
      </p>
    </section>

    <section id="extensions" class="aa-entry-section">
      <h2>Extensions studied</h2>
      <ul>
        <li>
          <strong>Alternative shrinkage targets.</strong> Shrinking toward a common empirical mean replaces the fixed origin with a location suggested
          by the coordinates while preserving a lower-dimensional residual problem.
        </li>
        <li>
          <strong>Heteroscedastic observations.</strong> Unequal variances motivate standardisation or whitening, but the transformation and the loss
          function must be kept aligned when risk is interpreted.
        </li>
        <li>
          <strong>Normal–Normal empirical Bayes.</strong> Under \(\theta_i\sim\mathcal N(\mu,\tau^2)\) and
          \(X_i\mid\theta_i\sim\mathcal N(\theta_i,\sigma_i^2)\), the posterior mean is
        </li>
      </ul>

$$
\operatorname E(\theta_i\mid X_i)
=
\frac{\tau^2}{\tau^2+\sigma_i^2}X_i
+
\frac{\sigma_i^2}{\tau^2+\sigma_i^2}\mu,
$$

      <p>
        making shrinkage a data-adaptive precision weighting. The project compares method-of-moments and marginal maximum-likelihood estimates of the
        hyperparameters.
      </p>
    </section>

    <section id="sure" class="aa-entry-section">
      <h2>SURE and simulation design</h2>
      <p>Stein's unbiased risk estimate provides an observable estimate of squared-error risk up to the model assumptions:</p>

$$
\operatorname{SURE}(\delta)
=
\lVert\delta(X)-X\rVert_2^2
+2\sigma^2\operatorname{div}\delta(X)
-d\sigma^2.
$$

      <p>
        The computational study compares the usual estimator, classical and positive-part James–Stein rules, mean-centred shrinkage, and empirical
        Bayes procedures across simulated signal and variance regimes. Monte Carlo risk and SURE serve different roles: repeated simulation estimates
        risk because \(\theta\) is known to the experimenter, while SURE estimates risk from a realised observation.
      </p>
    </section>

    <section id="results" class="aa-entry-section">
      <h2>Reported findings</h2>
      <p>
        The study recovered the classical James–Stein dominance pattern in the homoscedastic normal-means setting. In the reported heteroscedastic
        simulations, the marginal maximum-likelihood empirical-Bayes procedure recorded the lowest risk among the compared estimators.
      </p>
      <p>
        No numerical table, parameter grid, uncertainty interval, or executable source is public yet. The second statement is therefore a
        configuration-specific simulation result, not a general dominance theorem.
      </p>
    </section>

    <section id="limitations" class="aa-entry-section">
      <h2>Limitations</h2>
      <p>
        Risk rankings depend on dimension, signal geometry, shrinkage target, variance pattern, hyperparameter estimation, and the loss used after
        whitening. Monte Carlo comparisons also require fixed seeds, replication counts, standard errors, and clearly separated tuning and evaluation
        regimes. Positive-part shrinkage improves the classical rule but is non-smooth, which matters when applying divergence-based formulas.
      </p>
    </section>

    <section id="artifacts" class="aa-entry-section">
      <h2>Artifacts</h2>
      <p class="aa-empty">
        No report or source file was supplied for public release. A technical note and reproducible simulation package will be linked only when the
        parameter grid, seeds, baselines, and uncertainty summaries are ready.
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
        <dt>Public output</dt>
        <dd>Technical record</dd>
      </div>
    </dl>
    <nav class="aa-entry-toc" aria-label="On this page">
      <span>On this page</span>
      <a href="#model">Model</a>
      <a href="#estimator">Estimator</a>
      <a href="#risk">Risk argument</a>
      <a href="#extensions">Extensions</a>
      <a href="#sure">SURE</a>
      <a href="#results">Findings</a>
      <a href="#limitations">Limitations</a>
      <a href="#artifacts">Artifacts</a>
    </nav>
  </aside>
</div>
