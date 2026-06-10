# Ejercicio 2: Usar composición


class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_detalles(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}")


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            libro.mostrar_detalles()


# Crear instancias de Libro.
libro_1 = Libro("1984", "George Orwell", 1949)
libro_2 = Libro("Matar a un ruiseñor", "Harper Lee", 1960)

# Crear una instancia de Biblioteca y agregar libros.
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro_1)
biblioteca.agregar_libro(libro_2)

# Mostrar todos los libros de la biblioteca.
biblioteca.mostrar_libros()
