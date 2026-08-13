for curso in range(1, 5):
    print(f"Curso {curso}")
    asistieron = 0
    faltaron = 0
    for estudiante in range(1, 7):
        while True:
            entrada = input(f"estudiante {estudiante}: ")
            if entrada in ("0", "1"):
                asistencia = int(entrada)
                break
            else:
                print("Solo se admite 1 (asistió) o 0 (faltó). Intenta de nuevo.")
        if asistencia == 1:
            asistieron += 1
        else:
            faltaron += 1
    print(f"asistieron {asistieron}, faltaron {faltaron}")
