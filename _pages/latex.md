---
title: "LaTeX"
layout: gridlay
sitemap: false
permalink: /latex/
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

## LaTeX

This is a collection of projects I have developed in LaTeX. For more information, refer to [my CTAN](https://ctan.org/author/straat).

### Packages

<div class="jumbotron">
<h4><b>aeskwadraat</b></h4>
<a href="https://ctan.org/pkg/aeskwadraat" target="_blank"><button class="btn btn-info btn-sm">CTAN</button></a>
<a href="https://gitlab.com/iba-aes/latex-packages" target="_blank"><button class="btn btn-warning btn-sm">GIT</button></a>

This is a package catalogue for my study association A--Eskwadraat. It consists of packages for meeting notes, invoices, beamer presentations, and much more.

I largely rewrote a big chunk of the packages, added documentation and even converted parts to LaTeX3.
</div>

<div class="jumbotron">
<h4><b>reptheorem</b></h4>
<a href="https://ctan.org/pkg/reptheorem" target="_blank"><button class="btn btn-info btn-sm">CTAN</button></a>
<a href="https://github.com/jessestraat/reptheorem" target="_blank"><button class="btn btn-warning btn-sm">GIT</button></a>

When writing a large manuscript, it is sometimes beneficial to repeat a theorem (or lemma or...) at an earlier or later point for didactical purposes. However, thmtools’s built-in restatable only allows replicating theorems after they have been stated, and only in the same document.

This package solves the issue by making use of the .aux file, and also introduces its own file extension, .thm, to replicate theorems in other files.
</div>

<div class="jumbotron">
<h4><b>morederivatives</b></h4>
<a href="https://github.com/jessestraat/MoreDerivatives" target="_blank"><button class="btn btn-warning btn-sm">GIT</button></a>

This LaTeX package provides you with more options for derivatives. Not only does it include the regular and partial derivatives, but also more unorthodox ones, such as the rotated-varrho derivative.

The package was originally developed for the specific purpose of creating notation for the action of a connection \\(\nabla\\) on sections \\(s\\) along a path \\(\gamma(t)\\), being \\(\frac{\nabla(s\circ\gamma)}{\mathrm{d}t}\\). It then devolved into a collection of fun "cursed" derivative variations.
</div>

<div class="jumbotron">
<h4><b>HikeTeX</b></h4>
<a href="https://github.com/jessestraat/HikeTeX" target="_blank"><button class="btn btn-warning btn-sm">GIT</button></a>

This LaTeX package was written to create hikes for my scouting group. The route to be followed is often encoded in various puzzles. This package provides some tools for making such puzzles. I still use it regularly for the stripkaart functionality, since it works faster than alternative options.
</div>

### Templates

<div class="jumbotron">
<h4><b>Thesis template</b></h4>
<a href="https://github.com/jessestraat/thesistemplate" target="_blank"><button class="btn btn-warning btn-sm">GIT</button></a>

This template for large LaTeX projects is perfect for theses. It is developed with Utrecht University in mind. It uses several subfiles and creates a unique style.
</div>