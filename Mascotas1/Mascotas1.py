"""
Título de práctica: Mascotas1

Este es un programa que nos pedirá cuántos productos quiere el vendedor para su tienda,
donde al final del programa nos dará un resumen de los productos ingresados.

Autor: Johan Sebastian Herrera Hoyos <jsherrerah1@academia.usbbog.edu.co>
Fecha: 2025-03-25
"""
from datetime import datetime

class Mascota:
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
            "Fecha de ingreso": self.fecha_ingreso
        }

class Perro(Mascota):
    pass

class Gato(Mascota):
    pass

def validar_clase():
    while True:
        tipo = input("¿Qué clase es (P)erro o (G)ato? ").strip().lower()
        if tipo == 'p' or tipo == 'g':
            return tipo
        else:
            print("Opción inválida. Ingrese 'P' para Perro o 'G' para Gato.")

def validar_nombre(mensaje):
    while True:
        nombre = input(mensaje).strip()
        if nombre.replace(" ", "").isalpha():
            return nombre
        else:
            print("El nombre solo puede contener letras y espacios.")

def validar_edad(mensaje):
    while True:
        edad = input(mensaje).strip()
        if edad.isdigit():
            edad = int(edad)
            if edad > 0:
                return edad
            else:
                print("La edad debe ser un número mayor a 0.")
        else:
            print("Debe ingresar un número válido.")

def ingresar_mascota():
    tipo = validar_clase()
    nombre = validar_nombre(f"¿Cuál es el nombre del {'Perro' if tipo == 'p' else 'Gato'}? ")
    edad = validar_edad(f"¿Qué edad tiene '{nombre}'? ")
    raza = validar_nombre(f"¿De qué raza es '{nombre}'? ")

    if tipo == 'p':
        return Perro(nombre, edad, raza)
    else:
        return Gato(nombre, edad, raza)

def main():
    mascotas = []

    cantidad = validar_edad("¿Cuántas mascotas va a ingresar? ")
    for i in range(cantidad):
        print(f"\nMascota {i + 1}:")
        mascota = ingresar_mascota()
        mascotas.append(mascota)

    print("\nResumen:")
    print(f"|{'Clase':<6}|{'Nombre':<15}|{'Edad':<8}|{'Raza':<15}|{'Fecha de ingreso':<25}|")
    print("-" * 65)
    for m in mascotas:
        datos = m.obtener_datos()
        print(f"|{datos['Clase']:<6}|{datos['Nombre']:<15}|{datos['Edad']:<8}|{datos['Raza']:<15}|{datos['Fecha de ingreso']:<25}|")

if __name__ == "__main__":
    main()