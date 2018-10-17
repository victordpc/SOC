#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv

USERS = [
    'twitter/Top100_spain_friendships.txt',
    'twitter/Top100_united_kingdom_friendships.txt'
]
CSVUSERS = ['usuariosSpain.csv', 'usuariosUK.csv']
CSVFRIENDS = ['seguidoresSpain.csv', 'seguidoresUK.csv']

SEPARATOR = ','

CABECERA = 'Source' + SEPARATOR + 'Target' + SEPARATOR + 'Type' \
    + SEPARATOR + 'Id' + SEPARATOR + 'Label' + SEPARATOR + 'Weight'
TYPE = 'Directed'
LABEL = ''
WEIGHT = '1.0'

localDirectory = os.path.dirname(os.path.realpath(__file__))

for x in range(2):
    datos = dict()
    with open(CSVUSERS[x], 'r') as reader:
        for line in reader:
            partido = line.split(SEPARATOR)
            datos[partido[1]] = partido[0]

    i = 0
    f = open(CSVFRIENDS[x], 'w')
    f.write(CABECERA + '\n')

    with open(USERS[x], 'r') as reader:
        for line in reader:
            partido = line.split(':')
            idDestino = datos[partido[0]]

            for dato in partido[1].strip().split(' '):
                if dato != '':
                    idOrigen = datos[dato]
                    i += 1
                    f.write(
                        str(idOrigen) + SEPARATOR + str(idDestino) +
                        SEPARATOR + TYPE + SEPARATOR + str(i) + SEPARATOR +
                        LABEL + SEPARATOR + WEIGHT + '\n')

    f.close()
    print 'Ok ' + CSVFRIENDS[x]

USERSGLOBAL = [
    'twitter/Top100_france_friendships.txt',
    'twitter/Top100_germany_friendships.txt',
    'twitter/Top100_global_friendships.txt',
    'twitter/Top100_italy_friendships.txt',
    'twitter/Top100_united_states_friendships.txt',
    'twitter/Top100_spain_friendships.txt',
    'twitter/Top100_united_kingdom_friendships.txt'
]
CSVGLOBAL = 'usuariosGlobal.csv'
COUNTRIES = [
    'France', 'Germany', 'Global', 'Italy', 'United_states', 'Spain',
    'United_kingdom'
]
CSVFRIENDSGLOBAL = 'seguidoresGlobal.csv'
CSVFRIENDSINTERNACIONAL = 'seguidoresGlobalInternacionales.csv'

CABECERAPAISES = 'Id' + SEPARATOR + 'Label'
CSVCOUNTRIES = 'usuariosPaises.csv'
CSVCOUNTRIESGLOBAL = 'seguidoresPaises.csv'

resultado = dict()
datos = dict()
datosUsuariosPaises = dict()
paises = dict()
datosAristasPaises = dict()

with open(CSVGLOBAL, 'r') as reader:
    for line in reader:
        partido = line.split(SEPARATOR)
        datos[partido[1]] = partido[0]
        datosUsuariosPaises[partido[1]] = partido[2]

f = open(CSVCOUNTRIES, 'w')
f.write(CABECERAPAISES + '\n')

for z in range(7):
    paises[COUNTRIES[z].capitalize()] = z
    f.write(str(z) + SEPARATOR + COUNTRIES[z].capitalize() + '\n')

f.close()

f = open(CSVFRIENDSGLOBAL, 'w')
f.write(CABECERA + '\n')

h = open(CSVFRIENDSINTERNACIONAL, 'w')
h.write(CABECERA + '\n')

i = 0
for y in range(7):
    with open(USERSGLOBAL[y], 'r') as reader:
        for line in reader:
            partido = line.split(':')
            idDestino = datos[partido[0]]

            idPaisDestino = paises[datosUsuariosPaises[partido[0]].
                                   capitalize()]

            for dato in partido[1].strip().split(' '):
                if dato != '':
                    idOrigen = datos[dato]

                    idPaisOrigen = paises[datosUsuariosPaises[dato].
                                          capitalize()]
                    i += 1
                    f.write(
                        str(idOrigen) + SEPARATOR + str(idDestino) +
                        SEPARATOR + TYPE + SEPARATOR + str(i) + SEPARATOR +
                        LABEL + SEPARATOR + WEIGHT + '\n')

                    if idPaisOrigen != idPaisDestino:
                        h.write(
                            str(idOrigen) + SEPARATOR + str(idDestino) +
                            SEPARATOR + TYPE + SEPARATOR + str(i) + SEPARATOR +
                            LABEL + SEPARATOR + WEIGHT + '\n')

                    clave = str(idPaisOrigen) + '-' + str(idPaisDestino)
                    if datosAristasPaises.has_key(clave):
                        datosAristasPaises[
                            clave] = datosAristasPaises[clave] + 1
                    else:
                        datosAristasPaises[clave] = 1

    print 'Ok ' + COUNTRIES[y]

f.close()

g = open(CSVCOUNTRIESGLOBAL, 'w')
g.write(CABECERA + '\n')
i = 0

for arista, valor in datosAristasPaises.items():
    for nodo in arista.split('-'):
        g.write(str(nodo) + SEPARATOR)
    g.write(TYPE + SEPARATOR + str(i) + SEPARATOR + LABEL + SEPARATOR +
            str(valor) + '\n')
    i += 1

g.close()

print 'Ok All'
