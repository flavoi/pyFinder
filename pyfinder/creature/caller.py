#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Programma di censimento e gestione creature.

    @author: Flavio Marcato
"""
import json, sys

from pyfinder.config import RARR, COLORS

"""
    Inizializza una creatura con gli attributi di base
"""
def crea_nuova_creatura():
    pass

"""
    Estrae in una tabella tutte le creature censites in base di dati.
"""
def formatta_creature():
    pass

"""
    Invoca menu` principale.
"""
def main():
    ans = True
    while ans:
        print
        print "(1) Crea una nuova creatura\n(2) Stampa tutte le creature\n(e) Esci"
        ans=raw_input("Inserisci attivita` %s  " % RARR) 
        if ans == "1": 
            ca = crea_nuova_creatura()
            print COLORS['okgreen'] + "La creatura %s e` stato creato con successo." % ca + COLORS['endc']
        elif ans == "2":
            tabella_creature = formatta_creature()
            print tabella_creature
        elif ans == "e":
            print("Ciao!") 
            sys.exit(0)
        else:
            print COLORS['warning'] + "La scelta non e` valida, riprova." + COLORS['endc']

if __name__ == '__main__':
    main()	