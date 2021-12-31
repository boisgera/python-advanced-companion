---
title: Fonctions
---

Fonctions
--------------------------------------------------------------------------------

### Aperçu (**TODO**)

``` python
def fibonacci(n, start=(0, 1)):
    "Return a list of n Fibonnaci numbers."
    result = []
    a, b = start
    while len(result) <= n:
        result.append(a)
        a, b = b, a+b
    return result
```

`def`, arguments, valeurs par défaut, arguments optionnels, signature, `return`

``` python
>>> numbers = fibonacci(10)
>>> numbers
[0, 1, 1, 2, 3, 5, 8]
>>> numbers = fibonacci(20, start=(5,8))
>>> numbers
[5, 8, 13]
```

invocation (appel), arguments optionnels, argument spécifiés par position ou
par nom.


**TODO**
`def` `return`, retour réifiés (tuple), arguments positionnels ou nommés,
arguments par défaut (immutabilité, `None`, etc.).

``` python
def f(x, y, z=0):
    print("Please !")
    return 42
```

Mentionner type hints (ex avec Typer ?).



### Espaces de noms et portées

La [**portée**](https://fr.wikipedia.org/wiki/Port%C3%A9e_(informatique))
(🇺🇸 : **scope**) d'une variable au sein d'un programme détermine la manière
dont elle est associé à une valeur. Au niveau supérieur 
(d'un fichier, d'un module, de l'interpréteur Python, etc.), 
les variables sont **globales**. Le lien entre le nom de la variable et
la valeur qu'elle désigne est décrit par le dictionnaire `globals()` :
c'est l'**espace de nom** (🇺🇸 : **namespace**) associé aux variables globales.

``` python
>>> import math
>>> message = "Hello world"
>>> def answer():
...    return 42
...
>>> globs = globals()
>>> globs["math"] is math
True
>>> globs["message"] is message
True
>>> globs["answer"] is answer
True
```

Au sein des fonctions, il y a en général des variables **locales**
à la fonction. C'est en particulier le cas des paramètres de la fonction,
et -- en l'absence d'instruction contraire -- des variables qui y sont 
assignées. Dans le corps de cette fonction, l'espace de noms associé
peut être obtenu en invoquant `locals()`.

``` python
>>> x = 1
>>> def f(y):
...     z = 3
...     locs = locals()
...     print("x" in locs)
...     print("y" in locs)
...     print("z" in locs)
... 
>>> f(2)
False
True
True
```

Il est donc possible pour une variable locale de cacher (🇺🇸 : **shadow**) une
variable globale :

``` python
>>> a = 1
>>> def f():
...     a = 2  # assigned => local
...     print(a)
...
>>> a
1
>>> f()
2
>>> a # in the global scope => the value remains unchanged
1
```

En l'absence d'un tel assignement, au sein d'une fonction, les variables
globales restent accessibles, mais donc en lecture seule :

``` python
>>> a = 1
>>> def f():
...     print(a)
...
>>> f()
1
```

Si l'on souhaite assigner une nouvelle valeur à une variable globale dans
le corps d'une fonction, il est nécessaire d'y déclarer la variable comme 
globale :

``` python
>>> a = 1
>>> def f():
...     global a
...     a = 2
...
>>> print(a)
1
>>> f()
>>> print(a)
2
```

Il existe également une portée **intégrée** (🇺🇸 : **built-in**) et en cas
de fonctions **emboitées** (🇺🇸 : **nested**), le concept de portée externe ;
cf par exemple [la description de la règle LEGB](https://realpython.com/python-scope-legb-rule/).


Invocables
--------------------------------------------------------------------------------

On qualifie d'**invocable** (ou **appelable** ; 🇺🇸 : **callable**) tout objet se 
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
mais on n'a pas spécifié la taille du tigre ! 😉).

![[Calvin transformé en tigre](https://calvinandhobbes.fandom.com/wiki/Calvin_in_Tiger_Form_(Transmogrifier_alter_ego))](https://www.nicepng.com/png/full/198-1980373_calvin-and-hobbes-png-hd-calvin-and-hobbes.png)

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

Une fonction est **génératrice** si sa définition utilise le mot-clé `yield`.

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
    Yield all items from an iterable, then repeat this output sequence indefinitely. 
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

  - Implémentez votre propre version des fonctions standards `range`, `enumerate`
et `zip` en utilisant les fonctions génératrices.

  - Revoyez la définition de la fonction `fibonacci` pour en faire une fonction
    génératrice, qui renvoie les nombres de Fibonnaci sous forme d'itérateur
    plutôt que de liste. Faites en sorte que lorsque l'argument `n` n'est
    pas fournie, l'itérateur parcoure l'intégralité de la suite.


Programmation fonctionnelle 
--------------------------------------------------------------------------------

Un des traits de la [**programmation fonctionelle**][pf], un style de programmation que
supporte (en partie) Python, est de permettre de manipuler les fonctions comme 
des objets comme les autres, pouvant être désignés par des variables, 
stockés dans des conteneurs, passés comme arguments à d'autres fonctions, etc.
Une fonction acceptant comme argument des fonctions et/ou en renvoyant
est une **fonction d'ordre supérieur** (🇺🇸 : **higher-order function**).

[pf]: https://fr.wikipedia.org/wiki/Programmation_fonctionnelle

Les librairies mathématiques exploitent souvent avec profit ces fonctions
d'ordre supérieures. Ainsi, la librairie de différentiation automatique
[Autograd] définit une fonction d'ordre supérieur `grad` qui associe à 
une fonction d'un argument réel sa dérivée :

[Autograd]: https://github.com/HIPS/autograd#autograd---

Sa documentation donne l'exemple suivant d'usage :

``` python
>>> # Thinly-wrapped numpy
>>> import autograd.numpy as np 
>>> # The only autograd function you may ever need
>>> from autograd import grad   
>>> # Define a function
>>> def tanh(x):                
...     y = np.exp(-2.0 * x)
...     return (1.0 - y) / (1.0 + y)
...
>>> # Obtain its gradient function
>>> grad_tanh = grad(tanh)       
>>> # Evaluate the gradient at x = 1.0
>>> grad_tanh(1.0)               
0.41997434161402603
>>> # Compare to finite differences
>>> (tanh(1.0001) - tanh(0.9999)) / 0.0002
0.41997434264973155
```

Un autre usage important des fonctions d'ordre supérieur est l'exploitation 
de **fonctions de rappels** (🇺🇸 : **callbacks**), notamment dans les interfaces
graphiques.

Par exemple, regardons comment est programmé l'application graphique 
donnée comme example dans [le tutoriel de la bibliothèque Tk](http://tkdocs.com/tutorial/firstexample.html#design) :

![Convertisseur de pieds en mètres](images/converter.png)

L'interface graphique est en partie définie par le code :

``` python
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
```

Retenons simplement à ce stade que `root` est la fenêtre 
principale de l'application, `feet` le champ de texte où nous rentrons la
valeur de la longueur en pieds et `meters` le champ de texte qui devra
afficher la longueur équivalent en mètres.

Pour que l'application se comporte comme voulu, 
nous définissons une fonction `calculate` qui a chaque fois qu'elle
est invoquée, lit la longueur en pied et écrit la longeur en mètres :

``` python
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
```

Puis nous créons un bouton qui **rappelle** cette fonction (de rappel)
à chaque fois qu'il est pressé :

``` python
ttk.Button(
    mainframe, 
    text="Calculate", 
    command=calculate
).grid(column=3, row=3, sticky=W)
```

Quelques labels de plus dans l'interface graphique, un peu de positionnement, 
et nous sommes prếts à lancer la boucle d'exécution du code !

``` python
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()

root.mainloop()
```

### Lambda

Les **fonctions lambda** en Python sont une construction qui n'augmente pas
l'expressivité du langage -- on ne peut rien faire avec des fonctions
lambda qu'on ne pouvait déjà faire avec les fonctions classiques -- 
mais permet dans certains cas d'obtenir un code plus concis.

Ainsi, pour trouver numériquement le zéro de la fonction $x \mapsto x^2 - 2$ 
entre $0$ et $2$ avec `scipy`, après avoir importé une fonction de recherche 
de racines

``` python
from scipy.optimize import root_scalar as find_root
```

on peut définir la fonction qui nous intéresse, ce qui suppose de la nommer
(par exemple `f`) :

``` python
def f(x):
    return x*x - 2
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

Le mot-clé `lambda` fait référence à la notation traditionnelle du 
[$\lambda$-calcul](https://fr.wikipedia.org/wiki/Lambda-calcul) ; 
on y désignerait la fonction $x \mapsto x^2+1$ par la notation 
$(\lambda x.x^2+1)$.



### Fermetures

Ainsi parlait Wikipédia :

> Dans un langage de programmation, une **fermeture** ou **clôture** 
> (🇺🇸 : **closure**) est une fonction accompagnée de son environnement lexical.  
>
> L'**environnement lexical** d'une fonction est l'ensemble des variables non locales 
> qu'elle a capturées, soit par valeur (c'est-à-dire par copie des valeurs des variables), 
> soit par référence (c'est-à-dire par copie des adresses mémoires des variables).   
>
> Une fermeture est donc créée, entre autres, lorsqu'une fonction est définie 
> dans le corps d'une autre fonction et utilise des paramètres ou des variables 
> locales de cette dernière.
> 
> Source : [![](icons/Wikipedia.svg){style="height: 1em; display: inline; vertical-align: -0.175em;"} Fermeture (informatique)](https://fr.wikipedia.org/wiki/Fermeture_(informatique))

Essayons de donner un exemple concret illustrant cette définition.

#### Evaluateur d'expression

La fonction standard `eval` permet de calculer la valeur d'expressions
représentées par des chaînes de caractères. Ainsi :

``` python
>>> x = 1 
>>> y = 2
>>> eval("x + y")
3
```

Il est également possible d'ignorer l'espace de nom global et de spécifier 
explicitement l'espace de nom que devra utiliser l'évaluateur :

``` python
>>> namespace = {"x": 3, "y": 4}
>>> eval("x + y", namespace)
```

Nous aimerions disposer d'une fonction d'ordre supérieur -- disons `fun` --
qui associe à une expression, comme `"x+y"`, une fonction qui acceptera les 
arguments nommés nécessaires pour évaler l'expression -- ici `x` et `y` --
et renverra la valeur associée de l'expression.

Avec les fermetures de fonctions, rien de plus simple :

``` python
def fun(expression):
    def f(**kwargs): 
       return eval(expression, kwargs)
    return f
```

On remarquera que `eval(expression, kwargs)` utilise la variable `kwargs` qui
est locale à `f` (car passée en paramètre). Mais elle utilise également `expression`
qui est une variable locale de `fun` ; elle appartient à l'environnement
lexical de `f` qui est donc une fermeture.

Voilà comment utiliser notre fonction `fun` :

``` python
>>> add_xy = fun("x + y")
>>> add_xy(x=4, y=5)
9
```

--------------------------------------------------------------------------------

Les variables non-locales d'une fermeture sont accessibles en lecture seule
par défaut. Pour les modifier, il faut au préalable les déclarer explicitement
comme non-locales à la fermeture. 
(La situation est donc similaire celle des variables globales exploitées 
dans les fonctions.)

Par exemple, la fonction `make_get_set` génère deux fermetures qui accèdent
à la même variable `x` (qui est locale à `make_get_set`) : `get` permet de
lire la valeur de `x` et n'a donc pas besoin de la déclarer comme non-locale ;
mais `set` doit permettre de changer la valeur de cette variable et la déclare
donc comme non-locale :

``` python
def make_get_set(x):
     def get():
         return x
     def set(value):
         nonlocal x
         x = value
     return get, set
```

Exemple d'usage de ces fonctions :

``` python
>>> get, set = make_get_set(1)
>>> get()
1
>>> set(5)
>>> get()
5
```

--------------------------------------------------------------------------------

Il est bon de savoir que les variables non-locales sont capturées par référence 
en Python, et non par valeur, ce qui peut dans certains cas rendre votre vie 
... intéressante ! 😂

Par exemple, le programmeur ayant écrit

``` python
def make_actions():
    actions = []
    for i in range(3):
        def printer():
            print(i)
        actions.append(printer)
    return actions
```

s'attend probablement à générer une liste de 3 actions qui afficheront
respectivement 0, 1 et 2 lorsqu'elles seront appelées. 
Mais comme le `i` utilisé par la fonction 
`printer` est capturé par référence, sa valeur effective est déterminée
uniquement au moment de l'appel `print(i)`. Hors à ce moment-là, la boucle
`for` a déjà été exécutée, donc `i` vaut `2`. Par conséquent, on obtient
en fait :

``` python
>>> for action in make_actions():
...     action()
2
2
2
```

Le "hack" classique pour résoudre ce problème consiste à utiliser le fait
que les arguments par défaut d'une fonction sont évalués lors de sa définition.
Par conséquent, si l'on définit :

``` python
def make_actions():
    actions = []
    for i in range(3):
        def printer(i=i):
            print(i)
        actions.append(printer)
    return actions
```

on obtient comme souhaité

``` python
>>> for action in make_actions():
...     action()
0
1
2
```


### Décorateurs

Les **décorateurs** sont un "sucre syntaxique" utilisant le symbole `@`
et facilitant la mise en d'oeuvre d'un schéma assez courant 
que nous allons illustrer sur un exemple.

Imaginons que nous ayons développé une fonction `plus_one` 

``` python
def plus_one(x):
    return x + 1
```

mais qu'en la testant dans un programme, nous trouvons son comportement mystérieux. 
Pour comprendre ce qui se passe, nous modifions sa définition pour afficher 
ses arguments et les valeurs qu'elle renvoie à chaque fois qu'elle est appelée.

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

#### Exemple

La fonction d'ordre supérieur `count` ci-dessous peut être utilisée 
en conjonction avec un décorateur pour enregistrer le nombre de fois
 où une fonction a été invoquée (le nombre d'appels de la fonction
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
avec `@count` :

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


