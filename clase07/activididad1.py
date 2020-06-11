#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:00:58 2020

@author: danielaudd
"""

#Parte 1
suma = 0
prom = 0
notas = [1.0, 2.0, 3.0]
for e in notas:
    suma += e
prom = suma/len(notas)
print('prom',prom)

#Parte 2
from statistics import stdev 

std=stdev(notas)
print('std', std)

#Parte 3

ponderaciones=[0.5, 0.25, 0.25]
notas2 = [1.0, 2.0, 3.0]

suma=0
n=len(notas2)
for i in range(n):
    suma+=ponderaciones[i]*notas2[i]
nota_final=suma
    
print('nota final', nota_final)




