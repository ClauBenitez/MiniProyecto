import tkinter as tk
from AgregoEliminarTarea import GestorTareas
from MenuDesplegable import MenuFiltro
from reloj import Reloj

def main():
    ventana = tk.Tk()
    ventana.title("Gestor de Tareas Diarias- oasjoasjdoasjdosd")
    ventana.geometry("500x500")

    reloj = Reloj(ventana)
    gestor = GestorTareas(ventana)
    menu = MenuFiltro(ventana, gestor)

    ventana.mainloop()

if __name__ == "__main__":
    main()
#este es solo la carcaza hay que adecuar en funcion de la adecuacion de los modulos de ustedes