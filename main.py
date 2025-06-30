# main.py
import tkinter as tk
from tkinter import ttk
import time
import MenuDesplegable
import AgregoEliminarTarea

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("600x400")
ventana.configure(padx=20, pady=20)

# Etiquetas para reloj y fecha
label_reloj = tk.Label(ventana, font=("Segoe UI", 16))
label_reloj.grid(row=3, column=0, sticky="w", pady=(10, 0))

label_fecha = tk.Label(ventana, font=("Segoe UI", 16))
label_fecha.grid(row=3, column=1, sticky="e", pady=(10, 0))

# funcion para actualizar el reloj


def actualizar_reloj():
    tiempo_actual = time.strftime('%I:%M:%S %p')
    fecha_actual = time.strftime('%d/%m/%Y')
    label_reloj.config(text=tiempo_actual)
    label_fecha.config(text=fecha_actual)
    ventana.after(1000, actualizar_reloj)


# Listbox de tareas
lista_tareas = tk.Listbox(ventana, font=(
    "Segoe UI", 12), height=12, activestyle="none")
lista_tareas.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(10, 10))
ventana.rowconfigure(1, weight=1)
ventana.columnconfigure(0, weight=1)

# Entry de tarea
entrada = ttk.Entry(ventana, font=("Segoe UI", 12))
entrada.grid(row=0, column=0, padx=(0, 10), pady=(10, 0), sticky="ew")

# Scrollbar para la lista de tareas
scrollbar = ttk.Scrollbar(ventana, orient="vertical",
                          command=lista_tareas.yview)
scrollbar.grid(row=1, column=2, sticky="ns")
lista_tareas.config(yscrollcommand=scrollbar.set)

# Integración con módulos
MenuDesplegable.menuDesplegable(ventana, lista_tareas)
AgregoEliminarTarea.configurar(entrada, lista_tareas)

# Botón para agregar tarea
boton_agregar = ttk.Button(ventana, text="Agregar",
                           command=AgregoEliminarTarea.agregar_tarea)
boton_agregar.grid(row=0, column=1, pady=(10, 0))

# Botón para eliminar tarea
boton_eliminar = ttk.Button(
    ventana, text="Eliminar", command=AgregoEliminarTarea.eliminar_tarea)
boton_eliminar.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 10))


actualizar_reloj()
ventana.mainloop()
