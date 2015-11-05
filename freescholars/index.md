---
layout: default
title: Roster
---

<table class="pure-table pure-table-bordered">
<thead>
<tr>
    <th> Name </th>
    <th> Location </th>
    <th> Date </th>
    <th> Event </th>
    <th> Sponsors </th>
</tr>
</thead>
<tbody>

{% assign sorted = site.data.freescholars | sort:"name" %}
{% for item in sorted | sort:"name" %}
<tr>
    <td> {{ item.name }}</td>
    <td> {{ item.location }} </td>
    <td> {{ item.date }} </td>
    <td> {{ item.event }} </td>
    <td> {{ item.sponsors }} </td>
</tr>
{% endfor %}
</tbody>
</table>

Are you a freescholar?  Should your name be listed above?  Email [Lord Linhart Von Marburg](mailto:rmauler@gmail.com) or make a [pull request](https://github.com/academie-de-espee/academie-de-espee.github.io/pulls).
