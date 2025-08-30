---
title: Rapier Champions of Atlantia
---

For many years, Atlantian royalty have looked to rapier champions to support and represent them on the field of combat.  In an attempt to record our history, we've gathered information about past champions as best we can.  Have you been a champion for an Atlantian king or queen in the past?  Let us know.

{% for data in site.data.qrc %}
{% assign sword_type = data[0] %}
{% assign entries = data[1] %}

{% for entry in entries %}
{% assign reign_type = entry[0] %}
{% assign champions = entry[1] %}

## {{ reign_type }}'s {{ sword_type }} champions

<table class="pure-table pure-table-bordered sortable" width="100%">
<thead>
<tr>
    <th> Reign </th>
    <th> Date</th>
    <th> {{ reign_type }} </th>
    <th> Champion(s) </th>
</tr>
</thead>
<tbody>

{% for item in champions %}

{% if site.data.provosts[item.name] != null %} {% assign person = site.data.provosts[item.name] %} {% elsif site.data.freescholars[item.name] != null %} {% assign person = site.data.freescholars[item.name] %} {% else %} {% assign person = site.data.people[item.name] %} {% endif %}

<tr>
    <td> {{ item.reign }} </td>
    <td> <a href='https://op.atlantia.sca.org/awards_by_reign.php?reign_id={{item.reign}}'>{{ site.data.reigns[item.reign]['year'] }}</a></td>
    <td> {{ site.data.reigns[item.reign][reign_type] }} </td>
    <td>
    {% for i in item.opid %}
        <a href="https://op.atlantia.sca.org/op_ind.php?atlantian_id={{i}}">{{ site.data.op[i].title }} {{ site.data.op[i].name }}</a>{% if forloop.last == false %}, {% endif %}
    {% endfor %}
    </td>
</tr>
{% endfor %}
</tbody>
</table>

{% endfor %}
{% endfor %}

<script src="/js/sorttable.js"></script>
