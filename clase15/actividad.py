#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:06:13 2020

@author: danielaudd
"""

contagios=dict() #Crea un diccionario
with open('2020-05-01-CasosConfirmados.csv', 'r') as f:
    for line in f:
        if line.startswith('Met') == True:
            s=line.split(',')
            contagios[s[2]]=float(s[5][:-1]) 


print(contagios)

import operator

for comuna, casos in sorted(contagios.items(),  key=operator.itemgetter(1), reverse=True):
    print(comuna, casos)