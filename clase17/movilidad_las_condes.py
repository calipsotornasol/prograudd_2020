#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:29:04 2020

@author: danielaudd
"""
import matplotlib.pyplot as plt

from datetime import datetime

las_condes=list()


with open('IndiceDeMovilidad-IM.csv', 'r') as f:
    for line in f:
            s=line.split(',')
            if line.startswith('Regio'):
                fechas= s[6:]
            else:
                comuna=s[2]
                if comuna=='Las Condes':
                    las_condes=s[6:]  
                    
fechas[46]=fechas[46][:-1]

im_lcondes=[]
for n in las_condes:
    im_lcondes.append(float(n));


dates=[]

for n in fechas:
    dates.append(datetime.strptime(n, '%Y-%m-%d').date())
    

plt.ylabel('Indice Movilidad')
plt.xlabel('Fecha')
plt.xticks(rotation=45)
plt.title('Movilidad de Las Condes')
plt.plot(dates,im_lcondes, label='Las Condes')
plt.legend()
plt.savefig('movilidad_las_condes.png', bbox_inches='tight', dpi=200)