---
title: Interfaces de programmation applicative
author: 
  - "[Sebastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr), MINES ParisTech"
date: "Licence : [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
# author: ""
# license: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
---

🇺🇸 : Application Programming Interface (API)

Ce document fait suite à l'étude du 😷 [modèle épidémiologique SIR].

[modèle épidémiologique SIR]: https://boisgera.github.io/python-advanced-companion/tps/fonctions/


## Interface en ligne de commande

#### 🚀 Ligne de commande

Développez un fichier `SIR.py` qui affiche l'évolution jour par jour 
l'évolution pendant un an de la population de personnes infectées :

``` python
$ python SIR.py
1.00 1.07 1.15 1.23 1.32 1.42 1.52 1.62 1.74 1.86 1.99 2.13 2.27 2.43 2.59 2.77 2.95 3.14 3.35 3.57 3.80 4.04 4.29 4.55 4.83 5.12 5.42 5.74 6.06 6.40 6.75 7.11 7.48 7.86 8.25 8.65 9.05 9.46 9.87 10.28 10.69 11.10 11.50 11.89 12.28 12.66 13.03 13.39 13.73 14.05 14.36 14.66 14.93 15.18 15.40 15.61 15.78 15.93 16.06 16.15 16.22 16.26 16.28 16.27 16.24 16.18 16.11 16.01 15.89 15.75 15.60 15.42 15.23 15.02 14.80 14.57 14.32 14.07 13.80 13.53 13.25 12.96 12.68 12.39 12.10 11.82 11.54 11.26 10.98 10.70 10.43 10.16 9.89 9.62 9.36 9.10 8.85 8.60 8.35 8.11 7.88 7.65 7.42 7.21 6.99 6.79 6.58 6.39 6.20 6.01 5.83 5.65 5.48 5.31 5.15 4.99 4.84 4.69 4.55 4.41 4.27 4.14 4.01 3.89 3.77 3.65 3.54 3.43 3.33 3.23 3.13 3.03 2.94 2.85 2.77 2.68 2.60 2.52 2.45 2.38 2.31 2.24 2.17 2.11 2.05 1.99 1.94 1.88 1.83 1.78 1.73 1.68 1.63 1.59 1.55 1.50 1.46 1.42 1.39 1.35 1.31 1.28 1.25 1.21 1.18 1.15 1.12 1.09 1.07 1.04 1.01 0.99 0.96 0.94 0.92 0.89 0.87 0.85 0.83 0.81 0.79 0.78 0.76 0.74 0.73 0.71 0.70 0.68 0.67 0.65 0.64 0.63 0.61 0.60 0.59 0.58 0.57 0.56 0.55 0.54 0.53 0.52 0.51 0.50 0.49 0.48 0.47 0.46 0.46 0.45 0.44 0.43 0.43 0.42 0.41 0.41 0.40 0.39 0.39 0.38 0.38 0.37 0.37 0.36 0.36 0.35 0.35 0.34 0.34 0.33 0.33 0.33 0.32 0.32 0.31 0.31 0.31 0.30 0.30 0.30 0.29 0.29 0.29 0.29 0.28 0.28 0.28 0.27 0.27 0.27 0.27 0.27 0.26 0.26 0.26 0.26 0.25 0.25 0.25 0.25 0.25 0.25 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.22 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.25 0.25 0.25 0.25 0.25 0.25 0.26 0.26 0.26 0.26 0.26 0.27 0.27 0.27 0.27 0.27 0.28 0.28 0.28 0.28 0.29 0.29 0.29 0.29 0.30 0.30 0.30 0.31 0.31 0.31 0.32
```

#### Solution

::: collapse

``` python
import numpy as np
from scipy.integrate import solve_ivp

WEEK = 7
YEAR = 365

N = 100
beta = 1 / (WEEK)
gamma = 1 / (2 * WEEK)
omega = 1 / YEAR

S0, I0 = 99.0, 1.0
R0 = N - S0 - I0
t_span = [0.0, 5*YEAR]

def dSIR(t, SIR):
    S, I, R = SIR
    dS = omega * R - beta * I * S / N
    dI = beta * I * S / N - gamma * I
    dR = gamma * I - omega * R  
    return (dS, dI, dR)

if __name__ == "__main__":
    results = solve_ivp(
        dSIR, 
        t_span=t_span, 
        y0=(S0, I0, R0), 
        dense_output=True
    )
    sol = results["sol"]
    t = np.arange(0, 1*YEAR)
    S, I, R = sol(t)
    output = " ".join(f"{v:.2f}" for v in I)
    print(output)
```

:::

## Sparklines

On souhaite offrir en option un affichage "graphique" permettant 
d'interpréter plus facilement les résultats de la simulation.
Nous allons pour ce faire utiliser des ✨ [sparklines] et 
dans cet optique, essayer d'exploiter le projet [spark].

