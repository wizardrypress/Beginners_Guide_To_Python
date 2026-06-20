# Rastreador de gastos mejorado con OOP

import json
from pathlib import Path


ARCHIVO_GASTOS = Path("gastos.json")


class Gasto:
    def __init__(self, fecha, categoria, descripcion, monto):
        self.fecha = fecha
        self.categoria = categoria
        self.descripcion = descripcion
        self.monto = monto

    def convertir_a_diccionario(self):
        return {
            "fecha": self.fecha,
            "categoria": self.categoria,
            "descripcion": self.descripcion,
            "monto": self.monto,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["fecha"],
            datos["categoria"],
            datos["descripcion"],
            datos["monto"],
        )


class RastreadorDeGastos:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.gastos = self.cargar_gastos()

    def cargar_gastos(self):
        if not self.ruta_archivo.exists():
            return []

        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return [Gasto.desde_diccionario(gasto) for gasto in datos]
        except json.JSONDecodeError:
            print("El archivo de gastos está dañado o vacío. Se iniciará una lista nueva.")
            return []

    def guardar_gastos(self):
        datos = [
            gasto.convertir_a_diccionario()
            for gasto in self.gastos
        ]

        with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def agregar_gasto(self, gasto):
        self.gastos.append(gasto)
        self.guardar_gastos()

    def mostrar_gastos(self):
        if not self.gastos:
            print("No hay gastos registrados.")
            return

        print("\nGastos registrados:")
        print("-" * 60)

        for indice, gasto in enumerate(self.gastos, start=1):
            print(
                f"{indice}. {gasto.fecha} | "
                f"{gasto.categoria} | "
                f"${gasto.monto:.2f}"
            )
            print(f"   {gasto.descripcion}")

        print("-" * 60)

    def mostrar_total(self):
        total = sum(gasto.monto for gasto in self.gastos)
        print(f"Total gastado: ${total:.2f}")


def solicitar_monto():
    while True:
        try:
            monto = float(input("Monto del gasto: "))

            if monto <= 0:
                print("El monto debe ser mayor que cero.")
            else:
                return monto
        except ValueError:
            print("Entrada inválida. Ingresa un número.")


def crear_gasto_desde_entrada():
    fecha = input("Fecha del gasto (AAAA-MM-DD): ")
    categoria = input("Categoría: ")
    descripcion = input("Descripción: ")
    monto = solicitar_monto()

    return Gasto(fecha, categoria, descripcion, monto)


def mostrar_menu():
    print("""
Rastreador de gastos personales con OOP

1. Agregar gasto
2. Ver gastos
3. Ver total
4. Salir
""")


def main():
    rastreador = RastreadorDeGastos(ARCHIVO_GASTOS)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            gasto = crear_gasto_desde_entrada()
            rastreador.agregar_gasto(gasto)
            print("Gasto agregado correctamente.")
        elif opcion == "2":
            rastreador.mostrar_gastos()
        elif opcion == "3":
            rastreador.mostrar_total()
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida. Elige 1, 2, 3 o 4.")


if __name__ == "__main__":
    main()
