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

from config import BASE_DIR, INSTALLED_APPS

def main():
    requested_app = sys.argv[1]
    if requested_app in INSTALLED_APPS:
        chdir(BASE_DIR.child(requested_app))
        system("python caller.py")
    else:
        print "Applicazione '%s' non installata." % requested_app
        sys.exit() 

if __name__ == "__main__":

    try:
        if len(sys.argv) <= 1:
            raise ValueError("App supportate: %s" % [app for app in INSTALLED_APPS])
    except ValueError, e:
        print "Richiamare lo script con i parametri corretti.\npython %s <nome_app>" % scriptname(__file__)
        print e
        sys.exit(1)

    main()
    

