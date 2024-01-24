def main():
    voltaje1 = float(input(f"Ingrese el voltaje 1 : "))
    voltaje2 = float(input(f"Ingrese el voltaje 2 : "))
    voltaje3 = float(input(f"Ingrese el voltaje 3 : "))
        
    promedio = (voltaje1 + voltaje2 + voltaje3) /3
    
    if promedio < 115:
        print("VOLTAJE CORRECTO")
        
    elif 115 < promedio < 220 :
        print ("ALTO VOLTAJE")

    else:
        print ("PELIGRO")

if __name__ == "__main__":
    main ()