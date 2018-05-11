# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




def get_input():
    print('Dieses Programm berechnet die drei häufigsten Aminosäuren einer DNA-Sequenz.')
    while True:
        eingabe = input('Bitte DNA-Sequenz eingeben: ')
        eingabe = eingabe.upper()
        if len(eingabe)%3 != 0:
            print('Bitte beachte, dass je drei Nukleinsäuren eine Aminosäure ergeben.')
            continue
        if set(eingabe) - set('ATGC') != set():
            print('no')
            continue
        else:
            return eingabe




def count_L(DNA):
    return DNA.count('L')












#main

get_input()

print(count_L(eingabe)) 