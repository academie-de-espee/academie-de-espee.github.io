#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import json

a = requests.get("https://op.atlantia.sca.org/monarchs.php?printable=1&").content
soup = BeautifulSoup(a, "html.parser")
table = soup("table")[0]
tr = table.findAll("tr", recursive=False)[0]

reigns = [{}]

for row in tr.findAll("tr"):
    cells = row.findAll("td")
    if not len(cells):
        continue
    assert len(cells) == 5, repr(cells)

    reign = int(cells[0].text)
    reigns += [{"year": cells[1].text, "King": cells[2].text, "Queen": cells[3].text}]

assert len(reigns) > 1

with open("_data/reigns.json", "w") as fh:
    json.dump(reigns, fh, sort_keys=True, indent=4)
