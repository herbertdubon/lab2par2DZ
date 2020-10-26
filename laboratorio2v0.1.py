
import sys
from tqdm import tqdm
import time as time

#Se creo función salir para cerrar el programa
def salir():
    sys.exit()

#Se creo la función de menu con las opciones que el usuario puede elegir. Al final se le envia la opcion elegida 
# a la función lectura. El programa soporta la lectura de archivos json, txt, sin nombre de extensión y otros.  
def menu():
    print("""
    Seleccione una opcion para continuar:
    1. Especifique el nombre de archivo para procesar su contenido incluyendo su extensión (Ej: archivo.txt) 
    2. Salir del programa
        """)
    opcion = int(input('\nCuál opcion desea realizar?\n'))
    lectura(opcion)
    
#Se creo la función lectura a la cual se le pasa el parametro de la opcion elegida. Si es 1 procede a la lectura del
#archivo y si es 2 se sale del programa. A la función resultados se le pasa el parametro del nombre_archivo digitado por el usuario. 
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