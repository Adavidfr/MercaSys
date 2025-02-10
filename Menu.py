import tkinter as tk
from tkinter import messagebox, ttk
from inventario import productos
from funciones import registrarProducto, actualizarProducto, consultarInventario, eliminarProducto, gestionarStock

class MercaSysApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MercaSys - Gestión de Inventario")

        tk.Button(root, text="Registrar Producto", command=self.registrarProducto).pack(pady=5)
        tk.Button(root, text="Actualizar Producto", command=self.actualizarProducto).pack(pady=5)
        tk.Button(root, text="Consultar Inventario", command=self.consultarInventario).pack(pady=5)
        tk.Button(root, text="Eliminar Producto", command=self.eliminar_producto).pack(pady=5)
        tk.Button(root, text="Gestionar Stock", command=self.gestionar_stock).pack(pady=5)

    def registrarProducto(self):
        messagebox.showinfo("Registro", registrarProducto(productos, 104, "Mantequilla", 5, "kg", 35.0, "Lácteos", 2))

    def actualizarProducto(self):
        messagebox.showinfo("Actualización", actualizarProducto(productos, 101, Precio=14.0))

    def consultarInventario(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Inventario de Productos")

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

    def eliminarProducto(self):
        messagebox.showinfo("Eliminación", eliminarProducto(productos, 102))

    def gestionarStock(self):
        messagebox.showinfo("Gestión de Stock", gestionarStock(productos, 101, -5))

if __name__ == "__main__":
    root = tk.Tk()
    app = MercaSysApp(root)
    root.mainloop()
