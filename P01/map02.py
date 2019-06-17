#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv


def main():
    cargaDatos()

    datosUsuarios = dict()
    datosUsuariosPaises = dict()
    paises = dict()
    datosAristasPaises = dict()

    # Lee los datos de los usuarios globales previamente procesados
    cargaDatos2(datosUsuarios, datosUsuariosPaises)

    # Carga un diccionario con los paises que vamos a tratar y genera el csv para los
    # nodos de los paises
    cargaPaises(paises)

    # Procesamos los datos para escribir los Csv de las aristas de los usuarios globales,
    # los usuarios globales internacionales y procesar las relaciones entre los paises en conjunto
    procesadoGlobal(datosUsuarios, paises, datosUsuariosPaises,
                    datosAristasPaises)

    # Guardamos la información de los enlaces entre los paises
    guardardatos(datosAristasPaises)


def cargaDatos():
    for x in range(2):
        datos = dict()

        # Lee los datos de los usuarios desde csv previamente procesados
        with open(CSVUSERS[x], 'r') as reader:
            for line in reader:
                partido = line.split(SEPARATOR)
                datos[partido[1]] = partido[0]

        # Escribe los datos de los usuarios en los ficheros indicados
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

        print('Ok ' + CSVFRIENDS[x])


def cargaDatos2(datosUsuarios, datosUsuariosPaises):
    with open(CSVGLOBAL, 'r') as reader:
        for line in reader:
            partido = line.split(SEPARATOR)
            datosUsuarios[partido[1]] = partido[0]
            datosUsuariosPaises[partido[1]] = partido[2]


def cargaPaises(paises):
    f = open(CSVCOUNTRIES, 'w')
    f.write(CABECERAPAISES + '\n')
    for z in range(7):
        paises[COUNTRIES[z].capitalize()] = z
        f.write(str(z) + SEPARATOR + COUNTRIES[z].capitalize() + '\n')
    f.close()


def procesadoGlobal(datosUsuarios, paises, datosUsuariosPaises,
                    datosAristasPaises):
    f = open(CSVFRIENDSGLOBAL, 'w')
    f.write(CABECERA + '\n')
    h = open(CSVFRIENDSINTERNACIONAL, 'w')
    h.write(CABECERA + '\n')

    i = 0

    # Procesamos los siete origenes de datos disponibles
    for y in range(7):
        with open(USERSGLOBAL[y], 'r') as reader:
            for line in reader:

                # Obtenemos los identificadores del usuario y del pais
                # al que pertenece el destino de la arista
                partido = line.split(':')
                idDestino = datosUsuarios[partido[0]]
                idPaisDestino = paises[datosUsuariosPaises[
                    partido[0]].capitalize()]

                # Recorremos el resto de usuarios relacionados con el de destino
                for dato in partido[1].strip().split(' '):
                    if dato != '':
                        # Obtenemos los identificadores del usuario y del pais
                        # que marcan el origen de la arista
                        idOrigen = datosUsuarios[dato]
                        idPaisOrigen = paises[
                            datosUsuariosPaises[dato].capitalize()]
                        i += 1

                        # Escribimos en el fichero los datos de la arista del usuario
                        f.write(
                            str(idOrigen) + SEPARATOR + str(idDestino) +
                            SEPARATOR + TYPE + SEPARATOR + str(i) + SEPARATOR +
                            LABEL + SEPARATOR + WEIGHT + '\n')

                        # Si los paises del origen y destino de la arista no coinciden
                        # lo consideramos como un enlace internacional y nos gardamos los usuarios
                        if idPaisOrigen != idPaisDestino:
                            h.write(
                                str(idOrigen) + SEPARATOR + str(idDestino) +
                                SEPARATOR + TYPE + SEPARATOR + str(i) +
                                SEPARATOR + LABEL + SEPARATOR + WEIGHT + '\n')

                        # Guardamos la información de la arista a nivel de paises
                        clave = str(idPaisOrigen) + '-' + str(idPaisDestino)
                        if datosAristasPaises.get(clave, None) != None:
                            datosAristasPaises[
                                clave] = datosAristasPaises[clave] + 1
                        else:
                            datosAristasPaises[clave] = 1

        print('Ok ' + COUNTRIES[y])

    f.close()
    h.close()


def guardardatos(datosAristasPaises):
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
    print('Ok write global countries')


if __name__ == '__main__':
    USERS = [
        os.path.join(os.getcwd(), 'twitter', 'Top100_spain_friendships.txt'),
        os.path.join(os.getcwd(), 'twitter',
                     'Top100_united_kingdom_friendships.txt')
    ]
    CSVUSERS = ['usuariosSpain.csv', 'usuariosUK.csv']
    CSVFRIENDS = ['seguidoresSpain.csv', 'seguidoresUK.csv']

    SEPARATOR = ','

    CABECERA = 'Source' + SEPARATOR + 'Target' + SEPARATOR + 'Type' \
        + SEPARATOR + 'Id' + SEPARATOR + 'Label' + SEPARATOR + 'Weight'
    TYPE = 'Directed'
    LABEL = ''
    WEIGHT = '1.0'

    USERSGLOBAL = [
        os.path.join(os.getcwd(), 'twitter', 'Top100_france_friendships.txt'),
        os.path.join(os.getcwd(), 'twitter', 'Top100_germany_friendships.txt'),
        os.path.join(os.getcwd(), 'twitter', 'Top100_global_friendships.txt'),
        os.path.join(os.getcwd(), 'twitter', 'Top100_italy_friendships.txt'),
        os.path.join(os.getcwd(), 'twitter', 'Top100_united_states_friendships.txt'),
        os.path.join(os.getcwd(), 'twitter', 'Top100_spain_friendships.txt'),
        os.path.join(os.getcwd(), 'twitter', 'Top100_united_kingdom_friendships.txt')
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

    main()

    print('Ok All')
