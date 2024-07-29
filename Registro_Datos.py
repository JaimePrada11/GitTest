from datos import *

def registro():
    cargar_datos()
    usuario={}
    
    ID= input("Ingresa la ID")
    usuario["Nombre"] = input("Ingresa Nombre").upper()
    usuario["Apellido"] = input("Ingresa Apellido").upper()
    usuario["Correo"] = input("Ingresa Correo").upper()
    usuario["Cel"] = input("Ingresa celular").upper()
    
    Informacion[ID] = usuario
    guardar_datos()

def buscar():
    cargar_datos()
    id = input("cedula")
    if id not in Informacion:
        print("No existe")
    else:
        usuario = Informacion[id]
        print(f"cedula: {id}")
        print(f"nombre: {usuario['Nombre']}")
        print(f"nombre: {usuario['Apellido']}")
        print(f"nombre: {usuario['Correo']}")
        print(f"nombre: {usuario['Cel']}")
buscar()