#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 21:19:01 2018

@author: Bruno
"""

größte_zahl=1
Produkte = []
for n in range(1,1000):
    for m in range(1,1000):
        x = n*m
        x_new = str(x)
        if x >= 100: #es ist klar, dass das größte Palindrom größer als 99 ist. Eingefügt, damit es keine Probleme mit x_new[2] == x_new[-3] gibt. 
            if x_new[0] == x_new[-1] and x_new[1] == x_new[-2] and x_new[2] == x_new[-3]:
                große_zahl = x
                if größte_zahl < große_zahl:
                    größte_zahl = große_zahl

print(größte_zahl)