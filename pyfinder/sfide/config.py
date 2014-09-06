#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Questo script raccoglie le configurazioni
    per l'app 'personaggi'.

    @author: Flavio Marcato
"""


"""
	Una sfida puo` essere un mostro, un punto nevralgico della
	storia o in generale qualunque elemento che possa fornire punti
	esperienza.
"""
class Sfida:

    # Funzione costruttrice
    def __init__(self, nome_sfida, punti_esperienza):
        self.nome_sfida = nome_sfida
        self.punti_esperienza = punti_esperienza


    def print_sfida(self):
        return u"Nome sfida: %s | Valore sfida: %s" % (self.nome_sfida, self.punti_esperienza)

    # Stampa una rappresentazione minima del personaggio
    def __str__(self):
        return u"%s" % self.nome_sfida









