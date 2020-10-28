import sys
import numpy as np
import time

def salir():
    sys.exit()
    
def inputNumero(opcion):
    while True: 
        try:
            numero = float(input(opcion))
            break
        except ValueError:
            print("Favor ingresar una opcion válida.")
            pass        
    return numero

def menu(opciones):
    for i in range(len(opciones)):
        print("{:d}. {:s}".format(i+1, opciones[i]))

    eleccion = 0
    while not (np.any(eleccion == np.arange(len(opciones))+1)):
        eleccion = inputNumero("Favor elija una opcion: ")    
        lectura(eleccion)          

def lectura(eleccion):
    try:
        while True:
            if eleccion == 1:      
                nombre_archivo = input('\nIngrese el nombre del archivo: ')
                resultados(nombre_archivo)
            else:
                break
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
    



