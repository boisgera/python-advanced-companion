Conception orientée objet
================================================================================

Nous allons à nouveau remanier le programme [🐍 snake.py](../games/solutions/snake.py)
mais cette fois sans lui ajouter de fonctionnalités.
Nous nous contenterons de revisiter son organisation et de tenter de le rendre 
plus robuste / réutilisable / compréhensible.


Validation
--------------------------------------------------------------------------------

Quelles sont les valeurs admissibles pour la direction du serpent ?
Implémenter une fonction `check_direction` qui prenne en argument une
direction, ne renvoie rien si la direction est admissible et lève une
exception (de type `ValueError` ou `TypeError`, à déterminer) dans le cas contraire.

De même, toutes les listes de n-uplets représentant la géométrie du serpent 
ne sont pas valides. Faire la liste des toutes les conditions qui rendent 
la géométrie du serpent invalide ; on distinguera les

  - 🐛 **bugs** qui résultent d'erreurs de programmation et ne devraient pas exister,

  - 💀 **game over** qui peuvent arriver mais doivent entrainer la fin immédiate du jeu.

Mettre en correspondance ces catégories avec un type d'exception (soit
`TypeError`, soit `ValueError`, soit `SystemExit`), puis
implémenter une fonction `check_geometry` qui prenne en argument une 
géométrie de serpent, ne renvoie rien si elle est valide et lève 
l'exception appropriée dans le cas contraire.

Un type `Snake`
--------------------------------------------------------------------------------

Implémenter une classe `Snake` encapsulant la géométrie et la direction du
serpent :

    >>> geometry = [(10, 15), (11, 15), (12, 15)]
    >>> direction = (0, 1)
    >>> snake = Snake(geometry, direction)

Le constructeur de `Snake` doit valider la géométrie et la direction
(ou lever une exception). Stocker les arguments `geometry` et `direction` 
comme les attributs de même nom de l'instance snake.

    >>> snake.geometry
    [(10, 15), (11, 15), (12, 15)]
    >>> snake.direction
    (0, 1)

A-t'on la garantie que ces attributs restent valides quel que soit l'usage
que le programmeur fasse de l'instance `snake` dans son code ? Faire
disparaître les attributs publics `geometry` et `direction` au profit
d'attributs privés `_geometry` et `_direction`, puis développer des
méthodes `get_direction` et `set_direction` permettant d'accéder à l'attribut
`_direction` en assurant sa validité 

    >>> snake.get_direction()
    (0, 1)
    >>> snake.set_direction((0, -1))
    >>> snake.get_direction()
    (0, -1)

La même stratégie peut-être s'appliquer au cas de l'attribut `_geometry` ou 
doit-elle être modifiée pour garantir la validité de cet attribut privé dans
le temps ? Si c'est le cas, comment ?

Compléter les accesseurs `get_XXX` et `set_XXX` par des propriétés nommées `XXX`
et adapter le code client en conséquence.

En mouvement
--------------------------------------------------------------------------------

Introduire une méthode `move` dans la classe `Snake` qui va mettre à jour
la géométrie du serpent en tenant compte de la direction courante du serpent
et de la position des fruits (à remettre à jour le cas échéant).

Adapter la boucle générale du programme  [🐍 snake.py](../games/solutions/snake.py) 
pour intégrer les développements de la classe `Snake`. Vérifier en y jouant que le comportement du jeu reste identique.

Options supplémentaires
--------------------------------------------------------------------------------


  - 