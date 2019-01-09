#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import requests
import time
import xml.etree.ElementTree as ET


def obtenerUsuario(user):

    response = requests.get(
        "https://www.boardgamegeek.com/xmlapi/collection/%(usr)s?rated=1" % {'usr': user})

    # Si recibimos una respuesta 202 tenemos que esperar a que la api genere
    # los datos del usuario pedido, tenemos que volver a realizar la petición
    # pasados X segundos
    while response.status_code == 202:
        time.sleep(5)
        response = requests.get(
            "https://www.boardgamegeek.com/xmlapi/collection/%(usr)s?rated=1" % {'usr': user})

    print(response)

    # xml = response.text.replace('\t', ' ')

    if response.status_code == 200:
        root = ET.fromstring(response.text)
        # Obtenemos los nombres y los ids de los juegos valorados
        for child in root:
            idJuego = child.attrib['objectid']

            # Si no está en la lista de juegos añadidos continuamos
            if nodos_Juegos.get(idJuego, -1) == -1:

                for datosJuego in child:

                    # Nombre
                    if datosJuego.tag == 'name':
                        nombreJuego = datosJuego.text

                    # Año publicación
                    if datosJuego.tag == 'yearpublished':
                        yearJuego = datosJuego.text

                    # Estadisticas
                    if datosJuego.tag == 'stats':
                        minplayers = -1
                        maxplayers = -1
                        minplaytime = -1
                        maxplaytime = -1
                        playingtime = -1
                        numowned = -1
                        age = -1

                        # Los juegos nos siempre tienen las mismas estdisticas
                        for atributo in datosJuego.attrib:
                            if atributo == 'minplayers':
                                minplayers = datosJuego.attrib['minplayers']
                            if atributo == 'maxplayers':
                                maxplayers = datosJuego.attrib['maxplayers']
                            if atributo == 'minplaytime':
                                minplaytime = datosJuego.attrib['minplaytime']
                            if atributo == 'maxplaytime':
                                maxplaytime = datosJuego.attrib['maxplaytime']
                            if atributo == 'playingtime':
                                playingtime = datosJuego.attrib['playingtime']
                            if atributo == 'numowned':
                                numowned = datosJuego.attrib['numowned']
                            if atributo == 'age':
                                age = datosJuego.attrib['age']

                        for estadisticas in datosJuego:
                            if estadisticas.tag == 'rating':
                                nota = estadisticas.attrib['value']
                                valores_Juegos[idJuego] = float(nota)

                nodos_Juegos[idJuego] = nombreJuego
                juego = []
                juego.append(idJuego)
                juego.append(nombreJuego)
                juego.append(yearJuego)
                juego.append(minplayers)
                juego.append(maxplayers)
                juego.append(minplaytime)
                juego.append(maxplaytime)
                juego.append(playingtime)
                juego.append(numowned)
                juego.append(age)
                datos_Juegos.append(juego)
    else:
        usersError.append(user)


def calcularAristas():
    while len(valores_Juegos)!=0:
        juego1, valor1=valores_Juegos.popitem()

        if valor1 >= valorParaArista:
            for juego2, valor2 in valores_Juegos.items():
                if valor2 >= valorParaArista:
                    if juego1 != juego2:
                        # Creamos el identificador de la arista
                        clave = ''
                        if(int(juego1) < int(juego2)):
                            clave = juego1+'-'+juego2
                        else:
                            clave = juego2+'-'+juego1

                        # Si la clave existe ya en el diccionario incrementamos el valor de la arista
                        # si no existe lo añadimos

                        valorClave = aristas_Juegos.get(clave, 0)
                        aristas_Juegos[clave] = valorClave + 1

usersError = []
nodos_Juegos = dict()
datos_Juegos = []
datos_Juegos.append(['Id', 'Name', 'Year', 'MinPlayers', 'MaxPlayers',
                     'MinPlayTime', 'MaxPlayTime', 'PlayingTime', 'NumOwned', 'Age'])
valores_Juegos = dict()
aristas_Juegos = dict()
valorParaArista = 7.0

# Aciones por cada usuario
obtenerUsuario('masu')
calcularAristas()
valores_Juegos.clear()

# Aciones por cada usuario
obtenerUsuario('Gellyvs')
calcularAristas()
valores_Juegos.clear()

# Aciones por cada usuario
obtenerUsuario('tnomad')
calcularAristas()
valores_Juegos.clear()

# Aciones por cada usuario
obtenerUsuario('Thamoo')
calcularAristas()
valores_Juegos.clear()

print('Fin')
