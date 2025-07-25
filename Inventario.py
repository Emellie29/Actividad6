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

    talla=input("Ingrese la talla (S/M/L/XL): ").upper()
    while talla not in ["S","M","L","XL"]:
        print("Talla no valida")
        talla=input("Talla: ").upper()

    precio_uni=float(input("Precio unidad Q."))
    while precio_uni <=0:
        print("Precio debe ser mayor que Q.0.00.")
        precio_uni=float(input("Precio unidad Q."))

    stock=int(input("Ingrese la cantidad en stock: "))
    while stock <= 0:
        print("Ingrese una cantidad entera positiva")
        stock=int(input("Cantidad en stock: "))

producto[codigo]={
        "nombre_producto":nombre_producto,
        "categoria":categoria,
        "talla":talla,
        "precio_uni":precio_uni,
        "stock":stock,
    }

print("\nInventario:")
for codigo, datos in producto.items():
    print(f"Código: {codigo}")
    print(f"Nombre del producto: {datos['nombre_producto']}")
    print(f"Categoria: {datos['categoria']}")
    print(f"Talla: {datos['talla']}")
    print(f"Precio unidad: Q.{datos['precio_uni']:.2f}")
    print(f"Stock: {datos['stock']}")

print("Búsqueda")
busqueda = int(input("Ingrese el código del producto: ").strip())
if busqueda in producto:
        print("Producto encontrado:")
        print(f"Nombre: {producto[busqueda]['nombre_producto']}")
        print(f"Categoría: {producto[busqueda]['categoria']}")
        print(f"Talla: {producto[busqueda]['talla']}")
        print(f"Precio: Q{producto[busqueda]['precio_uni']:.2f}")
        print(f"Stock: {producto[busqueda]['stock']}")
else:
        print("Producto no encontrado.")

inventario=sum(p['precio_uni']*p['stock'] for p in producto.values())
print(f"\nTotal de inventario: Q.{inventario:.2f}")

conteo = {"Hombre": 0, "Mujer": 0, "Niño": 0}
for datos in producto.values():
    categoria = datos["categoria"]
    if categoria in conteo:
        conteo[categoria] += 1
print("\nCantidad de productos por categoría:")
for categoria, cantidad in conteo.items():
    print(f"{categoria}: {cantidad}")