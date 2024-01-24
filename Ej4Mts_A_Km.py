def convertir_a_kilometros(distancia_metros):
    distancia_km = distancia_metros/1000
    return distancia_km

distancia_metros = float(input("Ingrese la distancia en metros:"))

distancia_km = convertir_a_kilometros(distancia_metros)

print(f"La distancia en kilómetros es: {distancia_km} km")
