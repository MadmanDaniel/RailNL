from code.classes import station, load
from code.algorithm import randomize, greedy, functions, hillclimber
from code.visualisation.graph import get_map
from code.visualisation.hist import *

import csv
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

    print("Which Algorithm do you want?\n -> Random      (1)\n -> Greedy      (2)\n -> Hillclimber (3)\n------------------")
    chosen_alg = input("I choose: ")

    if chosen_alg == "1":
        # ----------------------------- RANDOM -----------------------
        algorithm = randomize.Random(data, max_time, max_traject)
        best_output = functions.best_output(algorithm)
        # ------------------------------------------------------------

    elif chosen_alg == "2":
        # ---------------------------- GREEDY ------------------------
        algorithm = greedy.Greedy(data, max_time, max_traject)
        best_output = functions.best_output(algorithm)
        # ------------------------------------------------------------
    elif chosen_alg == "3":
        # ---------------------------- HILLCLIMBER ------------------------
        print("Which algorithm do you want to apply?")
        print(" -> Random(1)\n -> Greedy (2)")
        apply_alg = input("I choose: ")
        if apply_alg == "1":
            algorithm = randomize.Random(data, max_time, max_traject)
        elif apply_alg == "2":
            algorithm = greedy.Greedy(data, max_time, max_traject)
        else:
            print("Error, pick a valid number")
            sys.exit()
        highest_algorithm = functions.best_output(algorithm)
        best_output = hillclimber.Hillclimber(data, highest_algorithm, max_time).get_best_q()
        # ------------------------------------------------------------
    else:
        print("Error, pick a valid number")
        sys.exit()
    print("Loading.......")

    
    print(f"\nOur best calculated quality is: {best_output[0]}")
    print("For data and visualization see the data/output-folder")
   
    # ---------------------------- GRAPH -------------------------
    # # maken van grafiek dmv gegeven coordinaten
    dist = get_dist()
    graph = get_map(data, best_output[1])
    # ------------------------------------------------------------
    
