<div align="center">
<img src="logo_UDD_Facultad_Ingenieria.jpg" style="float: center; height: 60px;" >
</div>

<h4 align="center">Taller de Programación</h4>
<h4 align="center">Examen</h4>
<h5 align="center">3 de Diciembre de 2019</h5>
**Instrucciones:**

- Lea atentamente el enunciado de cada uno de los problemas.
- Elija solo **TRES** de los CUATRO problemas del examen.
- Para cada problema cree un archivo.py distinto. El nombre del archivo debe ser el número del problema (uno.py, dos.py o tres.py)
- Comprima los problemas en un solo archivo **ZIP** y subalo a la sección Evaluación en [http://canvas.udd.cl](http://canvas.udd.cl). Solo tiene una oportunidad para subir sus respuestas.
- Recuerde que usaremos un software de detección de plagio para detectar copia.

<div style="page-break-after: always;"></div>
**(2pts) Problema 1.  Trabajando con Fechas**

Su primera tarea en su nuevo trabajo como Data Scientist es crear un código que trabaje con las fechas de las próximas reuniones a realizarse en su empresa, creando funciones que cumplan los siguientes requisitos:

- Programe la funcion `fecha_tupla` que recibe una fecha en el formato `'dd-mm-aaaa'` y devuelve la fecha de tipo tupla `('dd','mm','aaaa')`.
  ​

- Programe la funcion `fecha_string` que recibe una fecha de tipo tupla `('dd','mm','aaaa')` y retorna la fecha en el formato `'dd-mm-aaaa'`.
  ​

- Programe la funcion `comparar_fechas(fecha1,fecha2)` que recibe dos fechas de tipo tupla `('dd','mm','aa')` y retorna `2` si `fecha1` > `fecha2`, `1` si `fecha1` < `fecha2` y `0` si `fecha1`=`fecha2`.



**Hint:** Una manera eficiente de comparar fechas es primero comparar los años, luego si estos son iguales entonces comparar los meses y si estos tambien son iguales entonces comparar los días.

Todo lo anterior debe estar plasmado en un programa que solicite al usuario la función que desea ejecutar, **por ejemplo**:

```tex
¿Qué desea hacer?
1. Transformar fecha a tupla
2. Comparar fechas
Seleccione una opción: _ 
```

```python
def fecha_tupla(fecha):
    dd=fecha[0:2]
    mm=fecha[3:5]
    aa=fecha[6:10]
    
    return (dd,mm,aa)
    
def fecha_string(fecha):
    dd=fecha[0]
    mm=fecha[1]
    aa=fecha[2]
    
    return dd + '-' + mm + '-' + aa
    
 def comparar_fechas(fecha1,fecha2):
    ano1=fecha1[2]
    ano2=fecha2[2]
    
    mes1=fecha1[1]
    mes2=fecha2[1]
    
    dia1=fecha1[0]
    dia2=fecha2[0]
    
    if ano1>ano2:
        return 2
    
    elif ano1<ano2:
        return 1
    
    else:
        if  mes1> mes2:
            return 2
        
        elif mes1< mes2:
            return 1
        
        elif mes1==mes2:
            if dia1>dia2:
                return 2
            
            elif dia1<dia2:
                return 1
            
            else:
                return 0  
                
s=int(input('Que desea hacer?, seleccione 1 o 2'))

if int(s)==1:
    f=input('Ingrese fecha ')
    print(fecha_tupla(f))
           
if int(s)==2:
    f1=input('Ingrese fecha 1 ')
    f2=input('Ingrese fecha 2 ')
    
    f11=fecha_tupla(f1)
    f22=fecha_tupla(f2)
    
    print(comparar_fechas(f11,f22)) 


```

```tex
0.5 pts. Programar la funcion fecha_tupla correctamente
0.5 pts. Programar la funcion fecha_string correctamente
0.7 pts. Programar la funcion comparar_fecha correctamente
0.3 pts. Incluir menu
```
