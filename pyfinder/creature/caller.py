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
    taglia = raw_input("Inserisci la taglia: ")
    allineamento = raw_input("Inserisci l'allineamento: ")
    dadi_vita = raw_input("Inserisci i dadi vita: ")
    creatura = Creatura(nome, tipo, grado_sfida, taglia, allineamento, dadi_vita)
    creatura.save()
    return creatura

"""
    Estrae in una tabella tutte le creature censite in base di dati.
"""
def formatta_creature():
    # Registra i campi da esporre
    tabella = PrettyTable(["Nome creatura", "Tipo", "Grado sfida", "Taglia", "Allineamento", "Dadi vita"])
    tabella.align["Nome creatura"] = "l"
    tabella.align["Tipo"] = "l"
    tabella.padding_width = 1
    with open(JSON_FILE, 'r') as creature_correnti:
        creature = json.load(creature_correnti)
        # Evidenzia eventuale base di dati vuota
        if len(creature) == 0:
            tabella = COLORS['warning'] + "Non e` stata ancora censita alcuna creatura." + COLORS['endc']
        # Estrae le informazioni dalla base di dati
        for creatura in creature:
            riga = [
                creatura['nome'].title(), 
                creatura['tipo'], 
                creatura['grado_sfida'], 
                creatura['taglia'].upper(),
                creatura['allineamento'].upper(),
                creatura['dadi_vita'],
            ]
            tabella.add_row(riga)
    return tabella

"""
    Visualizza le informazioni di dettaglio di una creatura.
"""
def formatta_dettaglio_creatura(creatura):
    # Esponde informazioni di attacco
    tabella_attacco = PrettyTable(["Attacco", "Bonus di attacco", "Danni"])
    tabella_attacco.align["Attacco"] = "l"
    if creatura.attacco:
        for attacco in creatura.attacco:
            riga = [attacco.nome.title(), attacco.attacco, attacco.danni]
            tabella_attacco.add_row(riga)
    else: 
        tabella_attacco = COLORS['warning'] + "Non e` stato ancora definito alcun attacco." + COLORS['endc']
    # Esponde informazioni di difesa
    tabella_difesa = PrettyTable(["Classe armatura", "Punti ferita", "Resistenza ai danni"])
    if creatura.difesa:
        difesa = creatura.difesa
        riga = [difesa.classe_armatura, difesa.punti_ferita, difesa.resistenza_ai_danni]
        tabella_difesa.add_row(riga)
    else:
        tabella_difesa = COLORS['warning'] + "Non e` stata ancora definita alcuna difesa." + COLORS['endc']
    # Esponde informazioni di capacita` speciali
    tabella_speciale = PrettyTable(["Speciale", "Descrizione"])
    tabella_speciale.align["Speciale"] = "l"
    tabella_speciale.align["Descrizione"] = "l"
    if creatura.speciale:
        for speciale in creatura.speciale:
            # Formattazione dedicata a lunghe stringhe
            descrizione = speciale.descrizione.capitalize()
            LEN = 75
            descrizione = [descrizione[i:i+LEN] for i in range(0, len(descrizione), LEN)]
            descrizione_formattata = "\n".join(descrizione)
            riga = [speciale.nome.title(), descrizione_formattata]
            tabella_speciale.add_row(riga)
    else:
        tabella_speciale = COLORS['warning'] + "Non e` stata ancora definita alcuna capacita` speciale." + COLORS['endc']
    return (tabella_attacco, tabella_difesa, tabella_speciale)

"""
    Seleziona una creatura censita in base di dati tramite nome.
"""
def seleziona_creatura():
    nome_creatura = raw_input("Ricerca creatura tramite il suo nome: ")
    # Rirca in base di dati
    with open(JSON_FILE, 'r') as creature_correnti:
        creature = json.load(creature_correnti)
        occorrenze = [nome_creatura == creatura['nome'] for creatura in creature]
        if 1 in occorrenze:
            indice_creatura = occorrenze.index(1)
            creatura_estratta = creature[indice_creatura]
            creatura = Creatura()
            creatura.autopopola(creatura_estratta)
            return creatura
        else:
            return None

"""
    Entra in modalita` dettaglio per una creatura selezionata.
    Informazioni di dettaglio:
        - attributi di attacco
        - attributi di difesa
        - capacita` speciali
"""
def dettaglio_creatura(creatura):
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
            na = raw_input("Inserisci il nome dell'attacco: ")
            ba = raw_input("Inserisci il bonus di attacco: ")
            da = raw_input("Inserisci i danni: ")
            creatura.aggiungi_attacco(na, ba, da)
            print COLORS['okgreen'] + "Il nuovo attacco e` stato preparato con successo." + COLORS['endc']
        elif ans == "2":
            ca = raw_input("Inserisci la classe armatura: ")
            pf = raw_input("Inserisci i punti ferita: ")
            rd = raw_input("Inserisci eventuale resistenza ai danni: ")
            creatura.aggiungi_difesa(ca, pf, rd)
            print COLORS['okgreen'] + "La difesa e` stata preparata con successo." + COLORS['endc']
        elif ans == "3":
            ns = raw_input("Inserisci nome dello speciale: ")
            ds = raw_input("Inserisci la descrizione: ")
            creatura.aggiungi_speciale(ns, ds)
            print COLORS['okgreen'] + "Il nuovo speciale e` stato preparato con successo." + COLORS['endc']
        elif ans == "e":
            print("Ritorno al menu` principale.")
            break
        else:
            print COLORS['warning'] + "La scelta non e` valida, riprova." + COLORS['endc']
    creatura.save()
    return creatura

"""
    Invoca menu` principale.
"""
def main():
    ans = True
    while ans:
        print
        print "\
(1) Crea una nuova creatura\n\
(2) Stampa tutte le creature\n\
(3) Dettaglia creatura\n\
(4) Visualizza dettagli di una creatura\n\
(e) Esci\
"
        ans = raw_input("Inserisci attivita` %s  " % RARR) 
        if ans == "1": 
            ca = crea_nuova_creatura()
            print COLORS['okgreen'] + "La creatura %s e` stato creata con successo." % ca + COLORS['endc']
        elif ans == "2":
            tabella_creature = formatta_creature()
            print tabella_creature
        elif ans == "3":
            sc = seleziona_creatura()
            if sc is not None:
                print COLORS['okgreen'] + "Selezionata creatura %s, procedo." % sc + COLORS['endc']
                dc = dettaglio_creatura(sc)
                print COLORS['okgreen'] + "La creatura %s e` stato aggiornata con successo." % dc + COLORS['endc']
            else:
                print COLORS['warning'] + "La creatura da te inserita deve ancora essere censita." + COLORS['endc']
        elif ans == "4":
            sc = seleziona_creatura()
            if sc is not None:
                print COLORS['okgreen'] + "Selezionata creatura %s, procedo." % sc + COLORS['endc']
                tabelle_dettagli = formatta_dettaglio_creatura(sc)
                for td in tabelle_dettagli:
                    print td
            else:
                print COLORS['warning'] + "La creatura da te inserita deve ancora essere censita." + COLORS['endc']
        elif ans == "e":
            print("Ciao!") 
            sys.exit(0)
        else:
            print COLORS['warning'] + "La scelta non e` valida, riprova." + COLORS['endc']

if __name__ == '__main__':
    main()    