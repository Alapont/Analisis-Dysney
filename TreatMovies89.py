#!/usr/bin/python
# -*- coding: utf-8 -*-

from operator import itemgetter, attrgetter, methodcaller
import csv
import os
import re

genders = dict(men=0, woman=0)
womens = ["SHOCK & BARREL", 'LOCK,SHOCK, AND BARREL', "WITCH", 'LOCK, SHOCK & BARREL', 'LOCK AND SHOCK', 'SALLY',
'LOCK', 'JACK AND SALLY', 'WITCHES AND CREATURE LADY', 'LOCK, SHOCK, AND BARREL', 'WITCHES', 'CHILD CORPSE TRIO',
'JACK & SALLY']
origin = 'CountWords'
destination = 'GendersCount'

filename = 'TheNightmareBeforeChristmas.csv'

if os.path.exists(os.path.join(os.getcwd(), destination)) == False:
    os.mkdir(os.path.join(os.getcwd(), destination))

with open(os.path.join(os.path.join(os.getcwd(), origin), filename), 'r') as reader:
    for z in range(2):
        reader.readline()
    for line in reader:

        datos = line.split(';')
        if womens.count(datos[0].upper()) > 0:
            genders["woman"] = genders["woman"] + int(datos[1])
        elif datos[0]=='' or datos[1]=='':
            pass
        else:
            genders["men"] = genders["men"] + int(datos[1])

with open(os.path.join(os.path.join(os.getcwd(), destination), filename), 'w') as writer:
    writer.write(filename[:-(len(filename)-filename.find('.'))] + '\n')

    for key, value in genders.items():
        writer.write(key + ';' + str(value)+';\n')


del genders
