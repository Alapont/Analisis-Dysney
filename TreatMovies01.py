#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

charPattern = r'[\w]{1}[\w \']+:'

moviesFolder = 'Scripts'
treatedFolder = 'TreatedScripts'
movies = ['BeautyAndTheBeast.txt', 'Aladdin.txt', 'HunchbackOfNotreDame.txt', 'LittleMermaid.txt',
          'MaryPoppins.txt', 'AGoofyMovie.txt', 'TheLionKing.txt', 'TheRescuersDownUnder.txt', 'TheSleepingBeauty.txt']
cabecera = [6, 64, 26, 3, 1, 10, 21, 34, 0]

for x in range(len(movies)):
    indice = 0
    tratado = []
    ignorar = False
    with open(os.path.join(os.path.join(os.getcwd(), moviesFolder), movies[x]), 'r') as reader:
        # Eliminamos las lineas introductorias
        for z in range(cabecera[x]):
            reader.readline()

        # Tratamos el fichero
        for line in reader:

            if line.strip() != '':
                # Encontramos un inicio de dialogo
                matchObj = re.match(charPattern, line)
                if matchObj:
                    tratado.append(line.strip())
                    indice += 1
                else:
                    # Encontramos una linea y decidimos donde meterla
                    if(ignorar == False):
                        tratado[indice-1] = tratado[indice-1]+' '+line.strip()

    # Guardamos los resultados en un fichero
    with open(os.path.join(os.path.join(os.getcwd(), treatedFolder), movies[x]), 'w') as writer:
        for y in range(indice):
            writer.write(tratado[y]+'\n')
