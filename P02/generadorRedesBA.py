#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import netBA
import netxBA

# datosT = [5000]
# datosM = [3]
datosT = [5000, 1000, 500]
datosM = [3, 4]


def helpgeneradorRedesBA():
    strHelp = 'generadorRedesBA\n'
    strHelp += 'Usage:  generadorRedesBA Commands\n'
    strHelp += '\n'
    strHelp += 'Commands:\n'
    strHelp += '    gephi   - Genera redes de Barabasi-Albert para importar en gephi con las combinaciones de valores m=[3,4] y t=[500,1000,5000]\n'
    strHelp += '    netX    - Genera 10 redes de Barabasi-Albert con las combinaciones de valores m=[3,4] y t=[500,1000,5000] y devuelve las medias de los valores de las métricas'
    strHelp += ' \"densidad de las redes\" \"tamaño del hub más grande\" \"distancia media\" \"coeficiente de agrupamiento\"\n'
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


if default:
    helpgeneradorRedesBA()
else:
    mode = (sys.argv[1])
    if mode == 'gephi':
        crearRedBAGephi()

    elif mode == 'netX':
        crearRedBANetworkX()

    else:
        helpgeneradorRedesBA()
