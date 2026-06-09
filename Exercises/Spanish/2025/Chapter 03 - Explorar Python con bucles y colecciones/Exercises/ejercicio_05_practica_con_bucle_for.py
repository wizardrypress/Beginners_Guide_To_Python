# Ejercicio 5: Práctica con bucle for
# Escribe un bucle for para imprimir los primeros 10 números
# de la secuencia de Fibonacci.

a, b = 0, 1

for _ in range(10):
    print(a)
    a, b = b, a + b
