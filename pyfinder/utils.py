#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colorama import Fore, Back, Style, init

"""
    La seguente serie di funzioni formattano il colore dei
    messaggi. Si disattivano automaticamente in ambiente windows.
"""

def formatta_info(messaggio):
    init()
    s = Style.DIM + messaggio + Style.RESET_ALL
    return s

def formatta_avviso(messaggio):
    init()
    s = Fore.YELLOW + messaggio + Fore.RESET
    return s

def formatta_fallimento(messaggio):
    init()
    s = Fore.RED + messaggio + Fore.RESET
    return s

def formatta_successo(messaggio):
    init()
    s = Fore.GREEN + messaggio + Fore.RESET
    return s