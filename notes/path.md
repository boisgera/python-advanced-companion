# Mais qu'est-ce qui se PATH ?

⏲: 15 min.

**TL;DR.** Le fonctionnement des environnements conda repose sur la manipulation 
de la variable d'environnement `PATH` 
qui sélectionne quel fichier sera exécuté quand vous invoquer une commande dans 
un terminal.
Cette manipulation est permise par l'insertion par conda de code
dans un fichier de configuration qui est executé à chaque démarrage d'un 
nouveau terminal. Comme ce fichier peut également être modifié par d'autres
outils logiciels, ou édité manuellement, il est possible que le fonctionnement
de conda soit altéré et nécessite votre intervention.

> ℹ️ **Le terminal.** Les informations contenues dans ce document sont applicables
> au terminal Linux et Mac OS et sous Windows,
> au terminal git-bash (MinGW) ou au terminal bash associé à WSL (Windows
> Subsystem for Linux).

## Variables d'environnement

Des variables d'environnement sont définies dans votre terminal :

    $ echo "$USER"
    boisgera
    $ echo "$HOME"
    /home/boisgera
    $ echo $CONDA_EXE
    /home/boisgera/miniconda3/bin/conda
    $ echo "$DESKTOP_SESSION"
    ubuntu

Leur valeurs peuvent conditionner son fonctionnement. Par exemple, pour changer
le *prompt* (ou "invite de commande") qui dans l'exemple ci-dessus est `"$ "` et
le faire indiquer en plus le nom de l'utilisateur entre crochets, on peut
modifier la variable `PS1` :

    $ PS1="[$USER]$ "
    [boisgera]$ echo "$USER"
    boisgera
    [boisgera]$ echo "$HOME"
    /home/boisgera
    [boisgera]$ echo "the prompt is: $PS1"
    the prompt is: [boisgera]$

La commande `env` permet de lister toutes les variables d'environnements.

## Configuration du terminal

La modification que nous avons faite de l'invite de commande n'est pas définitive :
dès que nous allons ouvrir un nouveau terminal, l'invite de commande reviendra à
sa configuration par défaut. Il est possible de la rendre durable en modifiant
un fichier de configuration `.bashrc` qui est présent dans votre répertoire
racine (le contenu de la variable `HOME`).


> ⚠️ **Fichiers cachés.** Par convention, les fichiers dont le nom commence par 
> un point sont souvent cachés par défaut par les explorateurs de fichiers. 
> Il vous sera peut-être nécessaire de lui demander explicitement de les afficher 
> pour trouver votre fichier `.bashrc`.

> ⚠️ **Quel langage de shell?** Il est possible que le langage de shell que vous 
> utilisiez ne soit pas `bash` (le Bourne-again shell), mais par exemple `zsh` 
> (le Z shell). 
> La variable d'environnement `SHELL` devrait vous renseigner à ce sujet :
>
>     $ echo "$SHELL"
>     /bin/bash
>
> Si vous utilisez `zsh`, le fichier de configuration exécuté au démarrage d'un
> terminal sera `.zshrc` et non `.bashrc`.


Si j'édite mon fichier `.bashrc` en rajoutant à la fin la ligne 

    PS1="[$USER]$ "

j'aurais l'invite de commande que je souhaite dès le démarrage d'un nouveau
terminal. Faire cet ajout à la fin du fichier m'assure qu'il n'y aura pas
un bout de code qui va modifier ultérieurement la variable `PS1`.

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

## Environnements conda

Conda manipule la variable `PATH` pour isoler les environnements
conda que vous créez. Dans l'environnement de base conda vous pouvez ainsi avoir :

    (base) $ echo $PATH
    /home/boisgera/miniconda3/bin:/usr/local/bin:/usr/bin
    (base) $ which python
    /home/boisgera/miniconda3/bin/python
    (base) boisgera@oddball:~$ python
    Python 3.8.8 (default, Feb 24 2021, 21:46:12) 
    [GCC 7.3.0] :: Anaconda, Inc. on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

Mais si vous créez un environnement conda `my_project` :

    (base) boisgera@oddball:~$ conda create --name my_project 
    ...

alors l'activer va changer la valeur de `PATH` :

    (base) $ echo $PATH
    /home/boisgera/miniconda3/envs/bin:/usr/local/bin:/usr/bin
    (base) $ conda activate my_project
    (my_project) $ echo $PATH
    /home/boisgera/miniconda3/envs/my_project/bin:/usr/local/bin:/usr/bin

Cela permet, une fois que l'on aura installé un nouveau python dans cet
environnement, d'accéder facilement à cette version et non à celle qui
était dans l'environnement de base (ou déjà installée ailleurs).

    (my_project) $ conda install python=3.9
    ...
    (my_project) $ which python
    /home/boisgera/miniconda3/envs/my_project/bin/python
    (my_project) boisgera@oddball:~$ python
    Python 3.9.7 (default, Sep 16 2021, 13:09:58) 
    [GCC 7.5.0] :: Anaconda, Inc. on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

Pour permettre cela, conda insère dans votre fichier `.bashrc` un fragment de
code, qui doit ressembler à :

    # >>> conda initialize >>>
    # !! Contents within this block are managed by 'conda init' !!
    __conda_setup="$('/home/boisgera/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
        eval "$__conda_setup"
    else
        if [ -f "/home/boisgera/miniconda3/etc/profile.d/conda.sh" ]; then
            . "/home/boisgera/miniconda3/etc/profile.d/conda.sh"
        else
            export PATH="/home/boisgera/miniconda3/bin:$PATH"
        fi
    fi
    unset __conda_setup
    # <<< conda initialize <<<

Ce fragment va notamment modifier le `PATH` pour que les commandes
soient recherchées en priorité dans les fichiers installés par conda.

Mais ce système est relativement fragile ! Ainsi, si quelqu'un modifie ce
fichier de configuration et rajoute **après** le fragment de code 
conda quelque chose comme

    PATH="/home/boisgera/.local/bin:$PATH"

et qu'il existe un fichier exécutable `python` dans le repertoire 
`/home/boisgera/.local/bin`, c'est lui qui sera exécuté
lorsque vous invoquerez la commande `python`, même si vous êtes
dans un environnement conda ...
