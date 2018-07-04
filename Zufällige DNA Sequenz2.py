# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:35:23 2018

@author: student
"""

import random

def valid_input_gc():
    while True:
        gc_gehalt = input('Gewünschter GC-Gehlat in Prozent: ')
        try:
            gc_int = int(gc_gehalt)
            if gc_int < 0 or gc_int > 100:
                print('Bitte eine Zahl zwischen 0 und 100 eingeben!')
                continue
            else:
                break
        except ValueError:
            print('Bitte eine ganze Zahl zwischen 0 und 100 eingeben!')
    return gc_int

def valid_input_len():
    while True:
        seq_len = input('Gewünschte Sequenzlänge: ')
        try:
            seq_int = int(seq_len)
            if seq_int < 0:
                print('Bitte eine positive Zahl eingeben!')
                continue
            else:
                break
        except ValueError:
            print('Bitte eine ganze Zahl eingeben!')
    return seq_int

gc_int = valid_input_gc()
seq_int = valid_input_len()
g_int = c_int = gc_int/2
a_int = t_int = (100-gc_int)/2
print(''.join(random.choices(['G','C','A','T'], weights=[g_int, c_int, a_int, t_int], cum_weights=None, k = seq_int)))