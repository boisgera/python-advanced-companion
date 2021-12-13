🕹️ Conception orientée objet & Jeu vidéo
================================================================================

Nous allons remanier le jeu [🐍 snake.py](../games/solutions/snake.py)
mais dans une premier temps sans lui ajouter de fonctionnalités.
Nous nous contenterons de revisiter son organisation et de tenter de le rendre 
plus robuste / réutilisable / compréhensible / extensible. 
Nous tâcherons ensuite de tirer les bénéfices de cette réorganisation 
en développant – avec le minimum d'effort de développement – 
un 🤖 bot qui assistera le joueur dans la poursuite du hi-score. 


✔️ Validation
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

🐍 Un type `Snake`
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

Enfin, associer aux accesseurs `get_direction`, `set_direction`, 
`get_geometry` et `set_geometry` des propriétés `geometry` et `direction`
et adapter le code client en conséquence.

🏃 En mouvement
--------------------------------------------------------------------------------

Introduire une méthode `move` dans la classe `Snake` qui va mettre à jour
la géométrie du serpent en tenant compte de la direction courante du serpent
et de la position des fruits (à remettre à jour le cas échéant).

Adapter la boucle générale du programme  [🐍 snake.py](../games/solutions/snake.py) 
pour intégrer les développements de la classe `Snake`. Vérifier en y jouant que le comportement du jeu reste identique.

🗃️ Etat du jeu
--------------------------------------------------------------------------------

Définir une classe `State` représentant l'état à un instant donné du programme.
On souhaite pouvoir initialiser cet état par un code de la forme

``` python
state = State(
    snake=Snake([(10, 15), (11, 15), (12, 15)], DIRECTIONS["RIGHT"]), 
    fruit=(10, 10)
)
```

et que l'instance `state` expose les attributs `snake` et `fruit` (en lecture
et en écriture). 

Adapter le reste du code en conséquence. A-t'on encore besoin du mot-clé `global` ?
Pourquoi ?

Quelle autre type de fonctionnalité pourrait être prise en charge par la classe
`State` ?

⚙️ Moteur de jeu
--------------------------------------------------------------------------------

On souhaite désormais séparer aussi nettement que possible le code qui relève 
spécifiquement de notre jeu et le code générique, commun à (presque) tous les
jeux. Ce dernier type de code formera les bases d'un moteur de jeu et sera
développé dans le fichier `game.py` dans une classe `Game`. Cette classe 
devra prendre en charge l'initialisation de `pygame`, la gestion des fps, 
la récupération des évènements, etc.

On souhaite pouvoir exploiter cette classe en définissant une
classe `SnakeGame` qui hérite de la classe générique `Game` et qui régit 
le jeu du serpent. `SnakeGame` sera définie de la façon suivante :

``` python
from game import Game

class SnakeGame(Game):
    def process_events(self, events):
        snake = state.snake
        for event in events:
            if (
                event.type == pg.QUIT
                or event.type == pg.KEYDOWN
                and event.key == pg.K_q
            ):
                self.quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    snake.direction = DIRECTIONS["DOWN"]
                elif event.key == pg.K_UP:
                    snake.direction = DIRECTIONS["UP"]
                elif event.key == pg.K_RIGHT:
                    snake.direction = DIRECTIONS["RIGHT"]
                elif event.key == pg.K_LEFT:
                    snake.direction = DIRECTIONS["LEFT"]
        try:
            snake.move()
        except SystemExit as error:
            message = error.args[0]
            self.quit(error=message)

    def draw(self):
        snake = state.snake
        fruit_x, fruit_y = state.fruit
        self.caption = f"Score: {len(snake.geometry)}"
        draw_background(self.screen)
        for x, y in snake.geometry:
            draw_tile(self.screen, x, y, SNAKE_COLOR)
        draw_tile(self.screen, fruit_x, fruit_y, FRUIT_COLOR)
```

et le jeu sera lancé par :

``` python
snake_game = SnakeGame(size=(X * W, Y * H), fps=FPS)
snake_game.start()
```

Développer la classe `Game` en conséquence.

🧠 Intelligence Artificielle
--------------------------------------------------------------------------------

On souhaite faciliter la vie du joueur: lorsque celui-ci ne presse aucune touche
pendant une frame, votre programme devra prendre une décision à sa place pour
le rapprocher du fruit, en évitant de créer trop de collisions (au minimum:
en ne faisant jamais un demi-tour).

Développer une classe 🤖 `AssistedSnakeGame` qui prenne en charge cette 
fonctionnalité quand on lance le code de la façon suivante:

``` python
snake_game = AssistedSnakeGame(size=(X * W, Y * H), fps=FPS)
snake_game.start()
```
