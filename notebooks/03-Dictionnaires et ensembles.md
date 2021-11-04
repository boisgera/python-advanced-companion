---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Dictionnaires

```python
d = {"a":1, "b":2, "c":3}
```

```python
d
```

```python
d["a"] # lecture
```

```python
d["d"] = 4 # écriture
```

```python
d
```

```python
del d["a"] # effacement
```

```python
d
```

```python
d["a"]
```

```python
d.get("b", 0)
```

```python
d.get("a", 0)
```

```python
for x in d:
    print(x, ":", d[x])
```

```python
"a" in d
```

```python
"b" in d
```

```python
list(d)
```

```python
for x in d.keys():
    print(x)
```

```python
for x in d.values():
    print(x)
```

```python
for x in d.items():
    print(x)
```

```python
d.update({"e": 5, "f": 6})
```

```python
d
```

```python
dir(d)
```

```python
d.pop("b")
```

```python
d
```

```python
help(d.setdefault)
```

```python
from collections import defaultdict
```

```python
help(defaultdict)
```

```python
{"kjdslkjdlsdk": 90.0}
```

```python
{1: 4, 1.0: 8, 1.5j: 0, True: 90.90}
```

```python
{(1, 2): 7, (7, 8, 9): 9}
```

```python
{(1, ("aa", "bb")): 90}
```

```python
{[2]: 90.0}
```

```python
hash(1.34)
```

```python
hash("kjskdjsjdskj")
```

```python
hash(("kjdsjdks", 909090))
```

```python
hash([1, 2, 3])
```

```python
hash((1, [2, 3]))
```

```python
def f():
    pass
import sys
d = {1: 1.0, 2: f, 3: sys}
d
```

# Ensembles

```python
{1, 2, 3, 4}
```

```python
{} # empty dict
```

```python
type({})
```

```python
set()
```

```python
set([1, 2, 3])
```

```python
set([1, 1, 2, 3, 3, 3, 4])
```

```python
list(set([1, 1, 2, 3, 3, 3, 4]))
```

```python
s = {1, 2, "djksjds", (2, 3), (2, ("jsdksjk", 90))}
```

```python
s = {[]}
```

```python
s = {1, 2, "djksjds", (2, 3), (2, ("jsdksjk", 90))}
```

```python
s.add(42)
```

```python
s
```

```python
s.remove(42)
```

```python
s
```

```python
1 in s
```

```python
for x in s:
    print(x)
```

```python
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
```

```python
s1 | s2
```

```python
s1 & s2
```

```python
s1 - s2
```

```python

```
