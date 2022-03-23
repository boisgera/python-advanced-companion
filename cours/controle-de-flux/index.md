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

## While

Boucle while:

``` python
>>> numbers = [1, 2, 3]
>>> while numbers:
...     number = numbers.pop(0)
...     print(number)
...
1
2
3
```

## `For`

La boucle `for`

``` python
>>> numbers = [1, 2, 3]
>>> for number in numbers:
...     print(number)
...
1
2
3
```

Iterable: collection (listes, n-uplets, ensembles, dictionnaires, etc.), iterateur ou plus généralement itérable.

Ref: <https://docs.python.org/3/library/collections.abc.html#collections.abc.Sized>

  - `for x in y`, types builtins

  - itérable et appels explicites (ex sur un dict)




## Sortir des boucles

L'exécution des boucles `while` et `for` peuvent être interrompue, soit pour
accéder directement à l'itération suivante, avec le mot-clé `continue`, 
soit pour interrompre définitivement la boucle, avec le mot-clé `break`.

Par exemple:

``` python
>>> i = 0
>>> while i < 6:
...     if i % 2 == 0:  # i is even
...         continue
...     print(i)
...
1
3
5
```

et 

``` python
>>> i = 0
>>> while True:
...     if i >= 3:
...         break
...     print(i)
...     i += 1
...
0
1
2
```

La même mécanique s'applique au boucles `for`. A noter la clause optionnelle
`else` associée au boucles for, qui n'est exécutée que si aucun `break` 
n'a eu lieu.

``` python
>>> for i in [1, 2, 3]:
...     print(i)
... else:
...     print("ok")
...
1
2
3
ok
```

## Fonctions

Impact sur le flux de contrôle principalement, et *un peu, ad minimima* 
sur les namespaces ? Bof, non. Par contre, parler de `return`



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
En mode interactif, l'exception se manifeste par l'affichage suivant : 

  - un **traceback** pointant vers l'origine de l'erreur :
    
    `File "<stdin>", line 1, in <module>`

    (ici assez peu instructif il faut bien l'avouer.)

  - un **type** d'exception :
  
    - `ZeroDivisionError`, 
    
    - `ValueError` et 
    
    - `TypeError`.

  - un **message** explicatif : 
  
    - `"division by zero"`, 
    
    - `"math domain error"`, 

    - `"bad operand type for abs(): 'list'"`


### Conséquence d'une exception

Lorsqu'une exception est générée en mode interactif (REPL Python, notebook Jupyter,
etc.), l'environnement gère l'exception ; 
il vous signale qu'une exception s'est produite, mais vous pouvez continuer à
taper des commandes.

En revanche dans l'exécution classique d'un programme Python classique, 
en l'absence de gestion spécifique de l'exception, la survenue d'une exception 
interrompt brutalement le programme. Par exemple, l'exécution du programme Python

``` python
# file: main.py
print("Hello")
1 / 0
print("world!")
```

conduit à

``` bash
$ python main.py
Hello
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    1 / 0
ZeroDivisionError: division by zero
```

La chaîne de caractères `"world!"` ne sera jamais affichée.

### Gestion des exceptions

🚧 **TODO** 🚧

### Lever une exception

On peut lever (générer) une exception au moyen du mot-clé `raise`.

#### Simulation

Par exemple, pour reproduire les erreurs que l'on a rencontré jusqu'à présent :

``` python
>>> # 1 / 0
>>> raise ZeroDivisionError("float division by zero")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: float division by zero
```

``` python
>>> # math.sqrt(-1)
>>> raise ValueError("math domain error")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
```

``` python
>>> # abs([])
>>> raise TypeError("bad operand type for abs(): 'list'")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bad operand type for abs(): 'list'
```

#### Un example plus réaliste
On peut rapidemeent définir une fonction factorielle :

``` python
import math

def factorial(n):
    integers = range(1, n+1) # 1, 2, 3, ..., n (iterable)
    return math.prod(integers)
```

qui donne le bon résultat "quand tout va bien"

