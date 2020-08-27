---
title: Legacy of Collars
---

Handing down a collar from an existing master to the newest member of the order is a common tradition in Atlantia's Order of Defense.

These are the chain of legacy thus far:

{% for collar in site.data.collars %}
* {% for opid in collar %} {% assign byop = site.data.op[opid] %} {{ byop.name }} {% if forloop.last %}{% else %},{% endif %} {% endfor %}
{% endfor  %}
