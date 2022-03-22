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

## Booléens

Type booléen, opérateurs logiques, conversion en booléen des types built-in

### Opérateurs logiques

`not`, `and`, `or`, priorités (left-assoc. vs right-assoc).

opérateurs de comparaison

`is`, `is not`, 

``` python
(a is b) == (id(a) == id(b))
```

``` python
(a is not b) == not (a is b)
```

ordre:

`==`, `!=`, `<`, etc.

### Conversion automatiques / implicites

**en quelque sorte fausse** (🇺🇸 *false-ish*) ou **en quelque sorte vraie** (🇺🇸 *true-ish*)



``` python
>>> x = None
>>> bool(x)
False
```

Expliquer en amont cas de `bool`, avec `is`, `True` et `False`

Analyse: une seule valeur (en quelque sorte) fausse par type ;
en quelque sortie faux ssi égal à cette valeur, sinon (en quelque sorte) vraie.

| `type(x)`    | `bool(x) is False` | `bool(x) is True` |
|--------------|--------------------|-------------------|
| `bool`       | `x == False`       | `x != False`      |
| `int`        | `x == 0`           | `x != 0`          |
| `float`      | `x == 0.0`         | `x != 0.0`        |
| `complex`    | `x == 0.0j`        | `x != 0.0j`       |
| `str`        | `x == ""`          | `x != ""`         |
| `bytes`      | `x == b""`         | `x != b""`        |
| `tuple`      | `x == ()`          | `x != ()`         |
| `list`       | `x == []`          | `x != []`         |
| `set`        | `x == set()`       | `x != set()`      |
| `dict`       | `x == {}`          | `x != {}`         |

#### 🤔 Quelle est la logique de cette conversion ? {.details .info}

Pour tous les types standards listés ci-dessus : 

  - Si `x` est numérique (`bool`, `int`, `float`, `complex`), 
    il est en quelque sorte vrai si et seulement s'il est non-nul : 

    ``` python
    bool(x) == (x == 0)
    ```

  - Si `x` est un conteneur (`str`, `bytes`, `tuple`, `list`, `set`, `dict`),
    il est en quelque sorte vrai si et seulement s'il est vide :

    ``` python
    bool(x) == (len(x) == 0)
    ```

Alternative / "valeur par défaut" du type.

Singleton / `bool` et "is" ? Explication pratique / None ?

#### TODO: conseils / bonnes pratiques ? {.details}

du type éviter `if x is True`, `if todos == []` ou `if len(todos) > 0`.
Dans d'autres cas, être plus explicite (ex: `xml.etree` ou `numpy`) ?
Faire preuve de discernement.

#### TODO:

  - objets, par défaut ? `True` (sinon, à setter à `None`)

  - exploration autres types : files (tjs `True`), numpy arrays, xml element, etc. ?
    Array intéressant: pas obligé d'être convertible ; mélange de warnings,
    erreurs, et qui marche. Plus simple de ne pas se fier à la conversion
    implicite! Utiliser `.size` est le plus souvent ce que l'on veut. Sinon,
    utiliser `.any()` ou `.all()`.

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

  - `for / else`

## Fonctions

Impact sur le flux de contrôle principalement, et *un peu, ad minimima* 
sur les namespaces ?



## Exceptions

### Erreurs

En cas d'opération invalide, Python génère une erreur ; par exemple si vous 
divisez $1$ par $0$, calculez $\sqrt{-1}$ ou évaluez la valeur absolue
d'une liste vide, vous observez les messages suivants :

``` python
>>> 1.0 / 0.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: float division by zero
```

``` python
>>> import math
>>> math.sqrt(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
```

``` python
>>> abs([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bad operand type for abs(): 'list'
```

Techniquement, Python génère une erreur en **levant une exception**.
L'exception se manifeste en affichant : 

  - un **traceback** pointant vers l'origine de l'erreur :
    
    `File "<stdin>", line 1, in <module>`

    (ici assez peu instructif il faut bien l'avouer.)

  - son **type** :
  
    - `ZeroDivisionError`, 
    
    - `ValueError` et 
    
    - `TypeError`.

  - un **message** explicatif: 
  
    - `"division by zero"`, 
    
    - `"math domain error"`, 

    - `"bad operand type for abs(): 'list'"`


#### What about NumPy? {.details .info}

Les calculs erronés sont gérés différents par Python standard et NumPy. 
Là où Python standard génère des exceptions en présence de calculs invalides, 
NumPy permet d'utiliser des valeurs numériques spéciales telles que `inf` ($+\infty$)
et `nan` (Not-A-Number ou $\bot$). Ainsi:

``` python
>>> import numpy as np
>>> _ = np.seterr(all="ignore")
>>> np.float64(1.0) / np.float64(0.0)
inf
>>> np.sqrt(-1.0)
nan
```


#### Misc. Sandbox.

jdskdjslkd sdlj k jslkdj slkjd

``` python
>>> import numpy as np
>>> _ = numpy.seterr(all="ignore")
>>> np.sqrt(-1)
nan
>>> float64(1.0) / float64(0.0)
inf
```


#### ksdsmkd

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

#### ✨ Solution {.details}

- [x] A

- [x] B

- [ ] C

#### ✨ **Solution**

::: collapse :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


- [x] A

- [x] B

- [ ] C

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::