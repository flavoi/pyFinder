#!/env/bin/python
# -*- coding: utf-8 -*-

"""
	Questo script contiene alcune variabili di supporto e 
    l'elenco delle app installate.
"""

from unipath import Path

# Gruppo di giocatori corrente
GROUPNAME = 'atomics'

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
]