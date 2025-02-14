from tkinter import *
from tkinter import ttk
import tkinter
from inventario import productos
from tkinter import messagebox

# Configuración de la ventana principal
ventana = tkinter.Tk()
ventana.title("Mercasys")
ventana.geometry("750x640")

# Cargar y mostrar el logo
logo = PhotoImage(file="Elementos\imagen2.png")
logoLabel = Label(ventana, image=logo, )
logoLabel.pack()

# Creación de la tabla (Treeview) para mostrar los productos
my_tree = ttk.Treeview(ventana, show='headings', height=20)
style = ttk.Style()

# Lista de variables de texto para los campos de entrada
placeholderArray = [tkinter.StringVar() for _ in range(7)]  # Lista de StringVar, 7 elementos

for i in range(0, 6):
    placeholderArray[i] = tkinter.StringVar()

def actualizar_tabla():
    for data in my_tree.get_children():
        my_tree.delete(data)
    for item_id, details in productos.items():
        my_tree.insert(parent='', index='end', iid=str(item_id), text="", 
                        values=(item_id, details["Nombre"], details["Cantidad"], 
                                details["Unidad"], details["Precio"], 
                                details["Categoría"], details["Stock mínimo"]), 
                        tag="orow")
        my_tree.tag_configure('orow', background="#EEEEEE")
      
# Creación del marco principal
frame = tkinter.Frame(ventana, bg="#3c5a7f")
frame.pack(fill="x", expand=True)

btnColor = "#3c5a7f"

#FUNCIONES

def registrar(datos):
    global productos
    try:
        # Extraer los datos y validar
        item_id_str = datos[0].strip()
        if not item_id_str.isdigit():
            messagebox.showwarning("Error", "El ID debe ser un número entero.")
            return
        
        item_id = int(item_id_str)
        nombre = datos[1].strip()
        cantidad_str = datos[2].strip()
        unidad = datos[3].strip()
        precio_str = datos[4].strip()
        categoria = datos[5].strip()
        stock_minimo_str = datos[6].strip()

        if not (nombre and cantidad_str and unidad and precio_str and categoria and stock_minimo_str):
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")
            return

        if not cantidad_str.isdigit() or not stock_minimo_str.isdigit():
            messagebox.showwarning("Error", "Cantidad y Stock mínimo deben ser números enteros.")
            return

        try:
            cantidad = int(cantidad_str)
            precio = float(precio_str)
            stock_minimo = int(stock_minimo_str)
        except ValueError:
            messagebox.showwarning("Error", "Cantidad debe ser entero y Precio debe ser decimal.")
            return

        # Verificar si el ID ya existe
        if item_id in productos:
            messagebox.showwarning("Error", "El ID del producto ya existe.")
            return

        # Registrar el producto
        productos[item_id] = {
            "Nombre": nombre,
            "Cantidad": cantidad,
            "Unidad": unidad,
            "Precio": precio,
            "Categoría": categoria,
            "Stock mínimo": stock_minimo
        }

        messagebox.showinfo("Éxito", f"Producto '{nombre}' registrado correctamente.")

        # Ordenar productos por ID
        
        productos = dict(sorted(productos.items()))

        actualizar_tabla()  # Actualiza la tabla con el nuevo producto ordenado

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")


def actualizar():
    try:
        selectedItem = my_tree.selection()[0]
        selectedItemId = int(my_tree.item(selectedItem)['values'][0])
    except:
        messagebox.showwarning("", "Por favor selecciona un producto")
        return

    # Obtener y validar el ID como cadena antes de convertirlo
    id_str = idEntrada.get().strip()
    if not id_str:
        messagebox.showwarning("Error", "El campo ID no puede estar vacío")
        return

    try:
        itemId = int(id_str)
    except ValueError:
        messagebox.showwarning("Error", "El ID debe ser un número.")
        return

    nombre = nombreEntrada.get().strip()
    cantidad = cantidadEntrada.get().strip()
    unidad = unidadEntrada.get().strip()
    precio = precioEntrada.get().strip()
    categoria = categoriaEntrada.get().strip()
    stock = stockEntrada.get().strip()

    # Verificar que los demás campos no estén vacíos
    if not (nombre and cantidad and unidad and precio and categoria and stock):
        messagebox.showwarning("", "Por favor llena todos los campos")
        return

    if selectedItemId != itemId:
        messagebox.showwarning("", "No puedes cambiar el ID del producto")
        return

    try:
        if itemId not in productos:
            messagebox.showwarning("", "Id no encontrado")
            return
        
        productos[itemId] = {
            "Nombre": nombre,
            "Cantidad": int(cantidad),
            "Unidad": unidad,
            "Precio": float(precio),
            "Categoría": categoria,
            "Stock mínimo": int(stock)
        }

        messagebox.showinfo("", "Producto actualizado correctamente")
    except Exception as err:
        messagebox.showwarning("", "Error occurred ref: " + str(err))
        return

    actualizar_tabla()


