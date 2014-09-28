#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Questo script raccoglie le configurazioni
    per l'app 'archetipi'.

    @author: Flavio Marcato
"""
import json

from pyfinder.config import TEMPLATESLIST, Serializzabile
JSON_FILE = TEMPLATESLIST + '.json'

class Archetipo(Serializzabile):
    
    # Funzione costruttrice, inizializza tutti i dati generali
    def __init__(self, nome_archetipo, mod_tipo=None, mod_grado_sfida=0, mod_taglia=None, mod_allineamento=None, mod_dadi_vita=None):
        # Attributi generali
        self.nome_archetipo = nome_archetipo
        self.mod_grado_sfida = mod_grado_sfida
        self.mod_tipo = mod_tipo
        self.mod_taglia = mod_taglia
        self.mod_allineamento = mod_allineamento
        self.mod_dadi_vita = mod_dadi_vita

    # Salva l'archetipo in base di dati
    # E` possibile entrare in modifica creando un archetipo con 
    # nome gia` censito
    def save(self):
        with open(JSON_FILE, 'r+') as archetipi_correnti:
            archetipi = json.load(archetipi_correnti)
            archetipo_corrente = self.to_json()
            # Cerca occorrenza di un archetipo gia` presente
            e_nuova_occorrenza = True
            for n,i in enumerate(archetipi):
                if i['nome_archetipo'] == archetipo_corrente['nome_archetipo']:
                    archetipi[n] = archetipo_corrente
                    e_nuova_occorrenza = False
            # Se rilevata come nuova occorrenza, la appende alle esistenti
            if e_nuova_occorrenza:
                archetipi.append(archetipo_corrente)
            archetipi_correnti.seek(0)
            archetipi_correnti.write(json.dumps(archetipi, indent=2, sort_keys=True))
            archetipi_correnti.truncate()

    def __str__(self):
        return u'%s' % self.nome_archetipo

    # Interviene sugli attributi generali di una creatura
    # Per trovare numeri da sringhe: re.search("\d+", s).group()
    def modifica_generale(creatura):
        pass

    # Interviene sugli attributi di attacco di una creatura
    def modifica_attacco(creatura):
        pass

    # Interviene sugli attributi di difesa di una creatura
    def modifica_difesa(creatura):
        pass

    # Interviene sugli attributi speciali di una creatura
    def modifica_speciale(creatura):
        pass

    # La modifica degli attributi tramite archetipo e` volutamente stringente
    # @params creatura: un oggetto tipo Creatura dall'app 'creature'
    def applica_archetipo(self, creatura):
        creatura = modifica_generale(creatura)
        creatura = modifica_attacco(creatura)
        creatura = modifica_difesa(creatura)
        creatura = modifica_speciale(creatura)
        return creatura
