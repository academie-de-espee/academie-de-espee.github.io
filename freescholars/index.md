---
layout: default
title: Roster
roster:
   - name: Marguerite de Lyon
     location: Lochmere
     date: 10/04/2015
     form: Sword and Buckler
     event: Rapier Schola in Aethelmearc
     sponsors: Master Alessandro, Master Connor, and Lady Caitilin
   - name: Linhart Von Marburg
     location: Lochmere
     date: 11/22/2014
     form:
     event: Holiday Faire
     sponsors: Master Giacomo, Lord Celric, and Lord Arghylle
   - name: Torse Hartman
     location:
     date:
     form:
     event:
     sponsors:
   - name: Angeline Falconis
     location: Lochmere
     date:
     form:
     event:
     sponsors:
   - name: Sanada Terasu
     location: Sudentorre
     date: 11/22/2014
     form:
     event: Holiday Faire
     sponsors: Master Dante, Lord Benjamin, and Lord Brian
   - name: Colin McNab
   - name: Gilig von Baden
   - name: Aedh Ua Ruaic
   - name: Gawin Kappler
   - name: Jean Maurice le Marinier
   - name: Ella de Lille
   - name: Symone de la Rochelle
   - name: William Cameron
   - name: Turvon Kuznetsov
   - name: Alyna of the Ilex
   - name: Constanza de Talavera
   - name: Kenji Yoshimoto
   - name: Alyce Blood
   - name: Etain of Sutherland
---

<table class="pure-table pure-table-bordered">
<thead>
<tr>
    <th> Name </th>
    <th> Location </th>
    <th> Date </th>
    <th> Event </th>
    <th> Sponsors </th>
    <th> Favorite Form </th>
</tr>
</thead>
<tbody>
{% assign sorted = page.roster | sort:"name" %}
{% for item in sorted %}
<tr>
    <td> {{ item.name }}</td>
    <td> {{ item.location }} </td>
    <td> {{ item.date }} </td>
    <td> {{ item.event }} </td>
    <td> {{ item.sponsors }} </td>
    <td> {{ item.form }} </td>
</tr>
{% endfor %}
</tbody>
</table>

Are you a freescholar?  Should your name be listed above?  Email [Lord Linhart Von Marburg](mailto:rmauler@gmail.com) or make a [pull request](https://github.com/academie-de-espee/academie-de-espee.github.io/pulls).
