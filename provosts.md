---
title: Roster of Provosts
---

<table class="pure-table pure-table-bordered" width="100%">
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
    {% if item.provost == false %} {% continue %} {% endif %}
    {% assign person = site.data.op[item.op_id] %}
<tr>
    <td> <a href="http://op.atlantia.sca.org/op_ind.php?atlantian_id={{item.op_id}}"> {{ person.title }} {{ name }} </a> </td>
    <td> {{ item.date }} </td>
    <td> {{ item.event }} </td>
    <td> {{ item.monarchs }} </td>
</tr>
{% endfor %}
</tbody>
</table>
