import csv

class Station():
    """
    Making station objects from load.py
    """
    def __init__(self, station_name, xcoordination, ycoordination):
        self.station_name = station_name
        self.xcoordination = xcoordination 
        self.ycoordination = ycoordination