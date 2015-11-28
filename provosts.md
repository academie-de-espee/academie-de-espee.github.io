---
title: Roster
---

<table class="pure-table pure-table-bordered">
<thead>
<tr>
    <th> # </th>
    <th> Name </th>
    <th> Date </th>
    <th> event </th>
    <th> Monarch </th>
</tr>
</thead>
<tbody>
{% for item in site.data.provosts %}
<tr>
    <td> {{ forloop.index }} </td>
    <td> {{ item.name }}</td>
    <td> {{ item.award_date }} </td>
    <td> {{ item.event }} </td>
    <td> {{ item.monarchs }} </td>
</tr>
{% endfor %}
</tbody>
</table>
