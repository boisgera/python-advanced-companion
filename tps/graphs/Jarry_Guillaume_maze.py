# %%
# Python standard library
import math
import random

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
            if ((x, y), (x + 1, y)) not in edges:
                axes.plot([x + 1, x + 1], [y, y + 1], "k")
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



def full_maze(L, l): 
    # renvoie un maze plein, avec que des murs, de longueur L et de largeur L 
    noeuds = set()
    edges = set()
    poids = {}
    for i in range(L): 
        for j in range(l):
            noeuds.add( (i,j) )
    
    return (noeuds, edges, poids)


def empty_maze(L, l):
    # renvoie un maze vide, avec aucun mur, de longueur L et de largeur L 
    noeuds = set()
    edges = set()
    poids = {}
    for i in range(L): 
        for j in range(l):
            noeuds.add( (i,j) )
            if i+1 <= L: 
                edges.add( ((i, j),(i+1,j)) ) 
            if j+1 <= l: 
                edges.add( ((i,j), (i, j+1)) ) 
            if i-1 >= 0:
                edges.add( ((i, j), (i-1, j)) ) 
            if j-1 >= 0:
                edges.add( ((i, j), (i, j-1)) )
            poids[ ((i,j),(i+1,j))] = 1
            poids[ ((i,j),(i,j+1))] = 1
            poids[ ((i,j),(i-1,j))] = 1
            poids[ ((i,j),(i,j-1))] = 1

    return noeuds, edges, poids


def reachable_maze(maze, origin): 
    cells = set()
    todo = set()
    todo.add( origin)
    vertices, edges, weights = maze 
    while todo : 
        cell = todo.pop()
        x, y = cell
        for i in [-1, 1]: 
            if ( cell, (x,y+i) ) in edges :
                cells.add( (x, y+i))
            if ( cell, (x+i, y)) in edges : 
                cells.add( (x, y))
        cells.add(cell)
    
    return cells


maze = empty_maze(10, 10)
vertices, edges, weights = maze 
origin = (0, 0)

cells = reachable_maze(maze, origin) 
display_maze(maze, map=cells) 
plt.show()