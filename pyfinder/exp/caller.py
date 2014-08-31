#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Programma assegnazione punti esperienza. Supporta 
    varie modalita` di divisione, ma di default ragiona
    equamente tra tutti i personaggi giocanti.

    @author: Flavio Marcato
"""

import sys, json

from pyfinder.exp.config import PersonaggioGiocante

"""
    Inizializza personaggi di livello 1 con gli attributi
    di base.
"""
def crea_nuovo_personaggio():
    nome_giocatore = raw_input("Inserisci il nome del giocatore: ")
    nome_personaggio = raw_input("Inserisci il nome del personaggio: ")
    personaggio = PersonaggioGiocante(nome_giocatore, nome_personaggio)
    personaggio.save()
    return personaggio

"""
    Stampa tutti i personaggi salvati in base di dati.
"""
def stampa_personaggi():
    with open('personaggi.json', 'r') as personaggi_correnti:
        personaggi = json.load(personaggi_correnti)
        for p in personaggi:
            for key, value in p.iteritems():
                print "%s: %s" % (key, value),
                print "|",
            print

"""
    Assegna i punti esperienza equamente tra tutti
    i partecipanti.
"""
def divisione_comune():
	pass


"""
    Invoca il menu principale sulle funzionalita` supportate.
"""
def menu_start():
    ans = True
    while ans:
        print ("""
        1. Crea un nuovo personaggio
        2. Stampa tutti i personaggi
        e. Esci
        """)
        ans=raw_input("Quale attivita` vuoi fare? ") 
        
        if ans == "1": 
            pg = crea_nuovo_personaggio()
            print("\nPersonaggio %s creato con successo." % pg)
        
        elif ans == "2":
            stampa_personaggi()
        
        elif ans == "e":
            print("\nCiao!") 
            sys.exit(0)
        
        else:
            print("\nScelta non valida, riprova.") 


""" Invocazione programma principale. """
def main():
    menu_start()


if __name__ == '__main__':
    main()