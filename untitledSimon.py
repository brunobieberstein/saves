# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:38:45 2018

@author: student
"""
while True:
    eingabe = input('Wo ist Simon?\n 1: nicht hier \n 2: krank \n')
    try:
        e = int(eingabe)
    except ValueError:
        print('\n\n1 oder 2 du Mongo!')
        continue
    if e == 2:
        print('So ein Lappen!')
        break
    elif e == 1:
        print('\n\nIch habe gefragt: ')
        continue
    else:
        print('Was?')
        continue
    