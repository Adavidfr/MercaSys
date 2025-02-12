from tkinter import *
from tkinter import ttk
import tkinter
from inventario import productos  # Importación de productos
from funciones import registrar_producto, actualizar_producto, eliminar_producto, seleccionar_producto, encontrar_producto, limpiar_campos

window = tkinter.Tk()
window.title("Mercasys")
window.geometry("750x640")
my_tree = ttk.Treeview(window, show='headings', height=20)
style = ttk.Style()

placeholderArray = [tkinter.StringVar() for _ in range(7)]  # Lista de StringVar, 7 elementos

for i in range(0, 6):
    placeholderArray[i] = tkinter.StringVar()

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
    for item_id, details in productos.items():
        my_tree.insert(parent='', index='end', iid=item_id, text="", 
                        values=(item_id, details["Nombre"], details["Cantidad"], 
                                details["Unidad"], details["Precio"], 
                                details["Categoría"], details["Stock mínimo"]), 
                        tag="orow")
        my_tree.tag_configure('orow', background="#EEEEEE")
        my_tree.pack()

frame = tkinter.Frame(window, bg="#2f4a6c")
frame.pack(fill="x", expand=True)

btnColor = "#2f4a6c"


# Manage Frame
manageFrame = tkinter.LabelFrame(frame, text="Menú", borderwidth=5)
manageFrame.grid(row=0, column=0, sticky="nw", padx=30, pady=20)

registrarBtn = Button(manageFrame, text="Registrar", width=10, borderwidth=3, bg=btnColor, fg='white', command=lambda: registrar_producto([entry.get() for entry in placeholderArray]))
actiualizarBtn = Button(manageFrame, text="Actualizar", width=10, borderwidth=3, bg=btnColor, fg='white', command=lambda: actualizar_producto(placeholderArray, my_tree))
eliminarBtn = Button(manageFrame, text="Eliminar", width=10, borderwidth=3, bg=btnColor, fg='white', command=lambda: eliminar_producto(placeholderArray, my_tree))
encontrarBtn = Button(manageFrame, text="Encontrar", width=10, borderwidth=3, bg=btnColor, fg='white', command=lambda: encontrar_producto(placeholderArray, my_tree))
seleccionarBtn = Button(manageFrame, text="Seleccionar", width=10, borderwidth=3, bg=btnColor, fg='white', command= seleccionar_producto)
limpiarBtn = Button(manageFrame, text="Limpiar", width=10, borderwidth=3, bg=btnColor, fg='white', command=lambda: limpiar_campos(placeholderArray))

registrarBtn.grid(row=0, column=0, padx=5, pady=5)
actiualizarBtn.grid(row=1, column=0, padx=5, pady=5)
eliminarBtn.grid(row=2, column=0, padx=5, pady=5)
encontrarBtn.grid(row=4, column=0, padx=5, pady=5)
seleccionarBtn.grid(row=3, column=0, padx=5, pady=5)
limpiarBtn.grid(row=5, column=0, padx=5, pady=5)

# Entries Frame
entriesFrame = tkinter.LabelFrame(frame, text="Formulario", borderwidth=5)
entriesFrame.grid(row=0, column=1, sticky="ne", padx=20, pady=20)

idLabel = Label(entriesFrame, text="id", anchor="e", width=10)
nombreLabel = Label(entriesFrame, text="Nombre", anchor="e", width=10)
cantidadLabel = Label(entriesFrame, text="Cantidad", anchor="e", width=10)
unidadLabel = Label(entriesFrame, text="Unidad", anchor="e", width=10)
precioLabel = Label(entriesFrame, text="Precio", anchor="e", width=10)
categoriaLabel = Label(entriesFrame, text="Categoría", anchor="e", width=10)
stockLabel = Label(entriesFrame, text="Stock", anchor="e", width=10)

idLabel.grid(row=0, column=0, padx=10)
nombreLabel.grid(row=1, column=0, padx=10)
cantidadLabel.grid(row=2, column=0, padx=10)
unidadLabel.grid(row=3, column=0, padx=10)
precioLabel.grid(row=4, column=0, padx=10)
categoriaLabel.grid(row=5, column=0, padx=10)
stockLabel.grid(row=6, column=0, padx=10)

categoriaArray = ['Lacteos', 'Granos y Cereales', 'Enlatados', 'Especias y condimentos', 'Panaderia y galletas', 'Limpieza', 'Bebidas', 'Otros']

idEntrada = Entry(entriesFrame, width=60, textvariable=placeholderArray[0])
nombreEntrada = Entry(entriesFrame, width=60, textvariable=placeholderArray[1])
cantidadEntrada = Entry(entriesFrame, width=60, textvariable=placeholderArray[2])
unidadEntrada = Entry(entriesFrame, width=60, textvariable=placeholderArray[3])
precioEntrada = Entry(entriesFrame, width=60, textvariable=placeholderArray[4])
categoriaEntrada = ttk.Combobox(entriesFrame, width=57, textvariable=placeholderArray[5], values=categoriaArray)
stockEntrada = Entry(entriesFrame, width=60, textvariable=placeholderArray[6])

