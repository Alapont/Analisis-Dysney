#!/usr/bin/python
# -*- coding: utf-8 -*-

from operator import itemgetter, attrgetter, methodcaller
import csv
import os
import re

genders = dict(men=0, woman=0)
womens = ["WOMAN", 'GIRL','MRS. EVANS', 'SHARPETTES', 'GABRIELLA MONTEZ',
          'EMMA', 'LEA','JACKIE','SHARPAY EVANS','MARTHA COX','MARTHA COX AND CHAD DANFORTH'
          ,'MS. DARBUS','TAYLOR MCKESSIE','MRS. BOLTON','KELSI NIELSEN',
          "WOMAN", 'GIRL','SHARPAY', 'CHEERLEADERS', 'KELSI',
          'SCIENCE GIRL', 'DISTURBED GIRL','MISS MONTEZ','TEACHER','TAYLOR','MISS FALSAFF'
          ,'MISS DARBUS','GABRIELLA','TROY & GABRIELLA','MRS. DANFORTH'
          ,'KELSI','TIARA','MARTHA','MISS DARBUS']

origin = 'CountWords'
destination = 'GendersCount'

filename = 'HighSchoolMusical3.csv'

if os.path.exists(os.path.join(os.getcwd(), destination)) == False:
    os.mkdir(os.path.join(os.getcwd(), destination))

with open(os.path.join(os.path.join(os.getcwd(), origin), filename), 'r') as reader:
    for z in range(2):
        reader.readline()
    for line in reader:

        datos = line.split(';')
        if womens.count(datos[0].upper()) > 0:
            genders["woman"] = genders["woman"] + int(datos[1])
        elif datos[0] == '' or datos[1] == '':
            pass
        else:
            genders["men"] = genders["men"] + int(datos[1])

with open(os.path.join(os.path.join(os.getcwd(), destination), filename), 'w') as writer:
    writer.write(filename[:-(len(filename)-filename.find('.'))] + '\n')

    for key, value in genders.items():
        writer.write(key + ';' + str(value)+';\n')


del genders
