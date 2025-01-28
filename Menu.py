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

mostrarInterfaz()



