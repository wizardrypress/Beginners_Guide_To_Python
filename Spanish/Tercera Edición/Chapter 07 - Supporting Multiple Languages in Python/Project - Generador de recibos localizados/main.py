"""Proyecto del capítulo 7: Generador de recibos localizados.

Este proyecto demuestra un patrón sencillo de localización:

1. Guardar los mensajes visibles para el usuario en diccionarios.
2. Pedir al usuario un código de idioma.
3. Usar inglés como alternativa si el idioma solicitado no está disponible.
4. Mantener la misma lógica del programa sin importar el idioma seleccionado.
"""

from datetime import datetime


MENSAJES = {
    "en": {
        "store_name": "Wizardry Press Supply Shop",
        "items_label": "Items",
        "date_label": "Date",
        "total_label": "Total",
        "thank_you": "Thank you for shopping with us!",
    },
    "es": {
        "store_name": "Tienda de Suministros Wizardry Press",
        "items_label": "Artículos",
        "date_label": "Fecha",
        "total_label": "Total",
        "thank_you": "¡Gracias por comprar con nosotros!",
    },
    "pt": {
        "store_name": "Loja de Suprimentos Wizardry Press",
        "items_label": "Itens",
        "date_label": "Data",
        "total_label": "Total",
        "thank_you": "Obrigado por comprar conosco!",
    },
}


ARTICULOS = [
    {"name": "Notebook", "price": 12.99},
    {"name": "Pencil Set", "price": 4.50},
    {"name": "Backpack", "price": 29.95},
]


def seleccionar_idioma() -> dict[str, str]:
    """Pide un código de idioma y devuelve las etiquetas correspondientes."""
    print("Elige un idioma / Choose a language / Escolha um idioma")
    print("en = English")
    print("es = Español")
    print("pt = Português")

    codigo_idioma = input("Código de idioma: ").strip().lower()
    return MENSAJES.get(codigo_idioma, MENSAJES["en"])


def imprimir_recibo(etiquetas: dict[str, str], articulos: list[dict[str, float | str]]) -> None:
    """Imprime un recibo localizado usando las etiquetas seleccionadas."""
    fecha_actual = datetime.today()
    total = 0.0

    print()
    print("=" * 40)
    print(etiquetas["store_name"])
    print(f"{etiquetas['date_label']}: {fecha_actual.strftime('%Y-%m-%d')}")
    print("=" * 40)
    print(etiquetas["items_label"])

    for articulo in articulos:
        nombre = articulo["name"]
        precio = float(articulo["price"])
        total += precio
        print(f"- {nombre}: ${precio:.2f}")

    print("-" * 40)
    print(f"{etiquetas['total_label']}: ${total:.2f}")
    print(etiquetas["thank_you"])
    print("=" * 40)


def main() -> None:
    etiquetas = seleccionar_idioma()
    imprimir_recibo(etiquetas, ARTICULOS)


if __name__ == "__main__":
    main()
