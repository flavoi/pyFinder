#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Redireziona e richiama le app invocate dall'utente.
    Tutte le app installate sono riportate in config.py del pacchetto principale.

    @author: Flavio Marcato
"""

import sys
from os import chdir, system
from os.path import basename as scriptname

from config import BASE_DIR, INSTALLED_APPS, COLORS

"""
    Messaggio di benvenuto.
"""
def stampa_benvenuto(appname):
    print COLORS['okblue'] + "Applicazione '%s' attivata." % appname,
    print COLORS['endc']

"""
    Messaggio d'errore.
"""
def stampa_fallimento(appname):
    print COLORS['fail'] + "Applicazione '%s' non installata." % appname,
    print COLORS['endc']

"""
    Invoca il programma principale.
    Redireziona le logiche verso l'app specificata.
"""
def main(requested_app):
    if requested_app in INSTALLED_APPS:
        stampa_benvenuto(requested_app)
        chdir(BASE_DIR.child(requested_app))
        system("python caller.py")
    else:
        stampa_fallimento(requested_app)
        sys.exit(1) 

if __name__ == "__main__":
    # Verifica parametri di ingresso
    try:
        if len(sys.argv) <= 1:
            raise ValueError("App supportate: %s" % [app for app in INSTALLED_APPS])
    except ValueError, e:
        print "Richiamare lo script con i parametri corretti.\npython %s <nome_app>" % scriptname(__file__)
        print e
        sys.exit(1)
    # Lettura app desiderata
    main(sys.argv[1])
    

