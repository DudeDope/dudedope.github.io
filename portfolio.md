---
layout: default
title: Portfolio
permalink: /portfolio/
---

# Portfolio

Here's a collection of projects I've worked on, showcasing different technologies and problem-solving approaches.

<div class="project-grid">
    {% for project in site.projects %}
    <div class="project-card">
        <h3 class="project-title">{{ project.title }}</h3>
        <p class="project-description">{{ project.description }}</p>
        
        {% if project.technologies %}
        <div class="project-tech">
            {% for tech in project.technologies %}
            <span class="tech-tag">{{ tech }}</span>
            {% endfor %}
        </div>
        {% endif %}
        
        <div class="project-links">
            {% if project.github_url %}
            <a href="{{ project.github_url }}" target="_blank">GitHub</a>
            {% endif %}
            {% if project.demo_url %}
            <a href="{{ project.demo_url }}" target="_blank">Live Demo</a>
            {% endif %}
            <a href="{{ project.url }}">Learn More</a>
        </div>
    </div>
    {% endfor %}
</div>

## Featured Projects

### Machine Learning Portfolio
A comprehensive collection of ML projects including predictive models, natural language processing, and computer vision applications.

### Web Application Suite
Full-stack applications demonstrating modern web development practices with React, Node.js, and various databases.

### Open Source Contributions
Active contributions to various open source projects, including bug fixes, feature additions, and documentation improvements.

---

*Interested in collaboration or have a project in mind? [Get in touch!](/about/)*