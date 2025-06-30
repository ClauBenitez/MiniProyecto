# main.py
import tkinter as tk
from tkinter import ttk
import MenuDesplegable
import AgregoEliminarTarea

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("600x400")
ventana.configure(padx=20, pady=20)

# Listbox de tareas
lista_tareas = tk.Listbox(ventana, font=("Segoe UI", 12), height=12, activestyle="none")
lista_tareas.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(10, 10))
ventana.rowconfigure(1, weight=1)
ventana.columnconfigure(0, weight=1)

# Entry de tarea
entrada = ttk.Entry(ventana, font=("Segoe UI", 12))
entrada.grid(row=0, column=0, padx=(0, 10), pady=(10, 0), sticky="ew")

# Scrollbar para la lista de tareas
scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=lista_tareas.yview)
scrollbar.grid(row=1, column=2, sticky="ns")
lista_tareas.config(yscrollcommand=scrollbar.set)

# Integración con módulos
MenuDesplegable.menuDesplegable(ventana, lista_tareas)
AgregoEliminarTarea.configurar(entrada, lista_tareas)

# Botón para agregar tarea
boton_agregar = ttk.Button(ventana, text="Agregar", command=AgregoEliminarTarea.agregar_tarea)
boton_agregar.grid(row=0, column=1, pady=(10, 0))

# Botón para eliminar tarea
boton_eliminar = ttk.Button(ventana, text="Eliminar", command=AgregoEliminarTarea.eliminar_tarea)
boton_eliminar.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 10))

ventana.mainloop()
