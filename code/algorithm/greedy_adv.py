import copy
import random
from .randomize import Random
from code.algorithm import functions
class Greedy_look():
    " Random een startstation kiezen en vanuit daar de dichtbijzijnde station aan linken"
    def __init__(self, data):
        # De data van Load.py
        self.connection = copy.deepcopy(data.connection)
        self.station = copy.deepcopy(data.stations)
        self.used_connections = []

        # self.traject = []
        self.p = []
        self.T = []
        self.Min = []
        self.aantal_connections = 0

    def get_traject(self):
        """
        Maak een lijnvoering voor Noord- en Zuid-Holland 
        met maximaal zeven trajecten binnen een tijdsframe van twee uur, 
        waarbij alle verbindingen bereden worden, aan de hand van een Greedy Algoritme.
        """
        
        tijd = []
        traject = []
      
    
        #DEPT0
        start_station = "Alkmaar"

        traject.append(start_station)
        
        visited = set()
        # visited.add(start_station)

        get_con = self.connection[start_station]
        print(f"{start_station}{get_con}")
        for next_station in get_con:
            if next_station not in visited:
                traject.append(next_station)
                # visited.add(next_station)
                tijd.append(get_con[next_station])
                
                get_d1_con = self.connection[next_station]
            
            print(f"    {next_station}: {get_d1_con}")
            for next_d1_station in get_d1_con:
                if next_d1_station not in visited:
                    # visited.add(next_d1_station)
                    get_d2_con = self.connection[next_d1_station]
                    # get_d2_con.pop(next_d1_station, None)
                    print(f"        {next_d1_station}: {get_d2_con}")
        

                

                
                
            


            
