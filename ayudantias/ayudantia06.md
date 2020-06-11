### PrograUDD Ayudantía 06

**Instrucciones**: Resuelva con un compañero/a la siguiente lista de ejercicios. Recuerde discutir la estrategia para resolver cada problema, y luego escribir el código solución. Suba su solución como un archivo `ay06_apellido1apellido2.py` a Canvas, Sección Tareas > Ayudantías. 
**Guarde una copia de su solución en Google Drive.** 

**Para cada ejercicio escriba un comentario al inicio de su código declarando la entrada y salida de cada uno de los problemas.**

**1. Contactos.** Cree una lista de diccionarios con datos suyos y de 4 compañeros más. Cada diccionario debe contener nombre, año de nacimiento y comuna donde vive. Luego cree un programa que imprima la cantidad de personas que tienen su misma edad y viven en su misma comuna (incluyéndolo).

**2. Planetas.** Cree un diccionario que; como llaves (key), contenga los nombres de cada planeta del sistema solar, y como valores (value), una tupla en la que el primer elemento sea la magnitud de su peso en dicho planeta y el segundo elemento sea el área de la superficie del planeta.
Para calcular la magnitud de su peso en cada  planeta del sistema solar y la respectiva área, su programa deberá leer el archivo `gravedad_planetas.txt`. Este archivo contiene en cada línea: el nombre del planeta, su magnitud de aceleración de gravedad (en $m/s^2$) y su radio (en Km), respectivamente.
Recuerde que el peso es una medida de la fuerza gravitatoria que actúa sobre un cuerpo, y su magnitud se calcula cómo $P=ma$; dónde $P$ es el peso, $m$ la masa del cuerpo y $a$ la aceleración de gravedad. Además, el área de la superficie de una esfera está dada por $A=4\pi r$, dónde $r$ es el radio de la esfera.

**Nota:** en este ejercicio no debe usar la función `input()` para ingresar información por el teclado. Debe hacer código que lea la información dentro del archivo `gravedad_planetas.txt`.

**3. Estadísticas Planetarias.** Programe una función que retorne el nombre del planeta en el cual su peso es menor y el área del planeta Tierra. Su función debe recibir como argumento el diccionario que creó en el ejercicio 2. 

**4. VIH en América Latina.** Cree una función que retorne de mayor a menor el número de personas viviendo con VIH en países de America Latina. La funcion debe utilizar tuplas de dos elementos, y
ordenarlos según el segundo elemento de la tupla. Utilice como fuente el archivo `people_living_with_hiv_regional.csv`.

**Hint**: Puede utilizar la función sort la función itemgetter del módulo operator.
