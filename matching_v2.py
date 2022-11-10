# -*- coding: utf-8 -*-
# 二群から

import networkx as nx
from networkx.algorithms import bipartite
import numpy as np
import itertools
import matplotlib.pyplot as plt

number = 12
group1 = range(6)
group2 = range(6,12)
weights = [
    [0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 5, 4, 0, 0, 0],
    [0, 5, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 5, 0],
    [0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 1, 2, 1, 0, 0, 0, 0, 0, 1, 0],
    [5, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 2, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 9, 0],
    [0, 2, 0, 5, 0, 0, 1, 0, 0, 2, 0, 0],
]

node_color = ["b"] * 6
node_color.extend(["r"] * 6)

g = nx.Graph()
g.add_nodes_from(group1, bipartite=1)
g.add_nodes_from(group2, bipartite=0)

for (i,j) in itertools.product(group1, group2):
  print(i,j)
  g.add_edge(i, j, weight=weights[i][j])

A,B = bipartite.sets(g)
pos = dict()
pos.update((n,(1,i)) for i,n in enumerate(A))
pos.update((n,(2,i)) for i,n in enumerate(B))

edge_width = [ d['weight']*0.3 for (u,v,d) in g.edges(data=True)]

nx.draw_networkx(g, pos, node_color=node_color)
nx.draw_networkx_edges(g, pos, width=edge_width)
plt.axis("off")
plt.show()

d = nx.max_weight_matching(g)

for (i, j) in list(g.edges()):
    if (i, j) not in d:
        if (j, i) not in d:
            g.remove_edge(i,j)

edge_width = [ d['weight']*0.3 for (u,v,d) in g.edges(data=True)]

nx.draw_networkx(g, pos, node_color=node_color)
nx.draw_networkx_edges(g, pos, width=edge_width)
plt.axis("off")
plt.show()