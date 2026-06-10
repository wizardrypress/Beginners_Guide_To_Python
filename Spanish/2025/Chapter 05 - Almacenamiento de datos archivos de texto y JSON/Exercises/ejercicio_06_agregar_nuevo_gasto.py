# Ejercicio 6: Agregar un nuevo gasto a un archivo JSON

import json


def agregar_gasto(ruta_archivo, nuevo_gasto):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            gastos = json.load(archivo)
    except FileNotFoundError:
        gastos = []
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        gastos = []
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")
        return

    gastos.append(nuevo_gasto)

    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(gastos, archivo, indent=4, ensure_ascii=False)
    except Exception as error:
        print(f"Ocurrió un error: {error}")


nuevo_gasto = {
    "fecha": "2024-05-27",
    "monto": 75.20,
    "categoria": "Entretenimiento",
    "descripcion": "Entradas para un concierto",
}

agregar_gasto("gastos.json", nuevo_gasto)
