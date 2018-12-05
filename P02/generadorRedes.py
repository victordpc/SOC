#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import netBA
import netxBA
import random_netX


datosT = [5000, 1000, 500]
datosM = [3, 4]
datosRnodos=[500, 1000,  5000,  500,  1000, 5000,  500,   1000,   5000,   500, 1000, 5000]
datosRprob=[0.001,0.0005,0.0001,0.002,0.001,0.0002,0.0072,0.00395,0.00095,0.02,0.01,0.002]


def helpgeneradorRedesBA():
    strHelp = 'generadorRedesBA\n'
    strHelp += 'Usage:  generadorRedesBA Commands\n'
    strHelp += '\n'
    strHelp += 'Commands:\n'
    strHelp += '    gephi   - Genera redes de Barabasi-Albert para importar en gephi con las combinaciones de valores m=[3,4] y t=[500,1000,5000]\n'
    strHelp += '    netX    - Genera 10 redes de Barabasi-Albert con las combinaciones de valores m=[3,4] y t=[500,1000,5000] y devuelve las medias de los valores de las métricas\n'
    strHelp += '    random  - Genera 10 redes de Aleatorias de 5000, 1000 y 500 nodos y devuelve las medias de los valores de las métricas para todas las etapas\n'
    print(strHelp)


# Obtenemos los parametros
default = (len(sys.argv) == 1)


def crearRedBAGephi():
    for j in range(len(datosT)):
        for i in range(len(datosM)):
            netBA.redBA(datosM[i],datosT[j])


def crearRedBANetworkX():
    for j in range(len(datosT)):
        for i in range(len(datosM)):
            print('M ' + str(datosM[i]) + ' T ' + str(datosT[j]))
            print(netxBA.redBA(datosM[i], datosT[j]))


def crearRedAleatoriaNetworkX():
    for i in range(len(datosRnodos)):
            print('M ' + str(datosRnodos[i]) + ' P ' + str(datosRprob[i]))
            print(random_netX.redAleatoria(datosRnodos[i], datosRprob[i]))


if default:
    helpgeneradorRedesBA()
else:
    mode = (sys.argv[1])
    if mode == 'gephi':
        crearRedBAGephi()

    elif mode == 'netX':
        crearRedBANetworkX()

    elif mode== 'random':
        crearRedAleatoriaNetworkX()

    else:
        helpgeneradorRedesBA()
