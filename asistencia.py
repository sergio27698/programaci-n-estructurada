for curso in range (1,5):
    print(f"Curso {curso}")
    asistieron=0
    faltaron=0
    for estudiante in range (1,7):
        asistencia=int(input(f"estudiante {estudiante}:"))
        if asistencia ==1:
            asistieron +=1
        else:
            faltaron+=1 
            print(f"asistieron {asistieron},faltaron {faltaron}")

