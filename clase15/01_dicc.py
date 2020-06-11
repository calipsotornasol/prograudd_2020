notas = {'Diego'    : 4.1
        ,'Francisca': 5.5
        ,'Daniela'  : 6.8
        ,'Leo'      : 3.9}

#Imprimir llaves        
for llave in notas.keys():
    print(llave)
    
print('######')    
#Imprimir valores
    
for valor in notas.values():
    print(valor)
    

#Imprimir llaves y los valores
for llave, valor in notas.items():
    print(llave, valor)


print(notas)