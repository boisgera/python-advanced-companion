
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


#premier élément : ensemble de noeuds
#deuxieme élément : ensemble de paire de noeud
#troisième élément : dictionnaire de clé paire de noeud et de valeur poids attribué

def empty_maze(width,height):
    vertices = set()
    edges = set()
    weights = {}
    for i in range(width):
        for j in range(height):
            vertices.add((i,j))
    for vertex in vertices:
        i, j = vertex
        edges.update([((i,j),(i-1,j)),((i,j),(i+1,j)),((i,j),(i,j-1)),((i,j),(i,j+1))])
        off = []
        for edge in edges:
            e = edge[1]
            i,j = e
            if i<0 or j<0 or i>width or j>height:
                off.append(edge)
    for elt in off : 
        edges.remove(elt)
    for edge in edges:
        weights[edge] = 1
    
    return (vertices, edges, weights)

def full_maze(width,height):
    vertices = set()
    edges = set()
    weights = {}
    for i in range(width):
        for j in range(height):
            vertices.add((i,j))
    return (vertices, edges, weights)
    
full = full_maze(5,10)
empty = empty_maze(5,10)
#display_maze(full)

## Visualisation de labyrinthes prédéfinis 

with open("dense_maze-4x3.py",'r') as s:
    for line in s:
        maze = eval(line)

## Fonction reachable_set

def reachable_set(maze, origin):
    vertices = maze[0]
    edges = maze[1]
    weights = maze[2]
    cells = {origin}
    running = True
    while running:
        test = cells.copy()
        for cell in cells:
            A = {edge for edge in edges if edge[0]==cell}
            for edge in A:
                test.add(edge[1])
        if cells == test:
            running = False
        cells = test
    return cells

display_maze(maze, map = reachable_set(maze, (0,0)))
plt.show()

## Fonction reachable_path

def reachable_path(maze, origin):
    vertices = maze[0]
    edges = maze[1]
    weights = maze[2]
    