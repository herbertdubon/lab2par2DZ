
import errno
import os

while 1:
    print('Seleccione una opcion para continuar: ')
    print('1. Especifique el nombre de archivo para procesar su contenido: ')
    print('2. Salir del programa')
    opcion = int(input('\nCuál opcion desea realizar?\n'))
    
    if opcion == 1:
        archivo = input('\nIngrese el nombre del archivo: ')
        try:
            with open(archivo) as archivo:  
                print('El archivo ingresado se ha podido leer satisfactoriamente. ')
                contenido = archivo.read()
                #print(contenido)
                numero_caracteres = len(contenido)
                print('Hay {} caracteres en el archivo de texto.\n'.format(numero_caracteres))
                menu = input('\nDesea analizar otro archivo? (s/n)')
                if menu== "n":
                    break                       
        except FileNotFoundError:
            print('No existe el archivo {} en la carpeta.\n'.format(archivo))
            menu = input('\nDesea analizar otro archivo? (s/n)')
            if menu== "n":
                break