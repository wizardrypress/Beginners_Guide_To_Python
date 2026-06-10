# Ejercicio 2: Alcance y vida útil de las variables
# Este ejemplo muestra la diferencia entre una variable global
# y una variable local.

total = 0


def modificar_global():
    global total
    total += 10


def usar_local():
    total = 5
    print("Total local:", total)


print("Total global antes:", total)

modificar_global()
print("Total global después:", total)

usar_local()
print("Total global final:", total)
