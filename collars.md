---
title: Legacy of Collars
---

Handing down a collar from an existing master to the newest member of the order is a common tradition in Atlantia's Order of Defense.

These are the chain of legacy thus far:

{% assign sorted = site.data.collars | sort %}
{% for collar in sorted %}
* {% for opid in collar %} {% assign byop = site.data.op[opid] %} {{ byop.name }}{% if forloop.last %}{% else %},{% endif %} {% endfor %}
{% endfor  %}
