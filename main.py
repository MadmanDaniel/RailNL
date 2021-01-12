#%% 
# Code hierboven is alleen nodig voor Matplotlib 
# (dus visualisatie van de datapunten) -> is van extension Jupyter
from code.classes import station, load
from code.algorithm import randomize

import csv

if __name__ == "__main__":

    data = load.Load("data/opdracht1/StationsHolland.csv", "data/opdracht1/ConnectiesHolland.csv" )

    # random1 = randomize.Random(data)
    # print(random1.get_random())

    # all stations
    # print(data.get_station())
    # print("------")

    # all connections
    print(data.get_con()["Alkmaar"])
    print("------")

    
    
