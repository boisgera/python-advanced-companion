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

# # Généralités

a = 3.14

dir(a) # liste des attributs de a

"type" in dir(a) # "type" n'est pas un attribute de a !

type(a)

isinstance(a, float)

help(a)

# # Types numériques

# bool, int, float, complex (etc.)

b = True

c = False

2**1000 # entiers non bornés !

1 + 3 * 2

2**10

17 % 12

17 / 12

17 // 12

a = 42

bin(a)

hex(a)

0b101010

0x2a

0x2a == 42

type(0x2a)

3.14

from math import sin

sin(3.14)

int("300")

int(3.14)

int(3.94)

round(3.14)

round(3.94)

import math

math.floor(3.94)

0.1 + 0.2

f"{0.1:.1000}"

f"{0.2:.1000}"

f"{0.3:.1000}"

1j # complex number

1j * 1j

z = 0.7 + 0.3j

for attribute in dir(z):
    if not attribute.startswith("_"):
        print(attribute)

z.real

z.imag

z.conjugate

z.conjugate()

# # Conteneurs (listes et n-uplets)

# ## Listes
#
# Liste de références / adresses / pointeurs (vers les données).
#
# Taille variable, contenu modifiable.
#
# Liste d'objets (potentiellement) hétérogènes.

l = [1.0, 1.0 + 0.1j, 2, 3]

l[1]

l[1] = 42

del l[1]

l

l.append(12)

l

l.extend([9, 10, 11, 12])

l

help(l)

dir(l)

help(l.index)

l

help(l.pop)

l[-1]

l.pop()

l

l.pop(0)

l

help(l.remove)

l

l.remove(9)

l

l.index(10)

l.count(63)

l = [1, 2]
r = l.extend([3, 4])

r == None

l

l1 = [1, 2]
l2 = [3, 4]
l3 = l1 + l2

l1

l2 

l3

3 * [7, 1]

len(l)

for i in l:
    print(i)

for i in range(5):
    print(i)

range(5)

list(range(5))


# ## N-uplets
#
# De longueur fixe, non modifiables ("en surface")

def f():
    return "ok", 3.14 # or ("ok", 3.14)


status, value = f()

status

value

result = f()

result

type(result)

a = 1, 2

b = (1, 2)

a == b

empty_tuple = ()

type(empty_tuple)

len_1_tuple = (1,)

len_1_tuple

(((1)))

t = (1, 2)
t[0] = 2.0

l = [1, 2, 3]
t = (l, 2, 3, 3)
t

l.append(42)
t

# # Chaînes de caractère et données binaires

s = "jdslkdjsdlksj"

r = 'kldskdmlskdms'

"j'utilise des apostrophes"

'j' + "'" + 'utilise des apostrophes'

'j\'utilise des apostrophes'

print("a\nb")

print("a\tb")

print("\\")

s = "\\"
ord(s)

hex(92)

print("le slash est: \x5c")

hex(ord("a")) # ascii code of "a"

print("la lettre a: \x61")

print("smiley: \U0001f600")

print("\U0001f4a9")

s = "kjdslkdjslkdsljdlksdjdslkdjs -------------------- hhhhhhhh"

s[0:5] + s[-5:]

len(s)

for c in s:
    print(c)

s = "Sébastien"

s.encode("utf-8")

s.encode("latin-1")

s.encode("cp1252")

s.encode("utf-8").decode("utf-8")

s.encode("utf-8").decode("latin-1")

# # Fichiers (et chemins)

file = open("texte.txt", mode="w", encoding="utf-8")

file.write("Sébastien")

file.close()

f = open("texte.txt", mode="r", encoding="utf-8")

f.read()

f = open("texte.txt", mode="br") # binary mode

data = f.read()
data

data.decode("utf-8")


