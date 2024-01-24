def main ():
    base = float (input("Ingrese la base del triangulo: "))
    altura = float (input("Ingrese la altura del triangulo: "))
    
    area = (base * altura)/2
    
    if area > 1000:
        print (input("DATOS NO VALIDOS !!!EL AREA ES MAYOR A 1000!!!"))
        
    else: 
        print ("El area del triangulos: ", area)
    
if __name__ == "__main__":
    main ()