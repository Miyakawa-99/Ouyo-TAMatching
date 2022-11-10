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

tbe = pd.read_csv('data/input/survey.csv')
tbn = pd.read_csv('data/input/node0.csv')
tbe.insert(2, "capacity", 1)
ntbe = tbe.rename(columns={'respondent': 'node1', 'target': 'node2'})

g = graph_from_table(tbn, ntbe)[0]
d = nx.max_weight_matching(g)
pos = networkx_draw(g)
nx.draw_networkx_edges(g, pos, width=3, edgelist=[(i, j) for i, j in d])

plt.show()