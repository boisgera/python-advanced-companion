---
title: Fonctions
---

Fonctions
--------------------------------------------------------------------------------

### Définitions

`def` `return`, retour réifiés (tuple), arguments positionnels ou nommés,
arguments par défaut.

``` python
def f(x, y, z=0):
    print("Please !")
    return 42
```

Mentionner type hints (ex avec Typer ?).

### Valeurs de retour

$$
\int_0^1 f(x) \, dx
$$

### Espaces de nom

Portée / scope

🇺🇸 → Namespace 

(implicites)

globals / locals (builtin module, read-only, etc.)


Invocables
--------------------------------------------------------------------------------

🇫🇷 invocable (ou appelable)  → 🇺🇸 callable (or "function-like")

On qualifie d'invocable tout objet se comportant comme une fonction,
c'est-à-dire pouvant être appelé (invoqué) avec la même syntaxe que
les fonctions.

Ainsi, l'entier `0` n'est pas invocable :

``` pycon
>>> zero = 0
>>> zero()
TypeError: 'int' object is not callable
```

La fonction sans argument qui renvoie `0` est invocable :

``` pycon
>>> def zero_fun():
...     return 0
>>> zero_fun()
0
```

ce qui n'est pas une surprise puisque c'est une fonction !

``` pycon
>>> type(zero_fun)
<class 'function'>
>>> import types
>>> isinstance(zero_fun, types.FunctionType)
True
```

L'objet `int` est également invocable :

``` pycon
>>> int()
0
```

Pourtant, ce n'est pas une function, mais un type (c'est-à-dire une classe) :

``` pycon
>>> type(int)
<class 'type'>
>>> type(int) is type
True
>>> isinstance(int, types.FunctionType)
False
```

L'invocabilité des objets Python peut être testée avec la fonction `callable` :

``` pycon
>>> callable(zero)
False
>>> callable(zero_fun)
True
>>> callable(int)
True
```

Notons que ce test permet de dire si un objet est invocable, mais pas si
on peut l'invoquer sans arguments (ni combien d'arguments sont nécessaires,
de quel type, etc.). Ainsi :

``` pycon
>>> callable(hash)
True
```

Mais
``` pycon
>>> hash()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: hash() takes exactly one argument (0 given)
```

Toutefois
``` pycon
>>> hash(2**100)
549755813888
```

Pour en savoir plus sur les arguments attendus, il faudra se reporter 
à la documentation de l'objet considéré.


### Classes

Des fois difficile de distinguer classes de fonction (ex: `np.array`) ;
factories, etc.

### Méthodes

### Custom classes

`__call__`


Fonctions génératrices
--------------------------------------------------------------------------------

Une fonction est génératrice si sa définition utilise le mot-clé `yield`.

``` python
def one_two_three():
    yield 1
    yield 2
    yield 3
```

``` pycon
>>> iterator = one_two_three()
>>> next(iterator)
1
>>> next(iterator)
2
>>> next(iterator)
3
>>> next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

``` pycon
>>> for i in one_two_three():
...     print("i:", i) 
i = 1
i = 2
i = 3
```

``` pycon
>>> list(one_two_three())
[1, 2, 3]
```

**TODO:**

  - expliquer analogie "return multiples" et flux d'exécution plus complexe
    qu'une fonction classique

  - arguments

  - code entre yields

  - exemple de flux d'exécution "complexes"

  - qq uses cases: émulation fonctionnalités itertools (AVANT: range), etc.

  - valeur de retours



Higher-order Programming
--------------------------------------------------------------------------------

Fonctions comme "valeurs" ; lambda, decorateurs ; patterns d'usage: 
math (ODEs, autograd), filters/maps, callbacks, etc.

### Usages

### Décorateurs

### Lambda

### Closures


--------------------------------------------------------------------------------

``` pycon
test ligatures: -> ==
```