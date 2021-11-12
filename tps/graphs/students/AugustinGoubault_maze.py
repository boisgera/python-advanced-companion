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
    plt.show()


def full_maze(width, height):
    result=({(i,j) for i in range(width) for j in range(height)} ,set(),{})
    return result

#print (display_maze(full_maze(3,2)))


def empty_maze(width, height):
    vertices={(i,j) for i in range(width) for j in range(height)}
    edges=set()
    for i in range(width):
        for j in range(height):
            if i>0:
                edges.add(((i-1,j),(i,j)))
                edges.add(((i,j),(i-1,j)))
            if j>0:
                edges.add(((i,j-1),(i,j)))
                edges.add(((i,j),(i,j-1)))
            if i < width-1:
                edges.add(((i,j),(i+1,j)))
                edges.add(((i+1,j),(i,j)))
            if j < height-1:
                edges.add(((i,j),(i,j+1)))
                edges.add(((i,j+1),(i,j)))
    weights= {i:1 for i in edges}
    result=(vertices,edges,weights)
    return result

#print (display_maze(empty_maze(3,2)))




def create_rdmaze(width, heights,N):
    vertices={(i,j) for i in range(width) for j in range(heights)}
    edges=set()
    c=N//2
    while c>0:
        rd1,rd2=random.randrange(width),random.randrange(heights)
        edges.add(((rd1,rd2),(rd1+1,rd2)))
        edges.add(((rd1,rd2),(rd1,rd2+1)))
        c-=1
    weights= {i:1 for i in edges}
    result=(vertices, edges, weights) 
    return result



#print (display_maze(create_rdmaze(20,20,200)))



def reachable_set(maze, origin):
    vertices,edges,heights= maze
    todo=set()
    todo.add (origin)
    done=set()
    while todo:
        cell=todo.pop()
        x,y = cell
        for i in [-1,1]:
            if (cell, (x,y+i))  in edges and (x,y+i) not in done and (x,y+i) in vertices:
                todo.add((x,y+i))
            if (cell, (x+i,y)) in edges and (x+i,y) not in done and (x+i,y) in vertices:
                todo.add((x+i,y))
        done.add(cell)
    return done

            
maze =create_rdmaze(20,20,500)
origin = (0, 0)
cells = reachable_set(maze, origin) 
display_maze(maze, map=cells) 
plt.show()




