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

    return density, hubDegree, avgDistance, clustering


# take second element for sort
def takeSecond(elem):
    return elem[1]


# Creamos los ficheros de salida
def createFiles(model):
    if not os.path.exists(os.path.join(os.getcwd(), 'Result')):
        os.makedirs(os.path.join(os.getcwd(), 'Result'))

    result = os.path.join(
        os.getcwd(), 'Result',
        model.upper() + '.csv')

    if not os.path.exists(result):
        f = open(result, 'w')
        f.write('Model, Parameter, Density, HubDegree, AvgDistance, Clustering' + '\n')
        f.close()

    return result


# Sacar a fichero los datos para gephi
def toFiles(file, model, parameter, density, hubDegree, avgDistance, clustering):
    f = open(file, '+a')
    f.write(str(model) + ',' + str(parameter) + ', ' + str(density) + ', ' + str(hubDegree) +
            ', ' + str(avgDistance) + ', ' + str(clustering) + '\n')
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
    G.add_nodes_from(nodes)

    # Load edges
    for edge in edges:
        edge = edge.split(',')
        G.add_edge(edge[1], edge[2])
    return G


if __name__ == '__main__':
    # argv[1] network model
    # argv[2] nodes file name
    # argv[3] edges file name
    # argv[4] network parameter
    # if len(sys.argv) != 5:
    #     print("ERROR")
    #     exit(1)

    # name = sys.argv[1]
    # fNodes = sys.argv[2]
    # fEdges = sys.argv[3]
    # parameter = sys.argv[4]
    name='BA' 
    fNodes='Files/BA_NODOS_M3_T500_1.csv'        
    fEdges='Files/BA_ARISTAS_M3_T500_1.csv'  
    parameter='3'

    print(name + ' '+ parameter)

    if not os.path.exists(os.path.join(os.getcwd(), fNodes)):
        print("Nodes file don't exists")
        exit(1)
    if not os.path.exists(os.path.join(os.getcwd(), fEdges)):
        print("Edges file don't exists")
        exit(1)

    nodes, edges = readFiles()

    # Load nodes
    G = loadGraph()

    density, hubDegree, avgDistance, clustering = calculateMetrics(G)

    file = createFiles(name)
    toFiles(file, name, parameter, density, hubDegree, avgDistance, clustering)
