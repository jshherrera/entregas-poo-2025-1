import unittest
from Tienda1 import Producto, obtener_producto

class TestProducto(unittest.TestCase):
    """Clase para probar la clase Producto."""

    def test_init(self):
        """Prueba la inicialización de un objeto Producto."""
        producto = Producto("Pan", 2000, 10)
        self.assertEqual(producto.nombre, "Pan")
        self.assertEqual(producto.precio, 2000)
        self.assertEqual(producto.cantidad, 10)

    def test_str(self):
        """Prueba la representación en cadena de un objeto Producto."""
        producto = Producto("Pan", 2000, 10)
        self.assertEqual(str(producto), "Pan | 10 unidades | 2000 COP")

class TestObtenerProducto(unittest.TestCase):
    """Clase para probar la función obtener_producto."""

    def test_obtener_producto(self):
        """Prueba la obtención de un objeto Producto."""
        # Simula la entrada del usuario
        import io
        import sys
        entrada = io.StringIO("Pan\n2000\n10")
        sys.stdin = entrada

        producto = obtener_producto(1)
        self.assertEqual(producto.nombre, "Pan")
        self.assertEqual(producto.precio, 2000)
        self.assertEqual(producto.cantidad, 10)

if __name__ == "__main__":
    unittest.main()