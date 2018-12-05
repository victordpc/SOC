#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv
import random
import sys
import networkx as nx


# take second element for sort
def takeSecond(elem):
    return elem[1]


# Grafo inicial
def initialGraph(G, m):
    # Nodos iniciales
    for i in range(m + 1):
        G.add_node(i)


# Calculamos los datos requeridos
def calculateMetrics(G, enlaces, gradoMedio, density, hubDegree, avgDistance, clustering, componentes):
	enlaces +=nx.number_of_edges(G)

	Nodos,K = G.order(), G.size()
	gradoMedio += float(K*2)/Nodos
	
	density += nx.density(G)
	
	degree_sequence = sorted(nx.degree(G), key=takeSecond, reverse=True)
	hubDegree += degree_sequence[0][1]
	
	if nx.number_connected_components(G)==1:
		avgDistance += nx.average_shortest_path_length(G)
	clustering += nx.average_clustering(G)
	componentes += nx.number_connected_components(G)

	return enlaces,gradoMedio,density, hubDegree, avgDistance, clustering,componentes


# Creamos las variables de resultados
def redAleatoria(nNodes, p):
    # logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    # Creamos las variables de resultados
	enlaces = 0
	gradoMedio = 0
	density = 0
	hubDegree = 0
	avgDistance = 0
	clustering = 0
	componentes = 0

    # Creamos el grafo
	G = nx.Graph()


	for iteraccion in range(10):

		# Nodos iniciales
		initialGraph(G, nNodes)

		# Creamos las aristas
		for i in range(nNodes):
			j = i+1
			while j < nNodes:
				if p >= random.uniform(0, 1):
					G.add_edge(i,j)
				j += 1

		# Calculamos los datos requeridos
		enlaces, gradoMedio, density, hubDegree, avgDistance, clustering, componentes = calculateMetrics(G, enlaces, gradoMedio, density, hubDegree, avgDistance, clustering, componentes)

		# Limpiamos el grafo
		G.clear()

	resultEnlaces = enlaces / 10
	resultGradoMedio = gradoMedio / 10
	resultDensity = density / 10
	resultHubDegree = hubDegree / 10
	resultAvgDistance = avgDistance / 10
	resultClustering = clustering / 10
	resultComponentes = componentes / 10

	return resultEnlaces, resultGradoMedio, resultDensity, resultHubDegree, resultAvgDistance, resultClustering, resultComponentes


# redAleatoria(500,0.001)