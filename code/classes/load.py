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
                minutes = int(line[2])
                
                # https://stackoverflow.com/questions/20585920/how-to-add-multiple-values-to-a-dictionary-key-in-python
                # https://www.programiz.com/python-programming/nested-dictionary
                # making of a nested dict
                self.connection.setdefault(begin_station.station_name, {})
                if begin_station.station_name not in self.connection:
                    self.connection[begin_station.station_name] = {}
                if end_station.station_name not in self.connection:
                    self.connection[end_station.station_name] = {}
                
                self.connection[begin_station.station_name][end_station.station_name] = minutes
                self.connection[end_station.station_name][begin_station.station_name] = minutes

    def get_station(self):
        return self.stations

    def get_con(self):
        return self.connection

    def get_cor(self):
        cor = {}
        for key, value in self.stations.items():
            cor[key] = (value.xcoordination, value.ycoordination)
            
        return cor




        
                