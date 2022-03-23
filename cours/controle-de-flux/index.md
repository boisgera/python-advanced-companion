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

Le type booléen `bool` peut prendre deux valeurs : `False` et `True`.

### Logique 

Les opérateurs logiques "non" ($\neg$), "et" ($\wedge$) et "ou" ($\vee$)
sont désignés en Python par les mot-clés `not`, `and` et `or` 
et s'évaluent comme suit :

| Symbole | Opérateur | Expression   |       | Valeur  |
|---------|-----------|:-------------|-------|---------|
| $\neg$ | `not` | `not False`  | $\to$ | `True`  |
| $\neg$ | `not` | `not True`   | $\to$ | `False` |
| $\wedge$ | `and` | `False and False` | $\to$ | `False` |
| $\wedge$ | `and` | `False and True`  | $\to$ | `False` |
| $\wedge$ | `and` | `True and False`  | $\to$ | `False` |
| $\wedge$ | `and` | `True and True`   | $\to$ | `True`  |
| $\vee$ | `or` | `False or False` | $\to$ | `False` |
| $\vee$ | `or` | `False or True`  | $\to$ | `True` |
| $\vee$ | `or` | `True or False`  | $\to$ | `True` |
| $\vee$ | `or` | `True or True`   | $\to$ | `True`  |

### Comparaison

Les objets Python peuvent être comparés au moyen des opérateurs `==` (égal)
et `!=` (différents).

``` python
>>> 0 == 0
True
>>> 0 == 1
False
>>> "A" == "A"
True
>>> "A" == "B"
False
>>> [1, 2, 3] == [1, 2, 3]
True
>>> [1, 2, 3] == [4, 5, 6]
False
```

Si les objets sont d'un ordonnés (par exemple des entiers, des nombres
flottants, etc.), on peut également utiliser `<` (inférieur strictement à),
`<=` (inférieur ou égal à), `>` (supérieur strictement à) et `>=` (supérieur
ou égal à). 

L'ordre considéré dépend du type de l'objet ; par exemple pour les chaînes
de caractère, c'est l'ordre lexicographique qui est utilisé :

``` python
>>> "ABC" < "XYZ"
True
```

### Appartenance

Les opérateurs `in` et `not in` permettent de tester l'appartenance d'un
objet à un conteneur (une liste, une chaîne de caractères, un ensemble, etc.) :

``` python
>>> 1 in [1, 2, 3]
True
>>> 0 in [0, 1, 3]
False
>>> 1 not in [1, 2, 3]
False
>>> 0 not in [1, 2, 3]
True
```

``` python
>>> 1 in set([1, 2, 3])
True
>>> 0 in set()
False
>>> "Hello" in "Hello world!"
True
>>> "x" in {"x": 0.0, "y": 1.0}
True
```

### Egalité et identité

L'égalité entre objets 
-- testée par `==` (et `!=`) -- 
est parfois appelée **égalité structurelle**.
Elle se distingue de ce qu'on appelle **identité** 
-- ou **égalité référentielle** --
et qui est testée par `is` (et `is not`).

Un exemple permet de comprendre la différence ; considérons les trois listes
`a`, `b` et `c` :

``` python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> c = b
```

Les listes `a` et `b` sont égales, ainsi que `b` et `c`, mais ne sont pas
identiques, elles ne désignent pas le même objet (en mémoire) ;
les variables `b` et `c` par contre désignent le même objet :

``` python
>>> a == b
True
>>> b == c
True
>>> a is b
False
>>> b is c
True
```

En effet les variables `b` et `c` désignent le même objet (en mémoire),
contrairement à `a` et `b`. On peut aussi s'en assurer en évaluant 
l'**identifiant** de ces objets (un entier) avec la fonction `id` :

```
>>> id(a)
140636096399680
>>> id(b)
140636098130688
>>> id(c)
140636098130688
>>> id(a) == id(b)
False
>>> id(b) == id(c)
True
```

Une conséquence importante de cette distinction : les modifications de la liste
(désignée par) `b` vont impacter la liste `c` (qui est le même objet), mais
pas la liste `a` (qui est un objet distinct) :

``` python
>>> b.append(4)
>>> b
[1, 2, 3, 4]
>>> c
[1, 2, 3, 4]
>>> a
[1, 2, 3]
```

#### ⚠️ `x is not y` diffère de `x is (not y)`  {.details}

Bien qu'étant composé de deux mot-clés séparés par un espace, `is not` est
un opérateur en tant que tel. L'expression `x is not y` est équivalente
à `not (x is y)` ... mais plus lisible ! Si l'on a besoin d'utiliser
`is` et `not` comme des opérateurs distincts, pour signifier `x is (not y)`,
il conviendra de garder les parenthèses. Ainsi, avec

``` python
>>> x = 1
>>> y = True
```

on a 

```
>>> x is not y
True
>>> x is y
False
>>> not (x is y)
True
```

mais

``` python
>>> not y
False
>>> x is (not y)
False
```


### Prédicats

`any` et `all` qqpart?

### Priorités

📖 [Référence du langage Python / Expressions / Priorité des opérateurs][precedence]

[precedence]: https://docs.python.org/3/reference/expressions.html#operator-precedence

**TODO:** expliquer priorités et "group left to right" ... sauf si ça chaine ?
(cf doc)

 1. Appel de fonction
 2. `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==`
 3. `not`
 4. `and`
 5. `or`


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

#### TODO: formes normales disjonctives encouragées (détail).


#### Quizz 

L'expression `x and not y or z` est interprétée comme:

- [ ] `x and (not (y or z))`

- [ ] `x and ((not y)) or z)`

- [ ] `(x and (not y)) or z`

#### ✨ Solution {.details}

- [ ] `x and (not (y or z))`

- [ ] `x and ((not y)) or z)`

- [x] `(x and (not y)) or z`

En effet `not` a une priorité plus élevée que `and` qui a une priorité
plus élevée que `or`.


### Conversion explicites et automatiques / implicites

⚠️ and et or (et not ? si) ne font pas de conversion implicites, c'est plus subtil.

**en quelque sorte fausse** (🇺🇸 *false-ish*) ou **en quelque sorte vraie** (🇺🇸 *true-ish*)



``` python
>>> x = None
>>> bool(x)
False
```

Expliquer en amont cas de `bool`, avec `is`, `True` et `False`

Analyse: une seule valeur (en quelque sorte) fausse par type ;
en quelque sortie faux ssi égal à cette valeur, sinon (en quelque sorte) vraie.

**🚧 TODO.** Refactorer le tableau en se basant sur cette idée d'unique valeur
fausse (qui est d'ailleurs la valeur "par défaut", quand le constructeur n'a
pas d'argument).

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

La boucle `for`

``` python
for item in iterable:
    # do something
```

Iterable: collection (listes, n-uplets, ensembles, dictionnaires, etc.), iterateur ou plus généralement itérable.

Ref: <https://docs.python.org/3/library/collections.abc.html#collections.abc.Sized>

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