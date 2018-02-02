---
title: Blacksword Tournaments
---

Under construction.


<table class="pure-table pure-table-bordered" width="100%">
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

    {% if item.op_id != null %}
        <a href="http://op.atlantia.sca.org/op_ind.php?atlantian_id={{item.op_id}}">
    {% elsif person.op_id != null %}
        <a href="http://op.atlantia.sca.org/op_ind.php?atlantian_id={{person.op_id}}">
    {% endif %}

    {{ name }}

    {% if item.op_id != null %} </a> {% elsif person.op_id != null %} </a> {% endif %}
    </td>
    <td> {{ item.location }} </td>
    <td> {{ item.wins }} </td>
</tr>
{% endfor %}
</tbody>
</table>

Is your total not correct?  Email [Brian de Moray](mailto:bmc@shmoo.com) or make a [pull request](https://github.com/academie-de-espee/academie-de-espee.github.io/pulls).
