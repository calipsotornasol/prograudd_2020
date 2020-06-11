# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:28:21 2019

@author: Hugo
"""

r = input("Ingrese su rut: (Ej: 12345678-9) ")
x = []
for c in r[:-2]:
    x.append(int(c))

mult = [3,2,7,6,5,4,3,2]
suma = 0
for i in range(1,len(x)+1):
    suma += (x[-i])*(mult[-i])

d = 11-suma%11
if d == 10 and (r[-1]=="k" or r[-1]=="K"):
    print("El Rut esta correcto!!")
elif d==11 and r[-1]==0:
    print("El Rut esta correcto!!")
elif d==int(r[-1]):
    print("El Rut esta correcto!!")
else:
    print("El Rut NO esta correcto!!")
