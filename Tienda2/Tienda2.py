#!/usr/bin/env python3

"""
Título de práctica: Tienda 2
Aqui encontraremos un programa de una tienda

en el programa nos podemos encontrar con un modulo que nos pedira
3 productos con sus precios y sus cantidades, al final del programa nos dara un resumen
de los productos con sus cantidades y precios corresponsientes colocados

Autor: Johan sebastian herrera hoyos <jsherrerah1@acacdemia.usbbog.edu.co>
Fecha: 2025-07-03
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.

print("Hola querido usuario!")


def run():
    """script entrypoint"""
import sys

class Producto:
    """Clase para representar un producto."""

    def __init__(self, nombre, precio, cantidad, descripcion, clasificacion):
        """Inicializa un producto con los atributos proporcionados."""
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificacion = clasificacion

    def __str__(self):
        """Devuelve una representación en cadena del producto."""
        return (
            f"{self.nombre} | {self.cantidad} unidades | {self.precio} COP | "
            f"{self.descripcion} | {self.clasificacion}"
        )

def obtener_producto(num_producto):
    """Obtiene los atributos de un producto del usuario."""
    while True:
        nombre = input(f"Producto {num_producto}, ¿cuál es el nombre del producto? ")
        if not nombre.replace(" ", "").isalpha():
            print("El nombre del producto debe contener solo letras.")
            continue
        try:
            precio = int(input(f"¿Cuál es el precio de '{nombre}' en COP? "))
            if precio <= 0:
                print("El precio del producto debe ser mayor que cero.")
                continue
            cantidad = int(input(f"¿Qué cantidad hay de '{nombre}'? "))
            if cantidad <= 0:
                print("La cantidad del producto debe ser mayor que cero.")
                continue
            descripcion = input(f"Introduzca la descripción de '{nombre}': ")
            clasificacion = input(f"¿Qué clasificación tiene '{nombre}'? ")
            return Producto(nombre, precio, cantidad, descripcion, clasificacion)
        except ValueError:
            print("Valor inválido. Por favor, ingrese un número entero.")

def main():
    """Función principal del programa."""
    print("Hola querido usuario!")
    num_productos = int(input("¿Cuántos productos va a ingresar? "))
    productos = []
    for i in range(1, num_productos + 1):
        producto = obtener_producto(i)
        productos.append(producto)

    print("\nResumen:")
    print("|Producto |Cantidad |Precio |Descripción |Clasificación |")
    for producto in productos:
        print(producto)

    clasificaciones = {}
    for producto in productos:
        if producto.clasificacion in clasificaciones:
            clasificaciones[producto.clasificacion].append(producto)
        else:
            clasificaciones[producto.clasificacion] = [producto]

    print("\nResumen de productos por su calsificacion clasificación:")
    for clasificacion, productos in clasificaciones.items():
        print(f"{clasificacion}:")
        print("|Producto |Cantidad |Precio |Descripción |")
        for producto in productos:
            print(
                f"{producto.nombre} | {producto.cantidad} unidades | {producto.precio} COP | {producto.descripcion}"
            )

    print("\nresumen de Precios por clasificación:")
    print("|Clasificación |Precio |")
    for clasificacion, productos in clasificaciones.items():
        precio_total = sum(producto.precio for producto in productos)
        print(f"{clasificacion} | {precio_total} COP |")

if __name__ == "__main__":
    main()