#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

# charPattern = r'[\w]{1}[\w \']+:'
# scenePattern = r'[(]{1}:'
# blankLine = '\n'

pattern1 = re.compile(r'\([\w\d\s\.\,\-\'\"\/\:\;\?\!\#]*\)|\{[\w\d\s\.\,\-\'\"\/\:\;\?\!\#]*\}|\{[\w\d\s\.\,\-\'\"\/\:\;\?\!\#]*\)|\[[\w\d\s\.\,\-\'\"\/\:\;\?\!\#]*\]|\-{2,}',re.IGNORECASE)
pattern2 = re.compile(r'[ ]{2,}',re.IGNORECASE)

# moviesFolder = 'Scripts'
treatedFolder = 'TreatedScripts'
# movies = ['BeautyAndTheBeast.txt', 'Aladdin.txt', 'HunchbackOfNotreDame.txt', 'LittleMermaid.txt',
#           'MaryPoppins.txt', 'AGoofyMovie.txt', 'TheLionKing.txt', 'TheRescuersDownUnder.txt', 'TheSleepingBeauty.txt']
# cabecera = [6, 64, 26, 3, 1, 10, 21, 34, 0]

for filename in os.listdir(os.path.join(os.getcwd(), treatedFolder)):
    with open(os.path.join(os.path.join(os.getcwd(), treatedFolder), filename), 'r') as reader:
        movie=reader.read()
        movie=pattern1.sub('',movie)
        movie=pattern1.sub('',movie)
        movie=pattern2.sub(' ',movie)
    with open(os.path.join(os.path.join(os.getcwd(), treatedFolder), filename), 'w') as writer:
        writer.write(movie)
    movie=''
