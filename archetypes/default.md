---
date: '{{ .Date }}'
draft: true
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
description: ""
weight: 10
sidebar:
  enable: true
  fold: false
toc:
  enable: true
tags: []
---

<!-- 
IMPORTANT: Do NOT add an H1 header (# Title) that duplicates the title in the front matter above.
The title from the front matter is automatically used as the page title.
Start your content directly or with an H2 (## Section Title) if needed.
-->
