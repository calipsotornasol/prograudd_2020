### PrograUDD Tarea 2

**Instrucciones**: Resuelva con un compañero/a la siguiente lista de ejercicios. Entregue sus respuestas en archivos `.py` separados, los cuales deben estar comprimidos en un `.zip` con el nombre `APELLIDO_Tarea2.zip`. 

Ustedes han sido contratados como analistas de datos para una empresa de comunicaciones que desea hacer seguimiento del COVID-19 en el país, y también en el mundo. Para esto, se solicita que programe ciertas funciones y determine ciertos indicadores. En el enunciado de Canvas para esta Tarea, usted encontrará dos archivos de trabajo, `WHO-COVID-19-global-data.csv` y `UCI_T.csv`:

El archivo `WHO-COVID-19-global-data.csv` contiene la evolución del número de contagiados de covid-19 por país. En este archivo encontramos los siguientes campos:

* `date_reported`: Contiene la fecha correspondiente a los datos. Esta fecha es de la forma AAAA-MM-DD e incluye la hora y zona horaria. Para efectos de esta tarea, ignore la hora y zona horaria.

* `country_code`: Contiene el código del país al que corresponden los datos.

* `country`: Nombre del país al que corresponden los datos.

* `who_region`: Región del planeta a la que pertenece el país de acuerdo a la OMS.

* `new_cases`: Número de casos nuevos a la fecha del registro.

* `cumulative_cases`: Número acumulado de casos a la fecha del registro.

* `new_deaths`: Número de muertes nuevas a la fecha del registro.

* `cumulative_deaths`: Número acumulado de muertes a la fecha del registro.

Con este archivo, se solicita que realice las siguientes actividades:

**1. Casos por pais.** Programe la función `casos_pais(file,country,fecha)` que recibe un archivo del tipo `WHO-COVID-19-global-data.csv`, el nombre de un país y una fecha, y retorne una tupla con el pais, la fecha y el respectivo número de contagiados de COVID-19.

**2. Ranking por país .**  Programe la función  `n_caos_pais(n,fecha,file)` que retorna los `n` paises con más contagiados para una fecha específica.

**3. Máximo de fallecidos.** Programe la funcion `max_fallecidos(file)` que retorna una tupla con el pais con más fallecidos y el número de fallecidos.

**4. Comparando la muerte en dos países.** Programe la función `compara_muerte_paises(pais1, pais2, fecha, file)` que recibe el nombre de dos países, una fecha específica, y el archivo, y retorna cual de los dos países tiene un mayor numero de muertes nuevas, y cual tiene un mayor número acumulativo de muertes para esa fecha.


El archivo `UCI_T.csv` contiene la serie de tiempo del número de pacientes COVID-19 en UCI por región. Cada columna corresponde a una región, la primera fila corresponde al `codigo region`, y la segunda fila corresponde al total de la `poblacion`. Con este archivo, realice las siguientes actividades:

**5. Internados por region.** Programe la funcion `internados_region(file)` que reciba como entrada el archivo `UCI_T.csv`y retorne un diccionario con el **último** número de internados en UCI por región. El último número corresponde al registro más reciente (última fila). Las llaves del diccionario deben ser los nombres de la región y los valores el número de internados.

**6. Analizando el número de internados en el tiempo.** En la compañía que usted trabaja, les interesa saber como ha ido creciendo el número de internados en cada región con respecto al tamaño de la población. Se solicita crear la función `porcentaje_poblacion(file, region)` que reciba el archivo `UCI_T.csv`y el nombre de una región, y que retorne la fecha y el porcentaje de internados con respecto a la población de esa región. Luego, se solicita que grafique este porcentaje en el tiempo para una región elegida por usted (utilice Excel para realizar este gráfico). Entregue un pdf  dentro de su archivo `.zip` que contenga el gráfico generado, además de su apreciación respecto al crecimiento o decrecimiento del número de internados con respecto al tiemp. **No olvide indicar cual es la región que graficó**.

