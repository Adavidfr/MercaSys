from inventario import productos
import tkinter as tk
from tkinter import ttk

def mostrarInterfaz():

    ventana = tk.Tk()
    ventana.title("MercaSys")

    columnas = ("ID", "Nombre", "Cantidad", "Unidad", "Precio (USD)", "Categoría")
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings")

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor=tk.CENTER, width=120)

    for idProducto, detalles in productos.items():
        tabla.insert("", tk.END, values=(
            idProducto,
            detalles["Nombre"],
            detalles["Cantidad"],
            detalles["Unidad"],
            f"${detalles['Precio']:.2f}",
            detalles["Categoría"]
        ))

    tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    ventana.mainloop()

def agregarProducto(productos):
    ventana = tk.Tk()
    ventana.title("Agregar producto")

    tk.Label(ventana, text="ID del producto:").grid(row=0, column=0)
    idProducto = tk.Entry(ventana)
    idProducto.grid(row=0, column=1)

    tk.Label(ventana, text="Nombre del producto:").grid(row=1, column=0)
    nombre = tk.Entry(ventana)
    nombre.grid(row=1, column=1)

    tk.Label(ventana, text="Cantidad del producto:").grid(row=2, column=0)
    cantidad = tk.Entry(ventana)
    cantidad.grid(row=2, column=1)

    tk.Label(ventana, text="Unidad de medida:").grid(row=3, column=0)
    unidad = tk.Entry(ventana)
    unidad.grid(row=3, column=1)

    tk.Label(ventana, text="Precio (USD):").grid(row=4, column=0)
    precio = tk.Entry(ventana)
    precio.grid(row=4, column=1)

    tk.Label(ventana, text="Categoría:").grid(row=5, column=0)
    categoria = tk.Entry(ventana)
    categoria.grid(row=5, column=1)

    def guardarProducto():
        productos[idProducto.get()] = {
            "Nombre": nombre.get(),
            "Cantidad": int(cantidad.get()),
            "Unidad": unidad.get(),
            "Precio": float(precio.get()),
            "Categoría": categoria.get()
        }

        print("Producto agregado exitosamente.")
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardarProducto).grid(row=6, column=0, columnspan=2)

    ventana.mainloop()
mostrarInterfaz()
# agregarProducto(productos)



