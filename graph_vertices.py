import networkx as nx
import matplotlib.pyplot as plt
n=int(input("enter the number of vertices:"))

if n>3:
    G=nx.complete_graph(n)

    nx.draw(G,
            node_color='pink',
            node_size=1500,
            with_labels=True)
    plt.show()
else:
    print("minimum number of vertices should be more than 3")