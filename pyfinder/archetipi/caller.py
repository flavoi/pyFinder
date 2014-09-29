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
    Entra in modalita` dettaglio per un archetipo selezionato.
    Informazioni di dettaglio:
        - attributi di attacco
        - attributi di difesa
        - capacita` speciali
"""
def dettaglio_archetipo(archetipo):
    while True:
        print
        print "\
(1) Aggiungi attacco\n\
(2) Definisci difesa\n\
(3) Aggiungi speciale\n\
(e) Esci\
"
        ans = raw_input("Inserisci attivita` %s  " % RARR)
        if ans == "1":
            ba = int(raw_input("Inserisci il bonus di attacco: "))
            da = int(raw_input("Inserisci i danni: "))
            archetipo.aggiungi_mod_attacco(ba, da)
            print COLORS['okgreen'] + "Il bonus di attacco e` stato preparato con successo." + COLORS['endc']
        elif ans == "2":
            ca = int(raw_input("Inserisci il bonus alla classe armatura: "))
            pf = int(raw_input("Inserisci il bonus ai punti ferita per dado vita: "))
            rd = raw_input("Inserisci la nuova resistenza al danno: ")
            archetipo.aggiungi_mod_difesa(ca, pf, rd)
            print COLORS['okgreen'] + "Il bonus di difesa e` stato preparato con successo." + COLORS['endc']
        elif ans == "3":
            nc = raw_input("Inserisci il nome della nuova capacita` speciale: ")
            dc = raw_input("Inserisci relativa descrizione: ")
            archetipo.aggiungi_speciale(nc, dc)
            print COLORS['okgreen'] + "Il nuovo speciale e` stato preparato con successo." + COLORS['endc']
        elif ans == "e":
            print("Ritorno al menu` principale.")
            break
        else:
            print COLORS['warning'] + "La scelta non e` valida, riprova." + COLORS['endc']            
    archetipo.save()
    return archetipo

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
            sa = seleziona_archetipo()
            if sa is not None:
                print COLORS['okgreen'] + "Selezionato archetipo %s, procedo." % sa + COLORS['endc']
                da = dettaglio_archetipo(sa)
                print COLORS['okgreen'] + "L'archetipo %s e` stato aggiornato con successo." % da + COLORS['endc']
            else:
                print COLORS['warning'] + "L'archetipo da te inserito deve ancora essere censito." + COLORS['endc']
        elif ans == "4":
            pass
        elif ans == "5":
            chdir(BASE_DIR.child('archetipi'))
            so = seleziona_archetipo()
            if so is not None:
                chdir(BASE_DIR.child('creature'))
                sc = seleziona_creatura()
                if sc is not None:            
                    chdir(BASE_DIR.child('archetipi'))
                    if so.mod_attacco > 0 or so.mod_danni > 0:
                        la = raw_input("Indica gli attacchi impattati: ")
                        # La virgola separa i singoli campi
                        la = la.split(",")
                    cm = so.applica_archetipo(sc, la)
                    print COLORS['okgreen'] + "Creatura %s modellata con successo" % cm + COLORS['endc']
                else:
                    print COLORS['warning'] + "La creatura da te inserita deve ancora essere censita." + COLORS['endc']
            else:
                print COLORS['warning'] + "L'archetipo da te inserito deve ancora essere censito." + COLORS['endc']
        elif ans == "e":
            print("Ciao!") 
            sys.exit(0)
        else:
            print COLORS['warning'] + "La scelta non e` valida, riprova." + COLORS['endc']

if __name__ == '__main__':
    main()   