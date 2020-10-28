# lab2par2DZ
Laboratorio 2 Sistemas Expertos
<<<<<<< HEAD
ESCENARIO LABORATORIO:
Una institución esta utilizando una serie de técnicas y herramientas de Inteligencia Artificial
para el desarrollo de un traductor en tiempo real de conversaciones, actualmente se están
recolectando archivos conteniendo palabras de distintos idiomas.
Se le ha encomendado a Ud. desarrollar un programa en Python que cumpla con los siguientes
requerimientos.

LABORATORIO 2:
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
6. Codificar la solución utilizando estructuras de control y estructuras de datos de su elección,
debe informarse al usuario sobre el tiempo de ejecución utilizado hasta mostrar los
resultados especificados en el numeral 5. Se sugiere que su solución sea desarrollada en
ambiente de consola.
7. Se requiere aplicar todos los estándares de buenas prácticas de codificación desarrollados
en las sesiones de trabajo de la unidad 2.
9. Para el seguimiento a su propuesta técnica deberá crear un repositorio denominado
“lab2par2”+iniciales de sus apellidos (ejemplo: lab2par2FT; la estructura de éste debe ser:
- Desarrollo1: contiene el codigo fuente y archivos de entrada de datos solicitados en el
numeral 6.
- Todo el repositorio junto con todo su contenido debe cumplir con el estándares de
buenas prácticas desarrollados en las sesiones de trabajo de la unidad 2.
- La última transacción en la rama y en el repositorio no debe exceder la fecha y hora
límite de entrega de la presente guía de trabajo. En caso que no se siga esta indicación se
asignará la calificación de 0.0 a todo el trabajo presentado.
10. Elaborar un video con una duración igual o mayor a 5 minutos donde explique el
pseudocodigo o flujograma de la lógica de negocios (solicitado en el numeral 6), la
creación de la rama “desarrollo1”, actualización de la misma (mostrar cuantas
transacciones se realizaron) y características del código fuente (enfocarse en las buenas
prácticas y lógica de negocios).
En el video debe demostrarse el proceso de análisis de 2 archivos distintos y el resultado
obtenido por medio de su solución.
Al inicio del video debe mostrarse claramente su rostro en vivo, presentarse y hacer
mención que el video es relacionado a la resolucion del laboratorio2 de la materia de
sistemas expertos.
11. Deberá entregar por medio del aula virtual de la UEES, en el espacio de la materia Sistemas
Expertos, en el link de la pestaña “octubre” denominado “repeticion lab2-parcial2” un
archivo de texto con el nombre <APELLIDOS>_LAB2.TXT
(FERNANDEZTAMAYO_LAB2.TXT), este archivo debe contener:
- link de repositorio solicitado en esta guía de trabajo (el link debe apuntar a la rama
master del repositorio)
- link del video solicitado en el numeral 10
12. No se aceptarán entregas fuera de la fecha y hora estipulada, el medio de recepción es
exclusivamente por medio del aula virtual de la Universidad Evangélica.
  
# Explicación del código:

## Librerías utilizadas
import sys (Se ocupa sys para generar una función que salga del programa)
from tqdm import tqdm (Se ocupa tqdm para generar una barra de progreso para los analisis de archivos grandes y poder ver su status de progreso)
import time as time (Se ocupa para medir el tiempo de ejecución del programa)

## Funcion para salir del programa
def salir():
    sys.exit()

#Se creo la función de menu con las opciones que el usuario puede elegir. Al final se le envia la opcion elegida 
#a la función lectura. 
def menu():
    print("""
    Seleccione una opcion para continuar:
    1. Especifique el nombre de archivo para procesar su contenido incluyendo su extensión (Ej: archivo.txt): 
    2. Salir del programa
        """)
    opcion = int(input('\nCuál opcion desea realizar?\n'))
    lectura(opcion)
## Funcion de Lectura del archivo    
#Se creo la función lectura a la cual se le pasa el parametro de la opcion elegida. Si es 1 procede a la lectura del
#archivo y si es 2 se sale del programa. A la función resultados se le pasa el parametro del nombre_archivo digitado por el usuario. 
def lectura(opcion):
    try:
        while True:
            if opcion == 1:      
                nombre_archivo = input('\nIngrese el nombre del archivo: ')
                resultados(nombre_archivo)
                print('El nombre_archivo ingresado se ha podido leer satisfactoriamente.\n')
            else:
                salir()
    ## Se capturan los posibles errores de lectura del programa    
    except FileNotFoundError:
        print('El archivo no existe en la carpeta')
        opcion = input('\nDesea analizar otro archivo? (s/n)')
        if opcion == "s":
            menu()                               
        elif (opcion == "n"):
            salir()
            
    except ValueError:
        print('Opción digitada no válida')
        opcion = input('\nDesea analizar otro archivo? (s/n)')
        if opcion == "s":
            menu()                               
        elif (opcion == "n"):
            salir()

## Funcion de proceso de resultados
#Se crea la fución resultados a la cual se le pasa el parametro del nombre del archivo y se procesan los 4 resultados solicitados.
def resultados(nombre_archivo):
    while True:                   
        with open(nombre_archivo) as nombre_archivo:  
            inicio = time.time()            
            #La variable contenido hace referencia a la información dentro del archivo de texto.
            contenido = nombre_archivo.read()
            print('El nombre_archivo ingresado se ha podido leer satisfactoriamente.\n')
            
        #Numero de caracteres que hay en el archivo ingresado
        numero_caracteres = len(contenido)
        print('Hay {} caracteres en el archivo de texto.'.format(numero_caracteres))
        
        #Numero de palabras que hay en el archivo ingresado
        numero_palabras = contenido.split()
        print('Hay {} palabras en el archivo de texto.'.format(len(numero_palabras)))
        
        #Numero de lineas que hay en el archivo
        numero_lineas = len(contenido.splitlines())
        print('Hay {} lineas en el archivo de texto.'.format(numero_lineas)) 
        
        #Numero de palabras unicas que hay en el archivo
        lineas = contenido.split()
        palabras = []
        palabras_unicas = []
        for i in (lineas):
            palabras.append(i)
        for j in tqdm(palabras):
            if j not in palabras_unicas:
                palabras_unicas.append(j)
        print('Hay {} nombres unicos en el archivo de texto.'.format(len(palabras_unicas)))
        
        #Tiempo de ejecución programa
        print('Duracion: {} segundos'.format(time.time() - inicio))                       
        
        opcion = input('\nDesea analizar otro archivo? (s/n)')
        if opcion == "s":
            menu()                               
        elif (opcion == "n"):
            salir()            
menu()  
=======

Este repositorio es para entrega la resolución del laboratorio y parcial 2 de Sistemas Expertos. 
La rama desarrollo1 contiene todo el código y archivos solicitados en el laboratorio 2. 
El link para acceder a la rama de desarrollo1 es:

https://github.com/herbertdubon/lab2par2DZ/tree/desarrollo1
>>>>>>> 702f145da61458e4e4f273da456d75d5d30f1722
