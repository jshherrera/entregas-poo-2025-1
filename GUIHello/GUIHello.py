"""
Título de práctica: GUIHello

Desarrollo de un programa sencillo que muestre un saludo usando una interfaz gráfica basada en Tkinter.

Autor: Johan Sebastian Herrera Hoyos <jsherrerah1@academia.usbbog.edu.co>
Fecha: 2025-05-07
"""
import tkinter as tk
from tkinter import messagebox


class AplicacionSaludo:
    """Clase principal para la aplicación de saludo con interfaz gráfica."""

    def __init__(self):
        """Inicializa la interfaz gráfica y sus componentes."""
        self.ventana = tk.Tk()
        self.ventana.title("tk")
        self.ventana.resizable(False, False)

        # Crear y ubicar los widgets
        self.etiqueta = tk.Label(self.ventana, text="Como te llamas?")
        self.etiqueta.grid(row=0, column=0, padx=(10, 5), pady=10)

        self.entrada = tk.Entry(self.ventana, width=25)
        self.entrada.grid(row=0, column=1, padx=(5, 10), pady=10)

        self.boton_saludo = tk.Button(
            self.ventana,
            text="Saludo",
            width=10,
            command=self.mostrar_saludo
        )
        self.boton_saludo.grid(row=1, column=0, padx=10, pady=(0, 10))

        self.boton_salir = tk.Button(
            self.ventana,
            text="Salir",
            width=10,
            command=self.ventana.destroy
        )
        self.boton_salir.grid(row=1, column=1, padx=10, pady=(0, 10))

        self.ventana.mainloop()

    def mostrar_saludo(self):
        """Muestra un saludo personalizado en un cuadro de mensaje."""
        nombre = self.entrada.get().strip()
        if nombre == "":
            messagebox.showwarning(
                "Advertencia",
                "Por favor, ingresa tu nombre."
            )
        else:
            messagebox.showinfo("Saludo", f"Hola {nombre}!")


if __name__ == "__main__":
    app = AplicacionSaludo()
