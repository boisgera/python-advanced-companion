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

On qualifie d'invocable (ou appelable ; 🇺🇸 : callable) tout objet se 
comportant comme une fonction, 
c'est-à-dire pouvant être appelé (invoqué) avec la même syntaxe que les fonctions.

Ainsi, l'entier `0` n'est pas invocable :

``` python
>>> zero = 0
>>> zero()
TypeError: 'int' object is not callable
```

mais la fonction sans argument qui renvoie `0` est invocable :

``` python
>>> def zero_fun():
...     return 0
>>> zero_fun()
0
```

ce qui n'est pas une surprise puisque c'est une fonction !

``` python
>>> type(zero_fun)
<class 'function'>
>>> import types
>>> isinstance(zero_fun, types.FunctionType)
True
```
L'invocabilité des objets Python peut être testée avec la fonction `callable` :

``` python
>>> callable(zero)
False
>>> callable(zero_fun)
True
```

Notons que ce test permet de dire si un objet est invocable, mais pas si
on peut l'invoquer sans arguments (ni combien d'arguments sont nécessaires,
de quel type, etc.). Ainsi :

``` python
>>> callable(hash)
True
```

Mais
``` python
>>> hash()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: hash() takes exactly one argument (0 given)
```

Toutefois
``` python
>>> hash(2**100)
549755813888
```

Pour en savoir plus sur les arguments attendus, il faudra se reporter 
à la documentation de l'objet considéré.


### Types

Un objet comme `int` est également invocable :

``` python
>>> callable(int)
True
```

ce que l'on peut rapidement confirmer expérimentalement :

``` python
>>> int()
0
>>> int(0.0)
0
>>> int("0")
0
```

Pourtant, ce n'est pas une function, mais un type :

``` python
>>> type(int)
<class 'type'>
>>> type(int) is type  # 🤯
True
>>> isinstance(int, types.FunctionType)
False
```

Rappelons que les types (ou classes) ont vocation, quand on les appelle,
à créer des instances du type considéré :

``` python
>>> isinstance(int(), int)
True
>>> isinstance(int(0.0), int)
True
>>> isinstance(int("0"), int)
True
```

Les classes que vous définissez sont également invocables :

``` python
class Transmogrifier:
    pass
```

``` python
>>> callable(Transmogriphier)
True
>>> transmogriphier = Transmogriphier()
>>> isinstance(transmogriphier, Transmogrifier)
True
```

### Méthodes



