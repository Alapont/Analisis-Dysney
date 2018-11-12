#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

moviesFolder = 'Scripts'
treatedFolder = 'TreatedScripts'
movies = ['17Again.txt', 'Coco.txt', 'Frankenweenie.txt', 'Frozen.txt', 'GuardiansOfTheGalaxyVol2.txt',
          'PiratesOfTheCaribbean.txt', 'PiratesOfTheCaribbeanDeadMan\'sChest.txt', 'TheAvengers.txt',
          'TheChroniclesOfNarniaTheLionTheWitchAndTheWardrobe.txt', 'Thor.txt', 'ThorRagnarock.txt',
          'ToyStory.txt', 'Tron.txt', 'TronLegacy.txt', 'Up.txt', 'Wall-E.txt', 'Zootropia.txt',
          'StarWarsEpisodeIIAttackOfTheClones.txt', 'StarWarsEpisodeIVANewHope.txt', 'StarWarsEpisodeVTheEmpireStrikesBack.txt']

frases = [re.compile(r'^[ ]{20,25}[\w\.\`\"\-\'\()]', re.IGNORECASE),
          re.compile(r'^[ ]{18}[\w\.\`\"\-\']', re.IGNORECASE),
          re.compile(r'^[ ]{2,3}[\w\.\`\"\-\'\ ]|^[\t]{1,3}[\w\.\`\"\-\'\(\ ]', re.IGNORECASE),
          re.compile(r'^[ ]{18,23}[\w\.\`\"\-\'\(]', re.IGNORECASE),
          re.compile(r'^[ ]{16,35}[\w\.\`\"\-\']', re.IGNORECASE),
          re.compile(r'^[ ]{10,18}[\w\.\`\"\-\'\(]', re.IGNORECASE),
          re.compile(r'^[ ]{20,26}[\w\.\`\"\-\'\(\*\?\#]', re.IGNORECASE),
          re.compile(r'^[ ]{11}[\w\.\`\"\-\'\(\*\?]', re.IGNORECASE),
          re.compile(r'^[ ]{20,26}[\w\.\`\"\-\'\(\*\?]', re.IGNORECASE),
          re.compile(r'^[ ]{10,11}[\w\.\`\"\-\'\(\*\?]', re.IGNORECASE),
          re.compile(r'^[ ]{10,18}[\w\.\`\"\-\'\(\*\?]', re.IGNORECASE),
          re.compile(r'^[ ]{12,20}[\w\.\`\"\-\'\(\*\?]', re.IGNORECASE),
          re.compile(r'^[ ]{20,30}[\w\.\`\"\-\'\(\*\?]', re.IGNORECASE),
          re.compile(r'^[ ]{15,20}[\w\.\`\"\-\'\(\*\?]', re.IGNORECASE),
          re.compile(r'^[ ]{20,25}[\w\.\`\"\-\'\(\*\?]', re.IGNORECASE),
          re.compile(r'^[ ]{20,35}[\w\.\`\"\-\'\(\*\?\[]', re.IGNORECASE),
          re.compile(r'^[ ]{8,12}[\w\.\`\"\-\'\(\*\?\[]', re.IGNORECASE),
          re.compile(r'^[\t]{3}[\w\.\`\"\-\'\(\*\?\[]', re.IGNORECASE),
          re.compile(r'^[ ]{20,26}[\w\.\`\"\-\'\(\*\?\[]', re.IGNORECASE),
          re.compile(r'^[\t]{2,3}[\w\.\`\"\-\'\(\*\?\[\ ]', re.IGNORECASE)]

comentarios = [re.compile(r'^[ ]{10}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{6}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{0}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{3}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{10}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{0}[\w\.\`\"\-\,\[\?\#\{]', re.IGNORECASE),
               re.compile(r'^[ ]{14,15}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{10}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{14,15}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{0}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{0,8}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{0}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{0,9}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{0,6}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{0,10}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{0,12}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{0,4}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{0,4}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{10,16}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE),
               re.compile(r'^[ ]{0}[\w\.\`\"\-\,\[\?\#]', re.IGNORECASE)]

numPag = [re.compile(r'\d+.', re.IGNORECASE),
          re.compile(r'\d+.', re.IGNORECASE),
          re.compile(r'\d+.', re.IGNORECASE),
          re.compile(r'\d+.', re.IGNORECASE),
          re.compile(r'\d+', re.IGNORECASE),
          re.compile(r'\d+', re.IGNORECASE),
          re.compile(r'\d+', re.IGNORECASE),
          re.compile(r'\d+', re.IGNORECASE),
          re.compile(r'\d+', re.IGNORECASE),
          re.compile(r'\d+', re.IGNORECASE),
          re.compile(r'\d+', re.IGNORECASE),
          re.compile(r'\d+', re.IGNORECASE),
          re.compile(r'\d+', re.IGNORECASE),
          re.compile(r'\d+', re.IGNORECASE),
          re.compile(r'\d+.', re.IGNORECASE),
          re.compile(r'\d+.', re.IGNORECASE),
          re.compile(r'\d+.', re.IGNORECASE),
          re.compile(r'\d+.', re.IGNORECASE),
          re.compile(r'\d+.', re.IGNORECASE),
          re.compile(r'\d+.', re.IGNORECASE)]

parentesis = re.compile(r'\([\w\d\s\.\,\-\'\"\/\:\;\?\!\#]*\)', re.IGNORECASE)

cabecera = [33, 31, 25, 13, 34, 8, 20, 80, 26,
            36, 34, 55, 16, 80, 17, 128, 32, 42, 60, 14]

for x in range(len(movies)):
    indice = 0
    tratado = []

    with open(os.path.join(os.path.join(os.getcwd(), moviesFolder), movies[x]), 'r') as reader:
        # Eliminamos las lineas introductorias
        for z in range(cabecera[x]):
            reader.readline()

        # Tratamos el fichero
        for line in reader:

            if line.strip() != '':
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

    # Guardamos los resultados en un fichero
    with open(os.path.join(os.path.join(os.getcwd(), treatedFolder), movies[x]), 'w') as writer:
        for y in range(indice):
            writer.write(tratado[y]+'\n')
