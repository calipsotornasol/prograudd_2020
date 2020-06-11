### PrograUDD Ayudantía 04

**Instrucciones**: Resuelva con un compañero/a la siguiente lista de ejercicios. Recuerde discutir la estrategia para resolver cada problema, y luego escribir el código solución. Suba su solución como un archivo `ay04_apellido1apellido2.py` a Canvas, Sección Tareas > Ayudantías. **Guarde una copia de su solución en Google Drive.**

**Para cada ejercicio escriba un comentario al inicio de su código declarando la entrada y salida de cada uno de los problemas.**

Un ejemplo simple: Si el ejercicio le pide calcular e imprimir la variable `v_suma` que representa la suma de dos números `a` y `b`, enteros y positivos, el comentario debe ser:

**Entrada:** Dos números, a y b, enteros y positivos ingresados por teclado.
**Salida:** Impresión de la variable `v_suma`

**1. Rectángulo.** Escriba una funcion que permita dibujar un rectángulo en pantalla, siendo los argumentos de la función el número de caracteres de la base, el número de caracteres de la altura y el caracter con que se dibuja. Considere los caracteres `" %, & , * `.

**2. Números aleatorios.** Escriba un programa que genere 100 número aleatorios de 1 a 10 e imprima el número de pares y tríos que existen para un número `n` ingresado por el usuario.

**3. Movimiento rectilineo uniforme.** Escriba una función que permita calcular la velocidad de un automóvil ingresando la distancia recorrida en kilómetros y el tiempo en minutos que se demoró en llegar al destino.

**4. Cálculo de la UF.** Cree una función que permita calcular el valor en UF de un monto dado dependiendo del valor de la UF del día para el mes de septimebre. La función debe recibir como argumento el día y el monto a calcular. Utilice la siguiente tabla como base para el cálculo.

<center>

|  Día | Valor [pesos]  | Día | Valor [pesos]    | Día | Valor [pesos]   |
|  --- |  ---     | --- |    ---   | --- | ---      |
| 1    | 27.994,89| 11  | 28.013,06| 21  | 28.031,72|
| 2    | 27.996,69| 12  | 28.014,93| 22  | 28.033,59|
| 3    | 27.998,50| 13  | 28.016,79| 23  | 28.035,46|
| 4    | 28.000,30| 14  | 28.018,66| 24  | 28.037,33|
| 5    | 28.002,11| 15  | 28.020,52| 25  | 28.039,19|
| 6    | 28.003,91| 16  | 28.022,39| 26  | 28.041,06|
| 7    | 28.005,72| 17  | 28.024,26| 27  | 28.042,93|
| 8    | 28.007,52| 18  | 28.026,12| 28  | 28.044,80|
| 9    | 28.009,33| 19  | 28.027,99| 29  | 28.046,66|
| 10   | 28.011,20| 20  | 28.029,86| 30  | 28.048,53|

</center>

**5. OGame.** OGame es un juego de estrategia de mutijugadores masivos en linea en donde al inicio cada jugador controla un planeta y asume el rol de emperador. A medida que avanza el juego los emperadores, utilizando diferentes recursos, pueden colonizar y tomar el control de otros planetas.

OGame permite desarrollar diferentes estrategias para obtener recursos e invertirlos de manera más eficiente. Una de las formas de obtener recursos es mediante la utilización de minas y sintetizadores de deuterio que pueden construirse en los planetas que el jugador controla.

Genere un programa que **calcule e imprima la producción** de una mina de metal, cristal y un sintetizador de deuterio, **por hora y para un nivel específico** utilizando las siguientes fórmulas:

- Mina de Metal

Producción = $30\cdot nivel \cdot 1.1^{nivel}$

- Mina de Cristal

Producción = $20\cdot nivel \cdot 1.1^{nivel}$

- Sintetizador de Deuterio

Producción = $10 \cdot nivel\cdot1.1 ^{nivel}\cdot(1.44 - 0.004 \cdot t_{max}) \cdot v_{universo}$

, donde $t_{max}$ es la temperatura máxima del planeta y  `v_universo` es la velocidad del universo.

Para `t_max` utilice un valor aleatorio entre 10 y 30 y para `v_universo` considere un valor aleatorio entre 1 y 5. Su programa debe incluir una función para cada mina y el sintetizador de deuterio.

**6. Tabla de Multiplicar.** Programe una función  que imprima en pantalla la tabla de multiplicar para un número entero  `n` entre 1 y 20.

**7. Validaciones.** Escriba un programa utilizando funciones tal que este permita validar si un número `n` ingresado por teclado es mayor que 0 y menor a 11 y si un texto ingresado tiene un largo mínimo superior a 7 carácteres sin considerar los espacios. 

