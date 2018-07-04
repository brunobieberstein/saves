# -*- coding: utf-8 -*-
import random
import math


drops_in_circle_segment = 0
drops_in_square = 0
file = open('pi.txt', 'w')
file.write('lauf#\tpi_Wert\n')
while True:
    drops_in_square += 1
    drop_distance_from_origin = math.hypot(random.random(), random.random())
    if drop_distance_from_origin < 1:
        drops_in_circle_segment += 1

    if drops_in_square % 10000 == 0:
        file.write(
            '{0}\t{1}\n'
            .format(drops_in_square, 4*drops_in_circle_segment/drops_in_square)
            )
        if drops_in_square >= 70000000:
            print('done')
            break
file.close()
