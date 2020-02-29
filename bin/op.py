#!/usr/bin/env python

from multiprocessing.dummy import Pool
import requests
from bs4 import BeautifulSoup
import json
import yaml

titles = [
    "Lady",
    "Lord",
    "Master",
    "Countess",
    "Count",
    "Baroness",
    "Baron",
    "Mistress",
    "Duke",
    "Viscountess",
    "Viscount",
    "Sir",
    "King",
    "Queen",
    "Prince",
    "Princess",
    "Dame",
]


def get_title(op_id):
    try:
        text = requests.get(
            "http://op.atlantia.sca.org/op_ind.php?atlantian_id=%d" % op_id
        ).text
        soup = BeautifulSoup(text, "html.parser")
        p = soup.find_all("p")[6]
        name = p.text.strip().split("\n")[0]
        for title in titles:
            if name.startswith(title + " "):
                return op_id, title
    except Exception as err:
        print("unable to get title:", err)
    return op_id, None


def do_titles(data):
    for x in data:
        name = data[x]["name"]

        for title in titles:
            if name.startswith(title + " "):
                name = name[len(title) :].strip()
                data[x]["title"] = title
                data[x]["name"] = name

        try:
            name = str(name)
        except UnicodeEncodeError:
            pass

        data[x]["name"] = name

    return data


def missing_titles(data):
    def alive_count(lst):
        alive = map(lambda x: 1 if x.isAlive() else 0, lst)
        return reduce(lambda a, b: a + b, alive)

    missing = []
    for x in data:
        if "title" not in data[x]:
            missing.append(x)

    print("need to get titles for %d people" % len(missing))
    pool = Pool(5)
    results = pool.map(get_title, missing)
    for op_id, response in results:
        if response:
            # print op_id, response
            data[op_id]["title"] = response
    return data


text = requests.get("http://op.atlantia.sca.org/atlantian_op.php").text
# with open('/tmp/atlantian_op.php', 'r') as fh:
#    text = fh.read()
soup = BeautifulSoup(text, "html.parser")

people = {}

table = soup.find_all("table")[3]
for link in table.find_all("a"):
    href = link.get("href")
    if href.startswith("/op_award.php"):
        continue
    op_id = int(href[href.rindex("=") + 1 :])
    name = link.text.strip()
    people[op_id] = {"name": name}

people = do_titles(people)

text = requests.get("http://op.atlantia.sca.org/roa.php?printable=1").text
# with open('/tmp/roa.php?printable=1', 'r') as fh:
#    text = fh.read()
soup = BeautifulSoup(text, "html.parser")

for link in soup.find_all("a"):
    href = link.get("href")
    if href is None:
        continue

    op_id = int(href[href.rindex("=") + 1 :])
    name = link.text.strip()
    if op_id not in people:
        people[op_id] = {"name": name}
    else:
        people[op_id]["name"] = name

people = do_titles(people)

for op_id in people:

    name = people[op_id]["name"]

    if "[" in name and "]" in name:
        name = name[name.index("[") + 1 : name.index("]")]

    people[op_id]["name"] = name

people = do_titles(people)

people = missing_titles(people)

by_name = {}
for op_id in people:
    name = people[op_id]["name"]

    by_name[name] = {"op_id": op_id}

    if "title" in people[op_id]:
        by_name[name]["title"] = people[op_id]["title"]

with open("_data/op.json", "w") as fh:
    fh.write(yaml.dump(people, default_flow_style=False))

with open("_data/people.yml", "w") as fh:
    fh.write(yaml.dump(by_name, default_flow_style=False))
