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

import sys

if __name__ == "__main__":

    print("Holland (1) or Nationaal (2) ?")
    chosen_file = input("I choose: ")

    if chosen_file == "1":
        print("Loading....")
        stations_file = "data/opdracht1/StationsHolland.csv"
        connecties_file = "data/opdracht1/ConnectiesHolland.csv"
        max_time = int(120)
        max_traject = int(7)
    elif chosen_file == "2":
        print("Loading....")
        stations_file = "data/opdracht2/StationsNationaal.csv"
        connecties_file = "data/opdracht2/ConnectiesNationaal.csv"
        max_time = int(180)
        max_traject = int(20)
    else:
        print("Error, pick a valid number")
        sys.exit()

    data = load.Load(stations_file, connecties_file)

    # ----------------------------- RANDOM -----------------------
    random1 = randomize.Random(data, max_time, max_traject)
    # print(random1.get_traject())
    # print(random1.make_lijnvoering())
    # print(random1.get_solution())
    # ------------------------------------------------------------


    # ---------------------------- GREEDY ------------------------
    # greedy1 = greedy.Greedy(data, max_time, max_traject)
    # print(greedy1.get_solution())
    # ------------------------------------------------------------

    # print(data.all_con())



    # ---------------------------- GRAPH -------------------------
    # # maken van grafiek dmv gegeven coordinaten
    # dist = get_greedy_dist()
    # dist = get_random_dist()
    # dist = get_all_dist()
    graph = get_map(data, random1)
    # ------------------------------------------------------------
    
