#%% 
# Code hierboven is alleen nodig voor Matplotlib 
# (dus visualisatie van de datapunten) -> is van extension Jupyter
from code.classes import station, load
import csv
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

if __name__ == "__main__":

    data = load.Load("data/opdracht1/StationsHolland.csv", "data/opdracht1/ConnectiesHolland.csv" )
    
    # all stations
    print(data.get_station())
    print("------")

    # all connections
    print(data.get_con())
    print("------")

    #---------------------------------
    # # maken van grafiek dmv gegeven coordinaten
    # # eerst alle stations uitbeelden
    
    # plt.scatter(x_cor, y_cor)

    # plt.grid()
    # plt.show()
    #-//////////////////////////////////

    
    # ------------------------------------------------------------------------------------------------
    # https://stackoverflow.com/questions/20133479/how-to-draw-directed-graphs-using-networkx-in-python
    
    P = nx.Graph() 

    for key, value in data.get_con().items():
        P.add_nodes_from([key])

    edges = []
    for key, value in data.get_con().items():
        tup = tuple(value)
        for i in tup:
            e = []
            e.append(key)
            e.append(i)
            e= tuple(e)
            edges.append(e)
    
    
    P.add_edges_from(edges)


    
        
        
    
    # You can add nodes using add_nodes_from()
    # P.add_nodes_from(['A'])
    # # Use add_edges_from to add pairwise relationships
    # P.add_edges_from ([('B','C')])

    # print(P.nodes())
    # print(P.edges())
    nx.draw(P, with_labels = True)
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////
