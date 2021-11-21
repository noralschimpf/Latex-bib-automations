import json, os
import numpy as np
import networkx as nx
import pylab as P
import utils as u

def main():
    with open('referenceCategories/joint.json','r') as f:
        jointdic = json.load(f)


    nodedic = {}
    edges = []
    nodecounter = 0
    for key in jointdic:
        lis_nodes = key.split('-')
        if len(lis_nodes) == 2 and not '' in lis_nodes:
            for node in lis_nodes:
                if not (node in nodedic):
                    nodedic[node] = nodecounter
                    nodecounter += 1
            edges.append([nodedic[lis_nodes[0]], nodedic[lis_nodes[1]]])

    edges = np.array(edges)
    G = nx.Graph(); G.add_edges_from(edges)
    pos = nx.spring_layout(G, k=2, iterations=600)
    # nx.draw_networkx(G, pos, with_labels=False)
    nx.draw_networkx_labels(G,pos=pos, labels={nodedic[x]:x.replace(' ','\n') for x in nodedic}, font_color='whitesmoke')
    nx.draw_networkx_nodes(G, pos=pos, node_color='tab:blue', alpha=0.7,
                                 node_size=max([len(v) * 300 for v in nodedic]),
                                 )
    nx.draw_networkx_edges(G, pos=pos)
    P.tight_layout()
    P.show(block=True)

if __name__ == '__main__': main()