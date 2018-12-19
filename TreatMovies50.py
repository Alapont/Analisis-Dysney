#!/usr/bin/python
# -*- coding: utf-8 -*-

from operator import itemgetter, attrgetter, methodcaller
import csv
import os
import re

genders = dict(men=0, woman=0)
womens = ["BELLE", "WARDROBE", "BIMBETTES", "JASMINE", "LADY",
          "WOMEN", "WOMAN", "WOMAN 1", "WOMAN 2", "GYPSY MOTHER", "ESMERALDA"]

origin = 'CountWords'
destination = 'GeneresCount'


if os.path.exists(os.path.join(os.getcwd(), destination)) == False:
    os.mkdir(os.path.join(os.getcwd(), destination))

for filename in os.listdir(os.path.join(os.getcwd(), origin)):
    with open(os.path.join(os.path.join(os.getcwd(), origin), filename), 'r') as reader:
        for line in reader:
            for z in range(2):
                reader.readline()

            datos = line.split(';')
            if womens.count(datos[0].upper()) > 0:
                genders["woman"] = genders["woman"]+1
            else:
                genders["men"] = genders["men"]+1

    with open(os.path.join(os.path.join(os.getcwd(), destination), filename), 'w') as writer:
        for key, value in genders.items():
            writer.write(key + ';' + str(value))

del genders
