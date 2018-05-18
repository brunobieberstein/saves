# -*- coding: utf-8 -*-
import random
meine_liste=[]
max_liste=[]
min_liste=[]
n=1
x=1
y=1




for n in range(1000):
        meine_liste.append(random.randint(1, 10000))

print(meine_liste)
summe = sum(meine_liste)
mittelwert = summe/len(meine_liste)

sortierte_zahlen = sorted(meine_liste)
min_liste = sortierte_zahlen[:10]
max_liste = sortierte_zahlen[-10:]

    
print()    
print('kleinste 10 Zahlen:')
print(min_liste)
print()
print('größtee 10 Zahlen:')
print(max_liste)
print()
print('Der Mittelwert ist:')
print(mittelwert)



