---
title: Roster of Members
---

<table class="pure-table pure-table-bordered sortable" width="100%">
<thead>
<tr>
   <th> Name </th>
   <th> Rank </th>
   <th> Date </th>
</tr>
</thead>
<tbody>
{% for data in site.data.members %}
{% assign rank = data[0] %}
{% assign entries = data[1] | sorted %}
{% for entry in entries %}
<tr>
	<td>
    		{% if entry.op_id != null %}
       			<a href="http://op.atlantia.sca.org/op_ind.php?atlantian_id={{entry.op_id}}">
    		{% endif %}
		{{ entry.name }}
    		{% if entry.op_id != null %}
       			</a>
    		{% endif %}
	</td>
	<td> {{ rank }} </td>
	<td> {{ entry.date }} </td>
</tr>
{% endfor %}
{% endfor %}
</tbody>
</table>

Are you a member of the Academie?  Use [this Google Form](https://forms.gle/Ti43EFchB72UCxuC8) to join, or make a [pull request](https://github.com/academie-de-espee/academie-de-espee.github.io/pulls).

<script src="/js/sorttable.js"></script>
