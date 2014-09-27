#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Questo script raccoglie le configurazioni
    per l'app 'creature'.

    @author: Flavio Marcato
"""

import json

from pyfinder.config import CREATURELIST, Serializzabile
JSON_FILE = CREATURELIST + '.json'


"""
    Le abilita` di offesa di una creatura.
    Possono comprendere armi naturali o armi artificiali.
"""
class Attacco(Serializzabile):

    # Funzione costruttrice, inizializza tutti i dati rilevanti
    def __init__(self, nome=None, attacco=None, danni=None):
        self.nome = nome
        self.attacco = attacco
        self.danni = danni

    def __str__(self):
        return u"%s" % self.nome

"""
    Le abilita` di difesa di una creatura.
    Comprende sempre classe armatura, punti ferita e tiri salvezza.
"""
class Difesa(Serializzabile):

    # Funzione costruttrice, inizializza tutti i dati rilevanti
    def __init__(self, classe_armatura=None, punti_ferita=None, resistenza_ai_danni=None):
        self.classe_armatura = classe_armatura
        self.punti_ferita = punti_ferita
        self.resistenza_ai_danni = resistenza_ai_danni

    def __str__(self):
        return u"%s, %s, %s" % (self.classe_armatura, self.punti_ferita, self.resistenza_ai_danni)

"""
    Le abilita` speciali di una creatura.
    Comprende note particolari su qualunque aspetto.
"""
class Speciale(Serializzabile):
    
    # Funzione costruttrice, inizializza tutti i dati rilevanti
    def __init__(self, nome=None, descrizione=None):
        self.nome = nome
        self.descrizione = descrizione

    def __str__(self):
        return u"%s" % self.nome

"""
    Una creatura del bestiario.
    Include attributi generali e di dettaglio.
"""
class Creatura(Serializzabile):

    # Funzione costruttrice, inizializza tutti i dati rilevanti
    def __init__(self, nome=None, tipo=None, grado_sfida=None, taglia='m', allineamento='nn', dadi_vita=1):
    	# Dati generali
        self.nome = nome
    	self.tipo = tipo
    	self.grado_sfida = grado_sfida
        self.taglia = taglia
        self.allineamento = allineamento
        self.dadi_vita = dadi_vita
        # Dati di dettaglio
        self.attacco = []
        self.difesa = None
        self.speciale = []

    # Appende un attacco alla lista omonima
    def aggiungi_attacco(self, nome, attacco, danni):
        nuovo_attacco = Attacco(nome, attacco, danni)
        self.attacco.append(nuovo_attacco)

    # Valorizza gli attributi di difesa
    def aggiungi_difesa(self, classe_armatura, punti_ferita, resistenza_ai_danni):
        self.difesa = Difesa(classe_armatura, punti_ferita, resistenza_ai_danni)

    # Appende una capacita` speciale alla lista omonima
    def aggiungi_speciale(self, nome, descrizione):
        nuovo_speciale = Speciale(nome, descrizione)
        self.speciale.append(nuovo_speciale)

    # La modifica degli attributi tramite archetipo e` volutamente stringente
    # @params archetipo: un oggetti tipo archetipo dall'app 'archetipi'
    def applica_archetipo(self, archetipo):
        # Aggiornamento attributi generali
        self.nome += ' %s' % archetipo.nome_archetipo
        if archetipo.mod_tipo:
            self.tipo = archetipo.mod_tipo
        self.grado_sfida += archetipo.mod_grado_sfida
        if archetipo.mod_taglia:
            self.taglia = archetipo.mod_taglia
        if archetipo.mod_allineamento
            self.allineamento = archetipo.mod_allineamento
        self.dadi_vita += archetipo.mod_dadi_vita
        # Aggiornamento attributi di dettaglio (da completares)

    # Popola un'istanza a partire da un dizionario
    # I campi devono rispettare la firma del costruttore
    def autopopola(self, data):
        self.__init__(data['nome'], data['tipo'], data['grado_sfida'])
        if 'attacco' in data:
            for attacco in data['attacco']:
                self.aggiungi_attacco(attacco['nome'], attacco['attacco'], attacco['danni'])
        if 'difesa' in data:
            difesa = data['difesa']
            self.aggiungi_difesa(difesa['classe_armatura'], difesa['punti_ferita'], difesa['resistenza_ai_danni'])
        if 'speciale' in data:
            for speciale in data['speciale']:
                self.aggiungi_speciale(speciale['nome'], speciale['descrizione'])

    # Mappa l'oggetto in un dizionario formato json
    def to_json(self):
        creatura = {
            'nome': self.nome,
            'tipo': self.tipo,
            'grado_sfida': self.grado_sfida,
            'taglia': self.taglia,
            'allineamento': self.allineamento,
            'dadi_vita': self.dadi_vita,
        }
        # Preparazione attacco
        attacco_json = []
        if self.attacco:
            for n,i in enumerate(self.attacco):
                attacco_json.append(i.to_json())
            creatura['attacco'] = attacco_json 
        # Preparazione difesa
        if self.difesa:
            difesa_json = self.difesa.to_json()
            creatura['difesa'] = difesa_json
        # Preparazione speciale
        speciale_json = []
        if self.speciale:
            for n,i in enumerate(self.speciale):
                speciale_json.append(i.to_json())
            creatura['speciale'] = speciale_json
        return creatura

    # Salva la creatura in base di dati
    # E` possibile entrare in modifica creando una creatura con 
    # nome gia` censito
    def save(self):
        with open(JSON_FILE, 'r+') as creature_correnti:
            creature = json.load(creature_correnti)
            creatura_corrente = self.to_json()
            # Cerca occorrenza di una creatura gia` presente
            e_nuova_creatura = True
            for n,i in enumerate(creature):
                if i['nome'] == creatura_corrente['nome']:
                    creature[n] = creatura_corrente
                    e_nuova_creatura = False
            # Se rilevata come nuova creatura, la appende alle esistenti
            if e_nuova_creatura:
                creature.append(creatura_corrente)
            creature_correnti.seek(0)
            creature_correnti.write(json.dumps(creature, indent=2, sort_keys=True))
            creature_correnti.truncate()

    # Stampa una creatura 
    def __str__(self):
        return u"%s" % self.nome
