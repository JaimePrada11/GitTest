import json

Informacion = {}

Ruta = "Data_Base/Registro.json"

def guardar_datos():
    try:
        contenido = json.dumps(Informacion, indent=4, ensure_ascii=False)
        with open(Ruta, "w", encoding='utf-8') as file:
            file.write(contenido)
    except Exception as e:
        print(f"Error al guardar datos {e}")

def cargar_datos():
    try:
        with open(Ruta, "r", encoding='utf-8') as archivo:
            Informacion.update(json.load(archivo))
    except Exception as e:
        print(f"Error al cargar datos {e}")