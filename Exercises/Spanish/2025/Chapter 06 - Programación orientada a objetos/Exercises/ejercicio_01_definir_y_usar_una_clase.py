# Ejercicio 1: Definir y usar una clase


class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_detalles(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}")


# Crear instancias.
libro_1 = Libro("1984", "George Orwell", 1949)
libro_2 = Libro("Matar a un ruiseñor", "Harper Lee", 1960)

# Mostrar detalles.
libro_1.mostrar_detalles()
libro_2.mostrar_detalles()
