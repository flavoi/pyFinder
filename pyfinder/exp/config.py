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

	# Funzione costruttrice, supporta la creazione di un'istanza vuota
    def __init__(self, nome_giocatore=None, nome_personaggio=None):
        # Priorita` ai parametri da riga di comando
        self.nome_giocatore = nome_giocatore
        self.nome_personaggio = nome_personaggio
        self.punti_esperienza = 0        

    # Popola un'istanza a partire da una tupla, utile per caricare json
    # data[0] e` la chiave della riga
    # data[1] contiene le informazioni sul personaggio 
    def update_from_dict(self, data):
        self.nome_giocatore = data[0]
        self.nome_personaggio = data[1]["nome_personaggio"]

    # Assegna punti esperienza al giocatore corrente
    def add_punti_esperienza(self, punti):
    	self.punti_esperienza += punti

    # Salva il persoanggio in base di dati
    def save(self):
    	with open('personaggi.json', 'r+') as personaggi_correnti:
            personaggi = json.load(personaggi_correnti)
            personaggi[self.nome_giocatore] = {
                "nome_personaggio": self.nome_personaggio,
                "punti_esperienza": self.punti_esperienza,
            }
            personaggi_correnti.seek(0)  # rewind to beginning of file
            personaggi_correnti.write(json.dumps(personaggi,indent=2,sort_keys=True)) #write the updated version 
            personaggi_correnti.truncate() #truncate the remainder of the data in the file

    # Stampa una rappresentazione minima del personaggio
    def __str__(self):
    	return u"%s" % self.nome_personaggio


"""
	Una sfida puo` essere un mostro, un punto nevralgico della
	storia o in generale qualunque elemento che possa fornire punti
	esperienza.
"""
class Sfida:

    # Funzione costruttrice
    def __init__(self, nome_sfida, punti_esperienza):
        self.nome_sfida = nome_sfida
        self.punti_esperienza = punti_esperienza


    def print_sfida(self):
        return u"Nome sfida: %s | Valore sfida: %s" % (self.nome_sfida, self.punti_esperienza)

    # Stampa una rappresentazione minima del personaggio
    def __str__(self):
        return u"%s" % self.nome_sfida









