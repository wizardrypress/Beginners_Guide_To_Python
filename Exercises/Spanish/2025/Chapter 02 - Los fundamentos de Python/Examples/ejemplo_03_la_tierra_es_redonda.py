la_tierra_es_plana = False
la_tierra_tiene_forma_de_dona = False

if la_tierra_es_plana:
    print("¡Ten cuidado de no caerte!")
elif la_tierra_tiene_forma_de_dona:
    print("Hmmm, interesante teoría.")
    print("No estoy seguro de cómo calcularlo.")
else:
    PI = 3.14159265359
    RADIO_EN_MI = 3959
    RADIO_EN_KM = 6371

    area_tierra_en_mi = 4 * PI * (RADIO_EN_MI ** 2)
    area_tierra_en_km = 4 * PI * (RADIO_EN_KM ** 2)

    print("Superficie de la Tierra:")
    print(f"en millas cuadradas es {area_tierra_en_mi}")
    print(f"y en kilómetros cuadrados es {area_tierra_en_km}")
