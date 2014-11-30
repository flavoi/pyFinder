#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Programma invocazione dadi. Supporta potenzialmente
    lanci personalizzati e si basa su due parametri fondamentali:
    tipo di dado e modificatore/malus.

    @author: Flavio Marcato
"""
import sys
from random import randint
from prettytable import PrettyTable

from pyfinder.dadi.config import DADI
from pyfinder.config import COLORS

"""
    Calcola il singolo lancio.
    I parametri obbligatori sono il tipo di dado e il modificatore di competenza. 
    I parametri aggiuntivi aprono la strada ad altri tipi di lancio.
"""
def lancio_comune(tipo_dado, modificatore, *args):
    faccia_del_dado = randint(1, tipo_dado)
    totale = faccia_del_dado + modificatore
    return {'faccia_del_dado': faccia_del_dado, 'modificatore': modificatore, 'totale': totale}

"""
    Elabora lanci ripetuti. 
    Invoca il tipo di lancio specifico passato dal programma principale
    oppure quello di default.
"""
def ripeti(tipo_dado, modificatore, ripetizioni, tipo_lancio=lancio_comune):
    lanci = []
    for i in range(0, ripetizioni):
        lanci.append(tipo_lancio(tipo_dado, modificatore))
    return lanci

"""
    Estrae in una tabella tutti i lanci censiti in questa sessione.
"""
def formatta_lanci(lanci):
    # Registra i campi da esporre
    tabella = PrettyTable(["Tiro di base", "Modificatore", "Totale"])
    tabella.padding_width = 1
    for lancio in lanci:
        riga = [lancio['faccia_del_dado'], lancio['modificatore'], lancio['totale']]
        tabella.add_row(riga)
    return tabella

"""
    Invoca menu` principale.
"""
def main():
    print
    try: 
        # Definizione del dado
        tipo_dado = raw_input('Tipo di dado: ')
        if tipo_dado not in DADI:
            raise ValueError("Specificare un tipo di dado previsto. \n%s" % [dado for dado in DADI])
        tipo_dado = int(tipo_dado)
        try:
            modificatore = int(raw_input('Modificatore al tiro: '))
            ripetizioni = int(raw_input('Ripetizioni: '))
        except ValueError:
            raise ValueError("Assicurarsi di imputare un numero razionale.")
        # Lancio dei dadi
        # Prevede la specifica di lanci speciali, di default invoca un
        # lancio comune (standard_roll)
        lanci = ripeti(tipo_dado, modificatore, ripetizioni)
        # Stampa dei risultati
        tabella = formatta_lanci(lanci)
        print tabella
    except ValueError, e:
        print COLORS['fail'] + "Richiamare lo script con i parametri corretti." + COLORS['endc'] 
        print e
        

if __name__ == '__main__':
    main()
