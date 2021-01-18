# from code.classes.load import Load
import random
import copy
import csv

class Random():

    def __init__(self, data):
        # data from load.py
        self.connection = data.connection
        self.station = data.stations

        # self.traject = []
        self.p = []
        self.T = []
        self.Min = []
        self.aantal_connections = 0

        self.trajectconnection = copy.deepcopy(self.connection)

    def get_traject(self):
        """
        Maak een lijnvoering voor Noord- en Zuid-Holland 
        met maximaal zeven trajecten binnen een tijdsframe van twee uur, 
        waarbij alle verbindingen bereden worden.
        """
        
        traject = []
        time_max = int(120)
        time = []
        # loop = 0
        # self.trajectconnection = copy.deepcopy(self.connection)
        get_rdm_station = random.choice(list(self.trajectconnection))
        traject.append(get_rdm_station)

        while True:
            if sum(time) > time_max:
                break

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
        
        while True:
            
            T =[]
            while True:
                traject = Random.get_traject(self)
                    
                if traject[1] == 0:
                    continue
                T.append(traject)

                # = wanneer alle connecties bereden zijn
                p = []
                for i in self.trajectconnection.values():
                    if i == {}:
                        p.append(i)
                if len(p) == 22:
                    break

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
        return  T, len(T), len(p), all_time



    def get_solution(self):


        # total_stations = len(self.station)
        # p = lijnvoering[2]/total_stations

        ans = []
        lijnvoering_all = [] 
        for i in range(100):
            lijnvoering = Random.make_lijnvoering(self)
            lijnvoering_all.append(lijnvoering[0])
            T = lijnvoering[1]
            p = 1
            Min = lijnvoering[3]
            q = p*10000 - (T*100 + Min)
            ans.append(float(q))

        

        #https://www.geeksforgeeks.org/writing-csv-files-in-python/
        rows = [
            ['q', ans]

        ]
        filename = "data/quality/random_output.csv"

        with open(filename, 'w') as infile:  
            # creating a csv writer object  
            csvwriter = csv.writer(infile) 
                
            # writing the data rows  
            csvwriter.writerows(rows) 
        return ans
    

        

            
            
               

        
    

            
        
        
