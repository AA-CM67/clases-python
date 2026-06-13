import tkinter as tk
from tkinter import messagebox

# ==========================================
# CLASE CUENTA
# ==========================================

class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return True
        return False

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return True
        return False


# ==========================================
# CLASE CAJERO CON INTERFAZ
# ==========================================

class CajeroGUI:

    def __init__(self, ventana):

        self.cuenta = Cuenta("Juan Pérez", 1000000)

        self.ventana = ventana
        self.ventana.title("🏦 Cajero Automático")
        self.ventana.geometry("400x500")
        self.ventana.config(bg="#dbeafe")

        # TÍTULO
        titulo = tk.Label(
            ventana,
            text="🏦 CAJERO AUTOMÁTICO",
            font=("Arial", 18, "bold"),
            bg="#dbeafe"
        )
        titulo.pack(pady=20)

        # SALDO
        self.label_saldo = tk.Label(
            ventana,
            text=f"Saldo: ${self.cuenta.saldo:,.0f}",
            font=("Arial", 14),
            bg="#dbeafe"
        )
        self.label_saldo.pack(pady=10)

        # ENTRADA
        self.entry_monto = tk.Entry(
            ventana,
            font=("Arial", 14)
        )
        self.entry_monto.pack(pady=10)

        # BOTÓN DEPOSITAR
        btn_depositar = tk.Button(
            ventana,
            text="📥 Depositar",
            font=("Arial", 12),
            bg="green",
            fg="white",
            width=20,
            command=self.depositar
        )
        btn_depositar.pack(pady=10)

        # BOTÓN RETIRAR
        btn_retirar = tk.Button(
            ventana,
            text="📤 Retirar",
            font=("Arial", 12),
            bg="red",
            fg="white",
            width=20,
            command=self.retirar
        )
        btn_retirar.pack(pady=10)

        # BOTÓN CONSULTAR
        btn_consultar = tk.Button(
            ventana,
            text="💰 Consultar Saldo",
            font=("Arial", 12),
            bg="blue",
            fg="white",
            width=20,
            command=self.consultar
        )
        btn_consultar.pack(pady=10)

        # BOTÓN SALIR
        btn_salir = tk.Button(
            ventana,
            text="🚪 Salir",
            font=("Arial", 12),
            bg="black",
            fg="white",
            width=20,
            command=ventana.quit
        )
        btn_salir.pack(pady=20)

    def actualizar_saldo(self):
        self.label_saldo.config(
            text=f"Saldo: ${self.cuenta.saldo:,.0f}"
        )

    def depositar(self):

        try:
            monto = float(self.entry_monto.get())

            if self.cuenta.depositar(monto):
                messagebox.showinfo(
                    "Éxito",
                    f"Depósito exitoso de ${monto:,.0f}"
                )
                self.actualizar_saldo()
            else:
                messagebox.showerror(
                    "Error",
                    "Monto inválido"
                )

        except:
            messagebox.showerror(
                "Error",
                "Ingrese un número válido"
            )

    def retirar(self):

        try:
            monto = float(self.entry_monto.get())

            if self.cuenta.retirar(monto):
                messagebox.showinfo(
                    "Éxito",
                    f"Retiro exitoso de ${monto:,.0f}"
                )
                self.actualizar_saldo()
            else:
                messagebox.showerror(
                    "Error",
                    "Fondos insuficientes"
                )

        except:
            messagebox.showerror(
                "Error",
                "Ingrese un número válido"
            )

    def consultar(self):

        messagebox.showinfo(
            "Saldo",
            f"Saldo disponible:\n${self.cuenta.saldo:,.0f}"
        )


# ==========================================
# EJECUTAR PROGRAMA
# ==========================================

ventana = tk.Tk()

app = CajeroGUI(ventana)

ventana.mainloop()