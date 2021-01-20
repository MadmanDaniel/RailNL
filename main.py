#%% 
# Code hierboven is alleen nodig voor Matplotlib 
# (dus visualisatie van de datapunten) -> is van extension Jupyter
from code.classes import station, load
from code.algorithm import randomize, greedy
from code.visualisation.graph import get_map
from data.quality.hist import *

import csv
#import matplotlib.pyplot as plt
#import networkx as nx
#import numpy as np

if __name__ == "__main__":

    stations_file = "data/opdracht1/StationsHolland.csv"
    connecties_file = "data/opdracht1/ConnectiesHolland.csv"

    # stations_file = "data/opdracht2/StationsNationaal.csv"
    # connecties_file = "data/opdracht2/ConnectiesNationaal.csv"

    data = load.Load(stations_file, connecties_file)


    random1 = randomize.Random(data)
    print(random1.get_solution())
    # print(random1.get_solution())

    greedy1 = greedy.Greedy(data)
    print(greedy1.get_solution())

    

    
    # print("------------------------------------------")
    # # # all stations
    # print(data.get_station())
    # print("------------------------------------------")

    # # all connections
    #print(data.get_con())
    # print("------------------------------------------")

    #---------------------------------
    # # maken van grafiek dmv gegeven coordinaten
    dist = get_greedy_dist()
    # dist = get_random_dist()
    # graph = get_map(data)
    #----------------------------------
    
