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

            # loop += 1
            #pakt alle connecties van get_rdm_station
            get_connections = self.connection[get_rdm_station]

            # als alle connections gedelete zijn moet stoppen met loopen
            if get_connections == {}:
                break

            # pakt random connectie ervan
            get_rdm_connection = random.choice(list(get_connections))

            # als het in het traject al zit EN het maar 1 richting op kan
            if get_rdm_connection in traject and len(get_connections) == 1:
                break
            
            # pak de tijd ervan
            get_time = self.connection[get_rdm_station][get_rdm_connection]
            time.append(get_time)

            del self.connection[get_rdm_station][get_rdm_connection]
            del self.connection[get_rdm_connection][get_rdm_station]
            
            
            # nieuw begin station
            get_rdm_station = get_rdm_connection
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

    def test(self):
        l =[]
        for i in range(50):
            traject = Random.get_traject(self)
            
            l.append(traject)
            # for i in l:

        k = l[1]
        return  k