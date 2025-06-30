# agregarEliminarTareas.py
import tkinter as tk
import MenuDesplegable as menu

entrada_tarea = None
lista_tareas = None


def configurar(entry_widget, listbox_widget):
    global entrada_tarea, lista_tareas
    entrada_tarea = entry_widget
    lista_tareas = listbox_widget


def agregar_tarea():
    if not entrada_tarea or not menu.listaActiva:
        return

    texto = entrada_tarea.get().strip()
    if texto:
        menu.diccionarioListas[menu.listaActiva].append(
            {"texto": texto, "completada": False})
        entrada_tarea.delete(0, tk.END)
        menu.actualizarListaTareas()


def eliminar_tarea():
    if not lista_tareas or not menu.listaActiva:
        return

    seleccion = lista_tareas.curselection()
    if seleccion:
        del menu.diccionarioListas[menu.listaActiva][seleccion[0]]
        menu.actualizarListaTareas()
