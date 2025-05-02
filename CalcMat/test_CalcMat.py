import unittest
from CalcMat import Matriz # type: ignore


class TestMatriz(unittest.TestCase):
    """Casos de prueba para la clase Matriz de CalcMat."""

    def setUp(self):
        """Inicializa dos matrices para usar en las pruebas."""
        self.m1 = Matriz(1, 2, 3, 4)
        self.m2 = Matriz(5, 6, 7, 8)

    def test_suma(self):
        """Prueba la suma de dos matrices."""
        resultado = self.m1 + self.m2
        esperado = Matriz(6, 8, 10, 12)
        self.assertEqual(resultado.valores, esperado.valores)

    def test_resta(self):
        """Prueba la resta de dos matrices."""
        resultado = self.m1 - self.m2
        esperado = Matriz(-4, -4, -4, -4)
        self.assertEqual(resultado.valores, esperado.valores)

    def test_multiplicacion(self):
        """Prueba la multiplicación de dos matrices."""
        resultado = self.m1 * self.m2
        esperado = Matriz(19, 22, 43, 50)
        self.assertEqual(resultado.valores, esperado.valores)

    def test_str(self):
        """Prueba la representación en texto de una matriz."""
        esperado = "|1  2|\n|3  4|"
        self.assertEqual(str(self.m1), esperado)


if __name__ == "__main__":
    unittest.main()