#### 🚀 Clone, Install, Test

  - Cloner le dépôt github du projet spark sur votre machine. 

  - Installer spark dans votre environnement en exécutant la commande

    ```
    python setup.py install
    ``` 

    ou 

    ```
    pip install .
    ``` 

    dans le répertoire racine de ce projet.

  - Tester les interfaces en ligne de commande et Python de cet outil.

#### 🚀 "Forkez" le projet

Spark serait plus facile à utiliser s'il acceptait directement des données
sous forme de nombres flottants et pas uniquement des entiers.

  - Forkez le projet sur GitHub. 
  
  - Ajoutez-lui cette fonctionnalité.

  - Mettez à jour les fichiers `README.md` et `setup.py` en conséquence.

  - Puis déployez cette nouvelle version de spark dans votre environnement.

#### 🚀 Intégration

Faites en sorte que notre application affiche des sparklines représente 
l'évolution du niveau d'infection lorsque l'option `--sparklines` est
sélectionnée :

``` python
$ python SIR.py --sparklines
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▂▂▂▂▂▂▂▃▃▃▃▃▃▃▄▄▄▄▄▅▅▅▅▅▆▆▆▆▆▇▇▇▇▇▇▇██████████████████▇▇▇▇▇▇▇▇▇▆▆▆▆▆▆▆▅▅▅▅▅▅▅▄▄▄▄▄▄▄▄▄▃▃▃▃▃▃▃▃▃▃▃▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
```

#### Solution

::: collapse

``` python
import sys
import spark

...

if "--sparklines" in sys.argv[1:]:
    spark.spark_print(I)
else:
    output = " ".join(f"{v:.2f}" for v in I)
    typer.echo(output)
```

:::


[sparklines]: https://en.wikipedia.org/wiki/Sparkline 
[spark]: https://github.com/boisgera/spark.py

## Gestion des arguments

#### 🚀 Plus d'options

  - Etudier les fonctionnalités proposées par la bibliothèque [typer]. 
    On pourra se contenter de lire l'[exemple minimal] de d'introduction
    et la section consacrée aux [options avec aide].

  - Réimplementez la fonctionnalité des sparklines en utilisant `typer`
    plutôt que `sys.argv`. Vérifiez au passage que `typer` vous donne
    "gratuitement" le support pour l'option `--help`.

  - Profitez de cette migration vers `typer` pour permettre à l'utilisateur 
    de changer la valeur du taux de contagion :

    ``` bash
    $ python SIR.py --help
    Usage: SIR.py [OPTIONS]

    Options:
      --sparklines / --no-sparklines  Output sparklines  [default: no-sparklines]
      --beta FLOAT                    Contagion rate  [default:
                                      0.14285714285714285]
      --install-completion            Install completion for the current shell.
      --show-completion               Show completion for the current shell, to
                                      copy it or customize the installation.
      --help                          Show this message and exit.
    ```

    ``` bash
    $ python SIR.py --sparklines --beta=0.8
    ▁▂▃▅▆▇███▇▇▇▆▆▅▅▅▄▄▄▄▃▃▃▃▃▂▂▂▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
    ```                                                                                                 
    ``` bash
    $ python SIR.py --sparklines --beta=0.05
    ███▇▇▇▇▇▇▇▆▆▆▆▆▆▆▅▅▅▅▅▅▅▅▅▄▄▄▄▄▄▄▄▄▄▄▄▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
    ```            

#### Solution 

::: collapse

Initialement :

``` python
import typer

...

def main(
  sparklines: bool = typer.Option(False, help="Output sparklines")
):
    if sparklines:
        spark.spark_print(I)
    else:
         output = " ".join(f"{v:.2f}" for v in I)
         typer.echo(output)

if __name__ == "__main__":
    typer.run(main)
```

puis pour supporter l'option `--beta` :

``` python
...

def main(
    sparklines: bool = typer.Option(False, help="Output sparklines"),
    beta: float = typer.Option(beta, help="Contagion rate")
):
    globals()["beta"] = beta
    results = solve_ivp(dSIR, t_span=t_span, y0=(S0, I0, R0), dense_output=True)
    sol = results["sol"]
    t = np.arange(0, 1 * YEAR)
    S, I, R = sol(t)

    if sparklines:
        spark.spark_print(I)
    else:
        output = " ".join(f"{v:.2f}" for v in I)
        typer.echo(output)

...
```

:::
                                                                                     
[typer]: https://typer.tiangolo.com/
[exemple minimal]: https://typer.tiangolo.com/#the-absolute-minimum
[options avec aide]: https://typer.tiangolo.com/tutorial/options/help/
