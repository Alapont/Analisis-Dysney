#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv
import re
from operator import itemgetter, attrgetter, methodcaller

charPattern = r'[\w]{1}[\w ]+:'
scenePattern = r'[(]{1}:'
blankLine = '\n'


moviesFolder = 'IntermediateScripts2'
resultFolder = 'CountWords'

for filename in os.listdir(os.path.join(os.getcwd(), moviesFolder)):
    with open(os.path.join(os.path.join(os.getcwd(), moviesFolder), filename), 'r') as reader:
        data = dict()
        for line in reader:
            indice = line.find(':')

            if (indice != -1):
                partida = line.split(':')

                if len(partida) == 2:
                    nombre = partida[0].strip()
                    frase = partida[1].strip()

                    if data.has_key(nombre):
                        data[nombre] += len(frase.split())
                    else:
                        data[nombre] = len(frase.split())

        # Guardamos el resultado en un CSV

        if not os.path.exists(os.path.join(os.getcwd(), resultFolder)):
            os.makedirs(os.path.join(os.getcwd(), resultFolder))

        destino = filename[:-(len(filename)-filename.find('.'))]+'.csv'
        with open(os.path.join(os.path.join(os.getcwd(), resultFolder), destino), 'w') as writer:
            writer.write(filename+'\n')
            writer.write('Nombre; Palabras' + '\n')

            for clave in data.keys():
                if data[clave] > 0:
                    writer.write(str(clave).upper() + ';' + str(data[clave]) + ';\n')

        del data


