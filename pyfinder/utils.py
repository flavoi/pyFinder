#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import COLORS

"""
    La seguente serie di funzioni formattano il colore dei
    messaggi. Si disattivano automaticamente in ambiente windows.
"""

def formatta_info(messaggio):
    s = COLORS['okblue'] + messaggio + COLORS['endc']
    return s

def formatta_avviso(messaggio):
    s = COLORS['warning'] + messaggio + COLORS['endc']
    return s

def formatta_fallimento(messaggio):
    s = COLORS['fail'] + messaggio + COLORS['endc']
    return s

def formatta_successo(messaggio):
    s = COLORS['okgreen'] + messaggio + COLORS['endc']
    return s