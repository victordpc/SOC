#!/usr/bin/python3

import os
import csv

USERS = ["P01/material p1/twitter/Top100_spain_friendships.txt", "P01/material p1/twitter/Top100_united_kingdom_friendships.txt"]
CSVUSERS = ["P01/usuariosSpain.csv", "P01/usuariosUK.csv"]
CSVFRIENDS = ["P01/seguidoresSpain.csv", "P01/seguidoresUK.csv"]



CABECERA= "Source;Target;Type;Id;Label;Weight"
TYPE="Directed"
LABEL=""
WEIGHT="1.0"

localDirectory=os.path.dirname(os.path.realpath(__file__))

for x in range(2):
    datos =dict()
    with open(CSVUSERS[x], "r") as reader:
        for line in reader:
            partido = line.split(";")
            datos[partido[1]] = partido[0]

    i=0
    f=open(CSVFRIENDS[x],"w")
    f.write(CABECERA + "\n")

    with open(USERS[x], "r") as reader:
        for line in reader:
            partido = line.split(":")
            idDestino = datos[partido[0]]
            
            for x in partido[1].strip().split(" "): 
                if x != "":
                    idOrigen= datos[x]
                    i += 1
                    f.write(str(idOrigen) + ";" + str(idDestino) + ";" + TYPE + ";" + str(i) + ";" + LABEL + ";" + WEIGHT + "\n")

    f.close()
    print("Ok " + CSVFRIENDS[x])

USERS = ["P01/material p1/twitter/Top100_spain_friendships.txt", "P01/material p1/twitter/Top100_united_kingdom_friendships.txt"]
CSVUSERS = ["P01/usuariosSpain.csv", "P01/usuariosUK.csv"]
CSVFRIENDS = ["P01/seguidoresSpain.csv", "P01/seguidoresUK.csv"]

USERSGLOBAL = ["P01/material p1/twitter/Top100_france_friendships.txt","P01/material p1/twitter/Top100_germany_friendships.txt"
, "P01/material p1/twitter/Top100_global_friendships.txt", "P01/material p1/twitter/Top100_italy_friendships.txt"
, "P01/material p1/twitter/Top100_united_states_friendships.txt"]
CSVGLOBAL = "P01/usuariosGlobal.csv"
COUNTRIES = ["France", "Germany", "Global", "Italy", "US"]
CSVFRIENDSGLOBAL = "P01/seguidoresSpain.csv"




print("Ok All")