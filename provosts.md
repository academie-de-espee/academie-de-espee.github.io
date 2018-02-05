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
    <th> Relationships </th>
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
    <td> {% if item.relationships != null %}
        <ul style="margin-top:0; margin-bottom:0;">
        {% assign sorted_rels = item.relationships | sort %}
        {% for entry in sorted_rels %}
            {% assign name_rel = entry[0] %}
            {% assign item_rel = entry[1] %}
            <li> <b> {{ name_rel }} </b> : {{ item_rel }} </li>
        {% endfor %}
        </ul>
        {% endif %}
    </td>
</tr>
{% endfor %}
</tbody>
</table>
