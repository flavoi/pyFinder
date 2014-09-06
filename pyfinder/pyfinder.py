#!/env/bin/python
# -*- coding: utf-8 -*-

"""
    Menu principale. Richiama le app installate nel progetto corrente.
    Raccoglie noltre alcune funzioni di supporto.

    Il progetto e` incluso al $PYTHONPATH tramite il collegamente ~/.python

    @author: Flavio Marcato
"""

import sys
from os import chdir, system
from os.path import basename as scriptname

from config import BASE_DIR, INSTALLED_APPS, COLORS

# Messaggio di benvenuto
def print_welcome(appname):
    print COLORS['okblue'] + "Applicazione '%s' attivata." % appname,
    print COLORS['endc']

# Messaggio d'errore
def print_error(appname):
    print COLORS['fail'] + "Applicazione '%s' non installata." % appname,
    print COLORS['endc']

def main(requested_app):
    if requested_app in INSTALLED_APPS:
        print_welcome(requested_app)
        chdir(BASE_DIR.child(requested_app))
        system("python caller.py")
    else:
        print_error(requested_app)
        sys.exit() 


if __name__ == "__main__":

    # Verifica parametri di ingresso
    try:
        if len(sys.argv) <= 1:
            raise ValueError("App supportate: %s" % [app for app in INSTALLED_APPS])
    except ValueError, e:
        print "Richiamare lo script con i parametri corretti.\npython %s <nome_app>" % scriptname(__file__)
        print e
        sys.exit(1)

    # Messaggio di benvenuto
    requested_app = sys.argv[1]

    # Invocazione programmi
    main(requested_app)
    

