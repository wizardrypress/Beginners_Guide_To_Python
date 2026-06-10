# Ejercicio 3: Agregar texto a un archivo existente


def agregar_a_archivo(ruta_archivo, contenido):
    try:
        with open(ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(contenido)
    except Exception as error:
        print(f"Ocurrió un error: {error}")


agregar_a_archivo(
    "diario.txt",
    "2024-05-26: Practiqué escribir y leer archivos.\n",
)
