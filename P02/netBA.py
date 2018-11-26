#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import csv
import sys
import random
from random import randint

# ejecucion del programa ./netBA.py m, t
m = sys.argv[1]
t = sys.argv[2]
# m = 4
# t = 500

FICHERONODOS = 'P02/BA_NODOS' + '_M' + str(m) + '_T' + str(t) + '.csv'
FICHEROARISTAS = 'P02/BA_ARISTAS' + '_M' + str(m) + '_T' + str(t) + '.csv'

nodos = dict()
aristas = dict()
sumaGrados = (m * (m + 1))

for i in range(m + 1):
    nodos[i] = m

for i in range(m + 1):
    for j in range(m + 1):
        if (j > i):
            aristas[str(i) + '-' + str(j)] = str(i) + '-' + str(j)

for k in range(t):
    i += 1
    nodos[i] = m
    nuevosEnlaces = []

    l = 1
    while l <= m:
        nuevoEnlace = randint(1, sumaGrados)

        acumulado = 0
        for _nodo, _prob in nodos.items():
            acumulado += _prob
            if nuevoEnlace < acumulado:

                if _nodo not in nuevosEnlaces:
                    nuevosEnlaces.append(_nodo)
                    l += 1
                break

    for _enlace in nuevosEnlaces:  #str(_nodo) + '-' + str(l)
        aristas[str(_enlace) + '-' + str(i)] = str(_enlace) + '-' + str(i)
        nodos[_enlace] += 1

    sumaGrados += 2 * m

    # Sacar a fichero los datos para gephi

# Fichero de nodos
f = open(FICHERONODOS, 'w')
f.write('Id, Probabilidad' + '\n')
for _n, _p in nodos.items():
    f.write(str(_n) + ', ' + str(_p) + '\n')
f.close()

# Fichero de aristas
f = open(FICHEROARISTAS, 'w')
f.write('Id, Source, Target' + '\n')
i = 0
for _a in aristas.keys():
    _origen, _destino = _a.split('-')
    f.write(str(i) + ',' + str(_origen) + ', ' + str(_destino) + '\n')
    i += 1
f.close()
