# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:28:15 2018

@author: student
"""

with open(r'\\ufr.isi1.public.ads.uni-freiburg.de\br100\Python\repos\saves\Aufgaben\img7a.jpg','rb') as i:
    with open(r'\\ufr.isi1.public.ads.uni-freiburg.de\br100\Python\repos\saves\Aufgaben\decrypted.jpg','wb') as o:
        data = i.read()
        decrypted_data = []
        for zahl in data:
            neue_zahl = zahl - 1
            if neue_zahl < 0:
                neue_zahl = neue_zahl + 256
            decrypted_data.append(neue_zahl)
        o.write(bytes(decrypted_data))
    