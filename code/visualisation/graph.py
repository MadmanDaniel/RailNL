# Code hierboven is alleen nodig voor Matplotlib 
# (dus visualisatie van de datapunten) -> is van extension Jupyter
# from code.classes import station, load
import matplotlib.pyplot as plt
import networkx as nx
import random


def get_map(data, con):

    lijnvoering = con.make_lijnvoering()[4]
    
    P = nx.Graph() 
    pos = data.get_cor()
    P.add_nodes_from(pos)
    
    # edges = []
    # for key, value in data.get_con().items():
    #     tup = tuple(value)
    #     for i in tup:
    #         e = []
    #         e.append(key)
    #         e.append(i)
    #         e= tuple(e)
    #         edges.append(e)
    # P.add_edges_from(edges)


    some_colors = ["r", "b", "g", "y","c","m","y","k"]
    
    for a_traject in lijnvoering:

        traject = []
 
        for i in range(0, len(a_traject)):
            
            if i == len(a_traject) - 1:
                break

            connection1 = a_traject[i]
            connection2 = a_traject[i+1]
            connection = (connection1, connection2)
            traject.append(connection)


        P.add_edges_from(traject, color= random.choice(list(some_colors)), weight=3)
    

    # nx.draw_networkx_edges(P, pos, edgelist=x , edge_color='r')


    # print(x)
    print("---")
    print(lijnvoering)
    #https://stackoverflow.com/questions/25639169/networkx-change-color-width-according-to-edge-attributes-inconsistent-result
    edges = P.edges()
    colors = [P[u][v]['color'] for u,v in edges]
    weights = [P[u][v]['weight'] for u,v in edges]
    
    fig,ax = plt.subplots(1, figsize = (15,15))
    nx.draw(P, pos,with_labels = True, edge_color=colors, width=weights)
    plt.show()
    plt.savefig('data/quality/map.png')
    # return P.edges()
    
    # print(data.get_cor())
    # ------------------------------------------------------------------------------------------------
    # https://stackoverflow.com/questions/20133479/how-to-draw-directed-graphs-using-networkx-in-python

    #https://stackoverflow.com/questions/11804730/networkx-add-node-with-specific-position
    # You can add nodes using add_nodes_from()
    # P.add_nodes_from(['A'])
    # # Use add_edges_from to add pairwise relationships
    # P.add_edges_from ([('B','C')])
    # print(P.nodes())
    # print(P.edges())
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////
