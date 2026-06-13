import tkinter as Tk 
from tkinter import ttk 
from tkinter import messagebox

entrada_nombre = ttk.Entry

def saludar():
        nombre = entrada_nombre.get()
        if nombre == "":
            messagebox.showerror("error", "ingrese un nombre")

        else:
            messagebox.showinfo("saludo", f" hola{nombre}, mucho gusto")

def limpiar():
        entrada_nombre.delete(0, "end")

        ventana =Tk()
        ventana.title(" mi ventana")
        ventana.geometry("400x200")

        Label = ttk.Label(ventana, text="ingrese su nombre", font=("Blackadder ITC", 16))
        Label.pack(pady=50)

        entrada_nombre = ttk.Entry(ventana, width=14, font=("Blackadder ITC", 16))
        entrada_nombre.pack(pady=10)

        frame_botones = ttk.Frame(ventana)
        frame_botones.pack(pady=20)

        btn = ttk.Button(frame_botones, text="✔ saludar", command=saludar)
        btn.grid(column=0, row=0, padx=10)

        btn_limpiar = ttk.Button(frame_botones, text="🖊  limpiar", command=limpiar)
        btn_limpiar.grid(column=1, row=0, padx=10)

        btn_salir = ttk.Button(frame_botones, text="❌ salir", command=ventana.destroy)
        btn_salir.grid(column=2, row=0, padx=10)

        ventana.mainloop()
