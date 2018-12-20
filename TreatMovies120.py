#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv
import re
from operator import itemgetter, attrgetter, methodcaller

charPattern = r'[\w]{1}[\w ]+:'
scenePattern = r'[(]{1}:'
blankLine = '\n'


moviesFolder = 'GendersCount'
resultFolder = 'Result'
destino='Resultados.txt'

data = []
if os.path.exists(os.path.join(os.getcwd(), resultFolder)) == False:
    os.mkdir(os.path.join(os.getcwd(), resultFolder))

for filename in os.listdir(os.path.join(os.getcwd(), moviesFolder)):
    with open(os.path.join(os.path.join(os.getcwd(), moviesFolder), filename), 'r') as reader:
        titulo = (reader.readline()).strip()
        mujeres = (reader.readline()).strip()
        hombres = (reader.readline()).strip()

        datosMujeres = int((mujeres.split(';'))[1])
        datosHombres = int((hombres.split(';'))[1])

        total = datosHombres + datosMujeres

        porcentaje = float((float(datosMujeres) * 100)/float(total))
        porcentaje = float(str(porcentaje)[:-(8-len(str(porcentaje)))])

        data.append(titulo+':' + str(porcentaje))

with open(os.path.join(os.path.join(os.getcwd(), resultFolder), destino),'w') as writer:
    writer.write('Resultados en porcentaje de dialogo de mujeres'+'\n')

    for linea in data:
        writer.write(linea+'\n')

del data
