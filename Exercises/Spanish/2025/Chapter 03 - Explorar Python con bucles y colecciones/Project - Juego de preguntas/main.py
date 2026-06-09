# Juego básico de preguntas

import random

preguntas = [
    {
        "pregunta": "¿Qué tipo de dato se utiliza para almacenar elementos en una secuencia que mantiene el orden?",
        "opciones": ["Lista", "Tupla", "Conjunto", "Diccionario"],
        "respuesta_correcta": "Lista",
    },
    {
        "pregunta": '¿Cuál es la mejor forma de ganar la codiciada insignia de "Conquistador del Código Certificado"?',
        "opciones": [
            "Memorizar cada documento de Python palabra por palabra",
            "Copiar y pegar código de internet sin pensar ni probar",
            "Practicar y cometer errores",
            "Rezarle a los dioses de Python cada hora",
        ],
        "respuesta_correcta": "Practicar y cometer errores",
    },
    {
        "pregunta": "¿Qué colección de Python permite almacenar elementos únicos identificados por una clave?",
        "opciones": ["Lista", "Tupla", "Conjunto", "Diccionario"],
        "respuesta_correcta": "Diccionario",
    },
    {
        "pregunta": "¿Cuál es el mejor lugar para probar tu código?",
        "opciones": [
            "Directamente en producción; ahí hay más testers",
            "En un entorno de pruebas controlado",
            "No es necesario probar; si Python no se queja, todo está bien",
            "En la computadora de tu compañero, así puedes echarle la culpa",
        ],
        "respuesta_correcta": "En un entorno de pruebas controlado",
    },
    {
        "pregunta": "¿Qué estructura de Python debes usar para recorrer cada carácter de una palabra?",
        "opciones": ["Bucle for", "Bucle while", "Sentencia if", "Sentencia print"],
        "respuesta_correcta": "Bucle for",
    },
    {
        "pregunta": "¿Qué tipo de colección en Python evita los duplicados?",
        "opciones": ["Lista", "Tupla", "Conjunto", "Diccionario"],
        "respuesta_correcta": "Conjunto",
    },
    {
        "pregunta": "¿Dónde nacen los bugs?",
        "opciones": [
            "Cuando el desarrollador los escribió",
            "Cuando QA los descubrió, igual que la gravedad",
            "Después de que escaparon a producción",
            "Nunca. Yo no genero bugs, pero sí cobro por arreglarlos",
        ],
        "respuesta_correcta": "Cuando el desarrollador los escribió",
    },
]

puntuacion = 0

print("¡Bienvenido al juego básico de preguntas!")

random.shuffle(preguntas)

for indice, pregunta in enumerate(preguntas, start=1):
    print(f"\n{indice}/{len(preguntas)}: {pregunta['pregunta']}")

    for numero_opcion, opcion in enumerate(pregunta["opciones"], start=1):
        print(f"{numero_opcion}. {opcion}")

    respuesta_usuario = input("Tu respuesta (1-4): ")

    if (
        respuesta_usuario.isdigit()
        and 1 <= int(respuesta_usuario) <= len(pregunta["opciones"])
        and pregunta["opciones"][int(respuesta_usuario) - 1]
        == pregunta["respuesta_correcta"]
    ):
        print("¡Correcto! Ganaste un punto.")
        puntuacion += 1
    else:
        print(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta_correcta']}")

print(f"\nJuego terminado. Tu puntuación es: {puntuacion}/{len(preguntas)}")
