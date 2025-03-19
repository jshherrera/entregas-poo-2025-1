import unittest
from Tienda3 import Producto


class TestProducto(unittest.TestCase):
    """Clase de pruebas unitarias para la clase Producto poan y leche."""

    def setUp(self):
        """Configura productos de prueba antes de cada test."""
        self.producto_pan = Producto("Pan", 400, 1, "Pan por unidad", "Alimento")
        self.producto_leche = Producto("Leche", 6500, 1, "Litro de leche", "Bebida")

    def test_creacion_producto_pan(self):
        """Verifica que el producto Pan se crea correctamente."""
        self.assertEqual(self.producto_pan.nombre, "Pan")
        self.assertEqual(self.producto_pan.precio, 400)
        self.assertEqual(self.producto_pan.cantidad, 1)
        self.assertEqual(self.producto_pan.descripcion, "Pan por unidad")
        self.assertEqual(self.producto_pan.clasificacion, "Alimento")

    def test_creacion_producto_leche(self):
        """Verifica que el producto Leche se crea correctamente."""
        self.assertEqual(self.producto_leche.nombre, "Leche")
        self.assertEqual(self.producto_leche.precio, 6500)
        self.assertEqual(self.producto_leche.cantidad, 1)
        self.assertEqual(self.producto_leche.descripcion, "Litro de leche")
        self.assertEqual(self.producto_leche.clasificacion, "Bebida")

    def test_calcular_precio(self):
        """Verifica el cálculo del precio por cantidad."""
        self.assertEqual(self.producto_pan.calcular_precio(3), 1200)
        self.assertEqual(self.producto_pan.calcular_precio(0), 0)
        self.assertEqual(self.producto_pan.calcular_precio(5), 2000)
        self.assertEqual(self.producto_leche.calcular_precio(2), 13000)

    def test_calcular_inventario_precio(self):
        """Verifica el cálculo del precio total del inventario del producto."""
        self.assertEqual(self.producto_pan.calcular_inventario_precio(), 400)
        self.assertEqual(self.producto_leche.calcular_inventario_precio(), 6500)

    def test_str_producto(self):
        """Verifica la representación en cadena de los productos leche y pan."""
        producto_pan_str = str(self.producto_pan)
        self.assertIn("Pan", producto_pan_str)
        self.assertIn("400.0 COP" if isinstance(self.producto_pan.precio, float) else "400 COP", producto_pan_str)
        self.assertIn("1 unidades", producto_pan_str)
        self.assertIn("Pan por unidad", producto_pan_str)
        self.assertIn("Alimento", producto_pan_str)

        producto_leche_str = str(self.producto_leche)
        self.assertIn("Leche", producto_leche_str)
        self.assertIn("6500.0 COP" if isinstance(self.producto_leche.precio, float) else "6500 COP", producto_leche_str)
        self.assertIn("1 unidades", producto_leche_str)
        self.assertIn("Litro de leche", producto_leche_str)
        self.assertIn("Bebida", producto_leche_str)


if __name__ == "__main__":
    unittest.main()