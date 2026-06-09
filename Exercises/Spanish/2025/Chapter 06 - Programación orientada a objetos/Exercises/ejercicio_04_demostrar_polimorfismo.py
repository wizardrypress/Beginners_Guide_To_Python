# Ejercicio 4: Demostrar polimorfismo


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


def mostrar_detalles_del_libro(libro):
    libro.mostrar_detalles()


# Crear instancias de Libro y LibroElectronico.
libro_1 = Libro("1984", "George Orwell", 1949)
ebook_1 = LibroElectronico("1984", "George Orwell", 1949, 2)

# Demostrar polimorfismo.
mostrar_detalles_del_libro(libro_1)
mostrar_detalles_del_libro(ebook_1)
