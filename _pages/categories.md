---
title: "Blogs by category"
layout: page
sitemap: false
permalink: /blog/categories/
---

<a href="/blog/">← Back to blogs by date</a>

<h2>List of categories</h2>
{% assign categories = site.categories %}
<ul>
  {% for category in categories %}
  <li>
    <a href="#{{ category[0] | slugify }}">{{ category[0] }}</a>
  </li>
  {% endfor %}
</ul>

{% for category in categories %}
<h2 id="{{ category[0] | slugify }}">{{ category[0] }}</h2>
<ul>
  {% for post in category[1] %}
  <li>
    {{ post.date | date_to_string }}: <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title}}</a>
  </li>
  {% endfor %}
</ul>
{% endfor %}
