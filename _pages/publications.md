---
title: "Publications"
layout: gridlay
sitemap: false
permalink: /publications/
---

<style>
.jumbotron{
    padding:3%;
    padding-bottom:10px;
    padding-top:10px;
    margin-top:10px;
    margin-bottom:30px;
}
</style>

## Publications
There's nothing here yet! Check back later.

<div class="jumbotron">
### Preprints
{% bibliography --query @online --query @*[eprinttype=arXiv] %}
</div>

<div class="jumbotron">
### Journal articles
{% bibliography --query @article %}
</div>