#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 11:28:03 2020

@author: danielaudd
"""

condicion1=False
condicion2=False


#Valido el alto y el ancho
while condicion1==False:
    ancho=int(input('Ingrese el valor del ancho: '))
    alto=int(input('Ingrse el valor del alto: '))
    if alto<40 and ancho <30:
        condicion1=True
    else:
        print ('Valores incorrectos, por favor vuelva a ingresarlos')
      
#Valido y guardo el marcador
while condicion2==False:
    caracter= input('Que caracter usará, # o - o *, por favor seleccione una opción :')
    if (caracter=='#' or caracter=='*' or caracter=='-') :
        condicion2=True
    else :
        print ('Marcador incorrecto, por favor vuelva a ingresarlo')
     
        
    
#Establezco las variables 
base= caracter * ancho
lados= caracter + ' '*(ancho -2) + caracter


#Dibujo una forma
print(base)
for i in range(alto-2):
    print(lados)
print(base)

#Dibujo otra forma
#i=1
#while i<=alto:
    #if (i==1 or i==alto) :  #Dibujo lados del cuadradola base del rectangulo
        #print (base)
    #else:
        #print(lados) #Dibujo lados del cuadrado
    #i=i+1            
    
    
    