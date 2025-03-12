#!/usr/bin/env python3

"""
Título de práctica: Tienda 2
Aqui encontraremos un programa de una tienda

en el programa nos podemos encontrar con un modulo que nos pedira
3 productos con sus precios y sus cantidades, al final del programa nos dara un resumen
de los productos con sus cantidades y precios corresponsientes colocados

Autor: Johan sebastian herrera hoyos <jsherrerah1@acacdemia.usbbog.edu.co>
Fecha: 2025-28-02
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.

print("Hola querido usuario!")


def run():
    """script entrypoint"""
class Producto:
    """Clase para producto."""

    def __init__(self, nombre, precio, cantidad):
        """indica un producto con nombre, precio y cantidad."""
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        """Devuelve una representación en cadena del producto."""
        return f"{self.nombre} | {self.cantidad} unidades | {self.precio} COP"

def obtener_producto(num_producto):
    """Obtiene los atributos de un producto."""
    while True:
        nombre = input(f"Producto {num_producto}, ¿cuál es el nombre del producto? ")
        if not nombre.replace(" ", "").isalpha():
            print("El nombre del producto debe contener solo letras. Por favor, ingrese un nombre válido.")
        else:
            try:
                precio = int(input(f"¿Cuál es el precio de '{nombre}' en COP? "))
                if precio <= 0:
                    print("El precio del producto debe ser mayor que cero. Por favor, ingrese un precio válido.")
                else:
                    cantidad = int(input(f"¿Qué cantidad hay de '{nombre}'? "))
                    if cantidad <= 0:
                        print("La cantidad del producto debe ser mayor que cero. Por favor, ingrese una cantidad válida.")
                    else:
                        return Producto(nombre, precio, cantidad)
            except ValueError:
                print("Valor inválido. Por favor, ingrese un número entero.")

def main():
    """Función principal del programa."""
    productos = []

    for i in range(1, 4):
        producto = obtener_producto(i)
        productos.append(producto)

    print("\nResumen:")
    print("|Producto |Cantidad |Precio |")
    for producto in productos:
        print(producto)

if __name__ == "__main__":
    main()
