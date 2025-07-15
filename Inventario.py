productos={}
cantidad=int(input("Cantidad de productos que desea ingresar: "))
for i in range(cantidad):
    print(f"Producto no. {i+1}")

    codigo=int(input("Ingrese el código: ").strip())
    if codigo in productos:
        print(f"El producto ya existe. Ingrese uno diferente.")

    nombre_producto=input("Ingrese el nombre: ").strip()

    categoria=input("Ingrese la categoria (Hombre/Mujer/Niño): ").capitalize()
    while categoria not in ["Hombre","Mujer","Niño"]:
        print("Ingrese una categoria valida")
        categoria=input("Categoria: ").capitalize()

    talla=input("Ingrese la talla (S/M/L/XL): ")
    while talla not in ["S","M","L","XL"]:
        print("Ingrese una talla valida")
        talla=input("Talla: ").upper()

    precio_uni=int(input("Ingrese precio unitario: "))
    stock=int(input("Ingrese la cantidad en stock: "))
    productos[codigo]={
        "nombre_producto":nombre_producto,
        "categoria":categoria,
        "talla":talla,
        "precio_uni":precio_uni,
        "stock":stock,
    }