---
title: Contrôle de flux
author: 
  - "👤[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr), 
    🏦 MINES ParisTech, Université PSL"
date: "⚖️ Licence : [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
# author: ""
# license: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
---

# Intro

# Script

Déroulement linéaire du programme, ligne par ligne ...

# What if?

Exécution conditionnelle de code, "branching".

## Conditions / prédicats

Type booléen, "test", conversion en booléen des types built-in

## `If`

  - if

  - if-elif

  - if-else

  - conversion implicite en booléen.

# Boucles

## `While`

  - `while stuff`

  - `break`, `continue`

  - `while True` (?)

## `For`

  - `for x in y`, types builtins

  - itérable et appels explicites (ex sur un dict)

## Fonctions

Impact sur le flux de contrôle principalement, et *un peu, ad minimima* 
sur les namespaces ?



## Exceptions

``` pycon
>>> abs(-1.0)
1.0
>>> abs("Hello!")
Traceback (most recent call last):
...
TypeError: bad operand type for abs(): 'str'
```

``` pycon
>>> import math
>>> math.sqrt(-1)
Traceback (most recent call last):
...
ValueError: math domain error
```

``` pycon
>>> int(42)
42
>>> int(42.0)
42
>>> int("42")
42
>>> int("quarante-deux")
Traceback (most recent call last):
...
ValueError: invalid literal for int() with base 10: 'quarante-deux'
```

``` pycon
>>> 1/2
0.5
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

``` pycon
>>> import math
>>> math.sqrt(4.0)
2.0
>>> math.sqrt(-4.0)
Traceback (most recent call last):
...
ValueError: math domain error
```

``` pycon
>>> import numpy as np
>>> _ = np.seterr(all="ignore")  # disable numpy warnings
>>> np.sqrt(4.0)
2.0
>>> np.sqrt(-4.0)
nan
>>> np.sqrt(-4.0 + 0.0j)
2j
```


**TODO:**

  - Exposer les conséquences des "erreurs" dans un script, comment elles
    affectent l'exécution. Ca affecte bien le flot d'exécution!

  - Montrer l'impact dans une fonction ; puis dans des fonctions imbriquées.

  - Gérer les exceptions: `try/except` 

  - "Filtrage" des exceptions attrapées (puis multiplication des filtres)

  - `Try/except/finally` 

  - re-raise ? Ou après avoir appris comment lever une exception ?

  - Lever une exception (built-in ; ça suffira)


Sandbox
================================================================================

TODO quizz:

  - metadata to enable the stuff (selectively). Enable or disable by default?

  - metadata to have radio buttons instead of checkboxes 
    (we need to provide a common name then)

#### Quizz
Whadda whadda

- [ ] A

- [ ] B

- [ ] C

#### ✨ **Solution**

::: collapse :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


- [x] A

- [x] B

- [ ] C

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::