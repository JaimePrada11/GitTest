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

registro()