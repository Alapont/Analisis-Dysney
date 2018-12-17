#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

moviesFolder = 'Scripts'
IntermediateFolder = 'IntermediateScripts'
treatedFolder = 'TreatedScripts'
movies = ['StarWarsEpisodeVIITheForceAwakens.txt']

frases = [re.compile(r'^[ ]{11}[\w\.\`\"\-\'\()]', re.IGNORECASE)]

comentarios = [re.compile(r'^[ ]{10}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE)]

numPag = [re.compile(r'\d+.', re.IGNORECASE)]

parentesis = re.compile(r'\([\w\d\s\.\,\-\'\"\/\:\;\?\!\#]*\)', re.IGNORECASE)

cabecera = [97]

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
                    if not (line.strip().startswith('[') == True and line.strip().endswith(']') == True):
                        if not (line.strip().startswith('(') == True and line.strip().endswith(')') == True):
                            if not (line.strip().startswith('{') == True and line.strip().endswith('}') == True):
                                if not(line.strip() == 'CONTINUED:'):
                                    # Encontramos indicaciones de escena
                                    if(comentarios[x].match(line) == None) & (numPag[x].match(line.strip()) == None) & (parentesis.match(line.strip()) == None):

                                        matchObj = frases[x].match(line)
                                        if matchObj:
                                            # Encontramos una linea y decidimos donde meterla
                                            tratado[indice-1] = tratado[indice-1] + \
                                                ' '+line.strip()
                                        else:
                                            # Encontramos una frase
                                            tratado.append(line.strip()+':')
                                            indice += 1
                                    else:
                                        if line.strip() =='LOR SAN TEKKA':
                                            # Encontramos un personaje que habla en off screen
                                            tratado.append(line.strip()+':')
                                            indice += 1

        # Guardamos los resultados en un fichero
        with open(os.path.join(os.path.join(os.getcwd(), IntermediateFolder), movies[x]), 'w') as writer:
            for y in range(indice):
                writer.write(tratado[y]+'\n')

        os.rename(os.path.join(os.path.join(os.getcwd(), moviesFolder), movies[x]),
                  os.path.join(os.path.join(os.getcwd(), treatedFolder), movies[x]))
