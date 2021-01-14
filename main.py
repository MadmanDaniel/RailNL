#%% 
# Code hierboven is alleen nodig voor Matplotlib 
# (dus visualisatie van de datapunten) -> is van extension Jupyter
from code.classes import station, load
from code.algorithm import randomize
from code.visualisation.graph import get_map

import csv
#import matplotlib.pyplot as plt
#import networkx as nx
#import numpy as np

if __name__ == "__main__":
    stations_file = "data/opdracht1/StationsHolland.csv"
    connecties_file = "data/opdracht1/ConnectiesHolland.csv"
    data = load.Load(stations_file, connecties_file)

    random1 = randomize.Random(data)
    
    print(random1.get_traject())
    print(random1.test())
    
    # print("------------------------------------------")
    # # # all stations
    # print(data.get_station())
    # print("------------------------------------------")

    # # all connections
    # print(data.connection)
    # print("------------------------------------------")

    #---------------------------------
    # # maken van grafiek dmv gegeven coordinaten
    graph = get_map(data)
    #----------------------------------
    
