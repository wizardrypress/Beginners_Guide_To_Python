# Ejercicio 5: Escribir en un archivo JSON

import json


gastos = [
    {
        "fecha": "2024-05-25",
        "monto": 50.75,
        "categoria": "Supermercado",
        "descripcion": "Compras semanales",
    },
    {
        "fecha": "2024-05-26",
        "monto": 120.00,
        "categoria": "Servicios",
        "descripcion": "Factura de electricidad",
    },
]


def escribir_json(ruta_archivo, datos):
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except Exception as error:
        print(f"Ocurrió un error: {error}")


escribir_json("gastos.json", gastos)
