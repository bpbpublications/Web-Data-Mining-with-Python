import networkx as nx
 
G=nx.Graph()                ## Create a Graph object and assign it to G 
##Further reference to graph will be through this variable
 
G.add_edges_from([('A','B'),('B','C'),('C','E'),('E','D'),('C','F'),('G','F')])
print(G.nodes())            ## Print all nodes of graph G
print(G.edges())            ## Print all edges of graph G
nx.draw(G, with_labels = True) ##Prints the graph G
