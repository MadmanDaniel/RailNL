from code.algorithm import functions, greedy
import random
import copy


class Hillclimber():
    def __init__(self, data, best_output,  max_time):
        self.copy_connection = data.connection
        self.best_q = best_output[0]

        self.best_traject = best_output[1]
        
        self.used_time = best_output[2]
        self.con_notused = best_output[4]

        #aantal
        self.used_con = best_output[3]  

        self.max_time = max_time

        self.all_con = data.all_con()
        
    def delete_trajects(self):
        
        
        self.copy_traject = self.best_traject.copy()
        self.copy_notused = self.con_notused.copy()
        self.copy_time = self.used_time

        
        random_traject1 = random.choice(self.copy_traject)
        time_minus = 0
        for index, station in enumerate(random_traject1):
            if index  +1 == len(random_traject1):
                break
            get_time = self.copy_connection[random_traject1[index]][random_traject1[index+1]]

            if random_traject1[index] not in self.copy_notused:
                self.copy_notused[random_traject1[index]] = {}
            if random_traject1[index+1] not in self.copy_notused:
                self.copy_notused[random_traject1[index+1]] = {}

            self.copy_notused[random_traject1[index]][random_traject1[index+1]] = get_time
            self.copy_notused[random_traject1[index+1]][random_traject1[index]] = get_time
        
            time_minus += get_time
        self.copy_traject.remove(random_traject1)
        
        self.copy_time = (self.copy_time - time_minus)
        
        
        # print( functions.get_remain_con(self.copy_notused.items()))
        # print("----")
        
        
        return self.copy_traject, self.copy_time, self.copy_notused


    def add_trajects(self):
        # self.delete_trajects()
        self.copy_traject = self.delete_trajects()[0]
        self.copy_notused= self.delete_trajects()[2]
        self.copy_time= self.delete_trajects()[1]
        
    
        start_station = random.choice(list(self.copy_notused))
        traject = [start_station]
        time = []
        # print(self.copy_notused)
        while sum(time) < self.max_time:
        
            get_connections = self.copy_connection[start_station]

            next_station = []
            for station in get_connections:
                if station in self.copy_notused:
                    next_station.append(station)

            if next_station == []:
                next_station = random.choice(list(get_connections))
            else:
                next_station = random.choice(list(next_station))

            get_time = self.copy_connection[start_station][next_station]
            time.append(get_time)
            if sum(time) > self.max_time:
                time.pop()
                break
        
            traject.append(next_station)
            # print(self.copy_notused)
            
            if start_station in self.copy_notused:
                del self.copy_notused[start_station]
            if next_station in self.copy_notused:
                del self.copy_notused[next_station]
            
            # print(self.copy_notused)
             
            start_station = next_station

    
        self.copy_time = sum(time) + self.copy_time
        # print(len(self.copy_notused.values()))
        # print(self.all_con)
        p = (self.all_con - len(self.copy_notused.values()))  / self.all_con
        # print(self.copy_notused.items())
        # print( functions.get_remain_con(self.copy_notused.items()))
        self.copy_traject.append(traject)
        T = len(self.copy_traject)
        get_q = functions.get_q(p,T,self.copy_time)
        
        return get_q ,self.copy_traject, self.copy_time, self.copy_notused, p, T

    def get_best_q(self):
    
        for i in range(10):
            print(f"begin voor update: {self.best_traject}\n")
            print(f"begin voor update: {self.best_q, self.used_time }\n")
            self.delete_trajects()
            new_traject = self.add_trajects()
            
            print(f"data na update: {self.copy_traject}\n")
            print(f"data na update: {new_traject[0],new_traject[4], new_traject[5], new_traject[2]}" )

            if new_traject[0] > self.best_q:
                self.best_q = new_traject[0]
                self.best_traject = new_traject[1]
                self.used_time = new_traject[2]
                self.copy_notused = new_traject[3]
            

                
            

            







        
        