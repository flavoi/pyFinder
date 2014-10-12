#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Programma di censimento e gestione personaggi.

    @author: Flavio Marcato
"""

import json, sys, random

from pyfinder.config import RARR, COLORS, stampa_tabella
from pyfinder.personaggi.config import JSON_FILE, PersonaggioGiocante, get_group_exp


"""
    Inizializza personaggi di livello 1 con gli attributi di base.
"""
def crea_nuovo_personaggio():
    nome_giocatore = raw_input("Inserisci il nome del giocatore: ")
    nome_personaggio = raw_input("Inserisci il nome del personaggio: ")
    personaggio = PersonaggioGiocante(nome_giocatore, nome_personaggio)
    personaggio.save()
    return personaggio

"""
    Estrae in una tabella tutti i personaggi censiti in base di dati.
"""
def formatta_personaggi():
    campi = [
        ("Giocatore", "l"),
        ("Personaggio", "l"), 
        ("Esperienza", "c"),
    ]
    avviso = "Non e` stato ancora censito alcun personaggio."
    return (campi, JSON_FILE, avviso)
            
"""
    Invoca menu` principale.
"""
def main():
    ans = True
    while ans:
        print
        print "(1) Crea un nuovo personaggio\n(2) Stampa tutti i personaggi\n(e) Esci"
        ans=raw_input("Inserisci attivita` %s  " % RARR) 
        if ans == "1": 
            pg = crea_nuovo_personaggio()
            print COLORS['okgreen'] + "Il personaggio di %s e` stato creato con successo." % pg + COLORS['endc']
        elif ans == "2":
            personaggi = formatta_personaggi()
            print stampa_tabella(*personaggi)
        elif ans == "e":
            print("Ciao!") 
            sys.exit(0)
        else:
            print COLORS['warning'] + "La scelta non e` valida, riprova." + COLORS['endc']

if __name__ == '__main__':
    main()