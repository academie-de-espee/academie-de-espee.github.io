---
layout: default
title: Iron Spike holders
---

At Atlantia's 30 Year Celebration, in AS 46, the Free Scholars of the Academie started a new tradition for Atlantian rapier called the Iron Spike.  Following in tradition similar to the Iron Ring of numerous kingdoms, the Iron Spike is a token that must be worn by the holder at SCA events.  The holder should accept up to 3 challenges per day at official events that allow fighting, where the the victor of 3 of 5 passes gains the honor of holding the Iron Spike.

The Iron Spike was made by Lord Benjamin Lilje, and comes with a box Arghylle Buchanan, and a book provided by Lady Letia Thistelthueyt.  All challenges for the Iron Spike are recorded in the accompanying book.


<table class="pure-table pure-table-bordered">
<thead>
<tr>
    <th> Name </th>
    <th> Times Defended </th>
</tr>
</thead>
<tbody>

{{ assign total = 0 }}
{{ assign defended = 0 }}
{% for item in site.data.ironspike %}
{% capture defended %}{{ defended | plus: item.defended }}{% endcapture %}
{% capture total %}{{ total | plus: item.defended | plus: 1}}{% endcapture %}
<tr>
    <td> {{ item.name }}
    {% if item.current != null %} (Current Holder) {% endif %}
    </td>
    <td> {{ item.defended }} </td>
</tr>
{% endfor %}
</tbody>
</table>

<br>

<table class="pure-table pure-table-bordered">
<thead>
<tr>
    <th> Total Defended </th>
    <th> Total Challenges </th>
</tr>
</thead>
<tbody>
<tr>
    <td> {{ defended }} </td>
    <td> {{ total }} </td>
</tr>
</tbody>
</table>

Have you had the honor of holding the Iron Spike?  Should your name be listed above?  Email [Lord Brian de Moray](mailto:bmc@shmoo.com) or make a [pull request](https://github.com/academie-de-espee/academie-de-espee.github.io/pulls).
