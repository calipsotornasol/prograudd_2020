#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:59:29 2020

@author: danielaudd
"""


def contagiados_n(n, file):
    f = open(file,'r')
    comunas=[]
    contagiados=[]
    
    next(f)
    
    for line in f:
        L=line.split(',') 
        comunas.append(L[2])
        contagiados.append(float(L[5][:-1]))
    f.close()
    
    
    for i in range(len(contagiados)):
        if contagiados[i]>=n:
            print(comunas[i] + ': ' + str(contagiados[i]))
            
contagiados_n(80,'2020-05-01-CasosConfirmados.csv')

    
    
    
    
 