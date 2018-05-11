# -*- coding: utf-8 -*-
"""
Created on Wed May  9 10:41:37 2018

@author: student
"""
#Rückgabewerte: 1:positiv; 2:negativ; -1:unschlüsslig;


def evaluate_patient(data): # data[0] = x_1; data[1] = x_2; data[2] = x_n; data[3] = x_m;
    if data[0] < 0:
        data[0] = 0
    if data[1] < 0:
        data[1] = 0
    delta_x_1 = data[0] - data[2]
    delta_x_2 = data[1] - data[2]
    delta_x_m = data[3] - data[2]
    prdelta_x_1 = 100*delta_x_1/data[2]
    prdelta_x_2 = 100*delta_x_2/data[2]
    if data[2] > 8:
        return -1
    if delta_x_1 >= 0.35 and prdelta_x_1 >= 25:
        return 1
    if delta_x_2 >= 0.35 and prdelta_x_2 >= 25:
        return 1
    if delta_x_m >= 0.5:
        return 2
    else:
        return -1

def testing():
    data=(2,0,1.5,0)
    if evaluate_patient(data) != 1:
        raise AssertionError('falsches Ergebnis')
        
    data=(4,0,4,6)
    if evaluate_patient(data) != 2:
        raise AssertionError('falsches Ergebnis')
    
    data=(1,0,1,1.6)
    if evaluate_patient(data) != 2:
        raise AssertionError('falsches Ergebnis')
    
    data=(0,-0.003,4,0)
    if evaluate_patient(data) != 2:
        raise AssertionError('falsches Ergebnis')
        





if __name__ == '__main__':

    testing()
        