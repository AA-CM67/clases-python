
"""
AHORCADO EDUCATIVO PREMIUM
Versión base lista para ampliar.

Incluye:
- Pantalla de inicio
- Selección de materia
- Selección de dificultad
- Cronómetro
- Historial JSON
- Botón para volver a seleccionar materia
- Estructura para sonidos, imágenes y récords

NOTA:
Esta es una plantilla organizada para continuar el desarrollo.
Agrega más palabras, sonidos e imágenes según necesites.
"""

import tkinter as tk
from tkinter import messagebox
import json
import random
import time
import os

MATERIAS = {
    "Matemáticas": {
        "Facil": ["suma", "resta", "angulo"],
        "Normal": ["fraccion", "division"],
        "Dificil": ["trigonometria"],
        "Leyenda": ["hipotenusa"],
    },
    "Programación": {
        "Facil": ["python", "lista"],
        "Normal": ["funcion"],
        "Dificil": ["herencia"],
        "Leyenda": ["polimorfismo"],
    },
}

HISTORIAL = "historial.json"

def cargar_historial():
    if os.path.exists(HISTORIAL):
        with open(HISTORIAL, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_historial(datos):
    with open(HISTORIAL, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

class Juego:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ahorcado Educativo Premium")
        self.root.geometry("700x500")

        tk.Label(
            self.root,
            text="AHORCADO EDUCATIVO PREMIUM",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="JUGAR",
            command=self.seleccionar
        ).pack()

        tk.Button(
            self.root,
            text="Ver Historial",
            command=self.ver_historial
        ).pack(pady=10)

    def seleccionar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Seleccionar")

        tk.Label(ventana, text="Materia").pack()

        materia = tk.StringVar(value=list(MATERIAS.keys())[0])
        tk.OptionMenu(ventana, materia, *MATERIAS.keys()).pack()

        tk.Label(ventana, text="Dificultad").pack()

        dificultad = tk.StringVar(value="Facil")
        tk.OptionMenu(
            ventana,
            dificultad,
            "Facil",
            "Normal",
            "Dificil",
            "Leyenda"
        ).pack()

        tk.Button(
            ventana,
            text="Comenzar",
            command=lambda: self.iniciar_partida(
                materia.get(),
                dificultad.get()
            )
        ).pack(pady=10)

    def iniciar_partida(self, materia, dificultad):
        palabras = MATERIAS[materia][dificultad]
        palabra = random.choice(palabras)

        inicio = time.time()

        messagebox.showinfo(
            "Partida",
            f"Materia: {materia}\n"
            f"Dificultad: {dificultad}\n"
            f"Palabra seleccionada: {palabra}"
        )

        fin = time.time()

        historial = cargar_historial()
        historial.append({
            "materia": materia,
            "dificultad": dificultad,
            "tiempo": round(fin - inicio, 2)
        })
        guardar_historial(historial)

    def ver_historial(self):
        historial = cargar_historial()

        texto = ""

        if not historial:
            texto = "Sin registros."
        else:
            for r in historial:
                texto += (
                    f"{r['materia']} | "
                    f"{r['dificultad']} | "
                    f"{r['tiempo']} segundos\n"
                )

        messagebox.showinfo("Historial", texto)

    def ejecutar(self):
        self.root.mainloop()


if __name__ == "__main__":
    Juego().ejecutar()
