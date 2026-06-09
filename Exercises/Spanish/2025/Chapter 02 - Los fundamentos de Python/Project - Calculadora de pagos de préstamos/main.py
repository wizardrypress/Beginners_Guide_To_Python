# Calculadora de pagos de préstamos

# Entrada: solicita al usuario los detalles del préstamo.
monto_compra = float(input("Ingresa el monto de la compra: "))
tasa_interes_anual = float(input("Tasa de interés anual (%): ")) / 100
duracion_prestamo_anios = int(input("Duración del préstamo en años: "))
incluir_pago_inicial = input("¿Incluir pago inicial? (s/n): ")

pago_inicial = 0

if incluir_pago_inicial == "s" or incluir_pago_inicial == "S":
    pago_inicial = float(input("Monto del pago inicial: "))

# Calcula el monto del préstamo.
monto_prestamo = monto_compra - pago_inicial

# Calcula la tasa de interés mensual.
tasa_interes_mensual = tasa_interes_anual / 12

# Calcula el número total de pagos.
total_pagos = duracion_prestamo_anios * 12

# Calcula el pago mensual.
if tasa_interes_mensual == 0:
    pago_mensual = monto_prestamo / total_pagos
else:
    pago_mensual = (
        monto_prestamo * tasa_interes_mensual
    ) / (
        1 - (1 + tasa_interes_mensual) ** -total_pagos
    )

# Salida: muestra los detalles del préstamo.
print("\nDetalles del préstamo:")
print("\tMonto de la compra: ".format(monto_compra))
print("\tPago inicial: ".format(pago_inicial))
print("\tMonto del préstamo: ".format(monto_prestamo))
print(f"\tNúmero de pagos: {total_pagos} ({duracion_prestamo_anios} años)")
print("\tTasa de interés: {:.3f}%".format(tasa_interes_anual * 100))
print("\tPago mensual: ".format(pago_mensual))
