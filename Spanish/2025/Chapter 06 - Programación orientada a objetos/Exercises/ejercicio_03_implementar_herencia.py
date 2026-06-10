# Ejercicio 3: Implementar herencia


class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_detalles(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}")


class LibroElectronico(Libro):
    def __init__(self, titulo, autor, anio, tamanio_archivo):
        super().__init__(titulo, autor, anio)
        self.tamanio_archivo = tamanio_archivo

    def mostrar_detalles(self):
        print(
            f"Título: {self.titulo}, Autor: {self.autor}, "
            f"Año: {self.anio}, Tamaño del archivo: {self.tamanio_archivo} MB"
        )


# Crear instancias de LibroElectronico.
ebook_1 = LibroElectronico("1984", "George Orwell", 1949, 2)
ebook_2 = LibroElectronico("Matar a un ruiseñor", "Harper Lee", 1960, 1.5)

# Mostrar detalles.
ebook_1.mostrar_detalles()
ebook_2.mostrar_detalles()
