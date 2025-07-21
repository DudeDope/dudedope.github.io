---
layout: default
---

<div class="home">
    <div class="intro">
        <h1>Welcome to My Portfolio</h1>
        <p>I'm a passionate developer focused on creating innovative solutions and sharing knowledge through technical writing. Explore my projects and insights below.</p>
    </div>

    <div class="recent-posts">
        <h2>Recent Posts</h2>
        
        <div class="post-list">
            {% for post in site.posts limit:5 %}
            <div class="post-item">
                <h3>
                    <a class="post-link" href="{{ post.url | relative_url }}">
                        {{ post.title | escape }}
                    </a>
                </h3>
                <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>
                <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
            </div>
            {% endfor %}
        </div>

        <p><a href="{{ "/blog/" | relative_url }}">View all posts →</a></p>
    </div>
</div>