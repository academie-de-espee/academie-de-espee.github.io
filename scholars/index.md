---
title: Roster of Scholars
---

<table class="pure-table pure-table-bordered sortable" width="100%">
<thead>
<tr>
    <th> Name </th>
    <th> Location </th>
    <th> Favorite Form </th>
    <th> Miscellaneous </th>
</tr>
</thead>
<tbody>
{% assign sorted = site.data.scholars | sort %}
{% for entry in sorted %}
{% assign name = entry[0] %}
{% assign item = entry[1] %}
   
{% assign person = site.data.people[name] %}
<tr>
   <td>

    {% if item.op_id != null %}
        <a href="https://op.atlantia.sca.org/op_ind.php?atlantian_id={{item.op_id}}">
    {% elsif person.op_id != null %}
        <a href="https://op.atlantia.sca.org/op_ind.php?atlantian_id={{person.op_id}}">
    {% endif %}

   {{ person.title }} {{ name }}

    {% if item.op_id != null %} </a> {% elsif person.op_id != null %} </a> {% endif %}
    </td>
    <td> {{ item.location }} </td>
    <td> {{ item.form }} </td>
    <td> {{ item.misc }} </td>
</tr>
{% endfor %}
</tbody>
</table>

Are you a scholar?  Do you want your name listed above?  Facebook message or email [Virginie de Champagne](mailto:vvdelaitre@gmail.com). Alternative, you can make a [pull request](https://github.com/academie-de-espee/academie-de-espee.github.io/pulls).

<script src="/js/sorttable.js"></script>
