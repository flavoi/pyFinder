#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Questo script raccoglie le configurazioni
    per l'app 'sfide'.

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

    # Accesso al nome della sfida
    def get_nome_sfida(self):
        return self.nome_sfida

    # Accesso ai punti esperienza della sfida
    def get_punti_sfida(self):
        return self.punti_esperienza

    # La rappresentazione minima 
    def __str__(self):
        return u"%s" % self.nome_sfida









