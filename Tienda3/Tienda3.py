"""
Título de práctica: Tienda 3
Aqui encontraremos un programa de una tienda

este es un programa que nos pedira cuantos productos quiere el vendedor quiere pára su tienda
donde al final del programa nos dara un resumen de los productos ingresados.

Autor: Johan sebastian herrera hoyos <jsherrerah1@acacdemia.usbbog.edu.co>
Fecha: 2025-14-03
"""
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

    def calcular_precio(self, cantidad):
        """Devuelve el precio a pagar según la cantidad de producto indicado."""
        return self.precio * cantidad

    def calcular_inventario_precio(self):
        """Devuelve el valor total de mercancía de este producto en el inventario."""
        return self.precio * self.cantidad

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
    while True:
        try:
            num_productos = int(input("¿Cuántos productos vas a ingresar? "))
            if num_productos <= 0:
                print("El número de productos debe ser mayor que cero.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número en lugar de texto.")

    productos = []
    for i in range(1, num_productos + 1):
        print("\n")
        producto = obtener_producto(i)
        productos.append(producto)

    print("\nResumen:")
    print(
        "| {:<15} | {:<10} | {:<8} | {:<20} | {:<17} | {:<15} | {:<15} |".format(
            "Producto",
            "Cantidad",
            "Precio",
            "Descripción",
            "Clasificación",
            "precio total",
            "Precio x5 unidades"
        )
    )
    for producto in productos:
        print(
            "| {:<15} | {:<10} | {:<8} | {:<20} | {:<17} | {:<15} | {:<15} |".format(
                producto.nombre,
                f"{producto.cantidad} unidades",
                f"{producto.precio} COP",
                producto.descripcion,
                producto.clasificacion,
                f"{producto.calcular_inventario_precio()} COP",
                f"{producto.calcular_precio(5)} COP"
            )
        )

    clasificaciones = {}
    for producto in productos:
        if producto.clasificacion in clasificaciones:
            clasificaciones[producto.clasificacion].append(producto)
        else:
            clasificaciones[producto.clasificacion] = [producto]

    print("\nPrecio por clasificación:")
    print("| {:<15} | {:<6} |".format("Clasificación", "Precio"))
    for clasificacion, productos in clasificaciones.items():
        precio_total = sum(producto.precio for producto in productos)
        print("| {:<15} | {:<6} |".format(clasificacion, f"{precio_total} COP"))

if __name__ == "__main__":
    main()


