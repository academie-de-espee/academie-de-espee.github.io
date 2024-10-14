---
title: Iron Spike
---

At Atlantia's 30 Year Celebration, in AS 46, the Free Scholars of the Academie started a new tradition for Atlantian rapier called the Iron Spike.  Following in tradition similar to the Iron Ring of numerous kingdoms, the Iron Spike is a token that must be worn by the holder at SCA events.  The holder should accept up to 3 challenges per day at official events that allow fighting, where the the victor of 3 of 5 passes gains the honor of holding the Iron Spike.

The Iron Spike was made by Lord Benjamin Lilje, and comes with a box Arghylle Buchanan, and a book provided by Lady Letia Thistelthueyt.  All challenges for the Iron Spike are recorded in the accompanying book.

{% assign total = 0 %}
{% assign defended = 0 %}
{% assign holders = 0 %}

## Current Holder

{% assign latest = site.data.ironspike | last %}
{% assign name = latest.name %}
{% assign person = site.data.people[name] %}

{% if person.op_id != null %} <a href="http://op.atlantia.sca.org/op_ind.php?atlantian_id={{person.op_id}}"> {% endif %}
{{ person.title }} {{ name }}
{% if person.op_id != null %} </a> {% endif %}

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
{% for item in site.data.ironspike %}
{% capture defended %}{{ defended | plus: item.defended }}{% endcapture %}
{% capture total %}{{ total | plus: item.defended | plus: 1}}{% endcapture %}

{% assign person = site.data.people[item.name] %}

<tr>
    <td> {{ forloop.index }} </td>
    <td>
    {% if person.op_id != null %} <a href="http://op.atlantia.sca.org/op_ind.php?atlantian_id={{person.op_id}}"> {% endif %}
    {{ person.title }} {{ item.name }}
    {% if person.op_id != null %} </a> {% endif %}
    </td>
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
        {% assign person = site.data.people[name] %}
        <tr>
            <td>
            {% if person.op_id != null %} <a href="http://op.atlantia.sca.org/op_ind.php?atlantian_id={{person.op_id}}"> {% endif %}
            {{ person.title }} {{ name }}
            {% if person.op_id != null %} </a> {% endif %}
            </td>
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
        {% capture holders %}{{ holders | plus: 1 }}{% endcapture %}
    {% endif %}
{% endfor %}
</table>

</div>
</div>

<h3> Totals </h3>
<table class="pure-table pure-table-bordered">
<thead>
<tr>
    <th> Type </th>
    <th> Count </th>
</tr>
</thead>
<tbody>
<tr> <td> Holders </td> <td> {{ holders }} </td> </tr>
<tr> <td> Defended </td> <td> {{ defended }} </td> </tr>
<tr> <td> Challenges </td> <td> {{ total }} </td> </tr>
</tbody>
</table>

Have you had the honor of holding the Iron Spike?  Should your name be listed above?  Email [Lady Virginie de Champagne](mailto:vvdelaitre@gmail.com) or make a [pull request](https://github.com/academie-de-espee/academie-de-espee.github.io/pulls).

<script src="/js/sorttable.js"></script>