``` python
>>> factorial(0)
1
>>> factorial(1)
1
>>> factorial(2)
2
>>> factorial(3)
6
>>> factorial(10)
3628800
>>> factorial(20)
2432902008176640000
```

Mais en cas d'erreur sur le type de l'argument, l'erreur associée est quelque
peu cryptique :

``` python
>>> factorial("100")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in factorial
TypeError: can only concatenate str (not "int") to str
```

Il est possible de faire mieux, par exemple avec le code suivant :

``` python
def factorial(n):
    if not isinstance(n, int):
        message = f"{n!r} is not an integer"
        raise TypeError(message)
    integers = range(1, n+1) # 1, 2, 3, ..., n (iterable)
    return math.prod(integers)
```

On obtiendra alors l'erreur plus explicite

```
>>> factorial("100")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in factorial
TypeError: '100' is not an integer
```

Mais même ainsi nous pouvons encore avoir des surprises. 
Ainsi, si `n` est un entier mais qu'il est strictement négatif,
`factorial` va évaluer le `math.prod([])`, qui vaut 1.

``` python
>>> factorial(-1)
1
```

Corrigeons ce défaut de notre implémentation !

``` python
def factorial(n):
    if not isinstance(n, int):
        message = f"{n!r} is not an integer."
        raise TypeError(message)
    if n < 0:
        message = f"{n} < 0."
        raise ValueError(message) 
    integers = range(1, n+1) # 1, 2, 3, ..., n (iterable)
    return math.prod(integers)
```

``` python
>>> factorial(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 7, in factorial
ValueError: -1 < 0.
```

#### “It’s easier to ask forgiveness than it is to get permission.” {.details}

Une citation de [Grace Hopper], qui correspond à un style de gestion des
erreurs classique en Python. Au lieu de tester au préalable toutes les conditions
d'erreurs possibles, ce qui peut être fastidieux, 
on "fait ce qu'on a à faire" et on l'analyse ensuite le résultat
et éventuellement on gère les erreurs qui en résultent. 
Dans le cas de
la fonction factorielle, ce style pourrait se traduire comme suit :

``` python
def factorial(n):
    try:
        if n < 0:
            message = f"{n} < 0."
            raise ValueError(message) 
        integers = range(1, n+1) # 1, 2, 3, ..., n (iterable)
        return math.prod(integers)
    except TypeError:
        message = f"{n!r} is not an integer."
        raise TypeError(message)
```

``` python
>>> factorial(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in factorial
ValueError: -1 < 0.
```

``` python
>>> factorial("100")
Traceback (most recent call last):
  File "<stdin>", line 3, in factorial
TypeError: '<' not supported between instances of 'str' and 'int'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 11, in factorial
TypeError: '100' is not an integer.
```

[Grace Hopper]: https://en.wikipedia.org/wiki/Grace_Hopper


### Exceptions & contrôle de flux

Il n'est peut-être pas évident que les exceptions -- a priori destinées à
décrire des erreurs -- fournissent un puissant mécanisme de contrôle de flux.
Et pourtant c'est bien le cas ! 

A titre d'exemple, montrons comment un exception nous permet de sortir
de plusieurs boucles imbriquées (contrairement au mot-clé `break`). 
On peut ainsi utiliser (par exemple) l'exception `StopIteration`
dans le code suivant :


``` python
>>> try:
...     for i in range(10):
...         for j in range(10):
...             for k in range(10):
...                 print(i, j, k)
...                 if i + j + k == 7:
...                     raise StopIteration() 
... except StopIteration:
...     pass
...
0 0 0
0 0 1
0 0 2
0 0 3
0 0 4
0 0 5
0 0 6
0 0 7
```

A noter que cet usage n'est pas si exotique qu'il y paraît. 
En effet, Python utilise lui-même (implicitement) l'exception `StopIteration` 
dans les boucles `for` pour signaler l'épuisement d'un itérable.

Ainsi le code 

``` python
for i in [1, 2, 3]:
    print(i)
```

est équivalent à:

``` python
it = iter([1, 2, 3])
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break
```


Misc. & Sandbox
================================================================================

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

#### skdjskd

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

#### skjdjsdlkd

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