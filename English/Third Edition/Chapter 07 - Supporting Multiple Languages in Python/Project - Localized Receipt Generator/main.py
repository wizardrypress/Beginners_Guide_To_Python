"""Chapter 7 Project: Localized Receipt Generator.

This project demonstrates a simple localization pattern:

1. Store user-facing text in dictionaries.
2. Ask the user for a language code.
3. Fall back to English when the requested language is not supported.
4. Use the same program logic regardless of the selected language.
"""

from datetime import datetime


MESSAGES = {
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


ITEMS = [
    {"name": "Notebook", "price": 12.99},
    {"name": "Pencil Set", "price": 4.50},
    {"name": "Backpack", "price": 29.95},
]


def choose_language() -> dict[str, str]:
    """Ask the user for a language code and return the matching labels."""
    print("Choose a language / Elige un idioma / Escolha um idioma")
    print("en = English")
    print("es = Español")
    print("pt = Português")

    language_code = input("Language code: ").strip().lower()
    return MESSAGES.get(language_code, MESSAGES["en"])


def print_receipt(labels: dict[str, str], items: list[dict[str, float | str]]) -> None:
    """Print a localized receipt using the selected labels."""
    today = datetime.today()
    total = 0.0

    print()
    print("=" * 40)
    print(labels["store_name"])
    print(f"{labels['date_label']}: {today.strftime('%Y-%m-%d')}")
    print("=" * 40)
    print(labels["items_label"])

    for item in items:
        name = item["name"]
        price = float(item["price"])
        total += price
        print(f"- {name}: ${price:.2f}")

    print("-" * 40)
    print(f"{labels['total_label']}: ${total:.2f}")
    print(labels["thank_you"])
    print("=" * 40)


def main() -> None:
    labels = choose_language()
    print_receipt(labels, ITEMS)


if __name__ == "__main__":
    main()
