#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Questo script raccoglie le configurazioni
    per l'app 'creature'.

    @author: Flavio Marcato
"""

import json

from pyfinder.config import CREATURELIST
JSON_FILE = CREATURELIST + '.json'


"""
    Una creatura del bestiario.
    Oggetti di questo tipo sono scaricabili in un dizionario
    tramite l'attributo __dict__.
"""
class Creatura:

    # Funzione costruttrice, inizializza nome, tipo e grado sfida
    def __init__(self, nome=None, tipo=None, grado_sfida=None):
    	self.nome = nome
    	self.tipo = tipo
    	self.grado_sfida = grado_sfida

    # Salva la creatura in base di dati
    def save(self):
        with open(JSON_FILE, 'r+') as creature_correnti:
            creature = json.load(creature_correnti)
            creature[self.nome] = {
                'tipo': self.tipo,
                'grado_sfida': self.grado_sfida,
            }
            # Ritorna all'inizio del tracciato
            creature_correnti.seek(0)  
            # Aggiorna l'occorrenza appena preparata
            creature_correnti.write(json.dumps(creature, indent=2, sort_keys=True))
            creature_correnti.truncate()

    # Stampa una creatura 
    def __str__(self):
        return u"%s" % self.nome
