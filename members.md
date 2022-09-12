---
title: Roster of Masters
---

<table class="pure-table pure-table-bordered sortable" width="100%">
<thead>
<tr>
   <th> Name </th>
   <th> Date </th>
   <th> Rank </th>
</tr>
</thead>
<tbody>
{% for data in site.data.members %}
{% assign rank = data[0] %}
{% assign entries = data[1] %}
{% for entry in entries %}
<tr> 
	<td> 
    		{% if entry.ael_id != null %}
       			<a href="http://op.atlantia.sca.org/op_ind.php?atlantian_id={{entry.ael_id}}">
    		{% endif %}
		{{ entry.name }} 
    		{% if entry.ael_id != null %}
       			</a>
    		{% endif %}
	</td> 
	<td> {{ entry.date }} </td> 
	<td> {{ rank }} </td> 
</tr>
{% endfor %}
{% endfor %}
</tbody>
</table>

Are you a member of the Academie?  Do you want your name listed above?  Email Lord [Nicolo Santorio](mailto:nicolo.santorio@gmail.com) or make a [pull request](https://github.com/academie-de-espee/academie-de-espee.github.io/pulls).

<script src="/js/sorttable.js"></script>
