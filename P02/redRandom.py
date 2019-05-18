#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv
import random
import sys


# Creamos los ficheros de salida
def createFiles(N, p, i):
    if not os.path.exists(os.path.join(os.getcwd(), 'Files')):
        os.makedirs(os.path.join(os.getcwd(), 'Files'))

    FICHERONODOS = os.path.join(
        os.getcwd(), 'Files',
        'Random_NODOS' + '_N' + str(N) + '_T' + str(p) + '_' + str(i) + '.csv')
    FICHEROARISTAS = os.path.join(
        os.getcwd(), 'Files',
        'Random_ARISTAS' + '_N' + str(N) + '_T' + str(p) + '_' + str(i) + '.csv')
    return FICHERONODOS, FICHEROARISTAS


# Sacar a fichero los datos para gephi
def toFiles(FICHERONODOS, N, FICHEROARISTAS, aristas):
    # Fichero de nodos
    f = open(FICHERONODOS, 'w')
    f.write('Id' + '\n')
    for i in range(N):
        f.write(str(i) + '\n')
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
    # arg[1] -> N
    # arg[2] -> prob
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("ERROR")
        exit(1)
    N = int(sys.argv[1])
    prob = float(sys.argv[2])
    # N=100
    # prob=0.009

    i = 0
    if len(sys.argv) == 4:
        i = int(sys.argv[3])

    aristas = []

    for j in range(N):
        for k in range(i+1, N):
            ran = random.random()
            if(prob >= ran):
                aristas.append(str(j) + '-' + str(k))

    FICHERONODOS, FICHEROARISTAS = createFiles(N, prob, i)
    toFiles(FICHERONODOS, N, FICHEROARISTAS, aristas)
