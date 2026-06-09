# Ejercicio 6: Práctica con bucle while
# Escribe un bucle while para invertir una cadena.

texto_original = "hola"
texto_invertido = ""
indice = len(texto_original) - 1

while indice >= 0:
    texto_invertido += texto_original[indice]
    indice -= 1

print(texto_invertido)
