#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
from random import randint


# Crea un grafo completo con k=m
def initialGraph(m, nodos, aristas):
    for i in range(m+1):
        nodos.append(m)
        for j in range(m+1):
            if (j > i):
                aristas.append(str(i) + '-' + str(j))


# Calculamos los enlaces que se van a crear
def calculateEdges(m, sumaGrados, nodos, nuevosEnlaces):
    l = 1
    while l <= m:
        nuevoEnlace = randint(1, sumaGrados)

        acumulado = 0
        _nodo = -1
        for _prob in nodos:
            _nodo += 1
            acumulado += _prob
            if nuevoEnlace < acumulado:

                if _nodo not in nuevosEnlaces:
                    nuevosEnlaces.append(_nodo)
                    l += 1
                break


# Añadimos nuevos enlaces
def addNewEdges(nuevosEnlaces, aristas, nuevoNodo, nodos):
    for _enlace in nuevosEnlaces:
        aristas.append(str(_enlace) + '-' + str(nuevoNodo))
        nodos[_enlace] += 1


# Creamos los ficheros de salida
def createFiles(m, N, i):
    if not os.path.exists(os.path.join(os.getcwd(), 'Files')):
        os.makedirs(os.path.join(os.getcwd(), 'Files'))

    FICHERONODOS = os.path.join(
        os.getcwd(), 'Files',
        'BA_NODOS' + '_M' + str(m) + '_T' + str(N) + '_' + str(i) + '.csv')
    FICHEROARISTAS = os.path.join(
        os.getcwd(), 'Files',
        'BA_ARISTAS' + '_M' + str(m) + '_T' + str(N) + '_' + str(i) + '.csv')
    return FICHERONODOS, FICHEROARISTAS


# Sacar a fichero los datos para gephi
def toFiles(FICHERONODOS, nodos, FICHEROARISTAS, aristas):

    # Fichero de nodos
    f = open(FICHERONODOS, 'w')
    f.write('Id, Probabilidad' + '\n')
    _n = 0
    for _p in nodos:
        f.write(str(_n) + ', ' + str(_p) + '\n')
        _n += 1
    f.close()

    # Fichero de aristas
    f = open(FICHEROARISTAS, 'w')
    f.write('Id, Source, Target, Type' + '\n')
    i = 0
    for _a in aristas:
        _origen, _destino = _a.split('-')
        f.write(str(i) + ',' + str(_origen) + ', ' +
                str(_destino) + ',Undirected' '\n')
        i += 1
    f.close()


# Main
if __name__ == '__main__':
    # arg[1] -> m
    # arg[2] -> N
    # print(sys.argv)
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("ERROR")
        exit(1)

    i = 0
    if len(sys.argv) == 4:
        i = int(sys.argv[3])

    m = int(sys.argv[1])
    N = int(sys.argv[2])

    # m=4
    # N=500
    m0 = m+1
    t = N-m0

    nodos = []
    aristas = []
    sumaGrados = (m * (m + 1))

    initialGraph(m, nodos, aristas)

    for k in range(m0, t):
        nuevoNodo = k
        nuevosEnlaces = []

        calculateEdges(m, sumaGrados, nodos, nuevosEnlaces)

        nodos.append(m)

        addNewEdges(nuevosEnlaces, aristas, nuevoNodo, nodos)

        sumaGrados += 2 * m

    FICHERONODOS, FICHEROARISTAS = createFiles(m, N, i)
    toFiles(FICHERONODOS, nodos, FICHEROARISTAS, aristas)
