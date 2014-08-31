#!/env/bin/python
# -*- coding: utf-8 -*-

"""
	Questo script contiene le variabili di configurazione
	del progetto principale.
"""

from unipath import Path

# Cartella principale del progetto
BASE_DIR = Path(__file__).ancestor(1)

# Applicazioni installate
INSTALLED_APPS = [
	'dadi',
    'exp',
]

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