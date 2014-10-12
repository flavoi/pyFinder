#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Questo script contiene alcune variabili di supporto e 
    l'elenco delle app installate.
"""

import json
from unipath import Path
from abc import ABCMeta
from prettytable import PrettyTable

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

"""
    Centralizza la stampa di dati in formato tabellare.
    @params campi: lista dei campi da esporre, la singola tupla e`:
        - il nome
        - l'allineamento
    @params json: la base di dati di riferimento serializzata
    @params avviso: stampa un messaggio se la base di dati e` vuota
"""
def stampa_tabella(campi, nome_json, avviso):
    # Registra i campi da esporre
    tabella = PrettyTable(tupla[0] for tupla in campi)
    # Allinea i campi con la relativa impostazione
    for campo, allineamento in campi:
        tabella.align[campo] = allineamento  
    tabella.padding_width = 1
    with open(nome_json, 'r') as dati_correnti:
        dati = json.load(dati_correnti)
        # Evidenzia eventuale base di dati vuota
        if len(dati) == 0:
            tabella = COLORS['warning'] + "Non e` stato ancora censito alcun personaggio." + COLORS['endc']
        # Estrae le informazioni dalla base di dati
        for chiave in dati:
            riga = [chiave]
            for chiave, valore in dati[chiave].iteritems():
                riga.append(valore)
            tabella.add_row(riga)
    return tabella
