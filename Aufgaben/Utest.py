# -*- coding: utf-8 -*-
import random
import math


def calc_U (series1, series2):
    mit_N2_counter = 0
    ohne_N2_counter = 0
    for n in series1:
        for k in series2:
            if n > k:
                ohne_N2_counter += 1
            if n < k:
                mit_N2_counter += 1
            if n == k:
                mit_N2_counter += 0.5
                ohne_N2_counter += 0.5
    if ohne_N2_counter < mit_N2_counter:
        return ohne_N2_counter
    else:
        return mit_N2_counter


def calc_z_prob (z):
    gaussian_counter = 0
    n = 500000
    for i in range (0,n):
        if abs(random.gauss(0,1)) >= z:
            gaussian_counter += 1
    p = gaussian_counter / n
    return p


# Wachstum in cm von Roggen unter zwei Bedingungen
ohne_N2 = [2.1, 4.1, 2.0, 2.3, 3.1, 3.2, 3.4, 5.0, 3.2, 2.8]
mit_N2 = [3.1, 5.3, 6.2, 6.3, 6.2, 4.0, 4.9, 4.2, 4.5, 4.8]

n1 = len(ohne_N2)
n2 = len(mit_N2)

U_expect = n1 * n2 / 2
sigma_U = math.sqrt(n1 * n2 * (n1 + n2 + 1) / 12)
U = calc_U(ohne_N2, mit_N2)
print(U)

z = (U_expect - U - 0.5) / sigma_U
print('p-Wert (zweiseitiger Test):', calc_z_prob(z))
