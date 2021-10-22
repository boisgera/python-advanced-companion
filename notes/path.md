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

## Commandes et `PATH`

## Configuration du terminal


--------------------------------------------------------------------------------
⚠️ **Quel langage de shell?** Il est possible que le langage de shell que vous 
utilisiez ne soit pas `bash` (le Bourne-again shell), mais par exemple `zsh` 
(le Z shell). 
La variable d'environnement `SHELL` devrait vous renseigner à ce sujet:

    (base) $ echo "$SHELL"
    /bin/bash

Si vous utilisez zsh, le fichier de configuration exécuté au démarrage d'un
terminal sera `.zshrc` et non `.bashrc`.

--------------------------------------------------------------------------------
