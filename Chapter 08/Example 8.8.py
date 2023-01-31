import networkx as nx
G = nx.read_edgelist("Dataset/facebook_combined.txt")
print(nx.info(G))
