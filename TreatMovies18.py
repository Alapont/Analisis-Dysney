#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

moviesFolder = 'Scripts'
IntermediateFolder = 'IntermediateScripts'
treatedFolder = 'TreatedScripts'
movies = ['TheAvengersInfinityWar.txt']

cabecera = [0]

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

                if line.strip() != '':
                    if (line.find(':') != -1) or (not (line.strip().startswith('[') == True and line.strip().endswith(']') == True)):
                        tratado.append(line.strip())
                        indice += 1

        # Guardamos los resultados en un fichero
        with open(os.path.join(os.path.join(os.getcwd(), IntermediateFolder), movies[x]), 'w') as writer:
            for y in range(indice):
                writer.write(tratado[y]+'\n')

        os.rename(os.path.join(os.path.join(os.getcwd(), moviesFolder), movies[x]),
                  os.path.join(os.path.join(os.getcwd(), treatedFolder), movies[x]))
