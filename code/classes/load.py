import csv
from .station import Station
#import matplotlib.pyplot as plt


class Load():

    def __init__(self, station_file, connection_file):
        self.stations = {}
        self.connection = {}
        self.load_station(station_file)
        self.load_connection(connection_file)
        

    def load_station(self, station_file):
        with open(station_file, 'r') as infile:
            reader = csv.reader(infile)
            header = next(infile)

            for line in reader:
                # order = station, x_cor, y_cor
                station = Station(line[0], float(line[1]), float(line[2]))
                self.stations[station.station_name] = station
    
    def load_connection(self, connection_file):
        with open(connection_file, 'r') as infile:
            reader = csv.reader(infile)
            header = next(infile)

            for line in reader:
                begin_station = self.stations[line[0]]
                end_station = self.stations[line[1]]
                # distance = int(line[2])
                
                # "The magic of setdefault is that it initializes the value for that key if that key 
                # is not defined, otherwise it does nothing. 
                # https://stackoverflow.com/questions/20585920/how-to-add-multiple-values-to-a-dictionary-key-in-python
                self.connection.setdefault(begin_station.station_name, [])
                self.connection[begin_station.station_name].append(end_station.station_name)
                
    def get_station(self):
        return self.stations

    def get_con(self):
        return self.connection

    def get_xcor(self):
        # ik denk dat een loop niet effectief is om de x en y waardes uit te lezen voor een grafiek.
        # Later moeten we dit misschien nog aanpassen 
        x_cor = []
        for x in self.stations.values():
            x = x.xcoordination
            x_cor.append(x)
        return x_cor

    def get_ycor(self):
        y_cor = []
        for y in self.stations.values():
            y = y.ycoordination
            y_cor.append(y)
        return y_cor

    

        
                