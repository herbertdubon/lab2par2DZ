import sys
import time as time
import numpy as np
import menu

#Se creo función salir para cerrar el programa
def salir():
    sys.exit()

"""Se creo la función de menu con las opciones que el usuario puede
elegir. Al final se le envia la opcion elegida a la función lectura.
El programa soporta la lectura de archivos json, txt, sin nombre de 
extensión y otros.""" 
menuItems = np.array(["Procesar Archivo", "Salir"])
while True:
    eleccion = menu(menuItems);
    if eleccion == 1:
        archivo = input("Escriba el nombre del archivo: ")
        lectura(archivo)    
    elif eleccion == 2:
        break
    
"""Se creo la función lectura a la cual se le pasa el parametro de la
opcion elegida. Si es 1 procede a la lectura del #archivo y si es 2 se
sale del programa. A la función resultados se le pasa el parametro del 
nombre_archivo digitado
por el usuario.""" 
def lectura(opcion):
    try:
        while True:
            if opcion == 1:      
                nombre_archivo = input('\nIngrese el nombre del archivo: ')
                resultados(nombre_archivo)
            else:
                salir()
        
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

"""Se crea la fución resultados a la cual se le pasa el parametro del 
nombre del archivo y se procesan los 4 resultados solicitados."""
def resultados(nombre_archivo):
    while True:
        inicio = time.time()        
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

            #Tiempo de ejecución programa
            print('Duracion: {} segundos'.format(time.time() - inicio))  

            #Consulta por si el usuario desea analizar otro archivo. 
            #Esta opción lo regresa al menu principal de
            opcion = input('\nDesea analizar otro archivo? (s/n)')
            if opcion == "s":
                menu()                               
            elif (opcion == "n"):
                salir()    
menu()  

