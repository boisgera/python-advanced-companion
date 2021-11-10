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
def rotate(x1y1, x2y2):
    "Rotate a segment +90° with respect to its center"
    x1, y1 = x1y1
    x2, y2 = x2y2
    cx, cy = 0.5 * (x1 + x2), 0.5 * (y1 + y2)
    x3y3 = cx - (y1 - cy), cy + (x1 - cx)
    x4y4 = cx - (y2 - cy), cy + (x2 - cx)
    return x3y3, x4y4

def display_maze(graph, path=None, map=None):
    vertices, edges, weights = graph
    width = max(w for (w, h) in vertices) + 1
    height = max(h for (w, h) in vertices) + 1
    wh_ratio = width / height
    fig_width = 14  # inches
    fig_height = fig_width / wh_ratio
    fig, axes = plt.subplots(figsize=(fig_width, fig_height))
    axes.axis("equal")
    for x in range(width):
        for y in range(height):
            for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                xn, yn = x+dx, y+dy
                if ((x, y), (xn, yn)) in edges:
                    style = {"color": "grey", "linestyle": ":"}
                else:
                    style = {"color": "black", "linestyle": "-"}
                w1, w2 = rotate((x + 0.5, y + 0.5), (xn + 0.5, yn + 0.5)) # wall segment                    
                axes.plot([w1[0], w2[0]], [w1[1], w2[1]], **style)
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
############################################################################
###############Ca commence#################################################
#############################################################################

def empty_maze(width,height):
    V=[]
    E=[]
    P={}
    for i in range (0,width):
        for j in range (0,height):
            V.append((i,j))
            if i>0:
                E.append(((i,j),(i-1,j)))
                P[((i,j),(i-1,j))] = 1
            if i<width-1:
                E.append(((i,j),(i+1,j)))
                P[((i,j),(i+1,j))] = 1
            if j>0:
                E.append(((i,j),(i,j-1)))
                P[((i,j),(i,j-1))] = 1
            if j<height-1:
                E.append(((i,j),(i,j+1)))
                P[((i,j),(i,j+1))] = 1
    vertices = set(V)
    edges = set(E)
    weights = P
    return vertices, edges, weights


def full_maze(width,height):
    V=[]
    for i in range (0,width):
        for j in range (0,height):
            V.append((i,j))
    vertices = set(V)
    edges = set()
    weights = {}
    return vertices, edges, weights


#display_maze(eval(open('punctured_maze-50x25.py').read()))
#plt.show()
def reachable_neighbors(maze,vertice):
    S=[]
    E = maze[1]
    i,j=vertice
    if ((i,j),(i+1,j)) in E:
        S.append((i+1,j))
    if ((i,j),(i-1,j)) in E:
        S.append((i-1,j))
    if ((i,j),(i,j+1)) in E:
        S.append((i,j+1))
    if ((i,j),(i,j+1)) in E:
        S.append((i,j+1))
    return set(S)
    


def reachable_set(maze,origin):
    Maze = maze
    S= {origin}   # elems atteignables
    nouveaux = [origin] # cells venant d'être atteintes
    dlength = 1 # variation nb cells atteignable, algo s'arrête si nulle
    length = 1  #nb cells atteignables
    while dlength > 0:
        prochains= set() #cells prochainement atteints
        for elem in nouveaux:
            reachneighb = reachable_neighbors(Maze,elem)
            prochains= prochains|(reachneighb-S)
            S = S|reachneighb
        dlength = len(S) - length
        length = len(S)
        nouveaux = prochains
    return S

Maze = eval(open('walled_maze-50x25.py').read())
cells = reachable_set(Maze,(0,0))
print(cells)
display_maze(Maze,map=cells)
plt.show()