import sys
import numpy as np
import time

#Se creo función salir para cerrar el programa
def salir():
    sys.exit()
    
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

#Se creo la función de menu con las opciones que el usuario puede elegir. 
#Al final se le envia la opcion elegida a la función lectura. 
def menu(opciones):
    for i in range(len(opciones)):
        print("{:d}. {:s}".format(i+1, opciones[i]))

    eleccion = 0
    while not (np.any(eleccion == np.arange(len(opciones))+1)):
        eleccion = inputNumero("Favor elija una opcion: ")    
        lectura(eleccion)          

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
    




