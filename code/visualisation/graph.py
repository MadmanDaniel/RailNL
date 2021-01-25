# Code hierboven is alleen nodig voor Matplotlib 
# (dus visualisatie van de datapunten) -> is van extension Jupyter
# from code.classes import station, load
import matplotlib.pyplot as plt
import networkx as nx
import random

def random_color():
    # https://stackoverflow.com/questions/28999287/generate-random-colors-rgb
    random_color = "#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
    return random_color
    

def get_map(data, con):

    lijnvoering = con
    
    P = nx.Graph() 
    pos = data.get_cor()
    # P.add_nodes_from(pos)

    some_colors = ["r", "b", "g", "y","c","m","y","k"]
    # some_colors = list(random.choice(range))
    
    for a_traject in lijnvoering:
        traject = []
        for i in range(0, len(a_traject)):
            if i == len(a_traject) - 1:
                break
            connection1 = a_traject[i]
            connection2 = a_traject[i+1]
            connection = (connection1, connection2)
            traject.append(connection)
      
        P.add_edges_from(traject, color= random_color(), weight=2.5)
    
    # https://stackoverflow.com/questions/25639169/networkx-change-color-width-according-to-edge-attributes-inconsistent-result
    # https://stackoverflow.com/questions/20133479/how-to-draw-directed-graphs-using-networkx-in-python

    edges = P.edges()
    colors = [P[u][v]['color'] for u,v in edges]
    weights = [P[u][v]['weight'] for u,v in edges]
    # plt.grid()
    fig,ax = plt.subplots(1, figsize = (15,15))
    nx.draw(P, pos, edge_color=colors, width=weights, node_color="black", node_size=50)
    
    
    plt.show()
    plt.savefig('data/quality/map.png')

   
