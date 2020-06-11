#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:25:25 2020

@author: danielaudd
"""

def contagiados_n(n,file):  
    f = open(file,'r')
    contagiados=[]
    comuna=[]
    next(f)
    for linea in f:
        lista=linea.split(',')
        contagiados.append(float(lista[5][:-1]))
        comuna.append(lista[2])
    f.close()
    comunas_n = []
    for i in range(len(contagiados)):
        if contagiados[i] > n:
            comunas_n.append(comuna[i])
            
    return comunas_n

a = contagiados_n(10,'2020-05-01-CasosConfirmados.csv')
print(a)