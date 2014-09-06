#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Programma di censimento e gestione personaggi.

    @author: Flavio Marcato
"""

import json, sys, random
from prettytable import PrettyTable

from pyfinder.config import RARR, COLORS
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
    Estrae tutti i personaggi in una tabellas espondendo tutte le informazioni.
"""
def formatta_personaggi():
    # Registra i campi da esporre
    tabella = PrettyTable(["Giocatore", "Personaggio", "Esperienza"])
    tabella.align["Giocatore"] = "l"
    tabella.align["Personaggio"] = "l"
    tabella.padding_width = 1
    with open('personaggi.json', 'r') as personaggi_correnti:
        personaggi = json.load(personaggi_correnti)
        # Estrae le informazioni dalla base di dati
        for giocatore in personaggi:
            riga = [giocatore]
            for chiave, valore in personaggi[giocatore].iteritems():
                riga.append(valore)
            tabella.add_row(riga)
    return tabella
            

""" Invoca il menu` dell'app. """
def main():
    
    ans = True
    while ans:
        print
        print "(1) Crea un nuovo personaggio\n(2) Stampa tutti i personaggi\n(e) Esci"
        ans=raw_input("Inserisci attivita` %s  " % RARR) 
        
        if ans == "1": 
            pg = crea_nuovo_personaggio()
            print COLORS['okgreen'] + "Il Personaggio di %s e` stato creato con successo." % pg + COLORS['endc']
        
        elif ans == "2":
            tabella_personaggi = formatta_personaggi()
            print tabella_personaggi

        elif ans == "e":
            print("Ciao!") 
            sys.exit(0)
        
        else:
            print COLORS['warning'] + "La scelta non e` valida, riprova." + COLORS['endc']


if __name__ == '__main__':
    main()