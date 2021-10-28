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

# Généralités

```python
a = 3.14
```

```python
dir(a) # liste des attributs de a
```

```python
"type" in dir(a) # "type" n'est pas un attribute de a !
```

```python
type(a)
```

```python
isinstance(a, float)
```

```python
help(a)
```

# Types numériques


bool, int, float, complex (etc.)

```python
b = True
```

```python
c = False
```

```python
2**1000 # entiers non bornés !
```

```python
1 + 3 * 2
```

```python
2**10
```

```python
17 % 12
```

```python
17 / 12
```

```python
17 // 12
```

```python
a = 42
```

```python
bin(a)
```

```python
hex(a)
```

```python
0b101010
```

```python
0x2a
```

```python
0x2a == 42
```

```python
type(0x2a)
```

```python
3.14
```

```python
from math import sin
```

```python
sin(3.14)
```

```python
int("300")
```

```python
int(3.14)
```

```python
int(3.94)
```

```python
round(3.14)
```

```python
round(3.94)
```

```python
import math
```

```python
math.floor(3.94)
```

```python
0.1 + 0.2
```

```python
f"{0.1:.1000}"
```

```python
f"{0.2:.1000}"
```

```python
f"{0.3:.1000}"
```

```python
1j # complex number
```

```python
1j * 1j
```

```python
z = 0.7 + 0.3j
```

```python
for attribute in dir(z):
    if not attribute.startswith("_"):
        print(attribute)
```

```python
z.real
```

```python
z.imag
```

```python
z.conjugate
```

```python
z.conjugate()
```

# Conteneurs (listes et n-uplets)


## Listes

Liste de références / adresses / pointeurs (vers les données).

Taille variable, contenu modifiable.

Liste d'objets (potentiellement) hétérogènes.

```python
l = [1.0, 1.0 + 0.1j, 2, 3]
```

```python
l[1]
```

```python
l[1] = 42
```

```python
del l[1]
```

```python
l
```

```python
l.append(12)
```

```python
l
```

```python
l.extend([9, 10, 11, 12])
```

```python
l
```

```python
help(l)
```

```python
dir(l)
```

```python
help(l.index)
```

```python
l
```

```python
help(l.pop)
```

```python
l[-1]
```

```python
l.pop()
```

```python
l
```

```python
l.pop(0)
```

```python
l
```

```python
help(l.remove)
```

```python
l
```

```python
l.remove(9)
```

```python
l
```

```python
l.index(10)
```

```python
l.count(63)
```

```python
l = [1, 2]
r = l.extend([3, 4])
```

```python
r == None
```

```python
l
```

```python
l1 = [1, 2]
l2 = [3, 4]
l3 = l1 + l2
```

```python
l1
```

```python
l2 
```

```python
l3
```

```python
3 * [7, 1]
```

```python
len(l)
```

```python
for i in l:
    print(i)
```

```python
for i in range(5):
    print(i)
```

```python
range(5)
```

```python
list(range(5))
```

## N-uplets

De longueur fixe, non modifiables ("en surface")

```python
def f():
    return "ok", 3.14 # or ("ok", 3.14)
```

```python
status, value = f()
```

```python
status
```

```python
value
```

```python
result = f()
```

```python
result
```

```python
type(result)
```

```python
a = 1, 2
```

```python
b = (1, 2)
```

```python
a == b
```

```python
empty_tuple = ()
```

```python
type(empty_tuple)
```

```python
len_1_tuple = (1,)
```

```python
len_1_tuple
```

```python
(((1)))
```

```python
t = (1, 2)
t[0] = 2.0
```

```python
l = [1, 2, 3]
t = (l, 2, 3, 3)
t
```

```python
l.append(42)
t
```

# Chaînes de caractère et données binaires

```python
s = "jdslkdjsdlksj"
```

```python
r = 'kldskdmlskdms'
```

```python
"j'utilise des apostrophes"
```

```python
'j' + "'" + 'utilise des apostrophes'
```

```python
'j\'utilise des apostrophes'
```

```python
print("a\nb")
```

```python
print("a\tb")
```

```python
print("\\")
```

```python
s = "\\"
ord(s)
```

```python
hex(92)
```

```python
print("le slash est: \x5c")
```

```python
hex(ord("a")) # ascii code of "a"
```

```python
print("la lettre a: \x61")
```

```python
print("smiley: \U0001f600")
```

```python
print("\U0001f4a9")
```

```python
s = "kjdslkdjslkdsljdlksdjdslkdjs -------------------- hhhhhhhh"
```

```python
s[0:5] + s[-5:]
```

```python
len(s)
```

```python
for c in s:
    print(c)
```

```python
s = "Sébastien"
```

```python
s.encode("utf-8")
```

```python
s.encode("latin-1")
```

```python
s.encode("cp1252")
```

```python
s.encode("utf-8").decode("utf-8")
```

```python
s.encode("utf-8").decode("latin-1")
```

# Fichiers (et chemins)

```python
file = open("texte.txt", mode="w", encoding="utf-8")
```

```python
file.write("Sébastien")
```

```python
file.close()
```

```python
f = open("texte.txt", mode="r", encoding="utf-8")
```

```python
f.read()
```

```python
f = open("texte.txt", mode="br") # binary mode
```

```python
data = f.read()
data
```

```python
data.decode("utf-8")
```

```python

```
