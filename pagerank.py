import networkx as nx
import matplotlib.pyplot as plt

D = nx.DiGraph()  #d
n = int(input('Enter number of nodes: '))
for i in range(n):
    print(f'Enter node {i}:')
    D.add_weighted_edges_from([(input('Enter Parent: '), 
                                input('Enter Child: '),
                                int(input('Enter Weight: ')))])
    print('PageRank: ', nx.pagerank(D)) #p
    nx.draw(D, with_labels=True)  #d
plt.show()

#d2p nx