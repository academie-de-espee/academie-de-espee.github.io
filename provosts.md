---
title: Roster
---

<table class="pure-table pure-table-bordered">
<thead>
<tr>
    <th> Name </th>
    <th> Date </th>
    <th> Event </th>
    <th> Monarch </th>
</tr>
</thead>
<tbody>
{% assign sorted = site.data.provosts | sort %}
{% for entry in sorted %}
{% assign name = entry[0] %}
{% assign item = entry[1] %}
{% if item.provost == false %}
{% continue %}
{% endif %}
{% assign person = site.data.op[item.op_id] %}
<tr>
    <td>

    {% if item.op_id != null %}
    <a href="http://op.atlantia.sca.org/op_ind.php?atlantian_id={{item.op_id}}">
    {% endif %}

    {{ person.title }} {{ name }}

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
