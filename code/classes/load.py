import csv
from .station import Station

class Load():

    def __init__(self, station_file, connection_file):
        """
        Loading in of the CSV files in /data
        """
        self.stations = {}
        self.connection = {}
        self.load_station(station_file)
        self.load_connection(connection_file)
        
    def load_station(self, station_file):
        """
        Loading in of the CSV file in /data, StationsHolland.csv 
        """
        with open(station_file, 'r') as infile:
            reader = csv.reader(infile)
            header = next(infile)

            # make station objects with the data of the stations
            for line in reader:
                station = Station(line[0], float(line[1]), float(line[2]))
                self.stations[station.station_name] = station
    
    def load_connection(self, connection_file):
        """ 
        Loading in of the CSV file in /data, ConnectiesHolland.csv
        """
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

    def get_con(self):
        """
        Returning
        """
        return self.connection

    def all_con(self):
        """
        Returning 
        """
        x = []
        for key,value in self.connection.items():
            x += value
        return (len(x)/2)

    def get_cor(self):
        """
        Returning the coordinates of the station
        """
        cor = {}
        for key, value in self.stations.items():
            cor[key] = (value.ycoordination, value.xcoordination)
        return cor

    # def get_next_con(self, begin_station):
    #     return self.connection[begin_station]