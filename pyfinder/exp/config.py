#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Questo script raccoglie le configurazioni
    per l'app 'exp'.

    @author: Flavio Marcato
"""

import json


"""
    Un personaggio giocante. 
    Oggetti di questo tipo sono scaricabili in un dizionario
    tramite l'attributo __dict__.
"""
class PersonaggioGiocante:

	# Funzione costruttrice
    def __init__(self, nome_giocatore, nome_personaggio):
        self.nome_giocatore = nome_giocatore
        self.nome_personaggio = nome_personaggio
        self.punti_esperienza = 0

    # Assegna punti esperienza al giocatore corrente
    def add_punti_esperienza(punti):
    	self.punti_esperienza += punti

    # Salva il persoanggio in base di dati
    def save(self):
    	
    	with open('personaggi.json', 'r') as personaggi_correnti:
    		personaggi = json.load(personaggi_correnti)
    	
    	personaggi.append(self.__dict__)

    	with open('personaggi.json', 'wb') as personaggi_aggiornati:
    		json.dump(personaggi, personaggi_aggiornati)

    # Stampa una rappresentazione minima del personaggio
    def __str__(self):
    	return u"%s" % self.nome_personaggio

