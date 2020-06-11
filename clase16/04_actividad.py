#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:02:56 2020

@author: danielaudd
"""

cont_reg=dict()
with open("2020-06-01-CasosConfirmados-totalRegional.csv", "r") as T:
    next(T)
    for line in T:
        s=line.split(',')
        region=" ".join(s[0].split())
        if region == 'Total':
            continue
        cont_reg[region]=int(s[3])
        
print(cont_reg)

def remove_accents(s):
    return s.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('’','\'').replace('Ñ','N')

pcr_reg=dict()
with open("pcr.csv", "r") as g:
    next(g)
    for line in g:
        s=line.split(',')
        region =remove_accents(s[0])
        pcr_reg[region]=int(s[56])
                            
print(pcr_reg)

 

f = open("pcr_region.csv", "w")
for region, pcr in pcr_reg.items():
    linea=region + ' ' + str(pcr) + ' ' + str(cont_reg[region]) + '\n'
    f.write(linea)
f.close()





        


