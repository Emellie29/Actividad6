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

print("\nInventario:")
for codigo, datos in producto.items():
    print(f"Código: {codigo}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Categoria: {datos['categoria']}")
    print(f"Talla: {datos['talla']}")
    print(f"Precio unidad: Q.{datos['precio']:.2f}")
    print(f"Stock: {datos['stock']}")

print("\nBúsqueda")
busqueda=input("Ingrese código del producto: ").strip()
if busqueda in producto:
    print(f"Producto encotrado.")
    #datos=producto[busqueda]
    print(f"Nombre: {producto['nombre']}")
    print(f"Categoria: {producto['categoria']}")
    print(f"Talla: {producto['talla']}")
    print(f"Precio unidad: Q.{producto['precio']}")
    print(f"Stock: {producto['stock']}")
else:
    print("Producto no encontrado")


    producto[codigo]={
        "nombre_producto":nombre_producto,
        "categoria":categoria,
        "talla":talla,
        "precio_uni":precio_uni,
        "stock":stock,
    }