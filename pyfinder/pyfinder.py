#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Redireziona e richiama le app invocate dall'utente.
    Tutte le app installate sono riportate in config.py del pacchetto principale.

    @version: 1.2
    @author: Flavio Marcato
"""

import sys
from os import chdir, system
from os.path import basename as scriptname
from colorama import init
init()

from config import BASE_DIR, INSTALLED_APPS
from utils import formatta_avviso, formatta_fallimento, formatta_info

INFO = "App supportate: %s" % [app for app in INSTALLED_APPS]

"""
    Invoca il programma principale.
    Redireziona le logiche verso l'app specificata.
"""
def main(requested_app):
    if requested_app in INSTALLED_APPS:
        msg = "Applicazione %s attivata." % requested_app
        print formatta_info(msg)
        chdir(BASE_DIR.child(requested_app))
        system("python caller.py")
    else:
        msg = "Applicazione %s non installata." % requested_app
        print formatta_fallimento(msg)
        print formatta_info(INFO)
        sys.exit(1) 

if __name__ == "__main__":
    # Verifica parametri di ingresso
    try:
        if len(sys.argv) <= 1:
            raise ValueError(INFO)
    except ValueError, e:
        print formatta_avviso("Richiamare lo script con i parametri corretti.\npython %s <nome_app>") % scriptname(__file__)
        print e
        sys.exit(1)
    # Lettura app desiderata
    main(sys.argv[1])
    

