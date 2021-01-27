# from code.classes.load import Load
import random
import copy
import csv
import pandas as pd
from code.algorithm import functions

class Random():
    """
    It always searches a random station
    with a connection and
    as starting station a random station
    """

    def __init__(self, data, max_time, max_traject):
        """
        Initialize a Random
        """
        self.connection = data.connection
        self.copy_connection = copy.deepcopy(data.connection)
        self.all_con = data.all_con()
        self.max_time = max_time
        self.max_traject = max_traject



    def get_traject(self):
        """
        Creates a line for North and South Holland 
        with up to seven trajectories within a two hour time frame, 
        where all connections are ridden.
        """
        traject = []
        time_max = self.max_time
        time = []
        get_rdm_station = random.choice(list(self.copy_connection))
        traject.append(get_rdm_station)

        loops = 0

        while sum(time) < time_max:
            loops += 1

            get_connections = self.copy_connection[get_rdm_station]

            # pakt random connectie ervan
            get_rdm_connection = random.choice(list(get_connections))
    
            # pak de tijd ervan
            get_time = self.copy_connection[get_rdm_station][get_rdm_connection]
            
            time.append(get_time)
            if sum(time) > time_max:
                time.pop()
                break
            
            del self.copy_connection[get_rdm_station][get_rdm_connection]
            del self.copy_connection[get_rdm_connection][get_rdm_station]

            if self.copy_connection[get_rdm_station] == {}:
                del self.copy_connection[get_rdm_station]
       
            get_rdm_station = get_rdm_connection
            traject.append(get_rdm_connection)

            if self.copy_connection[get_rdm_connection] == {}:
                del self.copy_connection[get_rdm_connection]
                break

        return traject, sum(time), loops

    def make_lijnvoering(self):
        """
        Ensures that the trajectories are created,
        and the score is calculated
        """
        loops = 0
        while True: 
            
            all_traject = []
            time = 0
            while len(self.copy_connection) != 0:
                # loops += 1
                get_traject = Random.get_traject(self)
                all_traject.append(get_traject[0])
                time += get_traject[1]
                loops += get_traject[2]

                remain_con = functions.get_remain_con(self.copy_connection.items())
                # if remain_con < 5:
                #     break
            self.copy_connection = functions.my_copy(self.connection)
            # self.copy_connection = copy.deepcopy(self.connection)

            if len(all_traject) > self.max_traject:
                continue
            break
        
        # gives the amount of used connection
        
        used_con = self.all_con - remain_con
        p = used_con/self.all_con
        T = len(all_traject)
        Min = time
        
        get_q = functions.get_q(p, T, Min)
        # print(p, T,Min, get_q)
        
                
        return get_q, all_traject, loops