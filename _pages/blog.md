---
title: "Blog"
layout: page
sitemap: false
permalink: /blog/
---

<ul>
  <a href="/blog/categories">Sort by category</a>
  {% for post in site.posts %}
    <li>
      {{ post.date | date_to_string }}: <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title}}</a>
    </li>
  {% endfor %}
</ul>
