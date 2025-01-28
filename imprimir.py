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
