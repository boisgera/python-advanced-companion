#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Scientific stack
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# In[12]:


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


# In[13]:


def full_maze(width,height):
    A=[]
    for i in range(width):
        for j in range(height):
            A.append((i,j))
    A=set(A)
    B=set()
    C={}
    M=(A,B,C)
    return M


# In[14]:


maze = full_maze(50, 25)

print(maze)

display_maze(maze)


# In[ ]:


def empty_maze(width,height):
    L=full_maze(width,height)[0]
    A=[]
    for i in range(width):
        for j in range(height):
            if j+1<height:
                A.append((i,j),(i,j-1))
            if j-1>=0:
                A.append((i,j),(i,j-1))
            if i+1<width:
                A.append((i,j),(i+1,j))
            if i-1>=0:
                A.append((i,j),(i-1,j))
    A=set(A)
    
            

