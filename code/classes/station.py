import csv

class Station():
    """
    Loading in the stations
    """

    def __init__(self, station_name, xcoordination, ycoordination):
        self.station_name = station_name
        self.xcoordination = xcoordination 
        self.ycoordination = ycoordination
        self.connection = {}
        
    def add_connection(self, end_station, distance):
        self.connection[distance] = end_station

 

