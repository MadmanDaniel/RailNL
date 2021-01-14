# from code.classes.load import Load
import random
import copy

class Random():

    def __init__(self, data):
        # data from load.py
        self.connection = copy.deepcopy(data.connection)
        self.station = copy.deepcopy(data.stations)

        # self.traject = []

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
        # test om te beginnen met alkmaar
        # get_rdm_station = "Alkmaar"
        traject.append(get_rdm_station)
        while True:
            if sum(time) > time_max:
                break
            # print(traject)
            # loop += 1
            #pakt alle connecties van get_rdm_station
            get_connections = self.connection[get_rdm_station]

            # als alle connections gedelete zijn moet stoppen met loopen
            if get_connections == {}:
                break
            
            # pakt random connectie ervan
            get_rdm_connection = random.choice(list(get_connections))
           
            # als het in het traject al zit EN het maar 1 richting op kan
            if get_rdm_connection in traject and len(get_connections) == 0:
                break
            
            # pak de tijd ervan
            get_time = self.connection[get_rdm_station][get_rdm_connection]
            time.append(get_time)

            # {'Alkmaar': {'Hoorn': 24, 'Den Helder': 36, 'Castricum': 9}
            del self.connection[get_rdm_station][get_rdm_connection]
            # {'Alkmaar': { 'Den Helder': 36, 'Castricum': 9}

            #'Hoorn': {'Alkmaar': 24, 'Zaandam': 26}
            del self.connection[get_rdm_connection][get_rdm_station]
            #'Hoorn': { 'Zaandam': 26}

            
            # nieuw begin station
            get_rdm_station = get_rdm_connection
            if len(self.connection[get_rdm_connection]) ==0:
                del self.connection[get_rdm_connection] 
            if len(self.connection[get_rdm_station]) ==0:
                del self.connection[get_rdm_station] 
            traject.append(get_rdm_connection)
            

        # vb: als 110 is lager dan 120
        # Maar loop loopt nog door. laatste element moet daarom verwijderd worden.
        if sum(time) > time_max:
            time.pop()
            traject.pop()


        return traject, sum(time)

    def lijnvoering(self):
        pass
    
    # geeft een random station met gegeven connecties
    def get_random_station(self):
        return random.choice(list(self.connection.items()))

    # def test(self):
    #     l =[]
    #     for i in range(7): 
    #         traject = Random.get_traject(self)
    #         l.append(traject)
    #     # x = tuple
    #     # lijst l   
    #     for x in l:
    #         for y in range(len(x)):
    #             if x[y] == 0:
    #                 print(x[y])
                
            
            # if x[1] == 0:
            #     del l[x]
            # else: 
            #     break

            # for y in l[x]:
            #     if y == 0:
            #         print(l[x-1])
        # return l
    #(['Den Helder'], 0)
            
        
    def test2(self):
        l =[]
        i = 0
        while True:
            traject = Random.get_traject(self)
            i += 1
            if i == 7:
                break

            if self.connection.values() ==0:
                break
            
            print(traject)

        
            
        # l[is 1 traject]
        # l[][alleen number]