#Escribir una lista en un archivo donde cada linea del archivo
#contiene un elemento de la lista
def escribir_lista(file):
    f=open(file, 'a+')

    L=[1,2,3]

    for i in  range(len(L)):
        f.write(str(i) +'\n')

    f.close()
    
escribir_lista('archivo1.txt')


#Escribir una tabla de información en un archivo donde cada linea del archivo
#tres columnas separadas por espacio

def escribir_tabla(L):
    f=open('archivo2.txt', 'a+')
    f.write(' '.join(L) + '\n')
    f.close()
    
    g=open('archivo2.txt', 'r')
    for line in g:
        print(line)

L1=['Daniela', 'Opitz', '12345']
L2=['Yerka', 'Freire', '33333']

escribir_tabla(L1)

escribir_tabla(L2)