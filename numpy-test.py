# -*- coding: utf-8 -*-

import random
import math
import numpy as np


def valid_input():
    eingabe = input('Tropfenzahl in Millionen: ')
    try:
        eingabe = abs(int(eingabe))
        eingabe = eingabe*1000000
    except ValueError:
        print('Bitte eine Zahl eingeben!')
    return eingabe
        
def stdpi(drops):
    drops_in_circle_segment = 0
    for i in range(drops):
        drop_distance_from_origin = math.hypot(random.random(), random.random())
        if drop_distance_from_origin < 1:
            drops_in_circle_segment += 1
    return 4*drops_in_circle_segment/drops

def nppi(drops):
    return 4*np.sum(np.hypot(np.random.rand(drops),np.random.rand(drops))<1)/drops
    
if __name__ == '__main__':    
    print(nppi(valid_input()))