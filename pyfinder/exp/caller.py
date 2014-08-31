#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Programma assegnazione punti esperienza. Supporta 
    varie modalita` di divisione, ma di default ragiona
    equamente tra tutti i personaggi giocanti.

    @author: Flavio Marcato
"""

import sys, json

from pyfinder.exp.config import PersonaggioGiocante, Sfida

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
def print_personaggi():
    with open('personaggi.json', 'r') as personaggi_correnti:
        personaggi = json.load(personaggi_correnti)
        for p in personaggi:
            for key, value in p.iteritems():
                print "%s: %s" % (key, value),
                print "|",
            print


"""
    Inizializza una nuova sfida nell'insieme dei potenziali
    punti esperieza.
"""
def crea_nuova_sfida():
    nome_sfida = raw_input("Inserisci il nome della sfida: ")
    try:
        punti_esperienza = int(raw_input("Inserisci i punti esperienza: "))
    except ValueError:
        print "I punti esperienza sono solo numeri interi."
    sfida = Sfida(nome_sfida, punti_esperienza)
    return sfida


"""
    Stampa tutte le sfide censite in questa sessione.
"""
def stampa_sfide(sfide):
    for sfida in sfide:
        print sfida.print_sfida()


"""
    Invoca il menu principale sulle funzionalita` supportate.
"""
def menu_start():
    ans = True

    # L'elenco delle sfide e` memorizzato nella solas sessione corrente
    sfide = []
    
    while ans:
        print ("""
        1. Crea un nuovo personaggio
        2. Stampa tutti i personaggi
        3. Crea una sfida
        4. Stampa tutte le sfide
        e. Esci
        """)
        ans=raw_input("Quale attivita` vuoi fare? ") 
        
        if ans == "1": 
            pg = crea_nuovo_personaggio()
            print("\nPersonaggio %s creato con successo." % pg)
        
        elif ans == "2":
            print_personaggi()

        elif ans == "3":
            sf = crea_nuova_sfida()
            sfide.append(sf)
            print("\nSfida %s creata con successo." % sf)

        elif ans == "4":
            stampa_sfide(sfide)
        
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