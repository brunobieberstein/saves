# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 09:45:32 2018

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

def list_of_choices(gc_int):
    liste = []
    n = 0
    while n in range(0, gc_int):
        liste.append(''.join(random.choices(['G','C'])))
        n = n + 1
    at_int = 100 - gc_int
    n = 0
    while n in range(0, at_int):
        liste.append(''.join(random.choices(['A','T'])))
        n = n + 1
    return liste

def make_seq(liste, seq_int):
    seq_liste = []
    n = 0
    while n in range(0, seq_int):
        seq_liste.append(''.join(random.choices(liste)))
        n = n + 1
    seq_str = ''.join(seq_liste)
    return seq_str
    
    
    

gc_int = valid_input_gc()
seq_int = valid_input_len()
liste = list_of_choices(gc_int)
seq_str = make_seq(liste, seq_int)


print('')
print(seq_str)
