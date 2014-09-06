#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Programma di censimento e gestione personaggi.

    @author: Flavio Marcato
"""

import json, sys, random

from pyfinder.personaggi.config import PersonaggioGiocante, get_group_exp

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
        exp = get_group_exp(personaggi)
        print "Punti esperienza di gruppo: %s" % exp
        for giocatore, personaggio in personaggi.iteritems():
            print "%s" % giocatore,
            print


""" Invoca il menu` dell'app. """
def main():
    
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


if __name__ == '__main__':
    main()