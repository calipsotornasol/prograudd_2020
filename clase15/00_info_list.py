
def obtener_notas(estudiante, lista_nombres, lista_notas):
    i = lista_nombres.index(estudiante)
    nota = lista_notas[i]
    return (estudiante, nota)

nombres = ['Diego', 'Francisca', 'Daniela', 'Leo', 'Loreto']
notas = [4.1, 5.5, 6.8, 3.9, 7.0]

#Llamo a la funcion
nombre_est, nota = obtener_notas('Loreto', nombres, notas)
print(nombre_est, 'tiene un', nota)