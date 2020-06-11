### PrograUDD Ayudantía 05

**Instrucciones**: Resuelva con un compañero/a la siguiente lista de ejercicios. Recuerde discutir la estrategia para resolver cada problema, y luego escribir el código solución. Suba su solución como un archivo `ay05_apellido1apellido2.py` a Canvas, Sección Tareas > Ayudantías. **Guarde una copia de su solución en Google Drive.** 

**Para cada ejercicio escriba un comentario al inicio de su código declarando la entrada y salida de cada uno de los problemas.**

**1. Palindromo.** Programe una función que determine si una palabra es o no un palíndromo.

**2. Viaje por Santiago.** Cree la función `viaje(transporte,destino,profesion)` que recibe el tipo de `transporte` (`metro` o `micro`), el `destino` y la `profesion` de un usuario (`estudiante`, `no-estudiante`) y retorna la duración del viaje y el costo de este. Ingrese a <https://www.transantiago.cl/planifica> para ver la duración del viaje. Tiene que escoger al menos 4 destinos desde una ubicación a elección. Considere que si el usuario es estudiante, el valor de un viaje es `$220`, sino es `$680`.

**3. Cetáceos.** Chile es el segundo país con más especies de cetáceos en el mundo. El avistamiento de estas especies se puede realizar en todas las costas, pero para ello hay que seguir las distancias mínimas de observación y así proteger a nuestra fauna marina. Cree una función que al ingresar el `tipo` de cetáceo, retorne la distancia mínima para su observación. Para los cetáceos menores (`delfines` y `marsopas`) la distancia mínima es de 50m, para cetáceos mayores (`ballenas jorobadas`, `cachalotes`) es de 100m y para cetáceos gigantes (`ballenas azules`) es 300m. 

**4. Factorial.** Cree la función factorial y utilícela para crear la función combinatoria de n sobre k, dado un n y un k cualquiera. Recuerde que la combinatoria de n sobre k es: $$\frac{n!}{k!(n-k)!}$$


**5. Naipes.** Cree una función que escoja 12 cartas de un naipe inglés, entregando el número y la pinta de estas. Considere que existe solo un número de cada pinta, por lo que al escoger las 12 cartas no se pueden tener dos cartas iguales (mismo número y misma pinta).

**6. Carioca.** Utilizando la función anterior, cree el primer “round” del juego carioca entre 2 jugadores, en donde el jugador que tenga 2 trios gana. Si no existe un ganador, se volverá a realizar el “round”, por lo que se deben repartir las 12 cartas a cada jugador. 