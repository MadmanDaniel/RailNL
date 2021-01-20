# from code.classes.load import Load
import random
import copy
import csv
import pandas as pd

class Random():

    def __init__(self, data):
        # data from load.py
        self.connection = data.connection
        self.trajectconnection = copy.deepcopy(data.connection)
        # self.station = data.stations

    def get_traject(self):
        """
        Maak een lijnvoering voor Noord- en Zuid-Holland 
        met maximaal zeven trajecten binnen een tijdsframe van twee uur, 
        waarbij alle verbindingen bereden worden.
        """
        
        traject = []
        # time_max = int(120)
        time_max = float(120)
        time = []
        # loop = 0
        # self.trajectconnection = copy.deepcopy(self.connection)
        get_rdm_station = random.choice(list(self.trajectconnection))
        traject.append(get_rdm_station)

        while sum(time) < time_max:
            
            get_connections = self.trajectconnection[get_rdm_station]

            if get_connections == {}:
                break

            # pakt random connectie ervan
            get_rdm_connection = random.choice(list(get_connections))
            if get_rdm_connection in traject and get_connections == {} :
                break

            # pak de tijd ervan
            get_time = self.trajectconnection[get_rdm_station][get_rdm_connection]
            
            time.append(get_time)
            if sum(time) > time_max:
                time.pop()
                break
            
            del self.trajectconnection[get_rdm_station][get_rdm_connection]
            del self.trajectconnection[get_rdm_connection][get_rdm_station]
       
            get_rdm_station = get_rdm_connection
            traject.append(get_rdm_connection)
   
        return traject, sum(time)
    

    def make_lijnvoering(self): 
        loop = 0
        while True:
            
            T =[]
            while True:
                loop +=1
                traject = Random.get_traject(self)
                    
                if traject[1] == 0:
                    continue
                T.append(traject)
                # print(len(T))

                # = wanneer alle connecties bereden zijn
                p = []
                for i in self.trajectconnection.values():
                    if i == {}:
                        p.append(i)
                # if len(p) == 61:
                #     break
                if len(p) == 22:
                    break

                
                # if len(T) == 20:
                #     break
            # print(self.trajectconnection)
            #Herstellen van onze data als een volledige traject gemaakt is zodat we opnieuw kunnen loopen
            self.trajectconnection = copy.deepcopy(self.connection)
            
            #   max aantal trajecten
            if len(T) > 7:
                continue
            break
        # T =TRAJECTEN
        # len(T) = AANTAL TRAJECTEN
        # len(p) = AANTAL CONNECTIES OVER -> 22 =0
        all_time = []
        for i in T:
            all_time.append((i[1]))
        all_time = sum(all_time)
        print(f"aantal loops: {loop}")
       
        return  T, len(T), len(p), all_time


    def get_solution(self):

        ans = []
        lijnvoering_all = [] 
        for i in range(1000):
            lijnvoering = Random.make_lijnvoering(self)
            lijnvoering_all.append(lijnvoering[0])
            T = lijnvoering[1]
            p = 1
            Min = lijnvoering[3]
            q = p*10000 - (T*100 + Min)
            ans.append(float(q))

        #https://www.geeksforgeeks.org/writing-csv-files-in-python/
        
        data = {'q': ans
        }
        filename = "data/quality/random_output.csv"

        df = pd.DataFrame(data, columns = ['q'])
        df.to_csv(filename)

        return q


