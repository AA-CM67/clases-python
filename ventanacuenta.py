"""
🏦 CAJERO AUTOMÁTICO CON INTERFAZ GRÁFICA
Versión Tkinter + POO
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict
import tkinter as tk
from tkinter import messagebox, simpledialog


# ═══════════════════════════════════════════════════════
# CLASE ABSTRACTA
# ═══════════════════════════════════════════════════════
class CuentaBancaria(ABC):

    def __init__(self, numero_cuenta, titular, saldo=0):
        self._numero_cuenta = numero_cuenta
        self._titular = titular
        self._saldo = saldo
        self._historial = []

    @abstractmethod
    def calcular_comision(self, monto):
        pass

    @abstractmethod
    def get_tipo_cuenta(self):
        pass

    def depositar(self, monto):

        if monto > 0:
            self._saldo += monto

            self._registrar(
                "DEPÓSITO",
                monto
            )

            return True

        return False

    def retirar(self, monto):

        if monto <= 0:
            return False

        comision = self.calcular_comision(monto)

        total = monto + comision

        if total <= self._saldo:

            self._saldo -= total

            self._registrar(
                "RETIRO",
                -monto,
                f"Comisión ${comision:,.0f}"
            )

            return True

        return False

    def _registrar(self, tipo, monto, detalle=""):

        self._historial.append({
            "fecha": datetime.now(),
            "tipo": tipo,
            "monto": monto,
            "detalle": detalle
        })

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero_cuenta(self):
        return self._numero_cuenta

    @property
    def titular(self):
        return self._titular

    def get_historial(self):
        return self._historial.copy()


# ═══════════════════════════════════════════════════════
# CUENTA AHORROS
# ═══════════════════════════════════════════════════════
class CuentaAhorros(CuentaBancaria):

    def calcular_comision(self, monto):
        return 0

    def get_tipo_cuenta(self):
        return "💰 AHORROS"


# ═══════════════════════════════════════════════════════
# CUENTA CORRIENTE
# ═══════════════════════════════════════════════════════
class CuentaCorriente(CuentaBancaria):

    def __init__(
        self,
        numero_cuenta,
        titular,
        saldo=0,
        limite_sobregiro=500000
    ):

        super().__init__(
            numero_cuenta,
            titular,
            saldo
        )

        self._limite_sobregiro = limite_sobregiro

    def calcular_comision(self, monto):
        return monto * 0.02

    def get_tipo_cuenta(self):
        return "🏦 CORRIENTE"

    def retirar(self, monto):

        comision = self.calcular_comision(monto)

        total = monto + comision

        if total <= (
            self._saldo + self._limite_sobregiro
        ):

            self._saldo -= total

            self._registrar(
                "RETIRO",
                -monto,
                f"Comisión ${comision:,.0f}"
            )

            return True

        return False


# ═══════════════════════════════════════════════════════
# CUENTA NÓMINA
# ═══════════════════════════════════════════════════════
class CuentaNomina(CuentaBancaria):

    def calcular_comision(self, monto):
        return 0

    def get_tipo_cuenta(self):
        return "💼 NÓMINA"


# ═══════════════════════════════════════════════════════
# USUARIO
# ═══════════════════════════════════════════════════════
class Usuario:

    def __init__(self, nombre, pin):

        self._nombre = nombre
        self._pin = pin
        self._cuentas = {}

    def agregar_cuenta(self, cuenta):

        self._cuentas[
            cuenta.numero_cuenta
        ] = cuenta

    def verificar_pin(self, pin):

        return self._pin == pin

    def listar_cuentas(self):

        return list(
            self._cuentas.values()
        )

    @property
    def nombre(self):
        return self._nombre


# ═══════════════════════════════════════════════════════
# INTERFAZ GRÁFICA
# ═══════════════════════════════════════════════════════
class CajeroGUI:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "🏦 Cajero Automático"
        )

        self.root.geometry(
            "650x550"
        )

        self.root.configure(
            bg="#dfefff"
        )

        self.usuarios = {}

        self.usuario_actual = None

        self.cuenta_actual = None

        self.crear_usuarios()

        self.login()

    # ═══════════════════════════════════════════════════
    # USUARIOS DEMO
    # ═══════════════════════════════════════════════════
    def crear_usuarios(self):

        usuario1 = Usuario(
            "Juan Pérez",
            "1234"
        )

        usuario1.agregar_cuenta(
            CuentaAhorros(
                "001",
                "Juan Pérez",
                1000000
            )
        )

        self.usuarios["001"] = usuario1

        usuario2 = Usuario(
            "María García",
            "5678"
        )

        usuario2.agregar_cuenta(
            CuentaCorriente(
                "002",
                "María García",
                2000000
            )
        )

        self.usuarios["002"] = usuario2

        usuario3 = Usuario(
            "Carlos López",
            "9999"
        )

        usuario3.agregar_cuenta(
            CuentaNomina(
                "004",
                "Carlos López",
                750000
            )
        )

        self.usuarios["004"] = usuario3

    # ═══════════════════════════════════════════════════
    # LIMPIAR
    # ═══════════════════════════════════════════════════
    def limpiar(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    # ═══════════════════════════════════════════════════
    # LOGIN
    # ═══════════════════════════════════════════════════
    def login(self):

        self.limpiar()

        tk.Label(
            self.root,
            text="🏦 CAJERO AUTOMÁTICO",
            font=("Arial", 24, "bold"),
            bg="#dfefff"
        ).pack(pady=20)

        tk.Label(
            self.root,
            text="Número de cuenta",
            bg="#dfefff"
        ).pack()

        self.entry_cuenta = tk.Entry(
            self.root,
            font=("Arial", 14)
        )

        self.entry_cuenta.pack(
            pady=5
        )

        tk.Label(
            self.root,
            text="PIN",
            bg="#dfefff"
        ).pack()

        self.entry_pin = tk.Entry(
            self.root,
            show="*",
            font=("Arial", 14)
        )

        self.entry_pin.pack(
            pady=5
        )

        tk.Button(
            self.root,
            text="Iniciar Sesión",
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.autenticar
        ).pack(
            pady=20
        )

        tk.Label(
            self.root,
            text="Usuarios Demo\n001 → 1234\n002 → 5678\n004 → 9999",
            bg="#dfefff",
            font=("Arial", 11)
        ).pack(
            pady=10
        )

    # ═══════════════════════════════════════════════════
    # AUTENTICAR
    # ═══════════════════════════════════════════════════
    def autenticar(self):

        cuenta = self.entry_cuenta.get()

        pin = self.entry_pin.get()

        if cuenta in self.usuarios:

            usuario = self.usuarios[cuenta]

            if usuario.verificar_pin(pin):

                self.usuario_actual = usuario

                self.cuenta_actual = (
                    usuario.listar_cuentas()[0]
                )

                messagebox.showinfo(
                    "Bienvenido",
                    f"Hola {usuario.nombre}"
                )

                self.menu()

            else:

                messagebox.showerror(
                    "Error",
                    "PIN incorrecto"
                )

        else:

            messagebox.showerror(
                "Error",
                "Cuenta no encontrada"
            )

    # ═══════════════════════════════════════════════════
    # MENÚ
    # ═══════════════════════════════════════════════════
    def menu(self):

        self.limpiar()

        tk.Label(
            self.root,
            text=f"Bienvenido {self.usuario_actual.nombre}",
            font=("Arial", 20, "bold"),
            bg="#dfefff"
        ).pack(
            pady=20
        )

        self.label_saldo = tk.Label(
            self.root,
            text=f"💰 Saldo: ${self.cuenta_actual.saldo:,.0f}",
            font=("Arial", 18),
            bg="#dfefff"
        )

        self.label_saldo.pack(
            pady=10
        )

        botones = [

            ("Consultar Saldo", self.consultar_saldo),

            ("Depositar", self.depositar),

            ("Retirar", self.retirar),

            ("Ver Historial", self.historial),

            ("Cerrar Sesión", self.login)
        ]

        for texto, funcion in botones:

            tk.Button(
                self.root,
                text=texto,
                width=25,
                height=2,
                font=("Arial", 12),
                command=funcion
            ).pack(
                pady=6
            )

    # ═══════════════════════════════════════════════════
    # ACTUALIZAR SALDO
    # ═══════════════════════════════════════════════════
    def actualizar_saldo(self):

        self.label_saldo.config(
            text=f"💰 Saldo: ${self.cuenta_actual.saldo:,.0f}"
        )

    # ═══════════════════════════════════════════════════
    # CONSULTAR
    # ═══════════════════════════════════════════════════
    def consultar_saldo(self):

        messagebox.showinfo(
            "Saldo",
            f"Saldo disponible:\n${self.cuenta_actual.saldo:,.0f}"
        )

    # ═══════════════════════════════════════════════════
    # DEPOSITAR
    # ═══════════════════════════════════════════════════
    def depositar(self):

        monto = simpledialog.askfloat(
            "Depositar",
            "Ingrese monto:"
        )

        if monto:

            if self.cuenta_actual.depositar(monto):

                messagebox.showinfo(
                    "Éxito",
                    f"Depósito exitoso\n${monto:,.0f}"
                )

                self.actualizar_saldo()

            else:

                messagebox.showerror(
                    "Error",
                    "Monto inválido"
                )

    # ═══════════════════════════════════════════════════
    # RETIRAR
    # ═══════════════════════════════════════════════════
    def retirar(self):

        monto = simpledialog.askfloat(
            "Retirar",
            "Ingrese monto:"
        )

        if monto:

            if self.cuenta_actual.retirar(monto):

                messagebox.showinfo(
                    "Éxito",
                    f"Retiro exitoso\n${monto:,.0f}"
                )

                self.actualizar_saldo()

            else:

                messagebox.showerror(
                    "Error",
                    "Fondos insuficientes"
                )

    # ═══════════════════════════════════════════════════
    # HISTORIAL
    # ═══════════════════════════════════════════════════
    def historial(self):

        ventana = tk.Toplevel(
            self.root
        )

        ventana.title(
            "Historial"
        )

        ventana.geometry(
            "550x400"
        )

        texto = tk.Text(
            ventana,
            font=("Consolas", 10)
        )

        texto.pack(
            expand=True,
            fill="both"
        )

        historial = (
            self.cuenta_actual.get_historial()
        )

        if not historial:

            texto.insert(
                "end",
                "No hay movimientos\n"
            )

        else:

            for trans in historial:

                linea = (
                    f"{trans['fecha'].strftime('%d/%m/%Y %H:%M')} | "
                    f"{trans['tipo']} | "
                    f"${trans['monto']:,.0f} | "
                    f"{trans['detalle']}\n"
                )

                texto.insert(
                    "end",
                    linea
                )


# ═══════════════════════════════════════════════════════
# EJECUTAR
# ═══════════════════════════════════════════════════════
if __name__ == "__main__":

    root = tk.Tk()

    app = CajeroGUI(root)

    root.mainloop()