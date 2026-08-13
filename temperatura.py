for dia in range (4):
    print(f"dia {dia + 1}")
    suma=0
    for medicion in range (3):
        temp=float(input(f"medicion {medicion+1}:"))
        suma+=temp
        promedio=suma/3
    print(f" promedio del dia {dia + 1}:{promedio:.2f}")

    
