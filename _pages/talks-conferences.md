---
title: "Talks & conferences"
layout: page
permalink: /talks-conferences/
---

<div class="jumbotron">
<h2>Attended events</h2>
{% assign attended_conferences = site.data.talks-conferences | where: "role", "attended" | sort: "start_date" | reverse %}
{% for entry in attended_conferences %}
<div class="row">
  ({{ entry.start_date | date: "%B %Y" }}) <b><a href="{{entry.website}}">{{ entry.name }}</a></b> at {{ entry.location }}.{% if entry.talk_title %} <i>{{entry.talk_title}}</i>{% endif %}
</div>
{% endfor %}
</div>

<div class="jumbotron">
<h2>Seminar talks</h2>
{% assign spoken_seminars = site.data.talks-conferences | where: "role", "speaker" | sort: "start_date" | reverse %}
{% for entry in spoken_seminars %}
<div class="row">
  ({{ entry.start_date | date: "%B %Y" }}) <b><a href="{{entry.website}}">{{ entry.name }}</a></b> at {{ entry.location }}.{% if entry.talk_title %} <i>{{entry.talk_title}}</i>{% endif %}
</div>
{% endfor %}
</div>

<div class="jumbotron">
<h2>Seminars regularly attended</h2>
{% assign spoken_seminars = site.data.talks-conferences | where: "role", "regular" | sort: "start_date" | reverse %}
{% for entry in spoken_seminars %}
<div class="row">
  ({{ entry.start_date | date: "%B %Y" }}–{% if entry.end_date %}{{entry.end_date | date: "%B %Y"}}{% else %}current{% endif %}) <b><a href="{{entry.website}}">{{ entry.name }}</a></b> at {{ entry.location }}.{% if entry.talk_title %} <i>{{entry.talk_title}}</i>{% endif %}
</div>
{% endfor %}
</div>