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
                    writer.write(str(clave) + ';' + str(data[clave]) + '\n')

        del data


# for x in range(3):
#     with open(os.path.join(os.path.join(os.getcwd(), moviesFolder), pelis[x]), 'r') as reader:
#         for line in reader:
#             # if line == blankLine:
#             #     newLine = True

#             # newScene = re.match(scenePattern, line)
#             # if newLine && newScene:

#             matchObj = re.match(charPattern, line)
#             if matchObj:
#                 character = matchObj.group()[:-1]
#                 if data.has_key(character):
#                     data[character] = data[character]+1
#                 else:
#                     data[character] = 1

#                 if womens.count(character.upper()) > 0:
#                     genders["woman"] = genders["woman"]+1
#                 else:
#                     genders["men"] = genders["men"]+1

#     for key, value in sorted(data.items(), key=itemgetter(1), reverse=True):
#         print(key + " - " + str(value))

#     for key, value in genders.items():
#         print(key + " - " + str(value))
