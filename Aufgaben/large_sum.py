#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 18:09:57 2018

@author: Bruno
"""
x = 0
fobj = open('large_sum.txt')
for line in fobj:
    intline = int(line )
    x = x + intline
fobj.close()
print()
print('Die Summe beträgt:' ,x)