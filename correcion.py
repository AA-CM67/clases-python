import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def saludar():
    nombre = entrada_nombre.get()

    if nombre == "":
        messagebox.showwarning("error","ingresa un nombre")

    else:
        messagebox.showinfo("Saludo",f"Hola {nombre} mucho gusto")

def limpiar():
    entrada_nombre.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Mi Ventana")
ventana.geometry("500x250")

label_nombre = ttk.Label(ventana, text="ingrese su nombre:",font=("Blackadder ITC", 14))
label_nombre.pack(pady=15)

entrada_nombre = ttk.Entry(ventana, width=35, font=("Blackadder ITC", 16))
entrada_nombre.pack(pady=10)

frame_botones = ttk.Frame(ventana)
frame_botones.pack(pady=20)

btn_saludar = ttk.Button(frame_botones, text="✔  Saludar", command=saludar)
btn_saludar.grid(row=0, column=0, padx=10)

btn_limpiar = ttk.Button(frame_botones, text="🖊 Limpiar", command=limpiar)
btn_limpiar.grid(row=0, column=1, padx=10)

btn_salir = ttk.Button(frame_botones, text="✖ Salir", command=ventana.destroy)
btn_salir.grid(row=0, column=2, padx=10)

ventana.mainloop()