#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

puntosSuspensivos = re.compile(r'[.]{2,}')
puntosSuspensivos2 = re.compile(r'[. ]{3,}')
comillas = re.compile(r'"')
fin = re.compile(r'THE END:')
marcasScript = re.compile(
    r'January 2012: Final Shooting Script_2012_01_18_v2 [\d]{1,}')
marcasScript2 = re.compile(r'CUT TO BLACK.:')
parentesis = re.compile(
    r'\([\w\d\s\.\,\-\'\"\/\:\;\?\!\#]*\)|\{[\w\d\s\.\,\-\'\"\/\:\;\?\!\#]*\}|\*[\w\d\s\.\,\-\'\"\/\:\;\?\!\#]*\*|\{[\w\d\s\.\,\-\'\"\/\:\;\?\!\#]*\)|\[[\w\d\s\.\,\-\'\"\/\:\;\?\!\#]*\]|\-{2,}', re.IGNORECASE)
espaciosEnBlanco = re.compile(r'[ ]{2,}', re.IGNORECASE)
marcasDeEscena = re.compile(r'CUT TO::')
marcasDeEscena2 = re.compile(r'BACK TO::')
marcasDeEscena3 = re.compile(r'DISSOLVE TO::')
marcasDeEscena4 = re.compile(r'BACKS AWAY::')
doblesDosPuntos = re.compile(r'::')
saltosDeLinea = re.compile(r'[\n]{2,}')
numerosPagina = re.compile(r'[\d]{1,}:')
tabuladores = re.compile(r'[\\t]{1,}:')
espaciosEnLosNombres = re.compile(r'[ ]{1,}:[ ]{1,}')

intermediateScripts = 'IntermediateScripts'
intermediateScripts2 = 'IntermediateScripts2'

if os.path.exists(os.path.join(os.getcwd(), intermediateScripts2)) == False:
    os.mkdir(os.path.join(os.getcwd(), intermediateScripts2))

for filename in os.listdir(os.path.join(os.getcwd(), intermediateScripts)):
    with open(os.path.join(os.path.join(os.getcwd(), intermediateScripts), filename), 'r') as reader:
        movie = reader.read()
        # movie = puntosSuspensivos.sub('.', movie)
        movie = puntosSuspensivos2.sub('.', movie)
        movie = comillas.sub('', movie)
        movie = movie.replace('\t',' ')
        movie = marcasScript2.sub('', movie)
        movie = parentesis.sub('', movie)
        movie = fin.sub('', movie)
        movie = numerosPagina.sub('', movie)
        movie = parentesis.sub('', movie)
        movie = marcasDeEscena.sub('', movie)
        movie = marcasDeEscena2.sub('', movie)
        movie = marcasDeEscena3.sub('', movie)
        movie = marcasDeEscena4.sub('', movie)
        movie = doblesDosPuntos.sub(':', movie)
        movie = espaciosEnBlanco.sub(' ', movie)
        movie = espaciosEnLosNombres.sub(': ', movie)
        movie = saltosDeLinea.sub('\n', movie)
        movie = marcasScript.sub('', movie)
        movie = saltosDeLinea.sub('\n', movie)

    with open(os.path.join(os.path.join(os.getcwd(), intermediateScripts2), filename), 'w') as writer:
        writer.write(movie)
    movie = ''
