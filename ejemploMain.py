from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import random
import pymysql
import csv
from datetime import datetime
import numpy as np

window = tkinter.Tk()
window.title("Mercasys")
window.geometry("720x640")
my_tree = ttk.Treeview(window, show='headings', height=20)
style = ttk.Style()

placeholderArray = ['','','','','']

for i in range(0, 5):
    placeholderArray[i] = tkinter.StringVar()

dummydata = ['1', 'Apple', '10', '100', '1000']

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
    for array in dummydata:
        my_tree.insert(parent='', index='end', iid = array, text="", values=(array), tag="orow")
        my_tree.tag_configure('orow', background="#EEEEEE")
        my_tree.pack()
        
frame = tkinter.Frame(window, bg="#02577A")
frame.pack()

btnColor = "#19678E"

manageFrame = tkinter.LabelFrame(frame, text="Manage", borderwidth=5)
manageFrame.grid(row=0, column=0, sticky="w", padx=[10, 200], pady=20, ipadx=[6])

registrarBtn = Button(manageFrame, text="Registrar", width=10, borderwidth=3, bg=btnColor, fg='white')
actiualizarBtn = Button(manageFrame, text="Actualizar", width=10, borderwidth=3, bg=btnColor, fg='white')
eliminarBtn = Button(manageFrame, text="Eliminar", width=10, borderwidth=3, bg=btnColor, fg='white')
seleccionarBtn = Button(manageFrame, text="Seleccionar", width=10, borderwidth=3, bg=btnColor, fg='white')
encontrarBtn = Button(manageFrame, text="Encontrar", width=10, borderwidth=3, bg=btnColor, fg='white')
limpiarBtn = Button(manageFrame, text="Limpiar", width=10, borderwidth=3, bg=btnColor, fg='white')

registrarBtn.grid(row=0, column=0, padx=5, pady=5)
actiualizarBtn.grid(row=1, column=0, padx=5, pady=5)
eliminarBtn.grid(row=2, column=0, padx=5, pady=5)
seleccionarBtn.grid(row=3, column=0, padx=5, pady=5)
encontrarBtn.grid(row=4, column=0, padx=5, pady=5)
limpiarBtn.grid(row=5, column=0, padx=5, pady=5)

entriesFrame = tkinter.LabelFrame(frame, text="Form", borderwidth=5)
entriesFrame.grid(row=1, column=0, sticky="w", padx=[10, 200], pady=[0, 20], ipadx=[6])

itemIdLabel = Label(entriesFrame, text="Form", anchor="e", width=10)
nameLabel = Label(entriesFrame, text="Name", anchor="e", width=10)
priceLabel = Label(entriesFrame, text="Price", anchor="e", width=10)
qntLabel = Label(entriesFrame, text="QNT", anchor="e", width=10)

itemIdLabel.grid(row=0, column=0, padx=10)
nameLabel.grid(row=1, column=0, padx=10)
priceLabel.grid(row=2, column=0, padx=10)
qntLabel.grid(row=3, column=0, padx=10)

categoryArray = ['Networking Tools', 'Computer Parts', 'Repair Tools', 'Gadgets']

itemIdEntry = Entry(entriesFrame, width=50, textvariable=placeholderArray[0])
nameEntry = Entry(entriesFrame, width=50, textvariable=placeholderArray[1])
priceEntry = Entry(entriesFrame, width=50, textvariable=placeholderArray[2])
qntEntry = Entry(entriesFrame, width=50, textvariable=placeholderArray[3])
categoryCombo = ttk.Combobox(entriesFrame, width=47, textvariable=placeholderArray[4], values=categoryArray)

itemIdEntry.grid(row=0, column=2, padx=5, pady=5)
nameEntry.grid(row=1, column=2, padx=5, pady=5)
priceEntry.grid(row=2, column=2, padx=5, pady=5)
qntEntry.grid(row=3, column=2, padx=5, pady=5)
categoryCombo.grid(row=4, column=2, padx=5, pady=5)

generateIdBtn = Button(entriesFrame, text="GENERATE ID", borderwidth=3, bg=btnColor, fg='white')
generateIdBtn.grid(row=4, column=2, padx=5, pady=5)

style.configure(window)

my_tree["columns"] = ("Item Id", "Name", "Price", "Quantity", "Category", "Date")
my_tree.column("Item Id", anchor=W, width=76)
my_tree.column("Name", anchor=W, width=125)
my_tree.column("Price", anchor=W, width=125)
my_tree.column("Quantity", anchor=W, width=100)
my_tree.column("Category", anchor=W, width=150)
my_tree.column("Date", anchor=W, width=150)

my_tree.heading("Item Id", text="Item Id", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Price", text="Price", anchor=W)
my_tree.heading("Quantity", text="Quantity", anchor=W)
my_tree.heading("Category", text="Category", anchor=W)
my_tree.heading("Date", text="Date", anchor=W)

my_tree.tag_configure('row', background='#EEEEEE')
my_tree.pack()

refreshTable()

window.resizable(False, False)
window.mainloop()