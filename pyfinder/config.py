#!/env/bin/python
# -*- coding: utf-8 -*-

"""
	Questo script contiene le variabili di configurazione
	del progetto principale.
"""

from unipath import Path

BASE_DIR = Path(__file__).ancestor(1)

INSTALLED_APPS = [
	'dadi',
]

BCOLORS = {
    'header': '\033[95m',
    'bold': "\033[1m",
    'okblue': '\033[94m',
    'okgreen': '\033[92m',
    'warning': '\033[93m',
    'fail': '\033[91m',
    'endc': '\033[0m',
}