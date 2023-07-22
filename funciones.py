
import random

#Guardar patente
def patente(p, patentes):   
    estado = ""     
    
    if len(p) == 6:
        patentes.append(p)
        estado = (f"Patente {p} ingresada correctamente")
        return True, estado
    else:
        estado = (f"La patente debe tener 6 dígitos.")
        return False, estado
    
    
#Guardar marca
def marca(m, marcas):
    estado = ""
    
    if len(m) >= 2 and len(m) <= 15:
        marcas.append(m)
        estado = (f"Marca {m} ingresada correctamente")
        return True, estado
    else:
        estado = (f"Marca debe tener entre 2 y 15 digitos")
        return False, estado

  
#Guardar precio            
def precio(p, precios):
    estado = ""
    
    if p > 5000000:
        precios.append(p)
        estado = (f"Precio ${p} ingresado correctamente")
        return True, estado
    else:
        estado = (f"Precio debe ser superior a $5.000.000")
        return False, estado
    
    
#Verificar si el array estacionamiento tiene espacio o no para recibir nuevos autos
def disponibilidad(estacionamiento,filas,columnas):
    
    for f in range(filas):
        for c in range(columnas):
            posicion = estacionamiento[f,c]
            if posicion[4]  == "V":
                estado= "Hay disponibilidad"
                return True, estado
            
    estado= "Estacionamiento lleno"
    return False, estado


#Asignar patente a un estacionamiento
def asignar(p,patentes,estacionamiento,filas,columnas):
    estado=""    
    for i in patentes:
        if p == i: #Validar que la patente ingresada ya haya sido registrada    
                   
            flag= False
            while flag == False: #se iterara el bucle hasta encontrar un asiento vacio al azar                
                #Se genaran numeros random para la fila y columna       
                azar_fila = random.randint(0,filas -1)
                azar_columna = random.randint(0,columnas-1)                               
                posicion_random = estacionamiento[azar_fila, azar_columna] #posicion random dentro del array estacionamiento
                if posicion_random[4] == "V":      #si  esta vacio la posicion_random, se asigna el estacionamiento, si no, se vuelve a iterar el while hasta encontrarlo              
                    copia_estacionamiento = estacionamiento[azar_fila,azar_columna][:3] #Se crea una copia desde el indice 0 al 3
                    estacionamiento[azar_fila,azar_columna] = f"{copia_estacionamiento} O =>{p}"  #al estacionamiento random se le asigna una copia de el [:3] + O y la patente del vehiculo
                    estado= f"Patente {p} asignada al estacionamiento: {copia_estacionamiento[0]} "
                    flag= True
                    return estado     
                                  
    estado = f"Patente {p} no esta registrada"
    return estado