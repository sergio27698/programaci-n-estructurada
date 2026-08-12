for aula in range(1,5):
    print(f"aula {aula}")
    suma=0
    for estudiante in range (1,6):
        nota=float(input(f"nota del estudiamte {estudiante}:"))
        suma+=nota
        promedio=suma/5
        print(f"promedio del aula {aula +1}:{promedio:.2f}\n")

                   