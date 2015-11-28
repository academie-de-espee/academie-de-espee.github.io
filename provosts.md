---
title: Roster
---

<table class="pure-table pure-table-bordered">
<thead>
<tr>
    <th> # </th>
    <th> Name </th>
    <th> Date </th>
    <th> Event </th>
    <th> Monarch </th>
</tr>
</thead>
<tbody>
{% for entry in site.data.provosts %}
<tr>
    {% assign name = entry[0] %}
    {% assign item = entry[1] %}
    <td> {{ forloop.index }} </td>
    <td>

    {% if item.op_id != null %}
    <a href="http://op.atlantia.sca.org/op_ind.php?atlantian_id={{item.op_id}}">
    {% endif %}

    {{ item.title }} {{ name }}

    {% if item.op_id != null %}
    </a>
    {% endif %}

    <td> {{ item.date }} </td>
    <td> {{ item.event }} </td>
    <td> {{ item.monarchs }} </td>
</tr>
{% endfor %}
</tbody>
</table>
