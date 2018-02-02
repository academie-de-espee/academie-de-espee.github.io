---
title: Roster of Free Scholars
---

<table class="pure-table pure-table-bordered" width="100%">
<thead>
<tr>
    <th> Name </th>
    <th> Location </th>
    <th> Date </th>
    <th> Event </th>
    <th> Sponsors </th>
    <th> Miscellaneous </th>
</tr>
</thead>
<tbody>

{% assign sorted = site.data.freescholars | sort %}
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
    <td> {{ item.date }} </td>
    <td> {{ item.event }} </td>
    <td> {{ item.sponsors }} </td>
    <td> {{ item.misc }} </td>
</tr>
{% endfor %}
</tbody>
</table>

Are you a freescholar?  Should your name be listed above?  Email [Lord Linhart Von Marburg](mailto:rmauler@gmail.com) or make a [pull request](https://github.com/academie-de-espee/academie-de-espee.github.io/pulls).
