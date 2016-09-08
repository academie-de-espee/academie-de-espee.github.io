#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import json
import yaml

def do_titles(data):
    titles = ['Lady', 'Lord', 'Master', 'Countess', 'Count', 'Baroness', 'Baron', 'Mistress', 'Duke', 'Viscountess', 'Viscount', 'Sir']
    for x in data:
        name = data[x]['name']

        for title in titles:
            if name.startswith(title + ' '):
                name = name[len(title):].strip()
                data[x]['title'] = title
                data[x]['name'] = name

        try:
            name = str(name)
        except UnicodeEncodeError:
            pass

        data[x]['name'] = name

    return data

text = requests.get('http://op.atlantia.sca.org/atlantian_op.php').text
#with open('/tmp/atlantian_op.php', 'r') as fh:
#    text = fh.read()
soup = BeautifulSoup(text)

people = {}

table = soup.find_all('table')[3]
for link in table.find_all('a'):
    href = link.get('href')
    if href.startswith('/op_award.php'):
        continue
    op_id = int(href[href.rindex('=')+1:])
    name = link.text.strip()
    people[op_id] = {'name': name}

people = do_titles(people)

text = requests.get('http://op.atlantia.sca.org/roa.php?printable=1').text
#with open('/tmp/roa.php?printable=1', 'r') as fh:
#    text = fh.read()
soup = BeautifulSoup(text)

for link in soup.find_all('a'):
    href = link.get('href')
    if href is None:
        continue

    op_id = int(href[href.rindex('=')+1:])
    name = link.text.strip()
    if op_id not in people:
        people[op_id] = {'name': name}
    else:
        people[op_id]['name'] = name

people = do_titles(people)


for op_id in people:

    name = people[op_id]['name']

    if '[' in name and ']' in name:
        name = name[name.index('[')+1:name.index(']')]

    people[op_id]['name'] = name

people = do_titles(people)

by_name = {}
for op_id in people:
    name = people[op_id]['name']

    by_name[name] = {'op_id': op_id}

    if 'title' in people[op_id]:
        by_name[name]['title'] = people[op_id]['title']

with open('_data/op.json', 'w') as fh:
    fh.write(yaml.dump(people, default_flow_style=False))

with open('_data/people.yml', 'w') as fh:
    fh.write(yaml.dump(by_name, default_flow_style=False))
