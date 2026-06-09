# Ejercicio 2: Escribir en un archivo de texto


def escribir_archivo(ruta_archivo, contenido):
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
    except Exception as error:
        print(f"Ocurrió un error: {error}")


escribir_archivo(
    "diario.txt",
    "2024-05-25: Aprendí sobre el manejo de archivos en Python.\n",
)
