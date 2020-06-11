#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 11:36:39 2020

@author: danielaudd
"""

palabra=input('Ingrese una palabra a encriptar: ')
clave='murcielago'

aux=[]

for e in palabra:
    if e not in clave:
        aux.append(e)
        
    else:
        a=clave.index(e)
        aux.append(str(a))
    
z=''.join(aux)

print('Palabra encriptada', z)