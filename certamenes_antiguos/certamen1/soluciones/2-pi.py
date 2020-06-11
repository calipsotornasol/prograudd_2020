# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:58:17 2019

@author: Hugo
"""

print("Propuesta Certamen 1-Pregunta 1")
s = 0
k=1
resp=True
while resp==True:
    term=(-1)**(k + 1) / (2 * k - 1)
    s += (-1)**(k + 1) / (2 * k - 1)
    if abs(term)<0.00001:
        resp=False
    k=k+1
print(4 * s)