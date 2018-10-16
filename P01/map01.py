#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv

USERSSPAIN = \
    'twitter/Top100_spain_friendships_users.txt'
CSVUSERSSPAIN = 'usuariosSpain.csv'
USERSUK = 'twitter/Top100_united_kingdom_friendships_users.txt'
CSVUSERSUK = 'usuariosUK.csv'

USERS = [
    'twitter/Top100_france_friendships_users.txt',
    'twitter/Top100_germany_friendships_users.txt',
    'twitter/Top100_global_friendships_users.txt',
    'twitter/Top100_italy_friendships_users.txt',
    'twitter/Top100_united_kingdom_friendships_users.txt',
    'twitter/Top100_united_states_friendships_users.txt',
    ]
CSVGLOBAL = 'usuariosGlobal.csv'
COUNTRIES = [
    'France',
    'Germany',
    'Global',
    'Italy',
    'UK',
    'US',
    ]

SEPARATOR = ','

CABECERA = 'Id' + SEPARATOR + 'Label' + SEPARATOR + 'Country' \
    + SEPARATOR + 'Following' + SEPARATOR + 'Followers' + SEPARATOR \
    + 'Tweets'

pais = 'Spain'
i = 0
f = open(CSVUSERSSPAIN, 'w')

f.write(CABECERA + '\n')

with open(USERSSPAIN, 'r') as reader:
    for line in reader:
        partido = line.split(' ')
        resultado = str(i) + SEPARATOR + (partido[0])[0:len(partido[0])
            - 1] + SEPARATOR + pais + SEPARATOR + partido[1] \
            + SEPARATOR + partido[2] + SEPARATOR + partido[3]
        f.write(resultado + '\n')
        i += 1

f.close()
print 'Ok CSV spain'

i = 0
f = open(CSVUSERSUK, 'w')

f.write(CABECERA + '\n')

with open(USERSUK, 'r') as reader:
    for line in reader:
        partido = line.split(' ')
        resultado = str(i) + SEPARATOR + (partido[0])[0:len(partido[0])
            - 1] + SEPARATOR + partido[1] + SEPARATOR + partido[2] \
            + SEPARATOR + partido[3] + SEPARATOR + partido[4]
        f.write(resultado + '\n')
        i += 1

f.close()
print 'Ok CSV uk'

i = 0
datos = dict()

for x in range(6):

    with open(USERS[x], 'r') as reader:
        for line in reader:
            partido = line.split(' ')
            datos[(partido[0])[0:len(partido[0]) - 1]] = str(i) \
                + SEPARATOR + (partido[0])[0:len(partido[0]) - 1] \
                + SEPARATOR + partido[1] + SEPARATOR + partido[2] \
                + SEPARATOR + partido[3] + SEPARATOR + partido[4]

            i += 1

    print 'Ok read partial ' + COUNTRIES[x]

with open(USERSSPAIN, 'r') as reader:
    for line in reader:
        partido = line.split(' ')
        datos[(partido[0])[0:len(partido[0]) - 1]] = str(i) + SEPARATOR \
            + (partido[0])[0:len(partido[0]) - 1] + SEPARATOR + pais \
            + SEPARATOR + partido[1] + SEPARATOR + partido[2] \
            + SEPARATOR + partido[3]

        i += 1

print 'Ok read partial ' + pais

f = open(CSVGLOBAL, 'w')
f.write(CABECERA + '\n')

for dato in datos.values():
    f.write(dato + '\n')

f.close()

print 'Ok write global'

print 'Ok all'
