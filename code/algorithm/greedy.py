import random
from .randomize import Random
import copy

class Greedy():
    """Zoekt het steeds de kortste afstand met als beginstation een random"""

    def __init__(self, data):
        self.connection = data.connection
        self.trajectconnection = copy.deepcopy(self.connection)

        self.begin_station = random.choice(list(self.trajectconnection))

    def run(self):
        traject = []
        time_max = int(120)
        time = []
        # loop = 0
        # self.trajectconnection = copy.deepcopy(self.connection)
        # self.get_rdm_station = random.choice(list(self.trajectconnection))
        traject.append(self.begin_station)

        while sum(time) < time_max:
            if self.trajectconnection[self.begin_station] == {}:
                break

            new_station = Greedy.get_min(self)
 
            traject.append(new_station[0])
            time.append(new_station[1])
            if sum(time) > time_max:
                time.pop()
                traject.pop()
                break

            del self.trajectconnection[self.begin_station][new_station[0]]
            del self.trajectconnection[new_station[0]][self.begin_station]


            self.begin_station = new_station[0]
            # if self.trajectconnection[self.begin_station] == {}:
            #     del self.trajectconnection[self.begin_station]
            #     self.begin_station = random.choice(list(self.trajectconnection))
            #     print("OK")

        return traject, sum(time)

    def test(self):
        x=[]
        for i in range(5):
            x.append(Greedy.run(self))
        # print(self.trajectconnection)
        return x

    def make_lijnvoering(self): 
    
        loop = 0
        while True:
            
            T =[]
            while True:
                loop += 1
                # print(T)
                traject = Greedy.run(self)
                
                if traject[1] == 0:
                    self.begin_station = random.choice(list(self.trajectconnection))
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
        all_time = []
        for i in T:
            all_time.append((i[1]))
        all_time = sum(all_time)

        print(f"aantal loops: {loop}")
        print(f"aantal trajecten: {len(T)}")
        print(f"aantal min samen: {all_time}")

        return  T, len(T), len(p), all_time

    def get_min(self):
        #getting maximum distance of the connecties
        get_all_connections = self.trajectconnection[self.begin_station]

        sort = sorted(get_all_connections.items())

        min_value = sort[0]

        return min_value