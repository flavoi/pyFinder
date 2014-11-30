#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Questo script raccoglie le configurazioni
    per l'app 'personaggi'.

    @author: Flavio Marcato
"""

import json, random

from pyfinder.config import GROUPNAME, inizializza_dati
JSON_FILE = GROUPNAME + '.json'

"""
    Pesca un giocatore a caso e legge i suoi punti esperienza.
    La filosofia di gruppo vuole che tutti i giocatori siano allo stesso livello.

    @param personaggi: un dizionario contenente come chiave i nomi dei giocatori
                       e come contenuto i dati sui rispettivi personaggi.
"""
def get_group_exp(personaggi):
    membro_casuale = random.choice(personaggi.keys())
    return personaggi[membro_casuale]['punti_esperienza']


"""
    Un personaggio giocante. 
    Oggetti di questo tipo sono scaricabili in un dizionario
    tramite l'attributo __dict__.
"""
class PersonaggioGiocante:

	# Funzione costruttrice, inizializza nome giocatore, personaggi e pe
    def __init__(self, nome_giocatore=None, nome_personaggio=None):
        # Priorita` ai parametri da riga di comando
        self.nome_giocatore = nome_giocatore
        self.nome_personaggio = nome_personaggio
        self.punti_esperienza = 0
        try:
            with open(JSON_FILE, 'r') as personaggi_correnti:
                personaggi = json.load(personaggi_correnti)
                # Allinea punti esperienza al gruppo
                if len(personaggi) > 0:
                    self.punti_esperienza = get_group_exp(personaggi)
        except IOError:
            inizializza_dati(JSON_FILE)

    # Popola un'istanza a partire da una tupla, utile per caricare json
    # data[0] deve essere il nome del giocatore
    # data[1] deve contenere un dizionario di informazioni sul personaggio 
    def update_from_dict(self, data):
        self.nome_giocatore = data[0]
        self.nome_personaggio = data[1]['nome_personaggio']
        self.punti_esperienza = data[1]['punti_esperienza']

    # Assegna punti esperienza al giocatore corrente
    def add_punti_esperienza(self, punti):
        self.punti_esperienza += punti

    # Salva il persoanggio in base di dati
    def save(self):
        try:
            with open(JSON_FILE, 'r+') as personaggi_correnti:
                personaggi = json.load(personaggi_correnti)
                personaggi[self.nome_giocatore] = {
                    'nome_personaggio': self.nome_personaggio,
                    'punti_esperienza': self.punti_esperienza,
                }
                # Ritorna all'inizio del tracciato
                personaggi_correnti.seek(0)  
                # Aggiorna l'occorrenza appena preparata
                personaggi_correnti.write(json.dumps(personaggi, indent=2, sort_keys=True))
                personaggi_correnti.truncate()
        except IOError:
            inizializza_dati(JSON_FILE)

    # Dietro ogni personaggio c'e` una persona vera
    def __str__(self):
        return u"%s" % self.nome_giocatore
