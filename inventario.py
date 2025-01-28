productos = {
    # Lácteos
    101: {"Nombre": "Leche", "Cantidad": 30, "Unidad": "litros", "Precio": 12.0, "Categoría": "Lácteos", "Stock mínimo": 5},
    102: {"Nombre": "Yogurt", "Cantidad": 25, "Unidad": "unidades", "Precio": 2.0, "Categoría": "Lácteos", "Stock mínimo": 5},
    103: {"Nombre": "Queso", "Cantidad": 8, "Unidad": "kg", "Precio": 60.0, "Categoría": "Lácteos", "Stock mínimo": 2},
    104: {"Nombre": "Mantequilla", "Cantidad": 5, "Unidad": "kg", "Precio": 35.0, "Categoría": "Lácteos", "Stock mínimo": 2},
    105: {"Nombre": "Tetra Pak de leche", "Cantidad": 30, "Unidad": "unidades", "Precio": 11.0, "Categoría": "Lácteos", "Stock mínimo": 5},

    # Granos y cereales
    201: {"Nombre": "Arroz", "Cantidad": 20, "Unidad": "kg", "Precio": 30.0, "Categoría": "Granos y cereales", "Stock mínimo": 5},
    202: {"Nombre": "Frijoles", "Cantidad": 15, "Unidad": "kg", "Precio": 25.0, "Categoría": "Granos y cereales", "Stock mínimo": 5},
    203: {"Nombre": "Azúcar", "Cantidad": 10, "Unidad": "kg", "Precio": 20.0, "Categoría": "Granos y cereales", "Stock mínimo": 3},
    204: {"Nombre": "Harina", "Cantidad": 12, "Unidad": "kg", "Precio": 18.0, "Categoría": "Granos y cereales", "Stock mínimo": 3},
    205: {"Nombre": "Cereales", "Cantidad": 10, "Unidad": "cajas", "Precio": 25.0, "Categoría": "Granos y cereales", "Stock mínimo": 2},
    206: {"Nombre": "Harina de maíz", "Cantidad": 15, "Unidad": "kg", "Precio": 12.0, "Categoría": "Granos y cereales", "Stock mínimo": 2},

    # Enlatados
    301: {"Nombre": "Atún enlatado", "Cantidad": 30, "Unidad": "latas", "Precio": 12.0, "Categoría": "Enlatados", "Stock mínimo": 5},
    302: {"Nombre": "Sardinas", "Cantidad": 20, "Unidad": "latas", "Precio": 9.0, "Categoría": "Enlatados", "Stock mínimo": 5},
    303: {"Nombre": "Latas de vegetales", "Cantidad": 25, "Unidad": "latas", "Precio": 5.0, "Categoría": "Enlatados", "Stock mínimo": 5},
    304: {"Nombre": "Frutas en conserva", "Cantidad": 20, "Unidad": "latas", "Precio": 7.0, "Categoría": "Enlatados", "Stock mínimo": 5},
    305: {"Nombre": "Leche condensada", "Cantidad": 10, "Unidad": "latas", "Precio": 12.0, "Categoría": "Enlatados", "Stock mínimo": 3},

    # Especias y condimentos
    401: {"Nombre": "Comino", "Cantidad": 10, "Unidad": "frascos", "Precio": 3.0, "Categoría": "Especias y condimentos", "Stock mínimo": 5},
    402: {"Nombre": "Pimienta", "Cantidad": 10, "Unidad": "frascos", "Precio": 4.0, "Categoría": "Especias y condimentos", "Stock mínimo": 5},
    403: {"Nombre": "Caldo de pollo", "Cantidad": 30, "Unidad": "cubos", "Precio": 2.0, "Categoría": "Especias y condimentos", "Stock mínimo": 5},
    404: {"Nombre": "Salsa", "Cantidad": 15, "Unidad": "botellas", "Precio": 7.0, "Categoría": "Especias y condimentos", "Stock mínimo": 5},

    # Panadería y galletas
    501: {"Nombre": "Pan", "Cantidad": 50, "Unidad": "piezas", "Precio": 2.0, "Categoría": "Panadería y galletas", "Stock mínimo": 10},
    502: {"Nombre": "Galletas", "Cantidad": 100, "Unidad": "paquetes", "Precio": 3.0, "Categoría": "Panadería y galletas", "Stock mínimo": 10},
    503: {"Nombre": "Pan dulce", "Cantidad": 60, "Unidad": "piezas", "Precio": 1.5, "Categoría": "Panadería y galletas", "Stock mínimo": 10},

    # Limpieza
    601: {"Nombre": "Papel higiénico", "Cantidad": 50, "Unidad": "rollos", "Precio": 20.0, "Categoría": "Limpieza y cuidado del hogar", "Stock mínimo": 5},
    602: {"Nombre": "Detergente", "Cantidad": 25, "Unidad": "botellas", "Precio": 10.0, "Categoría": "Limpieza y cuidado del hogar", "Stock mínimo": 5},

    # Bebidas
    701: {"Nombre": "Agua embotellada", "Cantidad": 100, "Unidad": "botellas", "Precio": 1.0, "Categoría": "Bebidas", "Stock mínimo": 20},
    702: {"Nombre": "Refresco de cola", "Cantidad": 50, "Unidad": "botellas", "Precio": 2.5, "Categoría": "Bebidas", "Stock mínimo": 10},
    703: {"Nombre": "Jugo de naranja", "Cantidad": 30, "Unidad": "litros", "Precio": 3.5, "Categoría": "Bebidas", "Stock mínimo": 10},
    704: {"Nombre": "Café instantáneo", "Cantidad": 20, "Unidad": "frascos", "Precio": 4.0, "Categoría": "Bebidas", "Stock mínimo": 5},

    # Otros
    801: {"Nombre": "Chicles", "Cantidad": 200, "Unidad": "paquetes", "Precio": 0.5, "Categoría": "Otros", "Stock mínimo": 30},
    802: {"Nombre": "Caramelos", "Cantidad": 500, "Unidad": "piezas", "Precio": 0.1, "Categoría": "Otros", "Stock mínimo": 50},
    803: {"Nombre": "Encendedores", "Cantidad": 50, "Unidad": "piezas", "Precio": 1.0, "Categoría": "Otros", "Stock mínimo": 10},
    804: {"Nombre": "Bolsas de plástico", "Cantidad": 100, "Unidad": "paquetes", "Precio": 5.0, "Categoría": "Otros", "Stock mínimo": 20}
}