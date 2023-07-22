
""" 
Crear array bidimensional para simular un estacionamiento de autos en una matriz (3x3) o de cualquier medida.

Debe contener un menú con las siguientes indicaciones:

1 = Guardar patente, marca y precio. Patente de 6 dígitos, marca de 2 a 15 dígitos y precio mayor a $5.000.000.
2 = Asignar estacionamiento. Se solicitará la patente del vehículo, y solo se asignará estacionamiento si este ya está registrado en el punto 1. El número de estacionamiento se asignará al azar y solo si aún hay espacio disponible. La patente del vehículo quedará guardada en el estacionamiento.
3 = Mostrar estacionamiento. Muestra el estado de los estacionamientos, viendo cuáles están vacíos y ocupados (con la patente correspondiente).
4 = Salir del menú.

"""

import funciones as fn
import numpy as np

filas=3   
columnas=3

# Estacionamiento vacío array bidimensional
estacionamiento = np.empty((filas,columnas), dtype= object)

# Llenando con números el estacionamiento
num = 0
for f in range(filas):
    for c in range(columnas):
        num+=1
        estacionamiento[f,c] = f"{num} : V "  # V = VACÍO / O = OCUPADO

print(estacionamiento)

patentes= []
marcas = []
precios= []

flag= True
while flag == True:
    
    print("\n===== MENÚ =====")
    print("1 = Guardar patente, marca y precio")
    print("2 = Asignar estacionamiento")
    print("3 = Mostrar estacionamiento")
    print("4 = Salir \n")
    
    try:
        option = int(input("Ingrese la opción deseada: "))        
        
        if option == 1:
            print("Guardar patente, marca y precio\n")
            
            flag_patente= False
            while flag_patente == False:
                p= input("Ingrese patente del vehículo de 6 dígitos: ")
                flag_patente, estado = fn.patente(p, patentes)  # Retornar múltiples valores desde una función y asignarlos a variables separadas.
                print(estado)
                           
            flag_marca= False
            while flag_marca == False:
                m= input("Ingrese marca del vehículo: ")
                flag_marca, estado = fn.marca(m, marcas)  
                print(estado)   
                             
            flag_precio= False
            while flag_precio == False:
                p= int(input("Ingrese precio del vehículo: "))
                flag_precio, estado = fn.precio(p, precios) 
                print(estado) 
            
            print("\nPatente, marca y precio ingresados correctamente al sistema \n")
       
         
        elif option == 2:
            print("Asignar estacionamiento")
            disp, estado = fn.disponibilidad(estacionamiento,filas,columnas)
            print(estado)
            
            if disp == True: 
                p= input("Ingrese patente del vehículo: ")
                print(fn.asignar(p,patentes,estacionamiento,filas,columnas)) 
    
        elif option ==3:
            print(estacionamiento)
        
        elif option == 4:
            print("Salir")
            flag= False 
            
        else:
            print("Ingrese un número en el rango de 1 y 4.")        
    except:
        print("Ingrese un dato válido.")    