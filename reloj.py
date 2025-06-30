import tkinter as tk
import time

ventana = tk.Tk()
ventana.title('Reloj simple')
ventana.geometry('400x300')
ventana.configure(bg='blue')

titulo = tk.Label(ventana, text='Reloj Digital', font=('Arial', 24), bg='blue', fg='white')
titulo.pack(pady=20)

reloj = tk.Label(ventana, font=('Arial', 60), bg='blue', fg='white')
reloj.pack(anchor='center')

fecha = tk.Label(ventana, font=('Arial', 24), bg='blue', fg='white')
fecha.pack(pady=20)

def hora():
    tiempo_actual = time.strftime('%I:%M:%S %p')
    reloj.config(text=tiempo_actual)
    fecha_actual = time.strftime('%d/%m/%Y')
    fecha.config(text=fecha_actual)
    ventana.after(1000, hora)

hora()
ventana.mainloop()