def seleccionar():
    try:
        selected_item = my_tree.selection()[0]  
        valores = my_tree.item(selected_item, 'values')  

        for i in range(len(placeholderArray)):
            placeholderArray[i].set(valores[i])

    except IndexError:
        messagebox.showwarning("Selección Vacía", "Por favor, selecciona un producto de la lista.")

def eliminar(placeholderArray, my_tree):
    item_id_str = placeholderArray[0].get().strip()
    
    if not item_id_str:
        messagebox.showwarning("Error", "Debe seleccionar un producto para eliminar.")
        return
    
    try:
        item_id = int(item_id_str)
    except ValueError:
        messagebox.showwarning("Error", "El ID debe ser un número válido.")
        return

    if item_id not in productos:
        messagebox.showwarning("Error", "Producto no encontrado.")
        return

    respuesta = messagebox.askyesno("Confirmación", f"¿Seguro que desea eliminar el producto ID {item_id}?")
    if not respuesta:
        return

    del productos[item_id]
    messagebox.showinfo("Éxito", f"Producto ID {item_id} eliminado correctamente.")
    actualizar_tabla()


def consultar(placeholderArray, my_tree):
    buscar_id_str = placeholderArray[0].get().strip()
    buscar_nombre = placeholderArray[1].get().strip()

    found = False

    if buscar_id_str:
        try:
            buscar_id = int(buscar_id_str)
        except ValueError:
            messagebox.showwarning("Error", "El ID debe ser un número.")
            return

        if buscar_id in productos:
            found = True
        else:
            messagebox.showinfo("Buscar", f"No se encontró un producto con ID: {buscar_id}")
            return
    elif buscar_nombre:
        for pid, details in productos.items():
            if details["Nombre"].lower() == buscar_nombre.lower():
                buscar_id = pid
                found = True
                break
        if not found:
            messagebox.showinfo("Buscar", f"No se encontró un producto con nombre: {buscar_nombre}")
            return
    else:
        messagebox.showinfo("Buscar", "Por favor, ingresa un ID o nombre para buscar.")
        return

    my_tree.selection_set(str(buscar_id))
    my_tree.focus(str(buscar_id))
    seleccionar()
    messagebox.showinfo("Buscar", f"Producto encontrado: {buscar_id} - {productos[buscar_id]['Nombre']}")

def limpiar(placeholderArray):
    for var in placeholderArray:
        var.set("")
    print("Campos limpiados")

# Sección de menú con botones
# Se crea un LabelFrame llamado "Menú" dentro del frame principal
manageFrame = tkinter.LabelFrame(frame, text="Menú", borderwidth=5)
manageFrame.grid(row=0, column=0, sticky="nw", padx=30, pady=20)

# Se crean los botones para gestionar los productos en la base de datos
registrarBtn = Button(manageFrame, text="Registrar", width=10, borderwidth=3, bg=btnColor, fg='white', command=lambda: registrar([entry.get() for entry in placeholderArray]))
actualizarBtn = Button(manageFrame, text="Actualizar", width=10, borderwidth=3, bg=btnColor, fg='white', command=actualizar)
eliminarBtn = Button(manageFrame, text="Eliminar", width=10, borderwidth=3, bg="#a74b4b", fg='white', command=lambda: eliminar(placeholderArray, my_tree))
encontrarBtn = Button(manageFrame, text="Consultar", width=10, borderwidth=3, bg=btnColor, fg='white', command=lambda: consultar(placeholderArray, my_tree))
seleccionarBtn = Button(manageFrame, text="Seleccionar", width=10, borderwidth=3, bg=btnColor, fg='white', command= seleccionar)
limpiarBtn = Button(manageFrame, text="Limpiar", width=10, borderwidth=3, bg=btnColor, fg='white', command=lambda: limpiar(placeholderArray))

# Se organizan los botones en la cuadrícula del LabelFrame "Menú"
registrarBtn.grid(row=0, column=0, padx=5, pady=5)
actualizarBtn.grid(row=1, column=0, padx=5, pady=5)
eliminarBtn.grid(row=5, column=0, padx=5, pady=5)
encontrarBtn.grid(row=2, column=0, padx=5, pady=5)
seleccionarBtn.grid(row=3, column=0, padx=5, pady=5)
limpiarBtn.grid(row=4, column=0, padx=5, pady=5)

