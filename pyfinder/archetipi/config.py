#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Questo script raccoglie le configurazioni
    per l'app 'archetipi'.

    @author: Flavio Marcato
"""
import json, re
from os import chdir

from pyfinder.creature.config import Speciale
from pyfinder.config import TEMPLATESLIST, Serializzabile, BASE_DIR
JSON_FILE = TEMPLATESLIST + '.json'


class Archetipo(Serializzabile):
    
    # Funzione costruttrice, inizializza tutti i dati generali
    def __init__(self, nome_archetipo, mod_tipo=None, mod_grado_sfida=0, mod_taglia=None, mod_allineamento=None, mod_dadi_vita=0):
        # Attributi generali
        self.nome_archetipo = nome_archetipo
        self.mod_grado_sfida = mod_grado_sfida
        self.mod_tipo = mod_tipo
        self.mod_taglia = mod_taglia
        self.mod_allineamento = mod_allineamento
        self.mod_dadi_vita = mod_dadi_vita
        # Attributi di attacco
        self.mod_attacco = 0
        self.mod_danni = 0
        # Attributi di difesa
        self.mod_classe_armatura = 0
        self.mod_punti_ferita = 0
        self.mod_resistenza_ai_danni = None
        # Attributi di capacita` speciali
        self.speciale = []

    # Salva l'archetipo in base di dati
    # E` possibile entrare in modifica creando un archetipo con 
    # nome gia` censito
    def save(self):
        try:
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
        except IOError:
            inizializza_dati(JSON_FILE)
    
    # Popola i dati di attacco
    def aggiungi_mod_attacco(self, attacco, danni):
        self.mod_attacco = attacco
        self.mod_danni = danni

    # Popola i dati di difesa
    def aggiungi_mod_difesa(self, classe_armatura, punti_ferita, resistenza_ai_danni):
        self.mod_classe_armatura = classe_armatura
        self.mod_punti_ferita = punti_ferita
        self.mod_resistenza_ai_danni = resistenza_ai_danni

    # Popola i dati di capacita` speciali
    def aggiungi_speciale(self, nome, descrizione):
        self.speciale.append((nome, descrizione))

    def __str__(self):
        return u"%s" % self.nome_archetipo

    # Interviene sugli attributi generali di una creatura
    # Per estrarre numeri daz stringhe: re.search("\d+", s).group()
    def modifica_generale(self, creatura):
        creatura.nome += " %s" % self.nome_archetipo
        creatura.grado_sfida = int(float(creatura.grado_sfida) + float(re.search("\d+", self.mod_grado_sfida).group()))
        creatura.tipo = self.mod_tipo or creatura.tipo
        creatura.taglia = self.mod_taglia or creatura.taglia
        creatura.allineamento = self.mod_allineamento or creatura.allineamento
        creatura.dadi_vita = int(creatura.dadi_vita) + int(self.mod_dadi_vita)
        return creatura

    # Interviene sugli attributi di attacco di una creatura
    # @param selettivo: e` la lista di attacchi impattati dalla modifica
    #                   <vuoto> impatta su tutti gli attacchi della creatura
    #                    None non impatta su alcun attacco
    @staticmethod
    def gestisci_at(creatura_at, mod_at):
        bonus = int(creatura_at) + int(mod_at)
        if bonus >= 0:
            creatura_at = "+%s" % bonus
        else:
            creatura_at = "-%s" % bonus
        return creatura_at

    @staticmethod
    def gestisci_dn(creatura_dn, mod_dn):
        if creatura_dn:
            n_dadi = creatura_dn.split("d")[0]
            danni = creatura_dn.split("d")[1]
            pattern = dado = bonus = None
            if "+" in danni:
                pattern = "+"
            elif "-" in danni:
                pattern = "-"
            if pattern:
                dado = danni.split(pattern)[0]
                bonus = int(danni.split(pattern)[1]) + mod_dn
            else:
                dado = danni
                bonus = mod_dn
            creatura_dn = u"%sd%s" % (n_dadi,dado)
            if bonus > 0:
                creatura_dn += u"+%s" % bonus
        return creatura_dn

    def modifica_attacco(self, creatura, selettivo=None):
        if selettivo:
            for attacco in creatura.attacco:
                if attacco.nome in selettivo or selettivo[0] == '':
                    attacco.attacco = Archetipo.gestisci_at(attacco.attacco, self.mod_attacco)
                    attacco.danni = Archetipo.gestisci_dn(attacco.danni, self.mod_danni)
        return creatura

    # Interviene sugli attributi di difesa di una creatura
    @staticmethod
    def gestisci_rd(creatura_rd, mod_rd):
        if creatura_rd and mod_rd:
            # Determina il valore numerico piu` vantaggioso
            num_rd = int(re.search("\d+", creatura_rd).group())
            mod_num_rd = int(re.search("\d+", mod_rd).group())
            if mod_num_rd > num_rd:
                creatura_rd = creatura_rd.replace(str(num_rd), str(mod_num_rd))
            # Determina il suffisso piu` vantaggioso tramite 
            # valore maggiore o concatenazione
            suffix_rd = creatura_rd.split("/")[1]
            suffix_mod_rd = mod_rd.split("/")[1]
            if suffix_rd != suffix_mod_rd:
                try:
                    if int(suffix_mod_rd) > int(suffix_rd):
                        creatura_rd = creatura_rd.replace(str(suffix_rd), str(suffix_mod_rd))
                except ValueError:
                    creatura_rd += " e %s" % suffix_mod_rd
        else:
            creatura_rd = mod_rd
        return creatura_rd

    def modifica_difesa(self, creatura):
        if creatura.difesa is not None:
            creatura.difesa.classe_armatura = int(creatura.difesa.classe_armatura) + int(self.mod_classe_armatura)
            creatura.difesa.punti_ferita = int(creatura.difesa.punti_ferita) + int(self.mod_punti_ferita) * int(creatura.dadi_vita)
            creatura.difesa.resistenza_ai_danni = Archetipo.gestisci_rd(creatura.difesa.resistenza_ai_danni, self.mod_resistenza_ai_danni)
        return creatura

    # Interviene sugli attributi speciali di una creatura
    def modifica_speciale(self, creatura):
        for speciale in self.speciale:
            sp = Speciale(speciale[0], speciale[1])
            creatura.speciale.append(sp)
        return creatura

    # La modifica degli attributi tramite archetipo e` volutamente stringente
    # @params creatura: un oggetto tipo Creatura dall'app 'creature'
    def applica_archetipo(self, creatura, selettivo=None):
        creatura = self.modifica_generale(creatura)
        creatura = self.modifica_attacco(creatura, selettivo)
        creatura = self.modifica_difesa(creatura)
        creatura = self.modifica_speciale(creatura)
        chdir(BASE_DIR.child('creature'))
        creatura.save()
        chdir(BASE_DIR.child('archetipi'))
        return creatura
