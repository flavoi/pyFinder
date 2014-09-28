#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Programma di censimento e gestione archetipi.

    @author: Flavio Marcato
"""

import json, sys
from prettytable import PrettyTable

from pyfinder.config import RARR, COLORS
from pyfinder.archetipi.config import JSON_FILE, Archetipo

"""
    Inizializza un nuovo archetipo con gli attributi
    di base
"""
def crea_nuovo_archetipo():
    na = raw_input("Inserisci il nome dell'archetipo: ")
    mgs = raw_input("Inserisci il modificatore grado sfida: ")
    archetipo = Archetipo(nome_archetipo=na, mod_grado_sfida=mgs)
    archetipo.save()
    return archetipo

"""
    Estrae in una tabella tutti gli archetipi censiti in base di dati
"""
def formatta_archetipi():
    # Registra i campi da esporre
    tabella = PrettyTable(["Nome archetipo", "Grado sfida"])
    tabella.align["Nome archetipo"] = "l"
    tabella.padding_width = 1
    with open(JSON_FILE, 'r') as archetipi_correnti:
        archetipi = json.load(archetipi_correnti)
        # Evidenzia eventuale base di dati vuota
        if len(archetipi) == 0:
            tabella = COLORS['warning'] + "Non e` stato ancora censito alcun archetipo." + COLORS['endc']
        # Estrae le informazioni dalla base di dati
        for archetipo in archetipi:
            riga = [
                archetipo['nome_archetipo'].title(),
                archetipo['mod_grado_sfida'],
            ]
            tabella.add_row(riga)
    return tabella

"""
    Invoca menu` principale.
"""
def main():
    ans = True
    while ans:
        print
        print "\
(1) Crea un nuovo archetipo\n\
(2) Stampa tutti gli archetipi\n\
(3) Dettaglia un archetipo\n\
(e) Esci\
"
        ans = raw_input("Inserisci attivita` %s  " % RARR)
        if ans == "1":
            ao = crea_nuovo_archetipo()
            print COLORS['okgreen'] + "L'archetipo %s e` stato creato con successo." % ao + COLORS['endc']
        if ans == "2":
            tabella_archetipi = formatta_archetipi()
            print tabella_archetipi
        elif ans == "e":
            print("Ciao!") 
            sys.exit(0)
        else:
            print COLORS['warning'] + "La scelta non e` valida, riprova." + COLORS['endc']

if __name__ == '__main__':
    main()   