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
     location: Hawkwood
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
     location: Kappellenberg
     date:
     form:
     event:
     sponsors:
   - name: Gawin Kappler
     location: Calontir
     date:
     form:
     event:
     sponsors:
   - name: Jean Maurice le Marinier
   - name: Ella de Lille
   - name: Symone de la Rochelle
   - name: Turvon Kuznetsov
   - name: Alyna of the Ilex
   - name: Constanza de Talavera
     location: 
     date:
     form:
     event:
     sponsors: Percival Aldridge, ?, ?
   - name: Kenji Yoshimoto
     location: Bright Hills
   - name: Etain of Sutherland
     location: Nottinghill Coill
     date:
     form:
     event:
     sponsors:
   - name: Alyce / Alexander Blood
     location: Bright Hills
   - name: Angharad Melys
   - name: Anna / Adrian Collins
     location: Isenfir
     date:
     form:
     event:
     sponsors:
   - name: Bastian de la Salle
     location: Nottinghill Coill
     date:
     form:
     event:
     sponsors:
   - name: Beatrice LaGrave
   - name: Bledri Ap Llew
   - name: Briana of Skye
   - name: Calledon of Halbourne
   - name: Corun MacAnndra
   - name: Donovan Morgan
   - name: Duarte Negin de los Angeles y Blanco
   - name: Duncan MacLaren
   - name: Fredrick von Heinrich
   - name: Galen of Black Diamond
     location: Buckston-on-Eno 
     date:
     form:
     event:
     sponsors:
   - name: Gaston du Valmont
     location: Elvegast
     date:
     form:
     event:
     sponsors:
   - name: Gavin Briare
     location: 
     date:
     form:
     event:
     sponsors: Katherine Maunsel, ?, ?
   - name: Giovan Donato
     location: Buckston-on-Eno
     date:
     form:
     event:
     sponsors:
   - name: Iacopo Attaviano da Vizzi
   - name: Jack Wright
   - name: Jehan-Franc de Blauvac
   - name: Kostantin Volkovitch (Kostka)
   - name: Lucien de la Rochelle
   - name: Margaret Cameron
   - name: Marion le Red
     location: Elvegast?
     date:
     form:
     event:
     sponsors:
   - name: Matilda Grille (Tilly)
   - name: Orlando de Olivares Y Salazar
   - name: Penelope Blood
   - name: Séamus Ó Maoil Riain
   - name: Thorbrandr Olafsson
   - name: Thorgrimr inn Kyrri
   - name: William Cameron
     location: Caer Mear 
     date:
     form:
     event:
     sponsors:
   - name: Ylsa Broussard
---

<table class="pure-table pure-table-bordered">
<thead>
<tr>
    <th> Name </th>
    <th> Location </th>
    <th> Date </th>
    <th> Event </th>
    <th> Sponsors </th>
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
</tr>
{% endfor %}
</tbody>
</table>

Are you a freescholar?  Should your name be listed above?  Email [Lord Linhart Von Marburg](mailto:rmauler@gmail.com) or make a [pull request](https://github.com/academie-de-espee/academie-de-espee.github.io/pulls).
