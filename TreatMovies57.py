#!/usr/bin/python
# -*- coding: utf-8 -*-

from operator import itemgetter, attrgetter, methodcaller
import csv
import os
import re

genders = dict(men=0, woman=0)
womens = ["MARIE GIGGLES", 'ABIGAIL', 'MARIE TO BERLIOS', 'DUCHESS, MARIE, TOULOUSE', 'MARIE WAVES', "O'MALLEY AND MARIE", 'MARIE', 'DUCHESS, MARIE',
          'MARIE SINGS', 'MADAME', 'DUCHESS AND MARIE', "O'MALLEY, MARIE, SCAT CAT", 'MARIE AND BERLIOZ', 'AMELIA', 'AMELIA AND ABIGAIL', 'MADAME FROM THE FRONT DOOR'
          ,"DUCHESS TO WET O'MALLEY",'FROU-FROU','DUCHESS SIGHES','DUCHESS LAUGHS AND CLAPS',"DUCHESS TO O'MALLEY",'DUCHESS LAUGHS','DUCHESS']

origin = 'CountWords'
destination = 'GendersCount'

filename = 'Aristocats.csv'

if os.path.exists(os.path.join(os.getcwd(), destination)) == False:
    os.mkdir(os.path.join(os.getcwd(), destination))

with open(os.path.join(os.path.join(os.getcwd(), origin), filename), 'r') as reader:
    for z in range(2):
        reader.readline()
    for line in reader:

        datos = line.split(';')
        if womens.count(datos[0].upper()) > 0:
            genders["woman"] = genders["woman"] + int(datos[1])
        else:
            genders["men"] = genders["men"] + int(datos[1])

with open(os.path.join(os.path.join(os.getcwd(), destination), filename), 'w') as writer:
    writer.write(filename[:-(len(filename)-filename.find('.'))] + '\n')

    for key, value in genders.items():
        writer.write(key + ';' + str(value)+';\n')


del genders
