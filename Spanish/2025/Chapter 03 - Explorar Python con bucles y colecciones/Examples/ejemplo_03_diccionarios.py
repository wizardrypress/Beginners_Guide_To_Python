mascota = {
    "nombre": "Fido",
    "especie": "perro",
    "edad": 5,
}

print(mascota["edad"])
print(mascota)

mascota["juguete_favorito"] = "hueso de goma"
print(mascota)

mascota["edad"] = 6
print(mascota)

del mascota["especie"]
print(mascota)
