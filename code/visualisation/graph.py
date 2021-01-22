# Code hierboven is alleen nodig voor Matplotlib 
# (dus visualisatie van de datapunten) -> is van extension Jupyter
# from code.classes import station, load
import matplotlib.pyplot as plt
import networkx as nx


def get_map(data, con):

    lijnvoering = con.make_lijnvoering()[4]
    
    P = nx.Graph() 
    pos = data.get_cor()
    P.add_nodes_from(pos)
    
    edges = []
    for key, value in data.get_con().items():
        tup = tuple(value)
        for i in tup:
            e = []
            e.append(key)
            e.append(i)
            e= tuple(e)
            edges.append(e)
    P.add_edges_from(edges)


    x = []
    for station in lijnvoering:
        tup = station

        for i in range(0, len(tup)):
            if i == len(tup) - 1:
                break

            connection1 = tup[i]
            connection2 = tup[i+1]

            connection = [connection1,connection2]
            x.append(connection)
    print(x)
    print(lijnvoering)
    

    
    fig,ax = plt.subplots(1, figsize = (15,15))
    nx.draw(P, pos, with_labels = True)
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
