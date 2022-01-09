---
title: Le modèle épidémiologique SIR
author: Sébastien Boisgérault, MINES ParisTech
# author: [`Sebastien.Boisgerault@mines-paristech.fr`](mailto:Sebastien.Boisgerault@mines-paristech.fr)
# license: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
---

## TODO

  - function as an arg (solve_ivp)

  - investigate default values

  - use of kwargs (large option set)

  - function as a return value (dense_output)

  - autograd jacobian

  - function as an arg 2 (events). + Higher-order : optional level

  - function factory (modèle à compartiment)

## Introduction

Le modèle épidémiologique à compartiments SIR détermine 
l'évolution dans le temps, parmi une population supposée constante de
$N$ individus, du nombre d'individus susceptibles d\'être infectés $S$,
du nombre d'individus infectés $I$ et du nombre d'individus en
rémission (n'ayant plus de symptômes cliniques) $R$ (cf. ["The SEIRS
model for infectious disease
dynamics"](https://www.nature.com/articles/s41592-020-0856-2) pour la
présentation d'un modèle plus complet).

Le paramètre $\beta>0$ représente le taux de contagion, $\gamma>0$ le
taux de guérison et $\omega>0$ le taux de perte d'immunité (ces
grandeurs sont homogènes à l'inverse d\'un temps). On définit le nombre
de reproduction de base $R_0$ par

$$
R_0 := \frac{\beta}{\gamma}
$$

En l\'absence de naissances et de morts, ces grandeurs évoluent selon
les équations :

$$
\dot{S}(t) = \omega R(t) - \beta \frac{I(t)S(t)}{N} 
$$

$$
\dot{I}(t) = \beta \frac{I(t)S(t)}{N} - \gamma  I(t) 
$$

$$
\dot{R}(t) = \gamma I(t) - \omega R(t)
$$


## Dépendances

Python 3, NumPy, SciPy, Matplotlib.

``` python
from numpy import *
from numpy.linalg import *
from matplotlib.pyplot import *
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
```

## Stuff

📖 [`scipy.integrate.solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)

``` python
WEEK = 7
YEAR = 365
```

``` python
N = 100
beta = 1 / (WEEK)
gamma = 1 / (2 * WEEK)
omega = 1 / YEAR
```

``` python
def dSIR(t, SIR):
    S, I, R = SIR
    dS = omega * R - beta * I * S / N
    dI = beta * I * S / N - gamma * I
    dR = gamma * I - omega * R  
    return (dS, dI, dR)
```

``` python
S0, I0 = 99.0, 1.0
R0 = N - S0 - I0
t_span = [0.0, 5*YEAR]
results = solve_ivp(dSIR, t_span=t_span, y0=(S0, I0, R0))
t, y = results.t, results.y
```

``` python
plt.figure()
plt.plot(t, y, "+")
plt.show()
```

## Modèles compartimentaux

(Difficulté: 💀💀💀)

Vous avez sans doute remarqué que la dynamique du modèle SIR est entièrement
déterminée par les flux existant entre les "compartiments" de population
$S$, $I$ et $R$, qui peuvent être décrits par la structure :

``` python
SIR_dynamics = {
 ("S", "I"): "beta * I * S / N",
 ("I", "R"): "gamma * I",
 ("R", "S"): "omega * R"
}
```

Au lieu d'écrire "à la main" la fonction `dSIR` comme précédemment, 
on peut définir une fonction `make_d_state` qui prend comme argument
le type de dictionnaire ci-dessus et produit automatiquement la fonction
`dSIR_auto`[^why] :

[^why]: on peut ainsi éviter les erreurs dans la traduction du modèle de 
flux en équations différentielles, définir plus rapidement de nouveaux
modèles compartimentaux, etc.

``` python
dSIR_manu = dSIR
dSIR_auto = make_dstate(SIR_dynamics)
```

On vérifiera que les comportements de la version manuelle et automatique sont
identiques. Par exemple :

``` python
>>> dSIR_manu(0.0, (1/3, 1/3, 1/3))
(0.0007545118504022613, -0.023650793650793648, 0.02289628180039139)
>>> dSIR_auto(0.0, (1/3, 1/3, 1/3))
(0.0007545118504022613, -0.023650793650793648, 0.02289628180039139)
```

#### Solution

::: collapse

``` python
def make_dstate(dynamics):
    vars = []
    for s, t in dynamics.keys():
        if s not in vars:
            vars.append(s)
        if t not in vars:
            vars.append(t)
    n = len(vars)
    
    def fun(t, state):
        ns = globals().copy()
        for var, value in zip(vars, state):
            ns[var] = value
        dstate = []
        for i in range(n):
            d = 0
            var = vars[i]
            for (edge, expr) in dynamics.items():
                source, target = edge
                if source == var:
                    d -= eval(expr, ns)
                if target == var:
                    d += eval(expr, ns)
            dstate.append(d)
        return dstate
        
    return fun 
```

:::
