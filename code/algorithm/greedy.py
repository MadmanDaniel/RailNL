import random
from code.algorithm import functions
from .randomize import Random
import copy
import csv
import pandas as pd

class Greedy():
    """
    It always looks for the shortest distance,
    with a random starting station
    """

    def __init__(self, data, max_time, max_traject):
        """
        Initialize a Greedy
        """
        self.connection = data.connection
        self.copy_connection = copy.deepcopy(self.connection)
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
        loops = 0
        self.begin_station = random.choice(list(self.copy_connection))
        traject.append(self.begin_station)

        # Generates a trajectory using a random start station by connecting the nearest station each time, 
        # as long as the time condition is not broken
        while sum(time) < time_max:

            loops += 1

            get_con = self.copy_connection[self.begin_station]
            next_station = functions.get_shortest_des(get_con) 

            get_time = next_station[1]
            next_station = next_station[0]

            time.append(get_time)
            if sum(time) > time_max:
                time.pop()
                break

            # connections that have already been used are no longer possible to use
            del self.copy_connection[self.begin_station][next_station]
            del self.copy_connection[next_station][self.begin_station]

            if self.copy_connection[self.begin_station] == {}:
                del self.copy_connection[self.begin_station]

            # get next station
            self.begin_station = next_station
            traject.append(next_station)

            if self.copy_connection[next_station] == {}:
                del self.copy_connection[next_station]
                break

        return traject, sum(time),loops

    def make_lijnvoering(self): 
        """
        Creates a line by adding trajectories, by adding trajectiories from get_traject
        """
        loops = 0
        max_length = True
        while max_length:
            all_traject = []
            time = 0
            while self.copy_connection != {}:

                get_traject = Greedy.get_traject(self)
                all_traject.append(get_traject[0])
                time += get_traject[1]
                loops += get_traject[2]
                
                remain_con = functions.get_remain_con(self.copy_connection.items())
                # ends adding trajectories if there are already 5 connections left or less
                if remain_con <= 5:
                    break
            con_notused_str = self.copy_connection
            self.copy_connection = functions.my_copy(self.connection)

            if len(all_traject) > self.max_traject:
                continue
            break

        # calculate q
        used_con = self.all_con - remain_con
        p = used_con/self.all_con
        T = len(all_traject)
        Min = time
        get_q = functions.get_q(p, T, Min)
        return get_q, all_traject, Min, used_con, con_notused_str
