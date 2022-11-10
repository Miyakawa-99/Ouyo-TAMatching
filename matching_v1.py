# -*- coding: utf-8 -*-
# CSVデータ
import pandas as pd, networkx as nx, matplotlib.pyplot as plt
from ortoolpy import graph_from_table, networkx_draw
# pandas.DataFrame
from ortoolpy.optimization import MaxWeightMatching
# 乱数データ
import networkx as nx, matplotlib.pyplot as plt
from ortoolpy import networkx_draw
import csv

tbn = pd.read_csv('data/input/survey.csv')
tbe = pd.read_csv('data/input/node0.csv')
tbn['capacity'] = 0
g = graph_from_table(tbn, tbe)[0]
g = nx.Graph()
d = nx.max_weight_matching(g)
pos = networkx_draw(g)
nx.draw_networkx_edges(g, pos, width=3, edgelist=[(i, j) for i, j in d])
print(d)
plt.show()