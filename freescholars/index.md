---
layout: default
title: Roster
roster:
   - name: Linhart Von Marburg
     location: Lochmere
     award_date:
     form:
     event:
     sponsors:
     prize_date:
     prize_event:
   - name: Torse Hartman
     location: 
     award_date:
     form:
     event:
     sponsors:
     prize_date:
     prize_event:
   - name: Angeline Falconis
     location: Lochmere
     award_date:
     form:
     event:
     sponsors:
     prize_date:
     prize_event:
   - name: Gilig von Baden
   - Aedh Ua Ruaic
   - Gawin Kappler
   - Jean Maurice le Marinier
   - Ella de Lille
   - Symone de la Rochelle
   - William Cameron
   - Turvon Kuznetsov
   - Alyna of the Ilex
   - Constanza de Talavera
   - Kenji Yoshimoto
   - Alyce Blood
   - Etain of Sutherland
---

<table class="pure-table pure-table-bordered">
<thead>
<tr>
    <th> Name </th>
    <th> Date </th>
    <th> Event </th>
    <th> Sponsors </th>
    <th> Favorite Form </th>
</tr>
</thead>
<tbody>
{% for item in page.roster %}
<tr>
    <td> {{ item.name }}</td>
    <td> {{ item.award_date }} </td>
    <td> {{ item.event }} </td>
    <td> {{ item.sponsors }} </td>
    <td> {{ item.form }} </td>
</tr>
{% endfor %}
</tbody>
</table>

Are you a freescholar?  Should your name be listed above?  Email [Lord Linhart Von Marburg](mailto:rmauler@gmail.com) or make a [pull request](https://github.com/academie-de-espee/academie-de-espee.github.io/pulls).
