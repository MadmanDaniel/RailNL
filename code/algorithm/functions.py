
import random
import pandas as pd

def best_output(algorithm):
    highest_traject = algorithm.make_lijnvoering()
    highest_output = highest_traject[0]

    all_q = []
    for i in range(100):
        lijnvoering = algorithm.make_lijnvoering()
        all_q.append(lijnvoering[0])

        new_output = lijnvoering[0]
        if new_output > highest_output:
            highest_output = new_output
            highest_traject = lijnvoering

    data = {'q': all_q
    }
    filename = "data/quality/greedy_output.csv"
    df = pd.DataFrame(data, columns = ['q'])
    df.to_csv(filename)

    return highest_output, highest_traject[1]


def get_q(p,T,Min):
    q = round((p*10000 - (T*100 + Min)) , 2)
    return q

def get_shortest_des(get_con):
    sort = sorted(get_con.items(), key=lambda item: item[1])
    min_value = sort[0]
    return min_value

def get_remain_con(remain_con):
    used_con = []
    for key, value in remain_con:
        used_con += value
    used_con = (len(used_con)/2)

    return used_con
    

def my_copy(connection):
    copy_connection = dict()
    for k,v in connection.items():
        copy_connection[k] = v.copy()
    return copy_connection

def get_next_con(begin_station, connections):
    return connections[begin_station]

def get_time(connections, begin_station, next_station):
    return connections[begin_station][next_station]





# def get_solution(self):
#     total_loops = 0
#     ans = []
#     for i in range(1000):
#         lijnvoering = Random.make_lijnvoering(self)
#         total_loops += lijnvoering[3]

#         T = lijnvoering[0]
#         Min = lijnvoering[2]

#         used_con = lijnvoering[1]
#         p = used_con/self.all_con

        
#         ans.append(float(q))

    # #https://www.geeksforgeeks.org/writing-csv-files-in-python/
    # data = {'q': ans
    # }
    # filename = "data/quality/random_output.csv"

    # df = pd.DataFrame(data, columns = ['q'])
    # df.to_csv(filename)

    # # print(f"loops random: {total_loops}")
    # return print(f"loops randomize: {total_loops}")