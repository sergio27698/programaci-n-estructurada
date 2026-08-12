for categoria in range(1,4):
    print(f"categoria {categoria}:")
    total=0
    for producto in range(1,5):
        precio=float(input(f"precio del producto {producto}:"))
        total+=precio
        print(f"total de ventas categoria{categoria}:{total:.2f}")
