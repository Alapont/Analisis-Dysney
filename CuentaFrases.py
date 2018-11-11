#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv
import re
from operator import itemgetter, attrgetter, methodcaller

charPattern = r'[\w]{1}[\w ]+:'
scenePattern = r'[(]{1}:'
blankLine = '\n'

data = dict()
genders = dict(men=0, woman=0)
womens = ["BELLE", "WARDROBE", "BIMBETTES", "JASMINE", "LADY",
          "WOMEN", "WOMAN", "WOMAN 1", "WOMAN 2", "GYPSY MOTHER", "ESMERALDA"]
moviesFolder = 'Scripts'
pelis = ['BeautyAndTheBeast.txt',
         'Aladdin.txt', 'HunchbackOfNotreDame.txt']
newLine = False
changeScene = False

print(os.getcwd())
print(os.pardir)
print(os.path.join(os.pardir, moviesFolder))
print(os.path.join(os.path.join(os.getcwd(), moviesFolder), pelis[1]))


for x in range(3):
    with open(os.path.join(os.path.join(os.getcwd(), moviesFolder), pelis[x]), 'r') as reader:
        for line in reader:
            # if line == blankLine:
            #     newLine = True

            # newScene = re.match(scenePattern, line)
            # if newLine && newScene:

            matchObj = re.match(charPattern, line)
            if matchObj:
                character = matchObj.group()[:-1]
                if data.has_key(character):
                    data[character] = data[character]+1
                else:
                    data[character] = 1

                if womens.count(character.upper()) > 0:
                    genders["woman"] = genders["woman"]+1
                else:
                    genders["men"] = genders["men"]+1

    for key, value in sorted(data.items(), key=itemgetter(1), reverse=True):
        print(key + " - " + str(value))

    for key, value in genders.items():
        print(key + " - " + str(value))


del data
