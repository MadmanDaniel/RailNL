import random
from code.algorithm import functions
from .randomize import Random
import copy
import csv
import pandas as pd
class Greedy():
    """Zoekt het steeds de kortste afstand met als beginstation een random"""

    def __init__(self, data, max_time, max_traject):
        self.connection = data.connection
        self.trajectconnection = copy.deepcopy(self.connection)

        self.all_con = data.all_con()
    

        self.max_time = max_time
        self.max_traject = max_traject

        

    def get_traject(self):
        """
        Maak een lijnvoering voor Noord- en Zuid-Holland 
        met maximaal zeven trajecten binnen een tijdsframe van twee uur, 
        waarbij alle verbindingen bereden worden.
        """
        traject = []
        time_max = self.max_time
        time = []

        loops = 0

        self.begin_station = random.choice(list(self.trajectconnection))
        traject.append(self.begin_station)

        while sum(time) < time_max:

            loops += 1

            get_con = self.trajectconnection[self.begin_station]
            next_station = functions.get_shortest_des(get_con) 

            get_time = next_station[1]
            next_station = next_station[0]

            time.append(get_time)
            if sum(time) > time_max:
                time.pop()
                break

            del self.trajectconnection[self.begin_station][next_station]
            del self.trajectconnection[next_station][self.begin_station]

            if self.trajectconnection[self.begin_station] == {}:
                del self.trajectconnection[self.begin_station]

            self.begin_station = next_station
            traject.append(next_station)

            if self.trajectconnection[next_station] == {}:
                del self.trajectconnection[next_station]
                break

        return traject, sum(time),loops


    def make_lijnvoering(self): 
    
        loops = 0
        while True:
            all_traject =[]
            time = 0
            while self.trajectconnection != {}:
                get_traject = Greedy.get_traject(self)
                all_traject.append(get_traject[0])
                time += get_traject[1]
                loops += get_traject[2]

            self.trajectconnection = functions.my_copy(self.connection)

            if len(all_traject) > self.max_traject:
                continue
            break

        used_con = functions.get_remain_con(self.trajectconnection.items())
        p = used_con/self.all_con
        T = len(all_traject)
        Min = time

        get_q = functions.get_q(p, T, Min)
            
        # print(f"aantal loops: {loops}")
        return get_q, all_traject, len(all_traject), used_con, time, loops
