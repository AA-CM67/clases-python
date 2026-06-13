import tkinter as tk
from tkinter import messagebox
import random

opciones = ["papel", "piedra", "tijeras"]

def jugar(jugador):
    computadora = random.choice(opciones)
    
    if jugador == computadora:
        resultado = f"la computadora eligio {computadora}. n¡empate! se juega otra ronda."
    elif (
        (jugador == "papel" and computadora == "piedra") or
        (jugador == "piedra" and computadora == "tijeras") or
        (jugador == "tijeras" and computadora == "papel")
    ):  
        resultado = f"la computadora eligio {computadora}. ¡ganaste la partida!"
    else:
        resultado = f"la computadora elegio {computadora}. ¡perdiste!"
    messagebox.showinfo("Resultado", resultado)


ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijeras")
ventana.geometry("500x400")
ventana.config(bg="black")

titulo = tk.Label(ventana, text=" ¡papel, piedra o tijeras!", font=( "Edwardian Script ITC", 24, "bold"),fg="white", bg="black" )
titulo.pack(pady=20)

instruccion = tk.Label(ventana, text="elige tu opción:", font=("Edwardian Script ITC", 18), fg="white", bg="black")
instruccion.place(x=220, y=120)
instruccion.pack(pady=10)

boton_papel = tk.Button(ventana, text="papel", font=("Edwardian Script ITC", 18), fg="#00FF00", bg="black", activeforeground="#00FF00", activebackground="black", width=12,command=lambda: jugar("papel"))
boton_piedra = tk.Button(ventana, text="piedra", font=("Edwardian Script ITC", 18), fg="#00FF00", bg="black", activeforeground="#00FF00", activebackground="black", width=12,command=lambda: jugar("piedra"))
boton_tijeras = tk.Button(ventana, text="tijeras", font=("Edwardian Script ITC", 18), fg="#00FF00", bg="black", activeforeground="#00FF00", activebackground="black", width=12,command=lambda: jugar("tijeras"))

boton_papel.pack(pady=10)
boton_piedra.pack(pady=10)
boton_tijeras.pack(pady=10)

ventana.mainloop()
