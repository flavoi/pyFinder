#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    Programma invocazione dadi. Supporta potenzialmente
    lanci personalizzati ma si basa su due parametri fondamentali:
    tipo di dado e bonus/malus.

    @author: Flavio Marcato
"""
import sys

from random import randint
from termcolor import colored

from pyfinder.dadi.config import RARR, DADI
from pyfinder.config import BCOLORS

""" 
    Calcolo del singolo lancio.
    I parametri obbligatori sono il tipo di dado
    e il bonus/malus di competenza. Parametri aggiuntivi
    aprono la strada ad altri tipi di lancio.
"""
def lancio_comune(tipo_dado, bonus, *args):
    faccia_del_dado = randint(1, tipo_dado)
    totale = faccia_del_dado + bonus
    return {'faccia_del_dado': faccia_del_dado, 'bonus': bonus, 'totale': totale}


""" 
    Elaborazione ripetizioni. 
    Invoca il tipo di lancio specifico passato dal programma principale
    oppure quello di default.
"""
def ripeti(tipo_dado, bonus, ripetizioni, tipo_lancio=lancio_comune):
    lanci = []
    for i in range(0, ripetizioni):
        lanci.append(tipo_lancio(tipo_dado, bonus))
    return lanci


""" Invocazione programma principale. """
def main():

    try:
        
        # Lettura parametri
        tipo_dado = raw_input('Tipo di dado: ')        
        # Verifica tipo di dado
        if tipo_dado not in DADI:
            raise ValueError("Specificare un tipo di dado previsto. \n%s" % [dado for dado in DADI])

        tipo_dado = int(tipo_dado)
        bonus = int(raw_input('Bonus al tiro: '))
        ripetizioni = int(raw_input('Ripetizioni: '))

        # Lancio dei dadi
        # Prevede la specifica di lanci speciali, di default invoca un
        # lancio comune (standard_roll)
        lanci = ripeti(tipo_dado, bonus, ripetizioni)

        # Stampa dei risultati
        for lancio in lanci:
            print "%s Tiro base: %s" % (RARR, lancio['faccia_del_dado']),
            print "| Bonus: %s" % lancio['bonus'],
            print "| " + BCOLORS['okgreen'] + "Totale: %s" % lancio['totale'],
            print BCOLORS['endc'] 

    except ValueError, e:
        print "Richiamare lo script con i parametri corretti."
        print e
        


if __name__ == '__main__':
    main()
