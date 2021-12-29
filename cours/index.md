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

Appeler une fonction génératrice n'exécute pas son code immédiatement,
mais fournit comme valeur de retour un itérateur. Demander le premier élément
de cet itérateur exécute la fonction jusqu'à atteindre le premier 
`yield`; la fonction pause alors son exécution et renvoie la valeur 
fournie au `yield`. Demander le second objet reprend le fil de l'exécution
à ce point, jusqu'à atteindre le second `yield`, etc.

Ainsi, avec 

``` python
def one_two_three():
    yield 1
    yield 2
    yield 3
```

on obtient

``` pycon
>>> for i in one_two_three():
...     print(i)
1
2
3
```

et

``` pycon
>>> list(one_two_three())
[1, 2, 3]
```

#### Exemples ([itertools])

[itertools]: https://docs.python.org/3/library/itertools.html#module-itertools

``` python
def count(start=0, step=1):
    value = start
    while True:
        yield value
        value += step
```

``` pycon
>>> odd_numbers = count(1, 2)
>>> for number in odd_numbers:
...     print(number, sep=" ")
...     if number >= 20:
...         break
1 3 5 7 9 11 13 15 17 19 21
```

``` python
def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element
```



``` python
def repeat(object, times=None):
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object
```

``` pycon
>>> list(repeat(10, 3))
[10, 10, 10]
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