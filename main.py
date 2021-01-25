#%% 
# Code hierboven is alleen nodig voor Matplotlib 
# (dus visualisatie van de datapunten) -> is van extension Jupyter
from code.classes import station, load
from code.algorithm import randomize, greedy, functions
from code.visualisation.graph import get_map
from data.quality.hist import *

import csv
#import matplotlib.pyplot as plt
#import networkx as nx
#import numpy as np

import sys

if __name__ == "__main__":

    print("Which Rail connections do you want?\n -> Holland   (1)\n -> Nationaal (2)\n------------------")
    chosen_file = input("I choose number: ")

    while chosen_file != '1' and chosen_file != '2':        
        print("Error, pick a valid number")
        chosen_file = input("I choose number: ")

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

    data = load.Load(stations_file, connecties_file)

    print("Which Algorithm do you want?\n -> Random   (1)\n -> Greedy   (2)\n------------------")
    chosen_alg = input("I choose: ")

    if chosen_alg == "1":
        # ----------------------------- RANDOM -----------------------
        algorithm = randomize.Random(data, max_time, max_traject)
        # print(algorithm.make_lijnvoering())
        # ------------------------------------------------------------

    elif chosen_alg == "2":
        # ---------------------------- GREEDY ------------------------
        algorithm = greedy.Greedy(data, max_time, max_traject)
        # greedy1.get_solution()
        # ------------------------------------------------------------
    else:
        print("Error, pick a valid number")
        sys.exit()
    print("Loading.......")

    best_output = functions.best_output(algorithm)
    print(f"best output: {best_output}")
    # print(algorithm())



    # ---------------------------- GRAPH -------------------------
    # # maken van grafiek dmv gegeven coordinaten
    # dist = get_greedy_dist()
    # dist = get_random_dist()
    # dist = get_all_dist()
    graph = get_map(data, best_output[1])
    # ------------------------------------------------------------
    