# Sección de formulario de entrada de datos
# Se crea un LabelFrame llamado "Formulario" dentro del frame principal
entriesFrame = tkinter.LabelFrame(frame, text="Formulario", borderwidth=5)
entriesFrame.grid(row=0, column=1, sticky="ne", padx=20, pady=20)

# Se crean etiquetas para cada campo de entrada
idLabel = Label(entriesFrame, text="Id", anchor="e", width=10)
nombreLabel = Label(entriesFrame, text="Nombre", anchor="e", width=10)
cantidadLabel = Label(entriesFrame, text="Cantidad", anchor="e", width=10)
unidadLabel = Label(entriesFrame, text="Unidad", anchor="e", width=10)
precioLabel = Label(entriesFrame, text="Precio", anchor="e", width=10)
categoriaLabel = Label(entriesFrame, text="Categoría", anchor="e", width=10)
stockLabel = Label(entriesFrame, text="Stock", anchor="e", width=10)

# Se organizan las etiquetas en la cuadrícula
idLabel.grid(row=0, column=0, padx=10)
nombreLabel.grid(row=1, column=0, padx=10)
cantidadLabel.grid(row=2, column=0, padx=10)
unidadLabel.grid(row=3, column=0, padx=10)
precioLabel.grid(row=4, column=0, padx=10)
categoriaLabel.grid(row=5, column=0, padx=10)
stockLabel.grid(row=6, column=0, padx=10)

# Lista de categorías disponibles
categoriaArray = ['Lacteos', 'Granos y Cereales', 'Enlatados', 'Especias y condimentos', 'Panaderia y galletas', 'Limpieza', 'Bebidas', 'Otros']

# Campos de entrada para cada atributo del producto
idEntrada = Entry(entriesFrame, width=60, textvariable=placeholderArray[0])
nombreEntrada = Entry(entriesFrame, width=60, textvariable=placeholderArray[1])
cantidadEntrada = Entry(entriesFrame, width=60, textvariable=placeholderArray[2])
unidadEntrada = Entry(entriesFrame, width=60, textvariable=placeholderArray[3])
precioEntrada = Entry(entriesFrame, width=60, textvariable=placeholderArray[4])
categoriaEntrada = ttk.Combobox(entriesFrame, width=57, textvariable=placeholderArray[5], values=categoriaArray)
stockEntrada = Entry(entriesFrame, width=60, textvariable=placeholderArray[6])

# Se organizan los campos de entrada en la cuadrícula
idEntrada.grid(row=0, column=1, padx=5, pady=5)
nombreEntrada.grid(row=1, column=1, padx=5, pady=5)
cantidadEntrada.grid(row=2, column=1, padx=5, pady=5)
unidadEntrada.grid(row=3, column=1, padx=5, pady=5)
precioEntrada.grid(row=4, column=1, padx=5, pady=5)
categoriaEntrada.grid(row=5, column=1, padx=5, pady=5)
stockEntrada.grid(row=6, column=1, padx=5, pady=5)

# Configuración de la tabla (Treeview) para visualizar los productos
style.configure(ventana)

# Se definen las columnas de la tabla
my_tree["columns"] = ("Item Id", "Nombre", "Cantidad", "Unidad", "Precio", "Categoria", "Stock")

# Se configuran los anchos de columna y su alineación
my_tree.column("Item Id", anchor=W, width=76)
my_tree.column("Nombre", anchor=W, width=125)
my_tree.column("Cantidad", anchor=W, width=125)
my_tree.column("Unidad", anchor=W, width=100)
my_tree.column("Precio", anchor=W, width=100)
my_tree.column("Categoria", anchor=W, width=150)
my_tree.column("Stock", anchor=W, width=150)

# Se establecen los encabezados de cada columna
my_tree.heading("Item Id", text="Item Id", anchor=W)
my_tree.heading("Nombre", text="Nombre", anchor=W)
my_tree.heading("Cantidad", text="Cantidad", anchor=W)
my_tree.heading("Unidad", text="Unidad", anchor=W)
my_tree.heading("Precio", text="Precio", anchor=W)
my_tree.heading("Categoria", text="Categoria", anchor=W)
my_tree.heading("Stock", text="Stock", anchor=W)

# Se muestra la tabla en la interfaz
my_tree.pack()

actualizar_tabla()

# Se bloquea el redimensionamiento de la ventana para mantener el diseño
ventana.resizable(False, False)

# Se inicia el bucle principal de la interfaz gráfica
ventana.mainloop()