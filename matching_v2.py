# -*- coding: utf-8 -*-
import networkx as nx
from networkx.algorithms import bipartite
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 2グループに分ける
# 12人の受講者はどちらかのグループに所属(ちょうど半分でないと機能しない)
# TODO: UPDATE students
students = [
        {"id": 1, "group": "B"},
        {"id": 2, "group": "A"},
        {"id": 3, "group": "B"},
        {"id": 4, "group": "A"},
        {"id": 5, "group": "A"},
        {"id": 6, "group": "A"},
        {"id": 7, "group": "B"},
        {"id": 8, "group": "A"},
        {"id": 9, "group": "B"},
        {"id": 10, "group": "A"},
        {"id": 11, "group": "B"},
        {"id": 12, "group": "B"}
]

groupA_students = list(filter(lambda student : student['group'] == 'A', students))
groupA_ids = [d.get('id') for d in groupA_students]
groupB_students = list(filter(lambda student : student['group'] == 'B', students))
groupB_ids = [d.get('id') for d in groupB_students]

# IDでNodeを作る
g = nx.Graph()
g.add_nodes_from(groupA_ids, bipartite=0)
g.add_nodes_from(groupB_ids, bipartite=1)

df = pd.read_csv('data/input/survey.csv')

for i in groupA_ids:
  for j in groupB_ids:
    weight = 0
    print("respondent" + str(i))
    print("target" + str(j))
    item = df[(df['respondent'] == i) & (df['target'] == j)]
    rev_item = df[(df['respondent'] == j) & (df['target'] == i)]
    if not item.empty:
        weight = weight + int(item.loc[:, "weight"])
    if not rev_item.empty:
        weight = weight + int(rev_item.loc[:, "weight"])
    print(str(weight))
    g.add_edge(i, j, weight = weight)

d = nx.max_weight_matching(g)

# ここから描画
pos = {}
for i in groupA_ids:
  pos[i] = (1, i)

for j in groupB_ids:
  pos[j] = (2, j - len(groupB_students))

for (i, j) in list(g.edges()):
    if (i, j) not in d:
        if (j, i) not in d:
            g.remove_edge(i,j)
nx.draw_networkx(g, pos)
nx.draw_networkx_edges(g, pos)
plt.show()