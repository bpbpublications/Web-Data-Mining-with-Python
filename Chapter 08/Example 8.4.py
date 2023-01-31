import networkx as nx
G=nx.DiGraph()
G.add_edge('B','A')
G.add_edge('B','C')
G.add_edge('C','F')
G.add_edge('C','E')
G.add_edge('E','D')
G.add_edge('G','F')
nx.draw(G, with_labels = True)
