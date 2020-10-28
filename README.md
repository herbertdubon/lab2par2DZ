# lab2par2DZ
Laboratorio 2 Sistemas Expertos
<<<<<<< HEAD
ESCENARIO LABORATORIO:
Una institución esta utilizando una serie de técnicas y herramientas de Inteligencia Artificial
para el desarrollo de un traductor en tiempo real de conversaciones, actualmente se están
recolectando archivos conteniendo palabras de distintos idiomas.
Se le ha encomendado a Ud. desarrollar un programa en Python que cumpla con los siguientes
requerimientos.

Parcial 2:
1. Mostrar en pantalla que el usuario tiene 2 opciones:
- Especificar nombre de archivo y procesar su contenido
- Salir del programa
2. Si el usuario elige la primera opción se debe capturar el nombre del archivo, informar al
usuario que se pudo leer o no la entrada de datos; en caso que la fuente de datos no pudo
leerse informar al usuario que vuelva a intentar y se regresa al menu de opciones principal.
3. El nombre del archivo debe ser enviado al programa de procesamiento de contenido como
un parámetro.
4. Leer archivos en texto sin importar la extensión de éste (json, txt, sin extensión, otros).
5. Informar al usuario de los siguientes resultados en base al archivo facilitado por el usuario:
a) Número de caracteres (se incluyen espacios en blanco)
b) Número de palabras (separados por espacios en blanco)
c) Número de líneas
d) Número de palabras únicas (“NO” es diferente de “no”)
6. Optimizar su solución del laboratorio 2 haciendo énfasis en los elementos técnicos que han
facilitado la nueva propuesta, éstos pueden ser: funciones, librerías, estructuras de datos y
otros. El enfoque de optimización puede ser en: disminuir el tiempo de ejecución, mejorar
la exactitud de los resultados, disminuir líneas de código fuente o todos los anteriores .
7. Se requiere aplicar todos los estándares de buenas prácticas de codificación desarrollados
en las sesiones de trabajo de la unidad 2.
9. Para el seguimiento a su propuesta técnica deberá crear un repositorio denominado
“lab2par2”+iniciales de sus apellidos (ejemplo: lab2par2FT; la estructura de éste debe ser:
• Desarrollo2: contiene el codigo fuente y archivos de entrada de datos solicitados en el
numeral 6.
• Todo el repositorio junto con todo su contenido debe cumplir con el estándares de
buenas prácticas desarrollados en las sesiones de trabajo de la unidad 2.
• La última transacción en la rama y en el repositorio no debe exceder la fecha y hora
límite de entrega de la presente guía de trabajo. En caso que no se siga esta indicación se
asignará la calificación de 0.0 a todo el trabajo presentado.
• Si se comprobó la optimización “desarrollo2” debe consolidarse con la rama “master”.
10. Elaborar un video con una duración igual o mayor a 5 minutos donde explique el
pseudocodigo o flujograma de la lógica de negocios (solicitado en el numeral 6), la
creación de la rama “desarrollo2”, actualización de la misma (mostrar cuantas
transacciones se realizaron), consolidación con la rama master (en caso que se optimizó la
solución) y características del código fuente (enfocarse en las buenas prácticas y lógica de
negocios).
En el video debe demostrarse el proceso de análisis de 2 archivos distintos y el resultado
obtenido por medio de su solución. Se sugiere que sean los mismos archivos utilizados en
el laboratorio 2 para mostrar la diferencia de resultados en términos de optimización.
Al inicio del video debe mostrarse claramente su rostro en vivo, presentarse y hacer
mención que el video es relacionado a la resolucion del parcial2 de la materia de sistemas
expertos.
11. Deberá entregar por medio del aula virtual de la UEES, en el espacio de la materia Sistemas
Expertos, en el link de la pestaña “octubre” denominado “repeticion lab2-parcial2” un
archivo de texto con el nombre <APELLIDOS>_PAR2.TXT
(FERNANDEZTAMAYO_PAR2.TXT), este archivo debe contener:
• link de repositorio solicitado en esta guía de trabajo (el link debe apuntar a la rama
master del repositorio)
• link del video solicitado en el numeral 10
12. No se aceptarán entregas fuera de la fecha y hora estipulada, el medio de recepción es
exclusivamente por medio del aula virtual de la Universidad Evangélica.
  
# Explicación del código:

## Librerías utilizadas
import sys (Se Se ocupa sys para generar una función que salga del programa) 
import numpy as np (Se ocupa numpy para crear el array donde se analizaran los valores únicos.
import time (Se ocupa para medir el tiempo de ejecución del programa)

## Funcion Salir
#Se creo función salir para cerrar el programa
def salir():
    sys.exit()

## Funcion inputNumero
#Se creo la funcion inputNumero para el ingreso por teclado de la opcion    
def inputNumero(opcion):
    while True: 
        try:
            numero = float(input(opcion))
            break
        except ValueError:
            print("Favor ingresar una opcion válida.")
            pass        
    return numero

##Funcion Menu
#Se creo la función de menu con las opciones que el usuario puede elegir. 
#Al final se le envia la opcion elegida a la función lectura. 
def menu(opciones):
    for i in range(len(opciones)):
        print("{:d}. {:s}".format(i+1, opciones[i]))

    eleccion = 0
    while not (np.any(eleccion == np.arange(len(opciones))+1)):
        eleccion = inputNumero("Favor elija una opcion: ")    
        lectura(eleccion)          

##Funcion Lectura
#Se creo la función lectura a la cual se le pasa el parametro de la 
#opcion elegida. Si es 1 procede a la lectura del archivo y si es 2 se
#sale del programa. A la función resultados se le pasa el parametro del
#nombre_archivo digitado por el usuario. 
def lectura(eleccion):
    try:
        while True:
            if eleccion == 1:      
                nombre_archivo = input('\nIngrese el nombre del archivo: ')
                resultados(nombre_archivo)
            elif eleccion == 2:
                salir()
    #Si no encuentra el nombre del archivo devuele un mensaje de error.         
    except FileNotFoundError:
        print('El archivo no existe en la carpeta')
        lectura(1)                               
    
    #Si el usuario escribe una opcion no valida devuelve mensaje error.        
    except ValueError:
        print('Opción digitada no válida')
        lectura(1)

##Funcion Resultados
#Se crea la fución resultados a la cual se le pasa el parametro del 
#nombre del archivo y se procesan los 4 resultados solicitados.
def resultados(nombre_archivo):
    while True:
        #Se inicia el tiempo de ejecucion del programa
        inicio = time.time()
        
        #El programa soporta la lectura de archivos json, txt, sin 
        #nombre de extensión y otros.         
        with open(nombre_archivo) as nombre_archivo: 
            contenido = nombre_archivo.read() 
            print("""El nombre_archivo ingresado se ha podido leer \
satisfactoriamente.\n""")
            #Numero de caracteres que hay en el archivo ingresado
            numero_caracteres = len(contenido)
            print('Hay {} caracteres en el archivo de texto.'
            .format(numero_caracteres))
        
            #Numero de palabras que hay en el archivo ingresado
            numero_palabras = contenido.split()
            print('Hay {} palabras en el archivo de texto.'
            .format(len(numero_palabras)))
        
            #Numero de lineas que hay en el archivo
            numero_lineas = len(contenido.splitlines())
            print('Hay {} lineas en el archivo de texto.'
            .format(numero_lineas)) 
            
            #Numero de palabras unicas que hay en el archivo 
            arrayPalabras = np.array(numero_palabras)            
            palabras_unicas, conteo_unicas = np.unique(arrayPalabras, 
            return_counts=True)
            print('Hay {} nombres unicos en el archivo de texto.'
            .format(np.asarray(len(palabras_unicas))))

            #Tiempo de ejecución programa finaliza
            print('Duracion: {} segundos'.format(time.time() - inicio))  

            #Consulta por si el usuario desea analizar otro archivo. 
            otroArchivo = input('\nDesea analizar otro archivo? (s/n)')
            if otroArchivo == "s":
                lectura(1)                              
            elif (otroArchivo == "n"):
                salir()  
=======

Este repositorio es para entrega la resolución del laboratorio y parcial 2 de Sistemas Expertos. 
La rama desarrollo1 contiene todo el código y archivos solicitados en el laboratorio 2. 
El link para acceder a la rama de desarrollo1 es:

https://github.com/herbertdubon/lab2par2DZ/tree/desarrollo1

La rama desarrollo2 contiene todo el codigo y archivos solicitados en el parcial 2. 
https://github.com/herbertdubon/lab2par2DZ/tree/desarrollo2

>>>>>>> 702f145da61458e4e4f273da456d75d5d30f1722
