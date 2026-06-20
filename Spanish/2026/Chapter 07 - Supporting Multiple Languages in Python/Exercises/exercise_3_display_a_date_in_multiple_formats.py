# Exercise 3: Display a Date in Multiple Formats

from datetime import datetime

today = datetime.today()

us_format = today.strftime("%m/%d/%Y")
european_format = today.strftime("%d/%m/%Y")
iso_format = today.strftime("%Y-%m-%d")

print(f"United States format: {us_format}")
print(f"European format: {european_format}")
print(f"ISO 8601 format: {iso_format}")
