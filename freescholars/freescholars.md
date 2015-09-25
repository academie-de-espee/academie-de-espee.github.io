---
layout: default
title: Roster
roster:
  - name: sca name
    location: home barony
    award_date: date made a free scholar
    form: favorite weapon form
    event: event you were made a free scholar
    sponsors: your provost sponsors
    prize_date: date you played your prize
    prize_event: event you played your prize
---

<table class="pure-table pure-table-bordered">
<thead>
<tr>
    <th> # </th>
    <th> Name </th>
    <th> Date </th>
    <th> event </th>
    <th> Sponsors </th>
</tr>
</thead>
<tbody>
{% for item in page.roster %}
<tr>
    <td> {{ forloop.index }} </td>
    <td> {{ item.name }}</td>
    <td> {{ item.award_date }} </td>
    <td> {{ item.event }} </td>
    <td> {{ item.sponsors }} </td>
</tr>
{% endfor %}
</tbody>
</table>
