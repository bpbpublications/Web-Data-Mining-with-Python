import networkx as nx
G=nx.Graph()
G.add_edge('A','B',weight=6, relation='family')
G.add_edge('B','C',weight=13, relation='friend')
G.add_node('A',role='Director')
G.add_node('B',role='Coordinator')
G.add_node('C',role='Computer Operator')
print(G.nodes())
print(G.nodes(data='True'))
 
nx.draw(G, with_labels = True)


