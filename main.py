import tkinter as tk
from tkinter import ttk
import time

# Importar módulos
from MenuDesplegable import (
    diccionarioListas, seleccionarLista, crearNuevaLista,
    eliminarLista, actualizarListaTareas, actualizarMenuListas, menuDesplegable
)

# Ventana principal del gestor de tareas
ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("500x500")
ventana.configure(padx=20, pady=20, bg="white")

# Fuente para entradas
fuente = ("Segoe UI", 12)

# ==================== RELOJ DIGITAL SUPERIOR ====================

titulo = tk.Label(ventana, text='Reloj Digital', font=('Arial', 20), bg='blue', fg='white')
titulo.pack(pady=(5, 0))

reloj = tk.Label(ventana, font=('Arial', 36), bg='blue', fg='white')
reloj.pack()

fecha = tk.Label(ventana, font=('Arial', 16), bg='blue', fg='white')
fecha.pack(pady=(0, 10))

def hora():
    tiempo_actual = time.strftime('%I:%M:%S %p')
    reloj.config(text=tiempo_actual)
    fecha_actual = time.strftime('%d/%m/%Y')
    fecha.config(text=fecha_actual)
    ventana.after(1000, hora)

hora()  # Iniciar reloj

# ==================== ENTRADA DE TAREA ====================
entrada_tarea = ttk.Entry(ventana, font=fuente)
entrada_tarea.pack(fill='x', padx=10, pady=(0, 10))

# ==================== LISTA DE TAREAS ====================
frame_lista = tk.Frame(ventana)
frame_lista.pack(fill='both', expand=True)

lista_tareas = tk.Listbox(frame_lista, font=fuente, height=10, activestyle="none")
lista_tareas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=lista_tareas.yview)
scrollbar.pack(side="right", fill="y")
lista_tareas.config(yscrollcommand=scrollbar.set)

# ==================== BOTONES ====================
def agregar_tarea():
    tarea_texto = entrada_tarea.get().strip()
    if tarea_texto and MenuDesplegable.listaActiva:
        nueva_tarea = {"texto": tarea_texto, "completada": False}
        diccionarioListas[MenuDesplegable.listaActiva].append(nueva_tarea)
        actualizarListaTareas()
        entrada_tarea.delete(0, tk.END)

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion and MenuDesplegable.listaActiva:
        index = seleccion[0]
        del diccionarioListas[MenuDesplegable.listaActiva][index]
        actualizarListaTareas()

boton_frame = tk.Frame(ventana)
boton_frame.pack(fill='x', pady=10)

boton_agregar = ttk.Button(boton_frame, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack(side="left", expand=True, fill='x', padx=(0, 5))

boton_eliminar = ttk.Button(boton_frame, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(side="right", expand=True, fill='x', padx=(5, 0))

# ==================== MENÚ DESPLEGABLE ====================
# Se llama al menú que gestiona listas y lo conecta al Listbox que ya existe
import MenuDesplegable
MenuDesplegable.menuDesplegable(ventana, lista_tareas)

# Ejecutar la aplicación
ventana.mainloop()
