#%% 
# Code hierboven is alleen nodig voor Matplotlib 
# (dus visualisatie van de datapunten) -> is van extension Jupyter
# from code.classes import station, load
import matplotlib.pyplot as plt
import networkx as nx

def get_map(data):
    
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
    
    fig,ax = plt.subplots(1, figsize = (15,12))
    nx.draw(P, pos,with_labels = True)
    plt.show()
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

   