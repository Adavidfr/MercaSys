from inventario import productos

# 1. Registrar Producto
def registrar_producto(datos):
    id_, nombre, cantidad, unidad, precio, categoria, stock = datos
    if id_ not in productos:
        productos[id_] = {
            "Nombre": nombre,
            "Cantidad": cantidad,
            "Unidad": unidad,
            "Precio": precio,
            "Categoría": categoria,
            "Stock mínimo": stock
        }
        return True
    return False

# 2. Actualizar Producto
def actualizar_producto(id_, nuevos_datos):
    if id_ in productos:
        productos[id_].update(nuevos_datos)
        return True
    return False

# 3. Eliminar Producto
def eliminar_producto(id_):
    if id_ in productos:
        del productos[id_]
        return True
    return False

# 4. Seleccionar Producto
def seleccionar_producto(id_):
    return productos.get(id_, None)

# 5. Encontrar Producto por Nombre
def encontrar_producto(nombre):
    resultados = {id_: datos for id_, datos in productos.items() if nombre.lower() in datos["Nombre"].lower()}
    return resultados

# 6. Limpiar Campos
def limpiar_campos(entradas):
    for entrada in entradas:
        entrada.set("")
