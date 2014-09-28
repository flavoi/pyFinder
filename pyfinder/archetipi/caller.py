#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Programma di censimento e gestione archetipi.

    @author: Flavio Marcato
"""

import json, sys
from os import chdir
from prettytable import PrettyTable

from pyfinder.config import RARR, COLORS, BASE_DIR
from pyfinder.archetipi.config import JSON_FILE, Archetipo
from pyfinder.creature.caller import seleziona_creatura

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
    Seleziona una archetipo censita in base di dati tramite nome.
"""
def seleziona_archetipo():
    nome_archetipo = raw_input("Ricerca archetipo tramite il suo nome: ")
    # Rirca in base di dati
    with open(JSON_FILE, 'r') as archetipi_correnti:
        archetipi = json.load(archetipi_correnti)
        occorrenze = [nome_archetipo == archetipo['nome_archetipo'] for archetipo in archetipi]
        if 1 in occorrenze:
            indice_archetipo = occorrenze.index(1)
            archetipo_estratto = archetipi[indice_archetipo]
            # Ricostruisce un'istanza di archetipo
            archetipo = Archetipo(nome_archetipo)
            archetipo.__dict__.update(archetipo_estratto)
            return archetipo
        else:
            return None

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
(4) Visualizza dettagli di un archetipo\n\
(5) Applica un archetipo\n\
(e) Esci\
"
        ans = raw_input("Inserisci attivita` %s  " % RARR)
        if ans == "1":
            ao = crea_nuovo_archetipo()
            print COLORS['okgreen'] + "L'archetipo %s e` stato creato con successo." % ao + COLORS['endc']
        elif ans == "2":
            tabella_archetipi = formatta_archetipi()
            print tabella_archetipi
        elif ans == "3":
            pass
        elif ans == "4":
            pass
        elif ans == "5":
            so = seleziona_archetipo()
            chdir(BASE_DIR.child('creature'))
            sc = seleziona_creatura()            
            cm = so.applica_archetipo(sc)
            chdir(BASE_DIR.child('archetipi'))
            print COLORS['okgreen'] + "Creatura %s modellata con successo" % cm + COLORS['endc']
        elif ans == "e":
            print("Ciao!") 
            sys.exit(0)
        else:
            print COLORS['warning'] + "La scelta non e` valida, riprova." + COLORS['endc']

if __name__ == '__main__':
    main()   