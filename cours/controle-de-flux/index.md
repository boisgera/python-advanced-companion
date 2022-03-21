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

#### ✨ **Solution**

::: collapse :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


- [x] A

- [x] B

- [ ] C

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::