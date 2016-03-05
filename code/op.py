#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import json
import yaml

#text = requests.get('http://op.atlantia.sca.org/atlantian_op.php?printable=1').text
with open('/tmp/atlantian_op.php', 'r') as fh:
    text = fh.read()
soup = BeautifulSoup(text)

people = {}

table = soup.find_all('table')[3]
for link in table.find_all('a'):
    href = link.get('href')
    if href.startswith('/op_award.php'):
        continue
    op_id = int(href[href.rindex('=')+1:])
    name = link.text.strip()
    people[op_id] = name


#text = requests.get('http://op.atlantia.sca.org/roa.php?printable=1').text
with open('/tmp/roa.php?printable=1', 'r') as fh:
    text = fh.read()
soup = BeautifulSoup(text)

for link in soup.find_all('a'):
    href = link.get('href')
    if href is None:
        continue

    op_id = int(href[href.rindex('=')+1:])
    name = link.text.strip()
    people[op_id] = name

for op_id in people:
    name = people[op_id]
    if '[' in name and ']' in name:
        name = name[name.index('[')+1:name.index(']')]
    people[op_id] = name

with open('_data/op.json', 'w') as fh:
    fh.write(yaml.dump(people,canonical=True, explicit_start=True))
    #json.dump(people, fh, sort_keys=True, indent=4)
    #json.dump(people, fh, sort_keys=True, indent=4)
