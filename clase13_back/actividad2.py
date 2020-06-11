import math


def lista_cumpleanos(colegio,universidad):
    L=colegio.copy()
    for e in colegio:
        for f in universidad:
            if e == f:
                L.remove(f)
    
    lista_cumple=universidad + L
    return lista_cumple
    
def vasos(L):
    n_vasos=len(L)+len(L)/3
    return math.ceil(n_vasos)
    
print('Lista de cumpleaños' + '\n')    

C=['Tamara Vicencio', 'Vivian Munoz', 'Leo Ferres','Javiera Ventura', 'Francisca Varela']
U = ['Eduardo Graells', 'Leo Ferres', 'Loreto Bravo']


print('Amigos del colegio:', C, '\n')

print('Amigos de la universidad:', U, '\n')


print(lista_cumpleanos(C, U), '\n')

print('Vasos para el cumple', vasos(lista_cumpleanos(C,U)))