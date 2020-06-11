#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:38:39 2020

@author: danielaudd
"""

contagios=list()

with open('2020-05-01-CasosConfirmados.csv', 'r') as f:
    for line in f:
        if line.startswith('Met') == True:
            s = line.split(',')
            comuna = s[2]
            caso = float(s[5][:-1])
            contagios.append((caso, comuna))
            
print(contagios)

for caso, comuna in sorted(contagios, reverse=True):
    print(comuna, caso)
