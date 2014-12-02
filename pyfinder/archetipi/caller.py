#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Programma di censimento e gestione archetipi.

    @author: Flavio Marcato
"""

import json, sys
from os import chdir
from prettytable import PrettyTable

from pyfinder.config import RARR, COLORS, BASE_DIR, inizializza_dati
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
    try:
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
    except IOError:
        inizializza_dati(JSON_FILE)
    return tabella

def formatta_dettaglio_archetipi(archetipo):
    # Attributi generali
    tabella_generale = PrettyTable(["Mod. tipo", "Mod. taglia", "Mod. allineamento", "Mod. dadi vita"])
    if archetipo.mod_tipo or archetipo.mod_taglia or archetipo.mod_allineamento or archetipo.mod_dadi_vita: 
        riga_generale = [
            archetipo.mod_tipo,
            archetipo.mod_taglia,
            archetipo.mod_allineamento,
            archetipo.mod_dadi_vita,
        ]
        tabella_generale.add_row(riga_generale)
    else:
        tabella_generale = COLORS['warning'] + "Non e` stato ancora definito alcun modificatore generale." + COLORS['endc']
    # Attributi di attacco
    tabella_attacco = PrettyTable(["Mod. attacco", "Mod. danni"])
    if archetipo.mod_attacco or archetipo.mod_danni:
        riga_attacco = [
            archetipo.mod_attacco,
            archetipo.mod_danni,
        ]
        tabella_attacco.add_row(riga_attacco)
    else:
        tabella_attacco = COLORS['warning'] + "Non e` stato ancora definito alcun modificatore di attacco." + COLORS['endc']
    # Attributi di difesa
    tabella_difesa = PrettyTable(["Mod. classe armatura", "Mod. punti ferita", "Mod. resistenza ai danni"])
    if archetipo.mod_classe_armatura or archetipo.mod_punti_ferita or archetipo.mod_resistenza_ai_danni:
        riga_difesa = [
            archetipo.mod_classe_armatura,
            archetipo.mod_punti_ferita,
            archetipo.mod_resistenza_ai_danni,
        ]
        tabella_difesa.add_row(riga_difesa)
    else:
        tabella_difesa = COLORS['warning'] + "Non e` stato ancora definito alcun modificatore di difesa." + COLORS['endc']
    # Attributi di capacita` speciali
    tabella_speciale = PrettyTable(["Speciale", "Descrizione"])
    tabella_speciale.align["Speciale"] = "l"
    tabella_speciale.align["Descrizione"] = "l"
    if archetipo.speciale:
        for capacita in archetipo.speciale:
            nome = capacita[0].title()
            descrizione = capacita[1].capitalize()
            LEN = 75
            descrizione = [descrizione[i:i+LEN] for i in range(0, len(descrizione), LEN)]
            descrizione_formattata = "\n".join(descrizione)
            riga = [nome, descrizione_formattata]
            tabella_speciale.add_row(riga)
    else:
        tabella_speciale = COLORS['warning'] + "Non e` stata ancora definita alcuna capacita` speciale." + COLORS['endc']
    return (tabella_generale, tabella_attacco, tabella_difesa, tabella_speciale)    
    

"""
    Seleziona una archetipo censita in base di dati tramite nome.
"""
def seleziona_archetipo():
    nome_archetipo = raw_input("Ricerca archetipo tramite il suo nome: ")
    # Ricerca in base di dati
    try:
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
    except IOError:
        inizializza_dati(JSON_FILE)

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
            chdir(BASE_DIR.child('archetipi'))
            sa = seleziona_archetipo()
            if sa is not None:
                print COLORS['okgreen'] + "Selezionato archetipo %s, procedo." % sa + COLORS['endc']
                tabelle_dettagli = formatta_dettaglio_archetipi(sa)
                for td in tabelle_dettagli:
                    print td
            else:
                print COLORS['warning'] + "L'archetipo da te inserito deve ancora essere censito." + COLORS['endc']
        elif ans == "5":
            chdir(BASE_DIR.child('archetipi'))
            sa = seleziona_archetipo()
            if sa is not None:
                chdir(BASE_DIR.child('creature'))
                sc = seleziona_creatura()
                if sc is not None:            
                    chdir(BASE_DIR.child('archetipi'))
                    la = None
                    if sa.mod_attacco > 0 or sa.mod_danni > 0:
                        la = raw_input("Indica gli attacchi impattati: ")
                        # La virgola separa i singoli campi
                        la = la.split(",")
                    cm = sa.applica_archetipo(sc, la)
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