idEntrada.grid(row=0, column=1, padx=5, pady=5)
nombreEntrada.grid(row=1, column=1, padx=5, pady=5)
cantidadEntrada.grid(row=2, column=1, padx=5, pady=5)
unidadEntrada.grid(row=3, column=1, padx=5, pady=5)
precioEntrada.grid(row=4, column=1, padx=5, pady=5)
categoriaEntrada.grid(row=5, column=1, padx=5, pady=5)
stockEntrada.grid(row=6, column=1, padx=5, pady=5)

style.configure(window)

my_tree["columns"] = ("Item Id", "Nombre", "Cantidad", "Unidad", "Precio", "Categoria", "Stock")
my_tree.column("Item Id", anchor=W, width=76)
my_tree.column("Nombre", anchor=W, width=125)
my_tree.column("Cantidad", anchor=W, width=125)
my_tree.column("Unidad", anchor=W, width=100)
my_tree.column("Precio", anchor=W, width=100)
my_tree.column("Categoria", anchor=W, width=150)
my_tree.column("Stock", anchor=W, width=150)

my_tree.heading("Item Id", text="Item Id", anchor=W)
my_tree.heading("Nombre", text="Nombre", anchor=W)
my_tree.heading("Cantidad", text="Cantidad", anchor=W)
my_tree.heading("Unidad", text="Unidad", anchor=W)
my_tree.heading("Precio", text="Precio", anchor=W)
my_tree.heading("Categoria", text="Categoria", anchor=W)
my_tree.heading("Stock", text="Stock", anchor=W)

my_tree.pack()

#FUNCIONES

def registrar_producto(datos):
    # Extraer los datos del formulario
    item_id = datos[0]  # ID del producto
    nombre = datos[1]  # Nombre del producto
    cantidad = int(datos[2])  # Cantidad (convertido a entero)
    unidad = datos[3]  # Unidad de medida
    precio = float(datos[4])  # Precio (convertido a flotante)
    categoria = datos[5]  # Categoría del producto
    stock_minimo = int(datos[6])  # Stock mínimo (convertido a entero)

    # Verificar si el ID ya existe
    if item_id in productos:
        print("El ID del producto ya existe.")
        return

    # Registrar el nuevo producto en el diccionario 'productos'
    productos[item_id] = {
        "Nombre": nombre,
        "Cantidad": cantidad,
        "Unidad": unidad,
        "Precio": precio,
        "Categoría": categoria,
        "Stock mínimo": stock_minimo
    }

    print(f"Producto '{nombre}' registrado correctamente.")
    refreshTable()  # Actualiza la tabla con el nuevo producto

def actualizar_producto(placeholderArray, my_tree):
    # Obtener el ID del producto a actualizar
    item_id = placeholderArray[0].get()
    print(f"Buscando producto con ID: {item_id}")  # Agrega esta línea para depurar

    # Verificar si el ID existe en productos
    if item_id not in productos:
        print("Producto no encontrado.")
        return

    # Extraer los nuevos valores del formulario
    nombre = placeholderArray[1].get()
    cantidad = int(placeholderArray[2].get())
    unidad = placeholderArray[3].get()
    precio = float(placeholderArray[4].get())
    categoria = placeholderArray[5].get()
    stock_minimo = int(placeholderArray[6].get())

    # Actualizar los valores en el diccionario de productos
    productos[item_id] = {
        "Nombre": nombre,
        "Cantidad": cantidad,
        "Unidad": unidad,
        "Precio": precio,
        "Categoría": categoria,
        "Stock mínimo": stock_minimo
    }

    print(f"Producto '{item_id}' actualizado correctamente.")
    refreshTable()  # Actualiza la tabla con los cambios


def eliminar_producto(placeholderArray, my_tree):
    item_id = placeholderArray[0].get()

    # Verificar si el ID existe en productos
    if item_id not in productos:
        print("Producto no encontrado.")
        return

    # Eliminar el producto
    del productos[item_id]
    print(f"Producto '{item_id}' eliminado correctamente.")
    refreshTable()  # Actualiza la tabla después de la eliminación


def seleccionar_producto():
    # Obtener el ID del producto seleccionado en el Treeview
    selected_item = my_tree.selection()
    
    if not selected_item:
        print("No se ha seleccionado ningún producto.")
        return
    
    # Obtener los datos de la fila seleccionada
    item_id = my_tree.item(selected_item[0], 'values')[0]
    nombre = my_tree.item(selected_item[0], 'values')[1]
    cantidad = my_tree.item(selected_item[0], 'values')[2]
    unidad = my_tree.item(selected_item[0], 'values')[3]
    precio = my_tree.item(selected_item[0], 'values')[4]
    categoria = my_tree.item(selected_item[0], 'values')[5]
    stock_minimo = my_tree.item(selected_item[0], 'values')[6]
    
    # Llenar los campos del formulario con los datos seleccionados
    placeholderArray[0].set(item_id)
    placeholderArray[1].set(nombre)
    placeholderArray[2].set(cantidad)
    placeholderArray[3].set(unidad)
    placeholderArray[4].set(precio)
    placeholderArray[5].set(categoria)
    placeholderArray[6].set(stock_minimo)

    print(f"Producto seleccionado: {nombre} (ID: {item_id})")





refreshTable()

window.resizable(False, False)
window.mainloop()