#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Programma di censimento e gestione personaggi.

    @author: Flavio Marcato
"""

import json, sys, random
from prettytable import PrettyTable

from pyfinder.config import RARR, inizializza_dati
from pyfinder.utils import formatta_avviso, formatta_successo, formatta_fallimento
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
    # Registra i campi da esporre
    tabella = PrettyTable(["Giocatore", "Personaggio", "Esperienza"])
    tabella.align["Giocatore"] = "l"
    tabella.align["Personaggio"] = "l"
    tabella.padding_width = 1
    try:
        with open(JSON_FILE, 'r') as personaggi_correnti:
            personaggi = json.load(personaggi_correnti)
            # Evidenzia eventuale base di dati vuota
            if len(personaggi) == 0:
                tabella = formatta_avviso("Non e` stato ancora censito alcun personaggio.")
            # Estrae le informazioni dalla base di dati
            for giocatore in personaggi:
                riga = [giocatore]
                for chiave, valore in personaggi[giocatore].iteritems():
                    riga.append(valore)
                tabella.add_row(riga)
    except IOError:
        inizializza_dati(JSON_FILE)
        tabella = formatta_avviso("Non e` stato ancora censito alcun personaggio.")
    return tabella
            
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
            print formatta_successo("Il personaggio di %s e` stato creato con successo." % pg)
        elif ans == "2":
            tabella_personaggi = formatta_personaggi()
            print tabella_personaggi
        elif ans == "e":
            print("Ciao!") 
            sys.exit(0)
        else:
            print formatta_avviso("La scelta non e` valida, riprova.")

if __name__ == '__main__':
    main()