pet = {
    "name": "Fido",
    "species": "dog",
    "age": 5,
}

print(pet["age"])
print(pet)

pet["favorite_toy"] = "rubber bone"
print(pet)

pet["age"] = 6
print(pet)

del pet["species"]
print(pet)
