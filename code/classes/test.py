#%%
import csv
from pathlib import Path
import matplotlib.pyplot as plt

station_file = "/home/danieldjuly/RailNL/data/opdracht1/StationsHolland.csv"
connectie_file = "/home/danieldjuly/RailNL/data/opdracht1/Connecties.csv"

station = {}
connection = {}
with open(station_file, 'r') as infile:
    reader = csv.reader(infile)
    header = next(infile)

    for line in reader:
        x = float(line[1])
        y = float(line[2])
        station[line[0]] = [x,y]


with open(connectie_file, 'r') as infile:
    reader = csv.reader(infile)
    header = next(infile)


    for line in reader:
        begin = line[0]
        eind = line[1]







for i in station.items():
    print(i) 
print(station)




