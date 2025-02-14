# MercaSys - Sistema de Gestión de Inventario

## Propuesta

MercaSys es un programa diseñado para proporcionar un servicio integral de gestión de inventario específicamente para tiendas de abarrotes. Este sistema tiene como objetivo optimizar la administración de productos, reducir los errores humanos y mejorar la eficiencia operativa del negocio.

## Funciones Principales

MercaSys implementará funcionalidades CRUD (Crear, Leer, Actualizar y Eliminar), incluyendo:

- **Registrar productos**: Permite agregar nuevos productos con detalles como ID, nombre, cantidad, unidad, precio, categoría y stock mínimo.
- **Actualizar productos**: Permite modificar los detalles de un producto ya registrado.
- **Eliminar productos**: Permite eliminar un producto de la base de datos.
- **Consultar productos**: Permite buscar productos por ID o nombre.
- **Visualización en tabla**: Los productos registrados se muestran en una tabla con la opción de seleccionar, editar y eliminar elementos.

# Librerías Utilizadas

- **Tkinter**: Para la interfaz gráfica.
- **Ttk**: Extensión de Tkinter para widgets avanzados.
- **Messagebox**: Para mostrar mensajes de alerta e informativos.
- **Productos (importado de inventario)**: Diccionario que almacena la información de los productos.

# Validaciones Generales

Para garantizar la correcta operación y confiabilidad del sistema, **MercaSys** incorporará las siguientes validaciones:

- Verificación de campos vacíos al actualizar productos.
- Validación de tipo de datos (ID y cantidad deben ser enteros, precio debe ser flotante).
- Prevención de duplicación de IDs al registrar productos.
- Restricción para que el ID de un producto no sea modificado al actualizar.
- Control de selección de productos en la interfaz (mensajes de error si no se elige un producto).
- Mensajes de advertencia y confirmación para mejorar la experiencia del usuario.

# Características Adicionales

- **Reportes de inventario**: Generar reportes personalizados para identificar los productos más vendidos, faltantes o próximos a agotarse.
- **Búsqueda avanzada**: Buscar productos por nombre, Id, etc.
- **Interfaz amigable**: Diseñar una interfaz simple e intuitiva para facilitar el uso del sistema a usuarios con conocimientos básicos de tecnología.

MercaSys está diseñado para ser una herramienta esencial en la gestión diaria de una tienda de abarrotes, contribuyendo al crecimiento y sostenibilidad del negocio.

## Logotipo

![Logo](/Elementos/logo.png)

## **Boceto de la Interfaz Gráfica**

![Interfaz](/Elementos/interfaz.png)
