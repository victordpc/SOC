#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv

USERS = ['twitter/Top100_spain_friendships.txt',
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
                    f.write(str(idOrigen) + SEPARATOR + str(idDestino)
                            + SEPARATOR + TYPE + SEPARATOR + str(i)
                            + SEPARATOR + LABEL + SEPARATOR + WEIGHT
                            + '\n')

    f.close()
    print 'Ok ' + CSVFRIENDS[x]

USERSGLOBAL = ['twitter/Top100_france_friendships.txt',
               'twitter/Top100_germany_friendships.txt',
               'twitter/Top100_global_friendships.txt', 
               'twitter/Top100_italy_friendships.txt',
               'twitter/Top100_united_states_friendships.txt',
               'twitter/Top100_spain_friendships.txt',
               'twitter/Top100_united_kingdom_friendships.txt'
               ]
CSVGLOBAL = 'usuariosGlobal.csv'
COUNTRIES = ['France', 'Germany', 'Global', 'Italy', 'US','Spain','UK']
CSVFRIENDSGLOBAL = 'seguidoresGlobal.csv'



print 'Ok All'

			