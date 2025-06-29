import tkinter as tk
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x300")
ventana.configure(padx=20, pady=20)

# Fuente moderna
fuente = ("Segoe UI", 12)

# Entrada de tarea
entrada_tarea = ttk.Entry(ventana, font=fuente)
entrada_tarea.grid(row=0, column=0, padx=(0, 10), pady=(0, 10), sticky="ew")
ventana.columnconfigure(0, weight=1)


# Función para agregar tarea
def agregar_tarea():
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)


# Botón de agregar
boton_agregar = ttk.Button(ventana, text="Agregar", command=agregar_tarea)
boton_agregar.grid(row=0, column=1, pady=(0, 10))


# Listbox de tareas
lista_tareas = tk.Listbox(ventana, font=fuente, height=10, activestyle="none")
lista_tareas.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(0, 10))
ventana.rowconfigure(1, weight=1)

# Scrollbar para la lista
scrollbar = ttk.Scrollbar(ventana, orient="vertical",
                          command=lista_tareas.yview)
scrollbar.grid(row=1, column=2, sticky="ns")
lista_tareas.config(yscrollcommand=scrollbar.set)


# Función para eliminar tarea seleccionada
def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion[0])


# Botón de eliminar
boton_eliminar = ttk.Button(ventana, text="Eliminar", command=eliminar_tarea)
boton_eliminar.grid(row=2, column=0, columnspan=2, sticky="ew")

ventana.mainloop()
