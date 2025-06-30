# Importaciones
import tkinter as tk
from tkinter import simpledialog, messagebox

# Diccionario principal que almacena las listas y sus tareas
# Cada lista tiene una lista de tareas, y cada tarea es un diccionario con texto y estado
diccionarioListas = {
    "Lista 1": [
        {"texto": "Estudiar para el parcial", "completada": False},
        {"texto": "Leer apuntes", "completada": True}
    ],
    "Lista 2": [
        {"texto": "Comprar útiles", "completada": False},
        {"texto": "Armar presentación", "completada": False}
    ]
}

# Variables globales para controlar el estado actual
listaActiva = None  # Nombre de la lista seleccionada actualmente
listaTareas = None  # Referencia al widget Listbox donde se muestran las tareas
menuListas = None  # Referencia al menú desplegable con las listas

# Función que actualiza el contenido del Listbox con las tareas de la lista activa


def actualizarListaTareas():
    # Si no hay un Listbox asignado, no hace nada
    if listaTareas is None:
        return
    # Limpia todo lo que haya en el Listbox antes de actualizar
    listaTareas.delete(0, tk.END)

    # Si no hay lista activa o la lista activa no existe en el diccionario
    # se muestra un mensaje indicando que no hay lista seleccionada
    if not listaActiva or listaActiva not in diccionarioListas:
        listaTareas.insert(tk.END, "(Sin lista activa)")
        return

    # Si hay una lista activa, recorre sus tareas y las muestra en el Listbox
    for tarea in diccionarioListas[listaActiva]:
        texto = tarea["texto"]
        # Si la tarea está marcada como completada, añade un check al texto
        if tarea["completada"]:
            texto += " ✔️"
        listaTareas.insert(tk.END, texto)

# Función para seleccionar una lista y actualizar la vista de tareas


def seleccionarLista(nombreLista):
    global listaActiva
    listaActiva = nombreLista
    actualizarListaTareas()

# Función para crear una nueva lista, solicitando al usuario el nombre


def crearNuevaLista():
    global listaActiva
    # Pide al usuario que ingrese el nombre de la nueva lista
    nombreNueva = simpledialog.askstring(
        "Nueva lista", "Ingrese el nombre de la nueva lista:")
    # Solo crea la lista si el nombre no está vacío ni existe ya
    if nombreNueva and nombreNueva.strip() and nombreNueva not in diccionarioListas:
        # Añade la lista vacía al diccionario
        diccionarioListas[nombreNueva] = []
        listaActiva = nombreNueva  # La pone como lista activa
        actualizarMenuListas()  # Actualiza el menú de listas para que aparezca la nueva
        actualizarListaTareas()  # Actualiza la vista de tareas (vacía por ahora)

# Función para eliminar una lista existente


def eliminarLista():
    global listaActiva
    # Si no hay listas, muestra advertencia y no hace nada
    if len(diccionarioListas) == 0:
        messagebox.showwarning(
            "No permitido.", "Debe existir al menos una lista.")
        return
    # Pide al usuario el nombre exacto de la lista que quiere borrar, mostrando las opciones
    opciones = [nombre for nombre in diccionarioListas]
    nombreAEliminar = simpledialog.askstring(
        "Eliminar lista",
        "Nombre exacto de la lista a borrar:\n\n" + "\n".join(opciones)
    )
    # Si el nombre existe en el diccionario, pide confirmación para borrar
    if nombreAEliminar and nombreAEliminar in diccionarioListas:
        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Seguro que desea borrar la lista '{nombreAEliminar}'?\nSe perderán todas sus tareas."
        )
        # Si la lista borrada era la activa, limpia la lista activa
        if confirmar:
            fueListaActiva = nombreAEliminar == listaActiva
            del diccionarioListas[nombreAEliminar]

            if fueListaActiva:
                if diccionarioListas:
                    listaActiva = None

            actualizarMenuListas()  # Actualiza el menú para reflejar la eliminación
            actualizarListaTareas()  # Actualiza la vista de tareas

    # Si el usuario ingresó un nombre que no existe, muestra error
    elif nombreAEliminar:
        messagebox.showerror(
            "Error", f"La lista: '{nombreAEliminar}' no existe.")

# Función para actualizar el menú desplegable con las listas actuales


def actualizarMenuListas():
    # Si el menú no está creado, no hace nada
    if menuListas is None:
        return
    menuListas.delete(0, tk.END)  # Limpia las opciones del menú

    menuListas.add_command(label="Crear nueva lista", command=crearNuevaLista)
    menuListas.add_separator()  # Separador visual en el menú

    # Añade una opción por cada lista existente para poder seleccionarla
    for nombreLista in diccionarioListas:
        # El lambda guarda el nombre para que se pase a seleccionarLista correctamente
        menuListas.add_command(
            label=nombreLista, command=lambda n=nombreLista: seleccionarLista(n))

    menuListas.add_separator()
    menuListas.add_command(label="Eliminar lista", command=eliminarLista)

# Función para crear el menú desplegable y asociarlo a la ventana y Listbox


def menuDesplegable(ventana, listbox):
    global listaTareas, menuListas
    listaTareas = listbox  # Guarda la referencia al Listbox para actualizarlo

    # evento toggle
    listaTareas.bind("<Double-Button-1>", toggle_completada)


    # Crea la barra de menú en la ventana principal
    barraMenu = tk.Menu(ventana)
    ventana.config(menu=barraMenu)  # Asocia la barra de menú a la ventana

    # Crea el menú desplegable de listas
    menuListas = tk.Menu(barraMenu, tearoff=0)
    # Añade el menú desplegable a la barra con etiqueta "Listas"
    barraMenu.add_cascade(label="Listas", menu=menuListas)

    actualizarMenuListas()  # Inicializa el menú con las listas actuales
    actualizarListaTareas()  # Muestra las tareas de la lista activa (o el mensaje si no hay)

# Checkbox
def toggle_completada(event):
    if not listaActiva or listaActiva not in diccionarioListas or listaTareas is None:
        return

    seleccion = listaTareas.curselection()
    if not seleccion:
        return

    indice = seleccion[0]
    tarea = diccionarioListas[listaActiva][indice]
    tarea["completada"] = not tarea["completada"]
    actualizarListaTareas()

