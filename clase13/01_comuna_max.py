#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:20:53 2020

@author: danielaudd
"""

def comuna_max_contagiados(file):
    f = open(file,'r')
    comunas=[]
    contagiados=[]
    next(f)#Me salto la primera linea
    for line in f:
        L=line.split(',')
        comunas.append(L[2])
        contagiados.append(float(L[5][:-1]))
    f.close()
    
    contagiados_max=max(contagiados)
    comunas_contag_max=[]
    
    for i in range(len(contagiados)):
        if contagiados[i] == contagiados_max:
             comunas_contag_max.append(comunas[i])
    
    return comunas_contag_max
    
a=comuna_max_contagiados('2020-04-01-CasosConfirmados.csv')

print(a)