#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Questo script contiene alcune variabili di supporto e 
    l'elenco delle app installate.
"""

from unipath import Path
from abc import ABCMeta

# Raccolta corrente di giocatori
GROUPNAME = 'atomics'

# Raccolta corrente di creature
CREATURELIST = 'creature'

# Raccolta corrente di archetipi
TEMPLATESLIST = 'archetipi'

# Cartella principale del progetto
BASE_DIR = Path(__file__).ancestor(1)

# Simbolo freccia verso destra
RARR = "\xe2\x9e\x9c"

# Colori per la riga di comando
COLORS = {
    'header': '\033[95m',
    'bold': "\033[1m",
    'okblue': '\033[94m',
    'okgreen': '\033[92m',
    'warning': '\033[93m',
    'fail': '\033[91m',
    'endc': '\033[0m',
}

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
