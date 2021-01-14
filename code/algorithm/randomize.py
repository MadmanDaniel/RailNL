# from code.classes.load import Load
import random
import copy
import csv

class Random():

    def __init__(self, data):
        # data from load.py
        self.connection = copy.deepcopy(data.connection)
        self.station = copy.deepcopy(data.stations)

        # self.traject = []
        self.p = []
        self.T = []
        self.Min = []

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
        get_rdm_station = random.choice(list(self.connection))
        
        
        traject.append(get_rdm_station)
        while True:
            if sum(time) > time_max:
                break
            
            
            # loop += 1
            #pakt alle connecties van get_rdm_station
            get_connections = self.connection[get_rdm_station]

            # # als alle connections gedelete zijn moet stoppen met loopen
            if get_connections == {}:
                
                break

            # pakt random connectie ervan
            get_rdm_connection = random.choice(list(get_connections))
            # print(get_rdm_connection)
            # print(get_connections)
            # als het in het traject al zit EN het maar 1 richting op kan
            if get_rdm_connection in traject and get_connections == {} :
                break
            
            # pak de tijd ervan
            get_time = self.connection[get_rdm_station][get_rdm_connection]
            
            time.append(get_time)
            if sum(time) > time_max:
                time.pop()
                break
            

            del self.connection[get_rdm_station][get_rdm_connection]
            del self.connection[get_rdm_connection][get_rdm_station]

            # if len(self.connection[get_rdm_station]) == 0:
            #     self.connection.pop(get_rdm_station)
            # if len(self.connection[get_rdm_connection]) == 0:
            #     self.connection.pop(get_rdm_connection)
            
            # nieuw begin station
            get_rdm_station = get_rdm_connection
            
            traject.append(get_rdm_connection)
        
        return traject, sum(time)
    
    # geeft een random station met gegeven connecties
    def get_random_station(self):
        return random.choice(list(self.connection.items()))
    

    def make_lijnvoering(self): 
        T =[]
        while True:
            traject = Random.get_traject(self)
            
            if traject[1] == 0:
                continue
            T.append(traject)

            p = []
            for i in self.connection.values():
                if i == {}:
                    p.append(i)
            #pseudo voor als er geen connecties meer zijn
            if len(p) == 22:
                break
            
        
        return  T, len(T), len(p)

    def get_solution(self):

        total_stations = len(self.station)

        j=[]
        for i in self.connection.keys():
            j.append(i)
        all_possible_trajects = len(j)
        print(all_possible_trajects)
        lijnvoering = Random.make_lijnvoering(self)

        b = []
        for k in self.connection.values():
            b.append(k)
        print(b)
        
        # print(lijnvoering)
        T = lijnvoering[1]
        p = lijnvoering[2] 
        

    
    

        

            
            
               

        
    

            
        
        