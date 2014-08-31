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
        for giocatore, personaggio in personaggi.iteritems():
            print "%s | " % giocatore,
            for key, value in personaggio.iteritems():
                print "%s: %s | " % (key, value),
            print


"""
    Inizializza una nuova sfida nell'insieme dei potenziali
    punti esperieza.
    In caso di sfide omogenee e` possibile specificare il parametro
    numerosita` per moltiplicare automaticamente il punteggio.
"""
def crea_nuova_sfida():
    nome_sfida = raw_input("Inserisci il nome della sfida: ")
    try:
        punti_esperienza = int(raw_input("Inserisci i punti esperienza: "))
        numerosita = int(raw_input("Inserisci eventuale numerosita`: "))
        if numerosita:
            punti_esperienza = punti_esperienza * numerosita
    except ValueError:
        print "Inserire solo numeri interi."

    sfida = Sfida(nome_sfida, punti_esperienza)
    return sfida


"""
    Stampa tutte le sfide censite in questa sessione.
"""
def stampa_sfide(sfide):
    for sfida in sfide:
        print sfida.print_sfida()


"""
    Prende in carico le sfide censite, calcola il totale di 
    punti e li assegna ai personaggi in base di dati.
    Per motivi filosofici le ricompense sono sempre distribuite
    equamente tra i membri del gruppo.
"""
def assegna_punti_esperienza(sfide):
    
    # Calcola totale di punti
    punti_esperienza_totali = 0
    for sfida in sfide:
        punti_esperienza_totali += sfida.punti_esperienza

    # Carica i dati dei personaggi in formato lista di dizionari
    with open('personaggi.json', 'r') as personaggi_correnti:
        personaggi = json.load(personaggi_correnti)

        # Caclola equamente le ricompense
        punti_esperienza_a_testa = punti_esperienza_totali / len(personaggi)

    # Mappa i dati da dizionario a istanze di classe
    for personaggio in personaggi.iteritems():
        personaggio_aggiornato = PersonaggioGiocante()
        personaggio_aggiornato.update_from_dict(personaggio)
        personaggio_aggiornato.add_punti_esperienza(punti_esperienza_a_testa)
        personaggio_aggiornato.save()

    return punti_esperienza_a_testa

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
        5. Assegna punti esperienza
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

        elif ans == "5":
            pe = assegna_punti_esperienza(sfide)
            print("\n%s punti esperienza per personaggio assegnati con successo." % pe)

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