import networkx as nx
 
G=nx.Graph()                ## Create a Graph object and assign it to G 
##Further reference to graph will be through this variable
 
G.add_edge('A','B')		## Add edge (‘A’,’B’) to graph G
G.add_edge('B','C')		## Add edge (‘B’,’C’) to graph G
print(G.nodes())            	## Print all nodes of graph G
print(G.edges())            	## Print all edges of graph G
