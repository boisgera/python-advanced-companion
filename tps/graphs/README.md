Labyrinthes
================================================================================

Graphes
--------------------------------------------------------------------------------

Nous représenton  un graphe orienté et pondéré par le triplet composé :

  - d'un ensemble `vertices` de sommets,

  - d'un ensemble `edges` d'arêtes, représentées comme des paires de sommets,

  - d'un dictionnaire `weights` associant à chaque arête une valeur numérique.


Labyrinthes
--------------------------------------------------------------------------------

### Labyrinthes élémentaires

### Créez votre labyrinthe

### Echanges

Chemins
--------------------------------------------------------------------------------

Performance
--------------------------------------------------------------------------------

Annexe - Visualisation
--------------------------------------------------------------------------------

```python
# Scientific stack
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Visualization
# ------------------------------------------------------------------------------
def display_maze(graph, path=None, map=None):
    vertices, edges, weights = graph
    width = max(w for (w, h) in vertices) + 1
    height = max(h for (w, h) in vertices) + 1
    wh_ratio = width / height
    fig_width = 14  # inches
    fig_height = fig_width / wh_ratio
    fig, axes = plt.subplots(figsize=(fig_width, fig_height))
    axes.axis("equal")
    axes.plot([0, width, width, 0, 0], [0, 0, height, height, 0], "k")
    for x in range(width):
        for y in range(height):
            axes.plot([x + 1, x + 1], [y, y + 1], "k:")
            if ((x, y), (x + 1, y)) not in edges:
                axes.plot([x + 1, x + 1], [y, y + 1], "k")
            axes.plot([x, x + 1], [y + 1, y + 1], "k:")            
            if ((x, y), (x, y + 1)) not in edges:
                axes.plot([x, x + 1], [y + 1, y + 1], "k")
    axes.axis("off")

    if path:
        xs = np.array([x for (x, y) in path])
        ys = np.array([y for (x, y) in path])
        axes.plot(xs + 0.5, ys + 0.5, "r-")

    if map:
        if isinstance(map, set):
            map = {k: 1.0 for k in map}
        d_max = max(map.values())
        cmap = mpl.cm.get_cmap("viridis")

        for v, d in map.items():
            dx, dy = 1, 1
            rect = patches.Rectangle(v, dx, dy, facecolor=cmap(d / d_max))
            axes.add_patch(rect)
```