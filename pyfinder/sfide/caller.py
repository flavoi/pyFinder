#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Programma assegnazione punti esperienza. Supporta 
    varie modalita` di divisione, ma di default ragiona
    equamente tra tutti i personaggi giocanti.

    @author: Flavio Marcato
"""

from os import chdir
import sys, json

from pyfinder.personaggi.config import PersonaggioGiocante
from pyfinder.sfide.config import Sfida
from pyfinder.config import BASE_DIR

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
    chdir(BASE_DIR.child('personaggi'))
    with open('personaggi.json', 'r') as personaggi_correnti:
        personaggi = json.load(personaggi_correnti)
        # Calcola equamente le ricompense
        pe = punti_esperienza_totali / len(personaggi)

    # Mappa i dati da dizionario a istanze di PersonaggioGiocante
    for personaggio in personaggi.iteritems():
        personaggio_aggiornato = PersonaggioGiocante()
        personaggio_aggiornato.update_from_dict(personaggio)
        personaggio_aggiornato.add_punti_esperienza(pe)
        personaggio_aggiornato.save()

    return pe


""" Invoca il menu` dell'app. """
def main():
    ans = True

    # L'elenco delle sfide e` memorizzato nella solas sessione corrente
    sfide = []
    
    while ans:
        print ("""
        1. Crea una sfida
        2. Stampa tutte le sfide
        3. Assegna punti esperienza
        e. Esci
        """)
        ans=raw_input("Quale attivita` vuoi fare? ") 
    
        if ans == "1":
            nuova_sfida = crea_nuova_sfida()
            sfide.append(nuova_sfida)
            print("\nSfida %s creata con successo." % nuova_sfida)

        elif ans == "2":
            stampa_sfide(sfide)

        elif ans == "3":
            pe = assegna_punti_esperienza(sfide)
            print("\n%s punti esperienza per personaggio assegnati con successo." % pe)

        elif ans == "e":
            print("\nCiao!") 
            sys.exit(0)
        
        else:
            print("\nScelta non valida, riprova.") 

if __name__ == '__main__':
    main()