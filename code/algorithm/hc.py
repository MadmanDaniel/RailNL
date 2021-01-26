import copy
from code.algorithm import functions, randomize, greedy
import random
class Hillclimber():

    def __init__(self, data, max_time, max_traject):
        self.connections = data.connection
        self.copy_connection = copy.deepcopy(self.connections)
        self.all_con = data.all_con()

        self.max_time = max_time
        self.max_traject = max_traject
        self.traject = []
        self.time = []
        self.used_con = []
        

    def get_best_traject(self):
        iteration = 0
        # best_traject = randomize.Random.get_traject(self)
        best_traject = greedy.Greedy.get_traject(self)

        # print(best_traject)
        Min1 = best_traject[1]
        T1 = 1
        p1 = (self.all_con - (functions.get_remain_con(self.copy_connection.items()))) / self.all_con
        best_q= functions.get_q(p1,T1,Min1)

        # self.copy_connection = functions.my_copy(self.connections)

        for i in range(100):
            # print(best_traject)
            

            iteration += 1
            # get_traject = randomize.Random.get_traject(self)
            get_traject = greedy.Greedy.get_traject(self)

            if get_traject[0][0] in self.used_con:
                continue
            Min = get_traject[1]
            T =1
            p = (self.all_con - (functions.get_remain_con(self.copy_connection.items()))) / self.all_con 
            get_q = functions.get_q(p,T,Min)
            
            if get_q > best_q:
                best_traject = get_traject
                best_q = get_q
            self.copy_connection = functions.my_copy(self.connections)
    
        return best_traject

    def make_lijnvoering(self):
        lijnvoering = []
        Min = 0

        for i in range(self.max_traject):
            get_traject = self.get_best_traject()
 
            Min += get_traject[1]
            lijnvoering.append(get_traject[0])

        self.used_con = []
        for traject in lijnvoering:
            for index, station in enumerate(traject):
                if index +1 < len(traject):
                    if [traject[index], traject[index+1]] not in self.used_con:
                        self.used_con.append([traject[index], traject[index+1]])
                        self.used_con.append([traject[index+1], traject[index]])   
                       
        T = len(lijnvoering)
        p = (len(self.used_con)/2) / self.all_con
        get_q = functions.get_q(p, T, Min)

        # self.used_con = []
        print(p, T,Min, get_q)
        return get_q, lijnvoering ,Min, T
        


    
                
                
            

                

        
    

            
