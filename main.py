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
    #----------------------------------

    
