# Rastreador de gastos personales

import json
from pathlib import Path


ARCHIVO_GASTOS = Path("gastos.json")


def cargar_gastos():
    if not ARCHIVO_GASTOS.exists():
        return []

    try:
        with open(ARCHIVO_GASTOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        print("El archivo de gastos está dañado o vacío. Se iniciará una lista nueva.")
        return []


def guardar_gastos(gastos):
    with open(ARCHIVO_GASTOS, "w", encoding="utf-8") as archivo:
        json.dump(gastos, archivo, indent=4, ensure_ascii=False)


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


def agregar_gasto(gastos):
    fecha = input("Fecha del gasto (AAAA-MM-DD): ")
    categoria = input("Categoría: ")
    descripcion = input("Descripción: ")
    monto = solicitar_monto()

    gasto = {
        "fecha": fecha,
        "categoria": categoria,
        "descripcion": descripcion,
        "monto": monto,
    }

    gastos.append(gasto)
    guardar_gastos(gastos)

    print("Gasto agregado correctamente.")


def mostrar_gastos(gastos):
    if not gastos:
        print("No hay gastos registrados.")
        return

    print("\nGastos registrados:")
    print("-" * 60)

    for indice, gasto in enumerate(gastos, start=1):
        print(
            f"{indice}. {gasto['fecha']} | "
            f"{gasto['categoria']} | "
            f"${gasto['monto']:.2f}"
        )
        print(f"   {gasto['descripcion']}")

    print("-" * 60)


def mostrar_total(gastos):
    total = sum(gasto["monto"] for gasto in gastos)
    print(f"Total gastado: ${total:.2f}")


def mostrar_menu():
    print("""
Rastreador de gastos personales

1. Agregar gasto
2. Ver gastos
3. Ver total
4. Salir
""")


def main():
    gastos = cargar_gastos()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_gasto(gastos)
        elif opcion == "2":
            mostrar_gastos(gastos)
        elif opcion == "3":
            mostrar_total(gastos)
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida. Elige 1, 2, 3 o 4.")


if __name__ == "__main__":
    main()
