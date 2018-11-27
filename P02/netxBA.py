#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
from random import randint
import networkx as nx
import math
import logging

# ejecucion del programa ./netxBA.py m, t
# m = int(sys.argv[1])
# t = int(sys.argv[2])
# m = 4
# t = 500


# take second element for sort
def takeSecond(elem):
    return elem[1]


# Grafo inicial
def initialGraph(G, m):
    # Nodos iniciales
    for i in range(m + 1):
        G.add_node(i)

    # Aristas iniciales
    for i in range(m + 1):
        for j in range(m + 1):
            if (j > i):
                G.add_edge(i, j)


# Nuevas aristas
def addNewEdges(G, m, sumaGrados, nuevoNodo):
    l = 1
    while l <= m:
        nuevoEnlace = randint(1, sumaGrados)
        acumulado = 0

        for _nodo in G.nodes():
            acumulado += len(G.adj[_nodo])

            if nuevoEnlace < acumulado:

                if not G.has_edge(nuevoNodo, _nodo):
                    G.add_edge(nuevoNodo, _nodo)
                    l += 1
                break


# Calculamos los datos requeridos
def calculateMetrics(G, density, hubDegree, avgDistance, clustering):
    density += nx.density(G)
    degree_sequence = sorted(nx.degree(G), key=takeSecond, reverse=True)
    hubDegree += degree_sequence[0][1]
    avgDistance += nx.average_shortest_path_length(G)
    clustering += nx.average_clustering(G)

    return density, hubDegree, avgDistance, clustering


# Creamos las variables de resultados
def redBA(m, t):
    # logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    # Creamos las variables de resultados
    density = 0
    hubDegree = 0
    avgDistance = 0
    clustering = 0

    # Creamos el grafo
    G = nx.Graph()

    for iteraccion in range(10):

        # Nodos iniciales
        initialGraph(G, m)

        # Recorremos todos los pasos iniciados
        for k in range(t):
            # Calculamos el nuevo nodo
            nuevoNodo = k + m + 1

            # Grado total del grafo
            sumaGrados = G.number_of_edges() * 2

            # Añadimos el nodo nuevo
            G.add_node(nuevoNodo)

            addNewEdges(G, m, sumaGrados, nuevoNodo)

        # Calculamos los datos requeridos
        density, hubDegree, avgDistance, clustering = calculateMetrics(
            G, density, hubDegree, avgDistance, clustering)

        # Limpiamos el grafo
        G.clear()

        # logging.debug('Vuelta ' + str(iteraccion))

    resultDensity = density / 10
    resultHubDegree = hubDegree / 10
    resultAvgDistance = avgDistance / 10
    resultClustering = clustering / 10

    return resultDensity, resultHubDegree, resultAvgDistance, resultClustering
