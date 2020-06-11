<div align="center">
<img src="logo_UDD_Facultad_Ingenieria.jpg" style="float: center; height: 60px;" >
</div>

<h4 align="center">Taller de Programación</h4>
<h4 align="center">Certamen 1</h4>
<h5 align="center">10 de Septiembre de 2019</h5>

**Instrucciones:**

- Lea atentamente el enunciado de cada uno de los problemas.
- Elija solo **TRES** de los CUATRO problemas del certamen.
- Para cada problema cree un archivo.py distinto. El nombre del archivo debe ser el número del problema (uno.py, dos.py, tres.py o cuatro.py)
- Comprima los problemas en un solo archivo **ZIP** y subalo a la sección Evaluación en [http://canvas.udd.cl](http://canvas.udd.cl). Solo tiene una oportunidad para subir sus respuestas.
- Recuerde que usaremos un software de detección de plagio para detectar copia.
<div style="page-break-after: always;"></div>


#### 1. Entradas Lollapalooza (2 pts) 

Escriba un programa que simule la compra de entradas para 
el Lollapalooza. Para esto considere que el precio de la entrada 
depende de la fecha (mes) en que se compra la entrada y del tipo de entrada a comprar (pase diario o pase valido para los tres dias que dura el evento) y que además se pueden incluir el servicio adicional de estacionamiento.

El programa debe recibir el mes en que se relizará la compra,
el numero de días que asistirá al evento, el número de entradas a comprar, preguntar si se desea incluir estacionamiento e imprimir el valor total de la compra.

Considere que los precios de las entradas de acuerdo a la fecha se distribuyen según la tabla adjunta y que el cargo por el servio extra de estacionamiento es \$5.000 por día.

<center>

|   |FECHA | Pase diario | Pase para 3 días | 
|---|---   | ---   | ----| 
| EARLY BIRD | Agosto| | \$85.000 | 
| PREVENTA 1 | Septiembre-Octubre|  | \$140.000 |
| PREVENTA 2| Noviembre-Enero| \$85.000| \$180.000 | 
| ENTRADA GENERAL| Febrero-Marzo| \$100.000 | \$250.000 |

</center>
 
**NOTA:**

- Asuma que NO HAY un máximo de entradas disponibles para ninguna fecha de compra.

<div style="page-break-after: always;"></div>

#### 2. Serie (2 pts)

Escriba un programa  que reciba un numero $x_0$ a través del teclado e imprima una serie de números donde el valor del número $x_{i+1}$ de la serie depende del valor del numero anterior $x_{i}$ según las siguientes reglas:  

 - Cuando $x_i$ es **par**, el siguiente número de la serie es $x_i/2$
 - Cuando $x_i$ es **impar**, el siguiente número la serie es $3x_i+1$
 
El programa debe parar cuando $x_i$ sea igual a 1

**EJEMPLO**: 

Si el numero ingresado por teclado es 3 ($x_0=3$), el programa imprime `3, 10, 5, 16, 8, 4, 2, 1`.


#### 3. El poder del número 7 (2 pts)

Programe el juego 'El poder del 7'. El objetivo de este juego es imprimir todos los números entre 1 y x, donde x es ingresado por teclado, reemplazando con  el string `aplauso` todos los números que contengan el dígito 7 pero si el número contiene dos dígitos  iguales a 7, este debe ser reemplazado por un aplauso doble `aplauso aplauso`. 

#### 4. Verdulería (2 pts) 

La tienda de verduras y frutas `greenshop` ha iniciado la venta online de algunos de los productos de su catalogo. Por el momento, `greenshop` sólo vende frutas y verduras en paquetes de 1 kilogramo.

La tienda almacena los artículo disponibles y su precio en dos listas `tienda_articulo` y `tienda_precio`, donde la primera lista contiene el articulo disponible en la tienda y la segunda el valor de dicho producto para paquetes de 1 kilogramo.

Escriba un programa que simule la compra online la tienda de una persona cualquiera e imprima la boleta detallada de la compra (nombre del producto, precio del producto, cantidad y precio total de la compra). El programa debe recibir una lista de productos a comprar y una lista de la cantidad deseada de cada producto en kilogramos. Este debe funcionar aun cuando algunos elementos de la lista de compras deseada no existan en el catalogo del supermercado.

Para resolver el problema usted puede inventar su propia lista de compras o solicitarla lista a través del teclado.

Recuerde que para agregar un elemento `e` a una lista `L` puede utilizar la funcion `L.append(e)` y la funcion `L.index(e)` retorna la posición del elemento `e` en la lista `L`.

```python
super_articulo=['manzanas', 'peras, 'uva', 'papas', 'cebollas', 'tomates', 'paltas']
super_precio=['800', '1200', '500', '900', '800', '1500', '3000']


```

#### 4. Tweets (2 pts) 

Escriba un programa que reciba un texto y palabras clave separadas por comas a traves del teclado e imprima un **Tweet** siguiendo las siguientes reglas:

- Toda palabra del texto mayor a 4 letras debe ser acortada a las cuatro primeras 4 letras

- Las palabras acortadas deben reemplazar el ultimo caracter por el simbolo **@**

- Las palabras claves son ingresadas separadas por coma.

- Las palabras claves deben ser convertidas a hashtags agregando el simbolo # al inicio cada palabra clave

- El tweet final no debe sobrepasar los 154 caracteres 

**EJEMPLO**: 

Texto: "No quiero ser alarmista pero mi padre tiene una empresa de alarmas y seguridad y la voy a heredar."

Palabras clave: alarmas, seguridad

```python
** Su texto transformado es: **
No qui@ ser alar@ per@ mi pad@ tie@ una emp@ de #alarmas y #segurida y la voy a her@.
```


<div style="page-break-after: always;"></div>