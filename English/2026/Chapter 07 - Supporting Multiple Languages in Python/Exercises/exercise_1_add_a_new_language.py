# Exercise 1: Add a New Language

messages = { "en": "Hello", "es": "Hola", "pt": "Olá", "fr": "Bonjour" }
language = input("Choose a language (en/es/pt/fr): ")
print(messages.get(language, messages["en"]))
