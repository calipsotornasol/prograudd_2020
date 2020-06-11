#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:43:14 2020

@author: danielaudd
"""

cont_reg=dict()

with open("2020-06-01-CasosConfirmados-totalRegional.csv", "r") as T:
    next(T)
    for line in T:
        s=line.split(',')
        region=" ".join(s[0].split())
        casos_nuevos=int(s[3])
        if region == 'Total':
            continue
        cont_reg[region]=casos_nuevos

def remove_accents(s):
    return s.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('’','\'').replace('Ñ','N') 


pcr_reg=dict()

with open("PCR.csv", "r") as g:
    next(g)
    for line in g:
        s=line.split(',')
        regiones =remove_accents(s[0])
        pcr_reg[regiones]=int(s[56])
        
file = open("positividad.csv", "w")

for region, pcr in pcr_reg.items():
    positividad = 0
    if pcr > 0:
        positividad = 100*cont_reg[region]/pcr
    valores = [region, str(pcr), str(cont_reg[region]), "{:.2f}".format(positividad)]
    
    linea = ','.join(valores) + "\n"
    file.write(linea)
file.close()