producto={}
cantidad=int(input("Cantidad de productos que desea ingresar: "))
for i in range(cantidad):
    print(f"Producto no. {i+1}")

    codigo=int(input("Ingrese el código: ").strip())
    if codigo in producto:
        print(f"El producto ya existe. Ingrese uno diferente.")

    nombre_producto=input("Nombre del producto: ").strip()

    categoria=input("Ingrese la categoria (Hombre/Mujer/Niño): ").capitalize()
    while categoria not in ["Hombre","Mujer","Niño"]:
        print("Ingrese una categoria valida")
        categoria=input("Categoria: ").capitalize()

    talla=input("Ingrese la talla (S/M/L/XL): ")
    while talla not in ["S","M","L","XL"]:
        print("Talla no valida")
        talla=input("Talla: ").upper()

    precio_uni=float(input("Precio unidad Q."))
    while precio_uni <=0:
        print("Precio debe ser mayor que Q.0.00.")
        precio_uni=float(input("Precio unidad Q."))

    stock=int(input("Ingrese la cantidad en stock: "))
    while stock<0:
        print("Ingrese una cantidad entera positiva")
        stock=input("Cantidad en stock: ")

    producto[codigo]={
        "nombre_producto":nombre_producto,
        "categoria":categoria,
        "talla":talla,
        "precio_uni":precio_uni,
        "stock":stock,
    }