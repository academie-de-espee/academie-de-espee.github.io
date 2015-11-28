---
title: Iron Spike
---

At Atlantia's 30 Year Celebration, in AS 46, the Free Scholars of the Academie started a new tradition for Atlantian rapier called the Iron Spike.  Following in tradition similar to the Iron Ring of numerous kingdoms, the Iron Spike is a token that must be worn by the holder at SCA events.  The holder should accept up to 3 challenges per day at official events that allow fighting, where the the victor of 3 of 5 passes gains the honor of holding the Iron Spike.

The Iron Spike was made by Lord Benjamin Lilje, and comes with a box Arghylle Buchanan, and a book provided by Lady Letia Thistelthueyt.  All challenges for the Iron Spike are recorded in the accompanying book.

## Current Holder

{{ site.data.ironspike | last | map: "name" }}

<div class="pure-g">

<div class="pure-u-1 pure-u-md-1-2 pure-u-lg-1-2">

<h3> Past Holders </h3>

<table class="pure-table pure-table-bordered sortable">
<thead>
<tr>
    <th> # </th>
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
    <td> {{ forloop.index }} </td>
    <td> {{ item.name }} </td>
    <td> {{ item.defended }} </td>
</tr>
{% endfor %}
</tbody>
</table>

</div>


<div class="pure-u-1 pure-u-md-1-2 pure-u-lg-1-2">
<h3> Individual Totals </h3>
<table class="pure-table pure-table-bordered sortable">
<thead>
<tr>
    <th> Name </th>
    <th> Total Defended </th>
    <th> Total Gained </th>
</tr>
</thead>
{% assign all_names = site.data.ironspike | map: "name" | sort %}
{% assign names = all_names | join: " || "%}
{% capture names %} || {{ names }} || {% endcapture %}
{% for name in all_names %}
    {% capture current %} || {{ name }} || {% endcapture %}
    {% assign current_value = -1 %}
    {% if names contains current %}
        {% assign current_value = 0 %}
        {% assign gained = 0 %}
        <tr>
            <td> {{ name }} </td>
    {% endif %}
    {% for item in site.data.ironspike %}
        {% if name == item.name and current_value != -1 %}
            {% capture current_value %} {{ current_value | plus: item.defended }} {% endcapture %}
            {% capture gained %} {{ gained | plus: 1 }} {% endcapture %}
        {% endif %}
        {% capture names %} {{ names | replace: current, " || " }} {% endcapture %}
        {% capture names %} {{ names | replace: " ||  || ", " || " }} {% endcapture %}
    {% endfor %}
    {% if current_value != -1 %}
        <td> {{ current_value }} </td> <td> {{ gained }} </td> </tr>
    {% endif %}
{% endfor %}
</table>

</div>
</div>

<h3> Overall Totals </h3>
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

<script src="/js/sorttable.js"></script>
