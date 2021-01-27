from code.classes import station, load
from code.algorithm import randomize, greedy, functions, greedy_adv
import random
from code.visualisation.graph import get_map
# from data.quality.hist import *
stations_file = "data/opdracht1/StationsHolland.csv"
connecties_file = "data/opdracht1/ConnectiesHolland.csv"
max_time = 120
max_traject = int(7)

data = load.Load(stations_file, connecties_file)

greedy2= greedy_adv.Greedy_look(data)
print(greedy2.get_traject())
print("-----")
# print(data.connection)

# best_output = functions.best_output(algorithm)
# print(f"best output: {best_output[0]}\nlijntraject: {best_output[1]}")

# dist = get_greedy_dist()