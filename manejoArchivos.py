def guardar_txt(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)

# Ejemplo de uso
contenido = "Hola, este es un archivo de texto."
guardar_txt('ejemplo.txt', contenido)

def cargar_txt(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
    return contenido

# Ejemplo de uso
contenido = cargar_txt('ejemplo.txt')
print(contenido)

import csv

def guardar_csv(nombre_archivo, datos):
    with open(nombre_archivo, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos)

# Ejemplo de uso
datos = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Alice', 30, 'Nueva York'],
    ['Bob', 25, 'San Francisco']
]
guardar_csv('ejemplo.csv', datos)

import csv

def cargar_csv(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lector = csv.reader(archivo)
        datos = list(lector)
    return datos

# Ejemplo de uso
datos = cargar_csv('ejemplo.csv')
for fila in datos:
    print(fila)