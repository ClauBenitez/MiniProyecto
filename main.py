import tkinter as tk
from AgregoEliminarTarea import GestorTareas
from MenuDesplegable import MenuFiltro
from reloj import Reloj

def main():
    ventana = tk.Tk()
    ventana.title("Gestor de Tareas Diarias")
    ventana.geometry("500x500")

    reloj = Reloj(ventana)
    gestor = GestorTareas(ventana)
    menu = MenuFiltro(ventana, gestor)

    ventana.mainloop()

if __name__ == "__main__":
    main()
