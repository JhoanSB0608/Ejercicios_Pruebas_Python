def main():
    voltajes = []

    for i in range(5):
        voltaje = float(input(f"Ingrese el voltaje {i + 1}: "))
        voltajes.append(voltaje)

    promedio = sum(voltajes) / len(voltajes)

    if promedio > 220:
        print(f"ALTO VOLTAJE: {promedio}")
    else:
        print(f"VOLTAJE CORRECTO: {promedio}")
if __name__ == "__main__":
    main ()
