#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import sys
import networkx as nx


# Calculate metrics
def calculateMetrics(G):
    density = nx.density(G)
    degree_sequence = sorted(nx.degree(G), key=takeSecond, reverse=True)
    hubDegree = degree_sequence[0][1]

    if(nx.is_connected(G)):
        avgDistance = nx.average_shortest_path_length(G)
    else:
        avgDistance = 'not connected'
    clustering = nx.average_clustering(G)

    L=G.number_of_edges()

    degree=0
    for node in G:
        degree+=G.degree(node)
    K=degree / G.number_of_nodes()

    componentes= nx.number_connected_components(G)

    return density, hubDegree, avgDistance, clustering, L, K, componentes 


# take second element for sort
def takeSecond(elem):
    return elem[1]


# Creamos los ficheros de salida
def createFile(model):
    if not os.path.exists(os.path.join(os.getcwd(), 'Result')):
        os.makedirs(os.path.join(os.getcwd(), 'Result'))

    result = os.path.join(
        os.getcwd(), 'Result',
        model.upper() + '.csv')

    if not os.path.exists(result):
        f = open(result, 'w')
        if model.upper()=='BA':
            f.write('Model;Nodes;Parameter;Density;HubDegree;AvgDistance;Clustering;L' + '\n')
        else:
            f.write('Model;Nodes;Parameter;Density;HubDegree;AvgDistance;Clustering;L;K;NumComp' + '\n')
        f.close()

    return result


# Sacar a fichero los datos para gephi
def toFile(file, model, nNodes, parameter, density, hubDegree, avgDistance, clustering,L,K,componentes):
    f = open(file, '+a')
    if model.upper()=='BA':
        f.write(str(model) + ';' + str(nNodes) + ';' + str(parameter).replace('.', ',') + '; ' + str(density).replace('.', ',') + ';' + str(hubDegree).replace('.', ',') +
        ';' + str(avgDistance).replace('.', ',') + ';' + str(clustering).replace('.', ',')  + ';' + str(L).replace('.', ',') + '\n')
    else:
        f.write(str(model) + ';' + str(nNodes) + ';' + str(parameter).replace('.', ',') + '; ' + str(density).replace('.', ',') + ';' + str(hubDegree).replace('.', ',') +
        ';' + str(avgDistance).replace('.', ',') + ';' + str(clustering).replace('.', ',')  + ';' + str(L).replace('.', ',') + ';' + str(K).replace('.', ',') + ';' + str(componentes).replace('.', ',') + '\n')

    f.close()


def readFiles():
    # Read nodes in files
    with open(fNodes, "r") as f:
        nodes = f.readlines()
    f.close()

    del nodes[0]

    # Read edges in files
    with open(fEdges, "r") as f:
        edges = f.readlines()
    f.close()

    del edges[0]
    return nodes, edges


def loadGraph():
    # Load nodes
    G = nx.Graph()
    for node in nodes:
        node = node.split(',')
        G.add_nodes_from(node[0].strip())

    # Load edges
    for edge in edges:
        edge = edge.split(',')
        G.add_edge((edge[1]).strip(), (edge[2]).strip())
    return G


if __name__ == '__main__':
    # argv[1] network model
    # argv[2] number of nodes
    # argv[3] nodes file name
    # argv[4] edges file name
    # argv[5] network parameter
    if len(sys.argv) != 6:
        print("ERROR")
        exit(1)

    name = sys.argv[1]
    nNodes = sys.argv[2]
    fNodes = sys.argv[3]
    fEdges = sys.argv[4]
    parameter = sys.argv[5]

    # #
    # name='BA'
    # fNodes='Files/BA_NODOS_M4_T500_1.csv'
    # fEdges='Files/BA_ARISTAS_M4_T500_1.csv'
    # parameter='4'
    # #

    print(name + ' ' + parameter)

    if not os.path.exists(os.path.join(os.getcwd(), fNodes)):
        print("Nodes file don't exists")
        exit(1)
    if not os.path.exists(os.path.join(os.getcwd(), fEdges)):
        print("Edges file don't exists")
        exit(1)

    nodes, edges = readFiles()

    # Load nodes
    G = loadGraph()

    density, hubDegree, avgDistance, clustering, L, K, componentes = calculateMetrics(G)

    file = createFile(name)
    toFile(file, name, nNodes, parameter, density, hubDegree, avgDistance, clustering, L, K, componentes)
