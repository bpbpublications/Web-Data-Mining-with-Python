import networkx as nx
G=nx.Graph()
G.add_edge('A','B', relation='Family')
G.add_edge('B','C', relation='Friend')
G.add_edge('C','F', relation='Extended Family')
nx.draw(G, with_labels = True)
 
#In order to list all edges, we use G.edges() as following:
print(G.edges())
