"""
Título de práctica: Calculadora de matrices

Este programa es una calculadora de matrices 2x2 en Python

Autor: Johan Sebastian Herrera Hoyos <jsherrerah1@academia.usbbog.edu.co>
Fecha: 2025-04-02
"""
class Matriz:
    """Clase que representa una matriz 2x2."""

    def __init__(self, a11, a12, a21, a22):
        self.valores = [[a11, a12], [a21, a22]]

    def __add__(self, otra):
        """Suma de matrices."""
        return Matriz(
            self.valores[0][0] + otra.valores[0][0],
            self.valores[0][1] + otra.valores[0][1],
            self.valores[1][0] + otra.valores[1][0],
            self.valores[1][1] + otra.valores[1][1]
        )

    def __sub__(self, otra):
        """Resta de matrices."""
        return Matriz(
            self.valores[0][0] - otra.valores[0][0],
            self.valores[0][1] - otra.valores[0][1],
            self.valores[1][0] - otra.valores[1][0],
            self.valores[1][1] - otra.valores[1][1]
        )

    def __mul__(self, otra):
        """Multiplicación de matrices."""
        a11 = (self.valores[0][0] * otra.valores[0][0] +
               self.valores[0][1] * otra.valores[1][0])
        a12 = (self.valores[0][0] * otra.valores[0][1] +
               self.valores[0][1] * otra.valores[1][1])
        a21 = (self.valores[1][0] * otra.valores[0][0] +
               self.valores[1][1] * otra.valores[1][0])
        a22 = (self.valores[1][0] * otra.valores[0][1] +
               self.valores[1][1] * otra.valores[1][1])
        return Matriz(a11, a12, a21, a22)

    def __str__(self):
        """Representación legible de la matriz."""
        fila1 = f"|{self.valores[0][0]}  {self.valores[0][1]}|"
        fila2 = f"|{self.valores[1][0]}  {self.valores[1][1]}|"
        return f"{fila1}\n{fila2}"


def leer_entero(mensaje):
    """Solicita un número entero y valida la entrada."""
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
        except ValueError:
            print("> Entrada inválida. Debe ser un número entero.")
        else:
            return valor


def leer_matriz(numero):
    """Solicita al usuario ingresar los valores de una matriz 2x2."""
    print(f"> Matriz {numero}:")
    elementos = []
    for i in range(2):
        fila = []
        for j in range(2):
            valor = leer_entero(f"> Matriz {numero}: elemento {i},{j}\n< ")
            fila.append(valor)
        elementos.append(fila)
    return Matriz(*elementos[0], *elementos[1])


def main():
    """Función principal del programa."""
    matriz1 = leer_matriz(1)
    matriz2 = leer_matriz(2)

    print("> Matriz 1:")
    print(matriz1)
    print("> Matriz 2:")
    print(matriz2)

    print("> Escriba 1 para suma, ")
    print("          2 para resta, ")
    print("          3 para multiplicación ")

    opcion = leer_entero("< ")

    if opcion == 1:
        resultado = matriz1 + matriz2
        print("> La suma de las dos matrices es:")
    elif opcion == 2:
        resultado = matriz1 - matriz2
        print("> La resta de las dos matrices es:")
    elif opcion == 3:
        resultado = matriz1 * matriz2
        print("> La multiplicación de las dos matrices es:")
    else:
        print("> Opción inválida.")
        return

    print(resultado)


if __name__ == "__main__":
    main()
