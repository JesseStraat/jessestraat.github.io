---
title: "Publications"
layout: gridlay
permalink: /publications/
---

## Publications

There's nothing here yet! Check back later.

<input type="text" class="pub-search" id="pubSearch" placeholder="Filter by title, author, or year...">

<div class="section-card" id="pubList">
<h3>Preprints</h3>

{% bibliography --query @online %}

<h3>Journal articles</h3>

{% bibliography --query @article %}
</div>
