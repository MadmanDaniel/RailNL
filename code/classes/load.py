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
                minutes = float(line[2])
                
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

    def all_con(self):
        x = []
        for key,value in self.connection.items():
            x += value
        return (len(x)/2)

    def get_remain_con(self, remain_con):
        used_con = []
        for key, value in remain_con:
            used_con += value
        used_con = (len(used_con)/2)

        return used_con

    def get_shortest_des(self, get_con):
        sort = sorted(get_con.items(), key=lambda item: item[1])

        min_value = sort[0]
        return min_value



    def get_cor(self):
        cor = {}
        for key, value in self.stations.items():
            cor[key] = (value.ycoordination, value.xcoordination)
            
        return cor




        
                