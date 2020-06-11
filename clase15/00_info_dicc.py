def obtener_notas(estudiante, dict_notas):
    nota = dict_notas[estudiante]
    return nota

notas = {'Diego'    : 4.1
        ,'Francisca': 5.5
        ,'Daniela'  : 6.8
        ,'Leo'      : 3.9
        ,'Loreto'   : 7.0}

estudiante='Loreto'

 #Llamo a la funcion 
nota = obtener_notas(estudiante, notas)

print(estudiante, 'tiene un', nota)
