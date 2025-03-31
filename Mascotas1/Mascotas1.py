"""
Título de práctica: Mascotas1

Este es un programa que nos pedirá cuántos animales queremos inscribir y que clase de animal son, si son perros se colocara una P y si son gatos se colocara una G.

Autor: Johan Sebastian Herrera Hoyos <jsherrerah1@academia.usbbog.edu.co>
Fecha: 2025-03-25
"""
from datetime import datetime


class Mascota:
    """Clase base que representa una mascota."""
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().isoformat()

    def obtener_datos(self):
        return {
            "Clase": self.__class__.__name__,
            "Nombre": self.nombre,
            "Edad": f"{self.edad} años",
            "Raza": self.raza,
            "Fecha de ingreso": self.fecha_ingreso,
        }

    def __str__(self):
        return (
            f"Clase: {self.__class__.__name__}, Nombre: {self.nombre}, "
            f"Edad: {self.edad} años, Raza: {self.raza}, "
            f"Fecha de ingreso: {self.fecha_ingreso}"
        )


class Perro(Mascota):
    """Clase derivada que representa un perro."""
    pass


class Gato(Mascota):
    """Clase derivada que representa un gato."""
    pass


def validar_clase():
    """Solicita al usuario que elija entre perro o gato."""
    while True:
        tipo = input("¿Qué clase es (P)erro o (G)ato? ").strip().lower()
        if tipo in ('p', 'g'):
            return tipo
        print("Opción inválida. Ingrese 'P' para Perro o 'G' para Gato.")


def validar_nombre(mensaje):
    """Valida que el nombre contenga solo letras y espacios."""
    while True:
        nombre = input(mensaje).strip()
        if nombre.replace(" ", "").isalpha():
            return nombre
        print("El nombre solo puede contener letras y espacios.")


def validar_edad(mensaje):
    """Valida que la edad sea un número entero mayor a 0."""
    while True:
        edad = input(mensaje).strip()
        if edad.isdigit() and int(edad) > 0:
            return int(edad)
        print("Debe ingresar un número válido mayor a 0.")


def ingresar_mascota():
    """Solicita los datos para registrar una mascota."""
    tipo = validar_clase()
    nombre = validar_nombre(f"¿Cuál es el nombre del {'Perro' if tipo == 'p' else 'Gato'}? ")
    edad = validar_edad(f"¿Qué edad tiene '{nombre}'? ")
    raza = validar_nombre(f"¿De qué raza es '{nombre}'? ")

    return Perro(nombre, edad, raza) if tipo == 'p' else Gato(nombre, edad, raza)


def main():
    """Función principal del programa."""
    mascotas = []

    cantidad = validar_edad("¿Cuántas mascotas va a ingresar? ")
    for i in range(cantidad):
        print(f"\nMascota {i + 1}:")
        mascotas.append(ingresar_mascota())

    print("\nResumen:")
    print(f"|{'Clase':<6}|{'Nombre':<15}|{'Edad':<8}|{'Raza':<15}|{'Fecha de ingreso':<25}|")
    print("-" * 65)
    for mascota in mascotas:
        datos = mascota.obtener_datos()
        print(
            f"|{datos['Clase']:<6}|{datos['Nombre']:<15}|"
            f"{datos['Edad']:<8}|{datos['Raza']:<15}|"
            f"{datos['Fecha de ingreso']:<25}|"
        )


if __name__ == "__main__":
    main()
