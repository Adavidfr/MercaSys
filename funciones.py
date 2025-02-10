def registrarProducto(productos, idProducto, nombre, cantidad, unidad, precio, categoria, stockMinimo):
    if idProducto in productos:
        return "El producto ya existe."
    productos[idProducto] = {
        "Nombre": nombre,
        "Cantidad": cantidad,
        "Unidad": unidad,
        "Precio": precio,
        "Categoría": categoria,
        "Stock mínimo": stockMinimo
    }
    return "Producto registrado exitosamente."

def actualizarProducto(productos, idProducto, **kwargs):
    if idProducto not in productos:
        return "Producto no encontrado."
    productos[idProducto].update(kwargs)
    return "Producto actualizado exitosamente."

def consultarInventario(productos):
    return productos

def eliminarProducto(productos, idProducto):
    if idProducto in productos:
        del productos[idProducto]
        return "Producto eliminado exitosamente."
    return "Producto no encontrado."

def gestionarStock(productos, idProducto, cantidad):
    if idProducto in productos:
        productos[idProducto]["Cantidad"] += cantidad
        if productos[idProducto]["Cantidad"] < 0:
            productos[idProducto]["Cantidad"] = 0
        return "Stock actualizado exitosamente."
    return "Producto no encontrado."