# -*- coding: utf-8 -*-
# 去年まで使用してたもの。
# ほげほげ

# CSVデータ
import pandas as pd, networkx as nx, matplotlib.pyplot as plt
from ortoolpy import graph_from_table, networkx_draw
# pandas.DataFrame
from ortoolpy.optimization import MaxWeightMatching
# 乱数データ
import networkx as nx, matplotlib.pyplot as plt
from ortoolpy import networkx_draw
import csv

tbn = pd.read_csv('sampleNode.csv')
tbe = pd.read_csv('after.csv')
# with open('希望調査.csv', 'rt', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     for line in reader:
#         print(line)
#         with open('希望調査.csv', 'w') as newfile:
#             writer = csv.writer
g = graph_from_table(tbn, tbe)[0]
d = nx.max_weight_matching(g)
pos = networkx_draw(g)
nx.draw_networkx_edges(g, pos, width=3, edgelist=[(i, j) for i, j in d])
# plt.show()
print(d)