# Ejercicio 1: Leer desde un archivo de texto


def leer_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("No se encontró el archivo.")
    except PermissionError:
        print("No tienes permiso para leer este archivo.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")


leer_archivo("diario.txt")
