#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

moviesFolder = 'Scripts'
treatedFolder = 'TreatedScripts'
IntermediateFolder = 'IntermediateScripts'
movies = ['TheLionKingIISimbasPride.txt', 'TheLionKingIIIHakunaMatata.txt',
          'TheJungleBook.txt', 'AliceInWonderland.txt']

cabecera = [8, 4, 10, 2]
for x in range(len(movies)):
    indice = 0
    tratado = []

    if os.path.exists(os.path.join(os.path.join(os.getcwd(), moviesFolder), movies[x])):
        with open(os.path.join(os.path.join(os.getcwd(), moviesFolder), movies[x]), 'r') as reader:
            # Eliminamos las lineas introductorias
            for z in range(cabecera[x]):
                reader.readline()

            # Tratamos el fichero
            for line in reader:
                # Ignoramos las lineas en blanco y los saltos de escena
                if line.strip() != '':
                    if line.startswith('{') == False and line.endswith('}') == False:
                        if line.startswith('[') == False and line.endswith(']') == False:

                            if line.find(':') != -1:
                                tratado.append(line.strip())
                                indice += 1
                            else:
                                tratado[indice-1] = tratado[indice-1] + \
                                    ' ' + line.strip()

        # Guardamos los resultados en un fichero
        with open(os.path.join(os.path.join(os.getcwd(), IntermediateFolder), movies[x]), 'w') as writer:
            for y in range(indice):
                writer.write(tratado[y]+'\n')

        # Movemos el fichero tratado
        os.rename(os.path.join(os.path.join(os.getcwd(), moviesFolder), movies[x]),
                  os.path.join(os.path.join(os.getcwd(), treatedFolder), movies[x]))
