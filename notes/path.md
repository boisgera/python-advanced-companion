# Mais qu'est-ce qui se PATH ?

**TL;DR.** Le fonctionnement des environnements conda repose sur la manipulation 
de la variable d'environnement `PATH` 
qui sélectionne quel fichier sera executé quand vous invoquer une commande dans 
un terminal.
Cette manipulation est permise par l'insertion par conda de code
dans un fichier de configuration qui est executé à chaque démarrage d'un 
nouveau terminal. Comme ce fichier peut également être modifié par d'autres
outils logiciels, ou édité manuellement, il est possible que le fonctionnement
de conda soit altéré et nécessite votre intervention.

## Variables d'environnements

Un certain nombre de variables d'environnements sont définies dans votre
terminal. 

    $ echo "$USER"
    boisgera
    $ echo "$HOME"
    /home/boisgera
    $ echo $CONDA_EXE
    /home/boisgera/miniconda3/bin/conda
    $ echo "$DESKTOP_SESSION"
    ubuntu

Leur valeurs conditionnent sont fonctionnement. Par exemple, pour changer
le *prompt* (ou "invite de commande") qui dans l'exemple ci-dessus est `"$ "` et
le faire indiquer en plus le nom de l'utilisateur entre parenthèses :

    $ PS1="($USER)$ "
    (boisgera)$ echo "$USER"
    boisgera
    (boisgera)$ echo "$HOME"
    /home/boisgera
    (boisgera)$ echo "the prompt is: $PS1"
    the prompt is: (boisgera)$

La commande `env` permet de lister toutes les variables d'environnements qui
sont définies.

## Commandes et `PATH`

En général, vous allez invoquer des commandes dans le terminal par leur nom,
sans spécifier où se situe le fichier qui doit être exécuté. Par exemple,
vous allez faire

    $ git commit -m "initial commit"

plutôt que 

    $ /usr/bin/git commit -m "initial commit"

Vous laissez alors au terminal le soin de découvrir que le fichier exécutable
`git` est dans le répertoire `/usr/bin`. D'ailleurs si vous avez un doute,
vous pouvez demander quel est le résultat de cette résolution :

    $ which git
    /usr/bin/git

Ce mécanisme repose sur la variable d'environnement `PATH`

    $ echo "$PATH"
    /home/boisgera/miniconda3/bin:/usr/local/bin:/usr/bin

Voilà comment interpréter cette variable `PATH` :
quand j'invoque la commande `git`, le système va d'abord
rechercher un fichier exécutable `git` dans le répertoire 
`/home/boisgera/miniconda3/bin` et l'exécuter s'il le trouve. Dans le cas
contraire, il va faire la même chose dans le répertoire `/usr/local/bin`
et à nouveau en cas d'échec, essayer dans `/usr/bin`.

## Configuration du terminal


--------------------------------------------------------------------------------
⚠️ **Quel langage de shell?** Il est possible que le langage de shell que vous 
utilisiez ne soit pas `bash` (le Bourne-again shell), mais par exemple `zsh` 
(le Z shell). 
La variable d'environnement `SHELL` devrait vous renseigner à ce sujet:

    (base) $ echo "$SHELL"
    /bin/bash

Si vous utilisez `zsh`, le fichier de configuration exécuté au démarrage d'un
terminal sera `.zshrc` et non `.bashrc`.

--------------------------------------------------------------------------------
