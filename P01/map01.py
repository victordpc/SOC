#!/usr/bin/python3

import os
import csv

USERSSPAIN="P01/material p1/twitter/Top100_spain_friendships_users.txt"
CSVUSERSSPAIN="P01/usuariosSpain.csv"
USERSUK= "P01/material p1/twitter/Top100_united_kingdom_friendships_users.txt"
CSVUSERSUK="P01/usuariosUK.csv"

USERS = ["P01/material p1/twitter/Top100_france_friendships_users.txt","P01/material p1/twitter/Top100_germany_friendships_users.txt", "P01/material p1/twitter/Top100_global_friendships_users.txt", "P01/material p1/twitter/Top100_italy_friendships_users.txt", "P01/material p1/twitter/Top100_united_kingdom_friendships_users.txt","P01/material p1/twitter/Top100_united_states_friendships_users.txt"]
CSVGLOBAL = "P01/usuariosGlobal.csv"
COUNTRIES = ["France", "Germany", "Global", "Italy", "UK", "US"]

CABECERA= "Id;Label;Country;Following;Followers;Tweets"

pais="Spain"
i=0
f=open(CSVUSERSSPAIN,"w")

f.write(CABECERA + "\n")

with open(USERSSPAIN, "r") as reader:
    for line in reader:
        partido = line.split(" ")
        resultado = str(i) + ";" + partido[0][0:len(partido[0])-1] + ";" + pais + ";" + partido[1] + ";" + partido[2] + ";" + partido[3]
        f.write(resultado + "\n")
        i += 1

f.close()
print("Ok CSV spain")

i=0
f=open(CSVUSERSUK,"w")

f.write(CABECERA + "\n")

with open(USERSUK, "r") as reader:
    for line in reader:
        partido = line.split(" ")
        resultado = str(i) + ";" + partido[0][0:len(partido[0])-1] + ";"  + partido[1] + ";" + partido[2] + ";" + partido[3] + ";" + partido[4]
        f.write(resultado + "\n")
        i += 1

f.close()
print("Ok CSV uk")


i=0
datos =dict()

for x in range(6):

    with open(USERS[x], "r") as reader:
        for line in reader:
            partido = line.split(" ")
            datos[partido[0][0:len(partido[0])-1]]=str(i) + ";" + partido[0][0:len(partido[0])-1] + ";" + partido[1] + ";" + partido[2] + ";" + partido[3] + ";" + partido[4]

            # resultado = str(i) + ";" + partido[0][0:len(partido[0])-1] + ";" + partido[1] + ";" + partido[2] + ";" + partido[3] + ";" + partido[4]
            # f.write(resultado + "\n")
            i += 1

    print("Ok read partial "+ COUNTRIES[x])

with open(USERSSPAIN, "r") as reader:
    for line in reader:
        partido = line.split(" ")
        datos[partido[0][0:len(partido[0])-1]]=str(i) + ";" + partido[0][0:len(partido[0])-1] + ";" + pais + ";" + partido[1] + ";" + partido[2] + ";" + partido[3]

        # resultado = str(i) + ";" + partido[0][0:len(partido[0])-1] + ";" + pais + ";" + partido[1] + ";" + partido[2] + ";" + partido[3]
        # f.write(resultado + "\n")
        i += 1

print("Ok read partial "+ pais)

f=open(CSVGLOBAL,"w")
f.write(CABECERA + "\n")

for dato in datos.values():
    f.write(dato + "\n")

f.close()

print("Ok write global")

print("Ok all")