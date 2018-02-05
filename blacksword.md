---
title: Blacksword Tournaments
---

Under construction.


<div class="pure-g">

<div class="pure-u-1 pure-u-md-1-2 pure-u-lg-1-2">

<h3> Winners </h3>

<table class="pure-table pure-table-bordered sortable">
<thead>
<tr>
    <th> Name </th>
    <th> Location </th>
    <th> # of Wins </th>
</tr>
</thead>
<tbody>
{% assign sorted = site.data.blacksword | sort %}
{% for entry in sorted %}
{% assign name = entry[0] %}
{% assign item = entry[1] %}

{% assign person = site.data.people[name] %}

<tr>
    <td>
    {% if person.op_id != null %} <a href="http://op.atlantia.sca.org/op_ind.php?atlantian_id={{person.op_id}}"> {% endif %}
    {{ person.title }} {{ item.name }}
    {% if person.op_id != null %} </a> {% endif %}
    </td>
    <td> {{ item.location }} </td>
    <td> {{ item.wins }} </td>
</tr>
{% endfor %}
</tbody>
</table>

</div>

Is your total not correct?  Email [Brian de Moray](mailto:bmc@shmoo.com) or make a [pull request](https://github.com/academie-de-espee/academie-de-espee.github.io/pulls).
