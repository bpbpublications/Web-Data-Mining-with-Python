import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.community.centrality import girvan_newman
G = nx.karate_club_graph()
communities = girvan_newman(G)
 node_groups = []
for com in next(communities):
  node_groups.append(list(com)) 
print(node_groups) 
color_map = []
for node in G:
    if node in node_groups[0]:
        color_map.append('blue')
    else: 
        color_map.append('green')  
nx.draw(G, node_color=color_map, with_labels=True)
plt.show()
