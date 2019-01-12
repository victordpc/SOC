#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import networkx as nx

# Gestión de los ficheros que se usan


def configurarFicheros():
    result = True

    if not os.path.exists(os.path.join(os.getcwd(), carpetaFicheros)):
        result = False
    elif not os.path.exists(os.path.join(os.getcwd(), ficheroNodos)):
        result = False
    elif not os.path.exists(os.path.join(os.getcwd(), ficheroAristas)):
        result = False

    return result


def montarGrafo(grafo):

    # Para los calculos a realizar podemos generar
    # el grafo con la información de las aristas

    # Cargamos las aristas
    cargarAristas(grafo)


def cargarAristas(grafo):
    with open(ficheroAristas, 'r') as reader:
        # Leemos la cabecera
        reader.readline()

        for line in reader:
            arista = line.split(',')
            grafo.add_edge(int(arista[0].strip()),
                           int(arista[1].strip()), weight=float(arista[2].strip()))


def cargarJuegos():
    juegoId = dict()
    idJuego = dict()

    with open(ficheroNodos, 'r') as reader:
        # Leemos la cabecera
        reader.readline()

        for line in reader:
            juego = line.split(',')
            juegoId[juego[1].strip().upper()] = int(juego[0].strip())
            idJuego[int(juego[0].strip())] = juego[1].strip()

    return juegoId, idJuego


def recomendador(grafo, juegoId, idJuego, entrada):
    # Diccionario con los pesos de los juegos relacionados con la entrada
    salida = dict()
    resultado = []
    encontrados = []
    noEncontrados = []

    for juego in entrada:
        # Encontramos el juego pedido

        if juegoId.get(juego.upper(), -1) != -1:
            encontrados.append(juego)
            id = juegoId[juego.upper()]
            # Consultamos para cada juego sus vecinos
            consultarVecinosJuego(grafo, id, salida)
        else:
            noEncontrados.append(juego)

    # Eliminamos de la lista las posibles ocurrencias de los juegos de entrada
    for juego in encontrados:
        salida.pop(juego, 0)

    if len(salida) > 0:
        # Ordenamos los resultados
        # Obtenemos los X juegos con mayor valoración
        salidaOrdenada = sorted(salida.keys(), key=lambda x: salida[x])

        i = 0
        while i < respuestas:
            elegido = salidaOrdenada.pop()
            resultado.append(idJuego[elegido])
            i += 1

    return resultado, encontrados, noEncontrados


def consultarVecinosJuego(grafo, idJuego, salida):
    vecinos = grafo.neighbors(idJuego)

    # Devolvemos sus vecinos
    for vecino in vecinos:
        peso = (grafo.get_edge_data(idJuego, vecino))['weight']
        valor = salida.get(vecino, 0)
        salida[vecino] = peso + valor


def mensajeSalida(resultado, encontrados, noEncontrados):
    msg = ''

    if len(encontrados) > 0:
        msg = 'Las recomendaciones para '

        if len(encontrados) == 1:
            msg += 'el juego: '
        else:
            msg += 'los juegos: '

        for juego in encontrados:
            msg += juego+', '
        msg = msg[:-2]

        if len(resultado) == 1:
            msg += ' es'
        else:
            msg += ' son: '

        for juego in resultado:
            msg += juego+', '
        msg = msg[:-2]

        if len(noEncontrados) > 0:
            msg += '\n\nNo se ha encontrado información para '

            if len(noEncontrados) == 1:
                msg += 'el juego: '
            else:
                msg += 'los juegos: '

            for juego in noEncontrados:
                msg += juego+', '
            msg = msg[:-2]

    else:
        msg = 'No se ha encontrado información para ninguno de los juegos introducidos'

    return msg


def mensajeAyuda():
    msg = 'Recomendador juegotea, un recomendador basado en grafos\n\n'
    msg += 'Usage:  recomendador [arg ...]|[-h]\n'
    msg += '\n'
    msg += '    Introducir los nombres de los juegos separados por un único'
    msg += ' caracter de espacio, en caso de querer introducir un nombre'
    msg += ' compuesto por varias palabras introducirlo entre comillas\n'
    msg += '\n'
    msg += '    Commands:\n'
    msg += '      -h    - Muestra la ayuda\n'


def main():
    entrada = []
    error = False
    continuar = True
    msg = ''

    # Obtenemos los parámetros de entrada
    if len(sys.argv) > 1:
        for argumento in sys.argv:
            entrada.append(argumento)
        entrada.remove(entrada[0])

        # Controlamos si quieren mostrar la ayuda
        if entrada[0] == '-h':
            continuar = False
            mensajeAyuda()

    else:
        error = True
        msg = 'No se proporcionan argumentos de entrada'

    if (not error) & continuar:
        # Creamos el grafo
        G = nx.Graph()

        # Montamos el grafo
        montarGrafo(G)

        # Cargamos los juegos
        juegoId = dict()
        idJuego = dict()
        juegoId, idJuego = cargarJuegos()

        # Ejecutamos el algoritmo de recomendación
        resultado, encontrados, noEncontrados = recomendador(
            G, juegoId, idJuego, entrada)

        # Montamos el mensaje de salida
        msg = mensajeSalida(resultado, encontrados, noEncontrados)

    # Si se ha producido un error lo mostramos por pantalla
    if error:
        if len(msg) > 0:
            print(msg)
        print('Para consultar la ayuda ejecute con la opción -h')
    else:
        print(msg)


if __name__ == '__main__':
    msg = ''
    respuestas = 5
    # Configuración
    carpetaFicheros = 'Files'
    ficheroNodos = os.path.join(
        os.getcwd(), carpetaFicheros, 'NodosJuegos.csv')
    ficheroAristas = os.path.join(
        os.getcwd(), carpetaFicheros, 'AristasJuegos.csv')

    correcto = configurarFicheros()
    # Configuración

    if correcto:
        main()
    else:
        print('Error: No existen ficheros con datos de entrada')
