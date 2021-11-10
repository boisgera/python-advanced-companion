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

def full_maze(width, height):
    vertices=set()
    edges=set()
    weights={}
    for k in range(width):
        for l in range(height):
            vertices.add((k,l))
    return vertices, edges, weights

def empty_maze(width, height):
    vertices=set()
    edges=set()
    weights={}
    for k in range(width):
        for l in range(height):
            vertices.add((k,l))
            if k>0:
                edges.add(((k,l),(k-1,l)))
                weights[(k,l),(k-1,l)]=1
            if k<width-1:
                edges.add(((k,l),(k+1,l)))
                weights[(k,l),(k+1,l)]=1
            if l>0:
                edges.add(((k,l),(k,l-1)))
                weights[(k,l),(k,l-1)]=1
            if l<height-1:
                edges.add(((k,l),(k,l+1)))
                weights[(k,l),(k,l+1)]=1
    return vertices, edges, weights

def test_voisins(x,y):
    voisins=[]
    true_voisins=set()
    if x>0:
        voisins.append(x-1,y)
    if x<width-1:
        voisins.append(x+1,y)      
    if y>0:
        voisins.append(x,y-1)  
    if y<height-1:
        voisins.append(x-1,y)
    for w in voisins:
        if ((x,y), w) in edges or (w,(x,y)) in edges:
            true_voisins.add(w)
    return true_voisins

def deja(test_voisins(x,y),resultat):


def reachable_set(maze, origin):
    vertices,edges,weights =maze
    resultat=set()
    x,y=origin
    test_v=test_voisins(x,y)
    if deja(test_v,resultat)==[]:
        return resultat
    for x in deja(test_v,resultat):
        resultat=resultat|deja(test_v,resultat)

def voisins(maze,x,y):
    vertices,edges,weights =maze
    voisins=set()
    if (x-1,y) in vertices:
        voisins.add(x-1,y)
    if (x+1,y) in vertices:
        voisins.add(x+1,y)      
    if (x,y-1)  in vertices:
        voisins.add(x,y-1)  
    if (x-1,y) in vertices:
        voisins.add(x-1,y)
    return voisins

def reachable_set2(maze,origin):
    vertices,edges,weights =maze
    TODO=set()
    DONE=set()
    x,y=origin
    while TODO!=set():
        

    