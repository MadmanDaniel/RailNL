# from code.classes.load import Load
import random
import copy
import csv
import pandas as pd

class Random():

    def __init__(self, data, max_time, max_traject):
        self.connection = data.connection
        self.trajectconnection = copy.deepcopy(data.connection)
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
        get_rdm_station = random.choice(list(self.trajectconnection))
        traject.append(get_rdm_station)

        loops = 0

        while sum(time) < time_max:
            loops += 1

            get_connections = self.trajectconnection[get_rdm_station]

            # pakt random connectie ervan
            get_rdm_connection = random.choice(list(get_connections))
    
            # pak de tijd ervan
            get_time = self.trajectconnection[get_rdm_station][get_rdm_connection]
            
            time.append(get_time)
            if sum(time) > time_max:
                time.pop()
                break
            
            del self.trajectconnection[get_rdm_station][get_rdm_connection]
            del self.trajectconnection[get_rdm_connection][get_rdm_station]

            if self.trajectconnection[get_rdm_station] == {}:
                del self.trajectconnection[get_rdm_station]
       
            get_rdm_station = get_rdm_connection
            traject.append(get_rdm_connection)

            if self.trajectconnection[get_rdm_connection] == {}:
                del self.trajectconnection[get_rdm_connection]
                break

        return traject, sum(time), loops

    def make_lijnvoering(self):

        loops = 0
        while True: 
            
            all_traject = []
            time = 0
            while self.trajectconnection != {}:
                # loops += 1
                get_traject = Random.get_traject(self)
                all_traject.append(get_traject[0])
                time += get_traject[1]
                loops += get_traject[2]

            self.trajectconnection = copy.deepcopy(self.connection)
            if len(all_traject) > self.max_traject:
                continue
            break
        
        # gives the amount of used connection
        used_con = self.functions.get_remain_con(self.trajectconnection.items())

        # print(f"aantal loops: {loops}")

        return len(all_traject), used_con, time, loops


    def get_solution(self):
        total_loops = 0
        ans = []
        for i in range(100):
            lijnvoering = Random.make_lijnvoering(self)
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
        filename = "data/quality/random_output.csv"

        df = pd.DataFrame(data, columns = ['q'])
        df.to_csv(filename)

        print(f"loops random: {total_loops}")
        return q


