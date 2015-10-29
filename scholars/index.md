---
layout: default
title: Roster of Scholars
roster:
   - name: What your name listed?
     location: Lochmere
     form: 
---

<table class="pure-table pure-table-bordered">
<thead>
<tr>
    <th> Name </th>
    <th> Location </th>
    <th> Favorite Form </th>
</tr>
</thead>
<tbody>
{% for item in page.roster %}
<tr>
    <td> {{ item.name }}</td>
    <td> {{ item.location }} </td>
    <td> {{ item.form }} </td>
</tr>
{% endfor %}
</tbody>
</table>

Are you a scholar?  Do you want your name listed above?  Email [Lord Linhart Von Marburg](mailto:rmauler@gmail.com) or make a [pull request](https://github.com/academie-de-espee/academie-de-espee.github.io/pulls).
