#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

moviesFolder = 'Scripts'
treatedFolder = 'TreatedScripts'
IntermediateFolder = 'IntermediateScripts'
movies = ['TheIncredibles.txt']

personaje = re.compile(r'[A-Z.]{3,}')

cabecera = 29
for x in range(len(movies)):
    indice = 0
    tratado = []

    with open(os.path.join(os.path.join(os.getcwd(), moviesFolder), movies[x]), 'r') as reader:
        # Eliminamos las lineas introductorias
        for z in range(cabecera):
            reader.readline()

        # Tratamos el fichero
        for line in reader:
            # Ignoramos las lineas en blanco y los saltos de escena
            if line.strip() != '' and line.strip().startswith('______') == False and line.strip().endswith('______') == False:

                if personaje.match(line.strip()):
                    tratado.append(line.strip()+': ')
                    indice += 1
                else:
                    tratado[indice-1] = tratado[indice-1] + ' ' + line.strip()


    # Guardamos los resultados en un fichero
    with open(os.path.join(os.path.join(os.getcwd(), treatedFolder), movies[x]), 'w') as writer:
        for y in range(indice):
            writer.write(tratado[y]+'\n')

    # Movemos el fichero tratado
    os.rename(os.path.join(os.path.join(os.getcwd(), moviesFolder), movies[x]), 
        os.path.join(os.path.join(os.getcwd(), treatedFolder), movies[x]))
