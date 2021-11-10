# %%
# Python standard library
import math
import random

# Scientific stack
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def rotate(x1y1, x2y2):
    "Rotate a segment +90° with respect to its center"
    x1, y1 = x1y1
    x2, y2 = x2y2
    cx, cy = 0.5 * (x1 + x2), 0.5 * (y1 + y2)
    x3y3 = cx - (y1 - cy), cy + (x1 - cx)
    x4y4 = cx - (y2 - cy), cy + (x2 - cx)
    return x3y3, x4y4
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

        plt.show()

def full_maze(width, height):
    
    result = (
        {(i,j) for i in range(width) for j in range(height)},
        set(),
        {}
    )
    return result

def empty_maze(width, height):
    sommets = {(i,j) for i in range(width) for j in range(height)}
    aretes = set()
    for i in range(width):
        for j in range(height):
            if i>0:
                aretes.add(((i-1,j),(i,j)))
                aretes.add(((i,j),(i-1,j)))
            if i<width -1:
                aretes.add(((i+1,j),(i,j)))
                aretes.add(((i,j),(i+1,j)))
            if j>0:
                aretes.add(((i,j-1),(i,j)))
                aretes.add(((i,j),(i,j-1)))
            if j<height - 1:
                aretes.add(((i,j+1),(i,j)))
                aretes.add(((i,j),(i,j+1)))

    print(aretes)

    result = (
        sommets,
        aretes,
        {i : 1 for i in aretes}
    )
    return result
    
#print(display_maze(empty_maze(3,2)))

def reachable_set(maze,origin):
    todo = {origin}
    done = set()
    while todo:
        x= todo.pop()
        if (x[0]-1,x[1]) in maze[0]:
            if ((x[0]-1,x[1]),(x,x[1])) in maze[1]:
                if (x[0]-1,x[1]) not in done:
                    todo.add((x[0]-1,x[1]))
        if (x[0]+1,x[1]) in maze[0]:
            if ((x[0]+1,x[1]),(x[0],x[1])) in maze[1]:
                if (x[0]+1,x[1]) not in done:
                    todo.add((x[0]+1,x[1]))
        if (x[0],x[1]-1) in maze[0]:
            if ((x[0],x[1]-1),(x[0],x[1])) in maze[1]:
                if (x[0],x[1]-1) not in done:
                    todo.add((x[0],x[1]-1))
        if (x[0],x[1]+1) in maze[0]:
            if ((x[0],x[1]+1),(x[0],x[1])) in maze[1]:
                if (x[0],x[1]+1) not in done:
                    todo.add((x[0],x[1]+1))
        done.add((x[0],x[1]))      
    return done
cells = reachable_set(full_maze, (0,0) )
display_maze(full_maze,cmap = cells)

# %%
