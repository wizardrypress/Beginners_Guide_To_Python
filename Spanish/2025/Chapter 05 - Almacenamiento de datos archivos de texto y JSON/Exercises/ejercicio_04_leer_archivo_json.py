# Ejercicio 4: Leer desde un archivo JSON

import json


def leer_json(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            print(datos)
    except FileNotFoundError:
        print("No se encontró el archivo.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")


leer_json("gastos.json")
