productos={}
cantidad=int(input("Cantidad de productos que desea ingresar: "))
for i in range(cantidad):
    print(f"Cantidad {i+1}")
    codigo=input("Ingrese el código: ")
    nombredelproducto=input("Ingrese el nombre: ")
    caregoria=input("Ingrese la caregoria: ")
    talla=input("Ingrese la talla: ")
    preciounitario=input("Ingrese la preciounitario: ")
    cantidadenstock=int(input("Ingrese la cantidad en stock: "))
    productos[codigo]={
        "nombredelproducto":nombredelproducto,
        "caregoria":caregoria,
        "talla":talla,
        "preciounitario":preciounitario,
        "cantidadenstock":cantidadenstock,
    }
