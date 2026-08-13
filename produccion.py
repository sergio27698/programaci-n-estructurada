for maquina in range (3):
    print(f"maquina {maquina +1}")
    total=0
    for dia in range(5):
        productos=int(input(f"dia {dia +1} productos fabricados:"))
        total+=productos
    print(f"total producido por la maquina {maquina+1}:{total}\n")