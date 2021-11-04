# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Dictionnaires

d = {"a":1, "b":2, "c":3}

d

d["a"] # lecture

d["d"] = 4 # écriture

d

del d["a"] # effacement

d

d["a"]

d.get("b", 0)

d.get("a", 0)

for x in d:
    print(x, ":", d[x])

"a" in d

"b" in d

list(d)

for x in d.keys():
    print(x)

for x in d.values():
    print(x)

for x in d.items():
    print(x)

d.update({"e": 5, "f": 6})

d

dir(d)

d.pop("b")

d

help(d.setdefault)

from collections import defaultdict

help(defaultdict)

{"kjdslkjdlsdk": 90.0}

{1: 4, 1.0: 8, 1.5j: 0, True: 90.90}

{(1, 2): 7, (7, 8, 9): 9}

{(1, ("aa", "bb")): 90}

{[2]: 90.0}

hash(1.34)

hash("kjskdjsjdskj")

hash(("kjdsjdks", 909090))

hash([1, 2, 3])

hash((1, [2, 3]))


def f():
    pass
import sys
d = {1: 1.0, 2: f, 3: sys}
d

# # Ensembles

{1, 2, 3, 4}

{} # empty dict

type({})

set()

set([1, 2, 3])

set([1, 1, 2, 3, 3, 3, 4])

list(set([1, 1, 2, 3, 3, 3, 4]))

s = {1, 2, "djksjds", (2, 3), (2, ("jsdksjk", 90))}

s = {[]}

s = {1, 2, "djksjds", (2, 3), (2, ("jsdksjk", 90))}

s.add(42)

s

s.remove(42)

s

1 in s

for x in s:
    print(x)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s1 | s2

s1 & s2

s1 - s2


