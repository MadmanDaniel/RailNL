# #%%
from code.classes import station, load
import csv

if __name__ == "__main__":

    loading_in_files = load.Load("data/opdracht1/StationsHolland.csv", "data/opdracht1/ConnectiesHolland.csv" )
    
    # all stations
    print(loading_in_files.get_station())
    print("------")

    # all connections
    print(loading_in_files.get_con())

    # #test grafiek
    # import matplotlib.pyplot as plt
    # import matplotlib as mpl
    # import numpy as np

    # x = load.Load.xcoordination
    # y = station.Station.ycoordination
    # plt.plot(x,y)
    # plt.show()
