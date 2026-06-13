import tkinter as tk
from tkinter import messagebox

# Saldo inicial
saldo = 100000

# Función consultar saldo
def consultar_saldo():
    messagebox.showinfo("Saldo", f"Tu saldo es: ${saldo}")

# Función retirar dinero
def retirar():
    global saldo
    
    cantidad = int(entrada.get())

    if cantidad <= saldo:
        saldo -= cantidad
        messagebox.showinfo("Retiro", f"Retiro exitoso\nNuevo saldo: ${saldo}")
    else:
        messagebox.showerror("Error", "Saldo insuficiente")

# Crear ventana
ventana = tk.Tk()
ventana.title("Cajero Automático")
ventana.geometry("350x250")
ventana.config(bg="lightblue")

# Título
titulo = tk.Label(
    ventana,
    text="🏦 CAJERO AUTOMÁTICO",
    font=("Arial", 16, "bold"),
    bg="lightblue"
)
titulo.pack(pady=10)

# Entrada de dinero
label = tk.Label(
    ventana,
    text="Ingrese cantidad:",
    bg="lightblue",
    font=("Arial", 12)
)
label.pack()

entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

# Botón retirar
btn_retirar = tk.Button(
    ventana,
    text="Retirar",
    command=retirar,
    bg="green",
    fg="white",
    font=("Arial", 12)
)
btn_retirar.pack(pady=10)

# Botón consultar saldo
btn_saldo = tk.Button(
    ventana,
    text="Consultar saldo",
    command=consultar_saldo,
    bg="blue",
    fg="white",
    font=("Arial", 12)
)
btn_saldo.pack(pady=5)

# Ejecutar ventana
ventana.mainloop()