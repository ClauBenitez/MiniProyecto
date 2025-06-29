import tkinter as tk
from MenuDesplegable import menuDesplegable
# Comentado temporalmente porque el módulo abre ventana propia al importarse
#from AgregoEliminarTarea import GestorTareas
#from reloj import Reloj

def main():
    ventana = tk.Tk() # Crear ventana principal de la aplicación
    ventana.title("Gestor de Tareas Diarias")
    ventana.geometry("500x500")

    # Estas líneas se comentaron para evitar conflicto de ventanas múltiples
    # ya que lo demas modulos se van a modificar, decidi comentarlos.
    """ reloj = Reloj(ventana)
    gestor = GestorTareas(ventana) """


    lista_tareas = tk.Listbox(ventana) # Creo un widget Listbox para mostrar tareas
    lista_tareas.pack(fill=tk.BOTH, expand=True) # Ubico el Listbox para que se adapte al tamaño de ventana
    menu = menuDesplegable(ventana, lista_tareas) # Creo y asocio el menú desplegable, pasándole ventana y Listbox

    ventana.mainloop()

if __name__ == "__main__":
    main()
#este es solo la carcaza hay que adecuar en funcion de la adecuacion de los modulos de ustedes