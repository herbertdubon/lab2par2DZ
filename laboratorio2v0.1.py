
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
                print('El archivo ingresado se ha podido leer satisfactoriamente.\n')
                contenido = archivo.read()
                
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
                nombres = []
                nombres_unicos = []
                for i in lineas:
                    nombres.append(i)
                for j in nombres:
                    if j not in nombres_unicos:
                        nombres_unicos.append(j)
                count = 0
                for k in nombres_unicos:
                    count += 1
                print('Hay {} nombres unicos en el archivo de texto.'.format(count))                       
                menu = input('\nDesea analizar otro archivo? (s/n)')
                if menu== "n":
                    break                       
        except FileNotFoundError:
            print('No existe el archivo {} en la carpeta.\n'.format(archivo))
            menu = input('\nDesea analizar otro archivo? (s/n)')
            if menu== "n":
                break