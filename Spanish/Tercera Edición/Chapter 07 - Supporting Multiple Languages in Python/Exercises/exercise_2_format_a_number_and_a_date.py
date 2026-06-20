# Exercise 2: Format a Number and a Date

import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, '')

number = 1234567.89
formatted_number = locale.format_string("%n", number)
print(f"Formatted number: {formatted_number}")

today = datetime.today()
formatted_date = today.strftime("%m/%d/%Y")
print(f"Formatted date: {formatted_date}")
