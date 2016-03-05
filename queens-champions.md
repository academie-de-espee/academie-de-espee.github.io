---
title: Queen's Champions
---

Atlantian queens have had a rapier champion that supports and represents them on the field of combat.  In an attempt to record our history, we've gathered information about past champions as best we can.  Have you been a champion for an Atlantian queen in the past?  Let us know.

<table class="pure-table pure-table-bordered sortable">
<thead>
<tr>
    <th> Reign </th>
    <th> Date</th>
    <th> King & Queen </th>
    <th> Champion(s) </th>
</tr>
</thead>
<tbody>

{% for item in site.data.qrc %}

{% if site.data.provosts[item.name] != null %} {% assign person = site.data.provosts[item.name] %} {% elsif site.data.freescholars[item.name] != null %} {% assign person = site.data.freescholars[item.name] %} {% else %} {% assign person = site.data.people[item.name] %} {% endif %}

<tr>
    <td> {{ item.reign }} </td>
    <td> <a href='http://op.atlantia.sca.org/awards_by_reign.php?reign_id={{item.reign}}'>{{ site.data.reigns[item.reign]['year'] }}</a></td>
    <td> {{ site.data.reigns[item.reign]['queen'] }} </td>
    <td>
    {% for i in item.opid %}
        <a href="http://op.atlantia.sca.org/op_ind.php?atlantian_id={{i}}">{{ site.data.op[i] }}</a>{% if forloop.last == false %}, {% endif %}
    {% endfor %}
    </td>
</tr>
{% endfor %}
</tbody>
</table>

<script src="/js/sorttable.js"></script>
