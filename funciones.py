def imprimirProductos(productos):
    print("Listado de productos:")
    print("-" * 80)
    print("{:<10} {:<20} {:<10} {:<10} {:<15} {:<10}".format(
        "ID", "Nombre", "Cantidad", "Unidad", "Precio (USD)", "Categoría"
    ))
    print("-" * 80)

    for idProducto, detalles in productos.items():
        print("{:<10} {:<20} {:<10} {:<10} {:<15} {:<10}".format(
            idProducto,
            detalles["Nombre"],
            detalles["Cantidad"],
            detalles["Unidad"],
            f"${detalles['Precio']:.2f}",
            detalles["Categoría"]
        ))
    print("-" * 80)

def agregarProducto(productos):
    idProducto = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    unidad = input("Ingrese la unidad de medida del producto: ")
    precio = float(input("Ingrese el precio del producto (USD): "))
    categoria = input("Ingrese la categoría del producto: ")

    productos[idProducto] = {
        "Nombre": nombre,
        "Cantidad": cantidad,
        "Unidad": unidad,
        "Precio": precio,
        "Categoría": categoria
    }

    print("Producto agregado exitosamente.")
