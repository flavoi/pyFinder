#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Questo script contiene alcune variabili di supporto e 
    l'elenco delle app installate.
"""

from unipath import Path
from abc import ABCMeta
from os import name

# Raccolta corrente di personaggi
GROUPNAME = 'personaggi'

# Raccolta corrente di creature
CREATURELIST = 'creature'

# Raccolta corrente di archetipi
TEMPLATESLIST = 'archetipi'

# Cartella principale del progetto
BASE_DIR = Path(__file__).ancestor(1)

# Simbolo freccia verso destra
# Disattivata in ambiente windows
if name != 'nt':
    RARR = "\xe2\x9e\x9c"
else:
    RARR = ": "

# Applicazioni installate
INSTALLED_APPS = [
    'dadi',
    'personaggi',
    'sfide',
    'creature',
    'archetipi',
]

"""
    Definisce una classe pronta per essere salvata in un tracciato.
"""
class Serializzabile:
    __metaclass__ = ABCMeta

    def to_json(self):
        return self.__dict__

"""
    Inizializza un file di dati se non presente.
"""
def inizializza_dati(filename):
    f = open(filename, 'w+')
    f.write('{}')
    f.close()