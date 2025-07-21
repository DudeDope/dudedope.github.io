---
layout: default
title: Blog
permalink: /blog/
---

# Blog

Technical articles, tutorials, and thoughts on software development, machine learning, and technology trends.

<div class="post-list">
    {% for post in site.posts %}
    <div class="post-item">
        <h2>
            <a class="post-link" href="{{ post.url | relative_url }}">
                {{ post.title | escape }}
            </a>
        </h2>
        <p class="post-date">{{ post.date | date: "%B %d, %Y" }}</p>
        
        {% if post.tags and post.tags.size > 0 %}
        <div class="tag-list">
            {% for tag in post.tags %}
            <a href="{{ '/tags/' | append: tag | append: '/' | relative_url }}" class="tag">{{ tag }}</a>
            {% endfor %}
        </div>
        {% endif %}
        
        <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 50 }}</p>
    </div>
    {% endfor %}
</div>

## Topics I Write About

- **Machine Learning & AI**: Deep learning, neural networks, and practical ML applications
- **Web Development**: Modern frameworks, best practices, and architecture patterns
- **Data Science**: Data analysis, visualization, and statistical modeling
- **Software Engineering**: Code quality, testing, and development methodologies
- **Technology Trends**: Emerging technologies and industry insights

---

*Subscribe to the [RSS feed]({{ '/feed.xml' | relative_url }}) to stay updated with new posts.*