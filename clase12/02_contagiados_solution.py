#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:46:06 2020

@author: danielaudd
"""

#Abrimos el archivo
f = open('2020-05-01-CasosConfirmados.csv','r')
contagiados=[]
comuna=[]
for linea in f:
    lista=linea.split(',') #Paso texto antes de la coma a una lista    
    if lista[0]=='Metropolitana':
        contagiados.append(float(lista[5][:-1]))
        comuna.append(lista[2])
f.close()

#Imprimos una lista con las comunas de la RM y los contagiados

print(comuna)
print(contagiados)


#Copiamos la lista de contagiados a una lista auxiliar
contagiados_sort=contagiados.copy() 
contagiados_sort.sort(reverse=True)

print(contagiados_sort)

min_contagiados=min(contagiados_sort[:5])

print(min_contagiados)

print('Solucion 1:')
print('Las comunas con mas contagiados son:' + '\n')
for i in range(len(contagiados)):
    if contagiados[i]>=min_contagiados:
        print(comuna[i], contagiados[i])
