---
title: Roster of Masters
---

<table class="pure-table pure-table-bordered sortable" width="100%">
<thead>
<tr>
   <th> Name </th>
   <th> Location </th>
   <th> Date </th>
   <th> Event </th>
   <th> Reign </th>
   <th> Relationships </th>
</tr>
</thead>
<tbody>
{% assign sorted = site.data.masters | sort %}
{% for entry in sorted %}
{% assign name = entry[0] %}
{% assign item = entry[1] %}
   
{% assign byop = site.data.op[item.op_id] %}
{% assign person = site.data.people[name] %}
<tr>
  <td>
     
    {% if item.op_id != null %}
       <a href="http://op.atlantia.sca.org/op_ind.php?atlantian_id={{item.op_id}}">
    {% elsif person.op_id != null %}
       <a href="http://op.atlantia.sca.org/op_ind.php?atlantian_id={{person.op_id}}">
    {% endif %}
    
    {% if byop.title != null %} 
    {{ byop.title }}
    {% else %}
    {{ person.title }}
    {% endif %}
    {{ name }}

    {% if item.op_id != null %} </a> {% elsif person.op_id != null %} </a> {% endif %}
    </td>
    <td> {{ item.location }} </td>
    <td> {{ item.date }} </td>
    <td> {{ item.event }} </td>
    <td> {{ item.reign }} </td>
    <td> {% if item.relationships != null %}
        <ul style="margin-top:0; margin-bottom:0;">
        {% assign sorted_rels = item.relationships | sort %}
        {% for entry in sorted_rels %}
            {% assign name_rel = entry[0] %}
            {% assign item_rel = entry[1] %}
            <li> <b> {{ name_rel }} </b> : {{ item_rel }} </li>
        {% endfor %}
        </ul>
        {% endif %}
    </td>
</tr>
{% endfor %}
</tbody>
</table>

Are you a master?  Do you want your name listed above?  Email [Lady Virginie de Champagne](mailto:vvdelaitre@gmail.com) or make a [pull request](https://github.com/academie-de-espee/academie-de-espee.github.io/pulls).

<script src="/js/sorttable.js"></script>
