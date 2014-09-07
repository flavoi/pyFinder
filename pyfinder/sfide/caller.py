#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Programma assegnazione punti esperienza. Supporta 
    varie modalita` di divisione, ma di default ragiona
    equamente tra tutti i personaggi giocanti.

    @author: Flavio Marcato
"""

import os, sys, json
from prettytable import PrettyTable

from pyfinder.config import BASE_DIR, COLORS, RARR
from pyfinder.personaggi.config import PersonaggioGiocante
from pyfinder.sfide.config import Sfida


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
    Estrae in una tabella tutte le sfide censite in questa sessione.
"""
def formatta_sfide(sfide):
    # Registra i campi da esporre
    tabella = PrettyTable(["Sfida", "Punti"])
    tabella.align["Sfida"] = "l"
    tabella.padding_width = 1
    if len(sfide) > 0:
        for sfida in sfide:
            riga = [sfida.get_nome_sfida(), sfida.get_punti_sfida()]
            tabella.add_row(riga)
    else:
        tabella = COLORS['warning'] + "Nessuna sfida censita." + COLORS['endc']
    return tabella

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
    os.chdir(BASE_DIR.child('personaggi'))
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
    os.chdir(BASE_DIR.child('sfide'))
    return pe


"""
    Invoca menu` principale.
"""
def main():
    ans = True
    # L'elenco delle sfide e` memorizzato nella solas sessione corrente
    sfide = []
    while ans:
        print
        print ("(1) Crea una sfida\n(2) Stampa tutte le sfide\n(3) Assegna punti esperienza\n(e) Esci")
        ans=raw_input("Inserisci attivita` %s  " % RARR) 
    
        if ans == "1":
            nuova_sfida = crea_nuova_sfida()
            sfide.append(nuova_sfida)
            print COLORS['okgreen'] + "Sfida '%s' creata con successo." % nuova_sfida + COLORS['endc']

        elif ans == "2":
            tabella_sfide = formatta_sfide(sfide)
            print tabella_sfide

        elif ans == "3":
            pe = assegna_punti_esperienza(sfide)
            if pe:
                print COLORS['okgreen'] + "%s punti esperienza assegnati con successo ad ogni personaggio." % pe + COLORS['endc']
            else:
                print COLORS['warning'] + "Non ci sono punti esperienza da assegnare." + COLORS['endc']
            # Resetta le sfide una volta consumate
            sfide = []

        elif ans == "e":
            print "Ciao!"
            sys.exit(0)
        
        else:
            print COLORS['warning'] + "La scelta non e` valida, riprova." + COLORS['endc']

if __name__ == '__main__':
    main()