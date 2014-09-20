#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Programma di censimento e gestione creature.

    @author: Flavio Marcato
"""

import json, sys
from prettytable import PrettyTable

from pyfinder.config import RARR, COLORS
from pyfinder.creature.config import JSON_FILE, Creatura


"""
    Inizializza una creatura con gli attributi di base
"""
def crea_nuova_creatura():
    nome = raw_input("Inserisci il nome della creatura: ")
    tipo = raw_input("Inserisci il tipo di creatura: ")
    grado_sfida = raw_input("Inserisci il grado sfida: ")
    creatura = Creatura(nome, tipo, grado_sfida)
    creatura.save()
    return creatura

"""
    Estrae in una tabella tutte le creature censites in base di dati.
"""
def formatta_creature():
    # Registra i campi da esporre
    tabella = PrettyTable(["Nome creatura", "Tipo", "Grado sfida"])
    tabella.align["Nome creatura"] = "l"
    tabella.align["Tipo"] = "l"
    tabella.padding_width = 1
    with open(JSON_FILE, 'r') as creature_correnti:
        creature = json.load(creature_correnti)
        # Evidenzia eventuale base di dati vuota
        if len(creature) == 0:
            tabella = COLORS['warning'] + "Non e` stata ancora censito alcuna creatura." + COLORS['endc']
        # Estrae le informazioni dalla base di dati
        for creatura in creature:
            riga = [creatura]
            for chiave, valore in creature[creatura].iteritems():
                riga.append(valore)
            tabella.add_row(riga)
    return tabella

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