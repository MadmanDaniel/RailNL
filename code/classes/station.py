import csv

class Station():
    """
    Loading in the stations
    """

    def __init__(self, station_name, xcoordination, ycoordination):
        self.station_name = station_name
        self.xcoordination = xcoordination 
        self.ycoordination = ycoordination
        # self.distance = distance
        
    def add_connection(self, end_station, begin_station):
        self.connection[begin_station] = end_station

 

