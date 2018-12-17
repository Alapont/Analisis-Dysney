#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

parentesis = re.compile(
    r'\([\w\d\s\.\,\-\'\"\/\:\;\?\!\#]*\)|\{[\w\d\s\.\,\-\'\"\/\:\;\?\!\#]*\}|\{[\w\d\s\.\,\-\'\"\/\:\;\?\!\#]*\)|\[[\w\d\s\.\,\-\'\"\/\:\;\?\!\#]*\]|\-{2,}', re.IGNORECASE)
espaciosEnBlanco = re.compile(r'[ ]{2,}', re.IGNORECASE)
marcasDeEscena = re.compile(r'CUT TO::')
saltosDeLinea = re.compile(r'[\n]{2,}')
espaciosEnLosNombres = re.compile(r'[ ]{1,}:[ ]{1,}')

intermediateScripts = 'IntermediateScripts'
intermediateScripts2 = 'IntermediateScripts2'

if os.path.exists(os.path.join(os.getcwd(), intermediateScripts2))==False:
    os.mkdir(os.path.join(os.getcwd(), intermediateScripts2))

for filename in os.listdir(os.path.join(os.getcwd(), intermediateScripts)):
    with open(os.path.join(os.path.join(os.getcwd(), intermediateScripts), filename), 'r') as reader:
        movie = reader.read()
        movie = parentesis.sub('', movie)
        movie = parentesis.sub('', movie)
        movie = marcasDeEscena.sub('', movie)
        movie = espaciosEnBlanco.sub(' ', movie)
        movie = saltosDeLinea.sub('', movie)
        movie = espaciosEnLosNombres.sub(': ', movie)
    with open(os.path.join(os.path.join(os.getcwd(), intermediateScripts2), filename), 'w') as writer:
        writer.write(movie)
    movie = ''
