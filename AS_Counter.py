#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 22:35:48 2018

@author: Bruno
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""




def get_input():
    print('---------------------------------------------------------------------')
    print('Dieses Programm berechnet die drei häufigsten Aminosäuren einer DNA-Sequenz.')
    print('---------------------------------------------------------------------')
    while True:
        eingabe = input('Bitte DNA-Sequenz eingeben: ')
        eingabe = eingabe.upper()
        if len(eingabe)%3 != 0:
            print('Bitte beachte, dass je drei Nukleinsäuren eine Aminosäure ergeben.')
            continue
        if set(eingabe) - set('ATGC') != set():
            print('Die Eingabe enthält eine ungültige Nukleinsäure. Bitte A,T,G oder C verwenden.')
            continue
        else:
            return eingabe




def count_L(DNA):
    return DNA.count('L')












#main

x = get_input()

print(count_L(x)) 