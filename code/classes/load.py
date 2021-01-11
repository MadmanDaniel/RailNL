import csv
from .station import Station


class Load():

    def __init__(self, station_file):
        self.stations = {}
        self.load_station(station_file)
        # self.load_connection(connection_file)
        self.test = self.stations["Alkmaar"]

    def load_station(self, station_file):
        with open(station_file, 'r') as infile:
            reader = csv.reader(infile)
            header = next(infile)

            for line in reader:
                # order = station, x_cor, y_cor
                station = Station(line[0], float(line[1]), float(line[2]))
                self.stations[station.station_name] = station


# code hieronder werkt totaal niet
    # def load_connection(self, connection_file):
    #     with open(connection_file, 'r') as infile:
    #         reader = csv.reader(infile)
    #         header = next(infile)

    #         for line in reader:
    #             begin_station = self.stations[line[0]]
    #             end_station = self.stations[line[1]]
    #             distance = int(line[2])
    #             begin_station.add_connection(end_station, distance)

    def get(self):
        return self.test.station_name
        
                