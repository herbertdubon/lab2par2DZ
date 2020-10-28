from menu import *
import numpy as np

#Se crean opciones del menu solicitadas en el ejercicio
menuItems = np.array(["Procesar Archivo", "Salir"])

#se envia las opciones del menu como un array y se pasan como parametro 
# a la funcion menu. 
while True:
    eleccion = menu(menuItems);
    
    #Si la eleccion es 1 se envia el nombre del archivo a la funcion
    #lectura.
    if eleccion == 1:
        nombre_archivo = input("Escriba el nombre del archivo: ")
        lectura(nombre_archivo)
    
    #Si la eleccion es 2 se corre la funcion salir para cerrar el
    #programa.  
    elif eleccion == 2:
        salir()