Un [transmogriphieur](https://calvinandhobbes.fandom.com/wiki/Transmogrifier) 
peut transformer son utilisateur en ce qu'il souhaite (par défaut, un tigre 🐯 ;
[mais on n'a pas spécifié sa taille](https://static.wikia.nocookie.net/candh/images/6/60/Tigercalvin.png/revision/latest?cb=20111208210956) !).

<!-- not rendered on Github
![[Calvin transformé en tigre](https://calvinandhobbes.fandom.com/wiki/Calvin_in_Tiger_Form_(Transmogrifier_alter_ego))](https://static.wikia.nocookie.net/candh/images/6/60/Tigercalvin.png/revision/latest?cb=20111208210956)
-->

``` python
class Transmogriphier:
    def __init__(self, turn_into="tiger"):
        self.turn_into = turn_into
    def activate(self, user):
        return self.turn_into
```

``` python
>>> transmogriphier = Transmogriphier()
>>> transmogriphier.activate("calvin")
'tiger'
```

L'opération `transmogriphier.activate("calvin")` n'est pas "atomique" : elle
consiste d'abord à obtenir l'attribut `activate` de l'objet `transmogriphier`,
puis à l'invoquer avec l'argument `"calvin"`.

``` python
>>> transmogriphy = transmogriphier.activate
>>> callable(transmogriphy)
True
>>> transmogriphy("calvin")
'tiger'
```

Cela est possible car `activate` est une méthode (liée à l'instance
`transmogriphier` de `Transmogriphier`) et est donc invocable.

``` python
>>> transmogriphy
<bound method Transmogriphier.activate ...>
>>> type(transmogriphy)
<class 'method'>
>>> import types
>>> type(transmogriphy) is types.MethodType
True
```

### Instances

Notons qu'à ce stade `Transmogriphier` est invocable et la méthode `activate`
des transmogriphieurs également. Mais les transmogriphieurs eux-même ne le sont
pas :

``` python
>>> callable(transmogriphier)
False
```

Si nous estimons que c'est préférable, nous pouvons faire en sorte qu'ils le
deviennent. Il semble assez raisonnable de faire en sorte qu'invoquer un
transmogriphieur l'active :

``` python
class Transmogriphier:
    def __init__(self, turn_into="tiger")
        self.turn_into = turn_into
    def activate(self, user):
        return self.turn_into
    def __call__(self, user):
        return self.activate(user)
```

``` python
>>> transmogriphier = Transmogriphier()
>>> callable(transmogriphier)
True
```

Nous pouvons alors simplifier l'usage du transmogriphieur de la façon suivante :

``` python
>>> transmogriphier("calvin")
'tiger'
```

Fonctions génératrices
--------------------------------------------------------------------------------

Une fonction est génératrice si sa définition utilise le mot-clé `yield`.

  - Appeler une fonction génératrice n'exécute pas son code immédiatement,
    mais fournit comme valeur de retour un itérateur. 
    
  - Accéder au premier élément de cet itérateur exécute la fonction jusqu'à 
    atteindre le premier `yield` ; la fonction renvoie alors la valeur fournie 
    au `yield`, puis pause son exécution.  
    
  - Accéder au second élément de cet itérateur reprend le fil de l'exécution 
    à ce point, jusqu'à atteindre le second `yield`, etc.

Ainsi, avec 

``` python
def one_two_three():
    yield 1
    yield 2
    yield 3
```

on obtient

``` python
>>> for i in one_two_three():
...     print(i)
1
2
3
```

et

``` python
>>> list(one_two_three())
[1, 2, 3]
```

#### Exemples (source: [itertools])

[itertools]: https://docs.python.org/3/library/itertools.html#module-itertools

``` python
def count(start=0, step=1):
    """
    Generate the sequence start, start + step, start + 2*step, ...
    """
    value = start
    while True:
        yield value
        value += step
```

Usage :

``` python
>>> odd_numbers = count(start=1, step=2)
>>> for number in odd_numbers:
...     if number >= 20:
...         break
...     else:
...         print(number, sep=" ")
1 3 5 7 9 11 13 15 17 19
```

--------------------------------------------------------------------------------

``` python
def cycle(iterable):
    """
    Yield all items from an iterable, then repeat the same output sequence indefinitely. 
    """
    items = list(iterable)
    if items:
        for item in items:
            yield item
```

Usage :

``` python
>>> for i, item in enumerate(cycle("ABCD")):
...     if i >= 12:
...         break
...     else:
...         print(item, sep=" ")
A B C D A B C D A B C D
```

--------------------------------------------------------------------------------

``` python
def repeat(object, n=None):
    """
    Yield object an object n times (or indefinitely if n is None).
    """
    if n is None:
        while True:
            yield object
    else:
        for i in range(n):
            yield object
```

Usage :

``` python
>>> list(repeat(10, 3))
[10, 10, 10]
```

#### Exercices

Implémentez votre propre version des fonctions standards `range`, `enumerate`
et `zip` en utilisant les fonctions génératrices.

Programmation fonctionnelle / d'ordre supérieur
--------------------------------------------------------------------------------

Définition "partielle" programmation fonctionnelle. Un trait important:

Fonctions comme "valeurs" ; lambda, decorateurs ; patterns d'usage: 
math (ODEs, autograd), filters/maps, callbacks, etc.

Définition du terme "programmation d'ordre supérieur" (que permet la programmation
fonctionnelle).



### Fonctions lambda (ou anonymes)

Les fonctions lambda en Python sont une construction qui n'augmente pas
l'expressivité du langage -- on ne peut rien faire avec des fonctions
lambda qu'on ne pouvait déjà faire avec les fonctions classiques -- 
mais permet dans certains cas d'obtenir un code plus concis.

Ainsi, pour trouver numériquement le zéro de la fonction $x \mapsto x^2 - 2$ 
entre $0$ et $2$ avec `scipy`, après avoir importé une fonction de recherche 
de racines

``` python
>>> from scipy.optimize import root_scalar as find_root
```

on peut définir la fonction qui nous intéresse, ce qui suppose de la nommer
(par exemple `f`) :

``` python
>>> def f(x):
...     return x*x - 2
```

puis appeler la routine de recherche de zéros de `scipy`

``` python
>>> find_root(f, bracket=[0, 2])
      converged: True
           flag: 'converged'
 function_calls: 9
     iterations: 8
           root: 1.4142135623731364
```

Mais on peut aussi passer l'étape préalable de définition et de nommage de 
la function, et faire cet opération à la volée, dans l'appel à `find_root`,
au moyen d'une fonction lambda :

``` python
>>> find_root(lambda x: x*x-2, bracket=[0, 2])
      converged: True
           flag: 'converged'
 function_calls: 9
     iterations: 8
           root: 1.4142135623731364
```

Le mot-clé `lambda` fait référence à la notation traditionnelle du [$\lambda$-calcul](https://fr.wikipedia.org/wiki/Lambda-calcul).


### Fermetures (de fonctions)



> Dans un langage de programmation, une fermeture ou clôture 
> (🇺🇸 : *closure*) est une fonction accompagnée de son environnement lexical.  
>
> L'environnement lexical d'une fonction est l'ensemble des variables non locales 
> qu'elle a capturées, soit par valeur (c'est-à-dire par copie des valeurs des variables), 
> soit par référence (c'est-à-dire par copie des adresses mémoires des variables).   
>
> Une fermeture est donc créée, entre autres, lorsqu'une fonction est définie 
> dans le corps d'une autre fonction et utilise des paramètres ou des variables 
> locales de cette dernière.
> 
> Source : [Wikipedia](https://fr.wikipedia.org/wiki/Fermeture_(informatique))

### Décorateurs

Les décorateurs sont un "sucre syntaxique" utilisant le symbole `@`
et facilitant la mise en d'oeuvre d'un schéma assez courant 
que nous allons illustrer sur un exemple.

Imaginons que nous ayons développé une fonction `plus_one` 

``` python
def plus_one(x):
    return x + 1
```

mais qu'en la testant dans un programme, nous trouvons son comportement mystérieux. 
Pour comprendre ce qui se passe, nous modifions sa définition pour afficher 
ses arguments et les valeurs qu'elle renvoie à chacun de ses appels.

``` python
def plus_one(x):
    print("input:", x)
    y = x + 1
    print("output:", y)
    return y
```

avec la ferme intention de retirer ce code supplémentaire une fois le mystère 
éclairci.

Ce procédé n'est toutefois pas très satisfaisant. Plutôt que de modifier
le code de `plus_one`, nous pouvons développer une fonction 
`debug` qui prendra la fonction `plus_one` comme argument
et renverra une nouvelle fonction qui fonctionne comme `plus_one` à ceci
près qu'elle affiche les arguments et la valeur de sortie :

``` python
def debug(f):
    def f_debug(x):
        print("input:", x)
        y = f(x)
        print("output:", y)
        return y
    return f_debug
```

Pour tester le code en situation réelle, il nous suffit alors de remplacer
la fonction `plus_one` classique par cette nouvelle fonction

``` python
plus_one = debug(plus_one)
```

puis d'effacer uniquement cette ligne supplémentaire une fois le mystère éclairci.

Il s'avère que le code

``` python
def plus_one(x):
    return x + 1

plus_one = debug(plus_one)
```

est équivalent à la construction suivante utilisant les décorateurs :

``` python
@debug
def plus_one(x):
    return x + 1
```

On pourra trouver cette seconde notation plus agréable et lisible !

#### Exemples

Le décorateur `count` ci-dessous peut être utilisé pour enregistrer le nombre
de fois où une fonction a été invoquée (le nombre d'appels de la fonction
est stocké dans l'attribut `count` de la fonction).

``` python
def count(f):
    def counted_f(x):
        counted_f.count += 1
        return f(x)
    counted_f.count = 0
    return counted_f
```

Par exemple, si l'on recherche à localiser l'unique zéro de la fonction 
$x \mapsto x^2 - 2$, qui est $\sqrt{2}$, on peut la définir en la décorant 
avec la fonction d'ordre supérieur `count` :

``` python
@count
def f(x):
    return x*x - 2
```

Puis procéder par itérations successives pour produire une estimation de $\sqrt{2}$ :

``` python
>>> f(0)
-2
>>> f(1)
-1
>>> f(2)
2
>>> f(1.5)
0.25
>>> f(1.4)
-0.04000000000000026
>>> f(1.45)
0.10250000000000004
>>> f(1.43)
0.04489999999999972
>>> f(1.42)
0.01639999999999997
>>> f(1.41)
-0.011900000000000244
```

Et constater à posteriori combien d'appels de la fonction `f` ont été nécessaires :

``` python
>>> f.count
9
```


