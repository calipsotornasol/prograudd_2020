def promedio(lista):
    s = 0
    for e in lista:
        s += e
    return s/len(lista)
    
L = [1,2,3,4]
print('Promedio L1', promedio(L))

L2 = [1,1,1,1]
print('Promedio L2', promedio(L2))
