import random
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
        self.functions = data

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
            next_station = self.functions.get_shortest_des(get_con) 

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

    def test(self):
        x = []
        for i in range(7):
            print(x)
            x.append(Greedy.get_traject(self))
        return x


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
                # used_con = self.functions.get_remain_con(self.trajectconnection.items())
                # if used_con == 18:
                #     break

            self.trajectconnection = copy.deepcopy(self.connection)

            if len(all_traject) > self.max_traject:
                continue
            break

        used_con = self.functions.get_remain_con(self.trajectconnection.items())
            
        # print(f"aantal loops: {loops}")

        return len(all_traject), used_con, time, loops



    def get_solution(self):
        total_loops = 0
        ans = []
        for i in range(100):
            
            lijnvoering = Greedy.make_lijnvoering(self)
            total_loops += lijnvoering[3]

            T = lijnvoering[0]
            Min = lijnvoering[2]
            used_con = lijnvoering[1]
            p = used_con/self.all_con

            q = p*10000 - (T*100 + Min)
            ans.append(float(q))

        #https://www.geeksforgeeks.org/writing-csv-files-in-python/
        data = {'q': ans
        }
        filename = "data/quality/greedy_output.csv"

        df = pd.DataFrame(data, columns = ['q'])
        df.to_csv(filename)

        
        return print(f"loops greedy: {total_loops}")