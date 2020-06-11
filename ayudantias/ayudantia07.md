### PrograUDD Ayudantía 07

**Instrucciones**: Resuelva con un compañero/a la siguiente lista de ejercicios. Recuerde discutir la estrategia para resolver cada problema, y luego escribir el código solución. Suba su solución como un archivo `ay07_apellido1apellido2.py` a Canvas, Sección Tareas > Ayudantías. 

**1. Diario Secreto.**  Usted  tiene  acceso  al archivo `diario_secreto.txt`, el diario secreto  de  la  persona  más  chismosa  de  su clase y el cual contiene una lista de todos sus compañeros de clase y el nombre de la persona que les gusta separados por `,`. Programe un código que lea el diario secreto e imprima el número de personas que son correspondidas. Dos personas se  consideran  correspondidas  si  ambas  se  gustan  mutuamente.  Ejemplo:

Utilizando como output el archivo `diario_secreto.txt`

```python
Alavaro, Carla
Esteba, Andrea
Andrea, Julio
Julio, Esteban
Carla, Alvaro
```

Se obtiene como output:

`
2
`

**2. Notas programación** Utilizando el archivo `notas_prograudd.txt`, que contiene el promedio final del curso para cada estudiante, programe la función `notas_max(file)` que  recibe un archivo del estilo `notas_prograudd.txt` y retorna el nombre del estudiante o los estudiantes que obtuvieron la nota máxima. 

**3. Pandemia.** El archivo `WHO-COVID-19-global-data.csv` contiene la evolución del número de contagiados de covid-19 por país. Programe la función `max_pais(file, fecha)` que  recibe un archivo del tipo `WHO-COVID-19-global-data.csv` y una fecha en el formato `AAAA-MM-DD` y retorna el país con más personas contagiados con covid-19 (contagiados acumulados) para una fecha específica.

**4. Positividad covid-19.** El archivo `2020-06-01-CasosConfirmados-totalRegional.csv` contiene el número de casos confirmados de covid-19 para Chile por región del día `2020-06-01` y el archivo `pcr.csv` contiene el número de tests PCR realizado por región por día. Programe la función `positividad(file1, file2)` que recibe los archivos anteriormente descritos y devuelve un archivo nuevo llamado `positividad.csv`, el que contiene el nombre de la región, el número de tests PCR realizados, el número de tests positivos y la positividad (el número de casos positivos dividido por el número de tests realizados) para el último día registrado en el archivo, tal como se muestra a continuación:

```python
Arica y Parinacota,0,13,0.00
Tarapaca,445,152,34.16
Antofagasta,247,67,27.13
Atacama,289,8,2.77
Coquimbo,177,33,18.64
Valparaiso,587,166,28.28
Metropolitana,11285,4436,39.31
O'Higgins,196,23,11.73
Maule,0,37,0.00
Nuble,639,32,5.01
Biobio,1295,75,5.79
Araucania,491,34,6.92
Los Rios,114,5,4.39
Los Lagos,994,0,0.00
Aysen,24,0,0.00
Magallanes,107,1,0.93
```


