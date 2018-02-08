---
---

<ul>
{% for item in site.personas %}
  <li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endfor %} 
</ul>
