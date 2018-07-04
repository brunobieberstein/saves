# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

file = open('qft_data.txt', 'r')

def parse_input(file):
    if next(file)[:2] == '<>':
        layout = []
        data = []
        n = 0
        for line in file:
            if line[:2] != '<>':
                n += 1
                a = [item.strip() for item in line.split(',')]
                a.remove(a[0])
                layout.append(a)
            else:
                break
        for line in file:
            if n > 0:
                n -= 1
                a = [item.strip() for item in line.split(',')]
                a.remove(a[0])
                a = [float(item) if item != '' else float('nan') for item in a]
                data.append(a)
            else:
                break
    else:
        print('FileError')
    return (data,layout)

data, layout = parse_input(file)
        
    