import unittest
from Tienda3 import Producto, obtener_producto

class TestProducto(unittest.TestCase):

    def test_producto(self):
        producto = Producto("Pan", 2000, 10, "Pan tajado", "Alimento")
        self.assertEqual(producto.nombre, "Pan")
        self.assertEqual(producto.precio, 2000)
        self.assertEqual(producto.cantidad, 10)
        self.assertEqual(producto.descripcion, "Pan tajado")
        self.assertEqual(producto.clasificacion, "Alimento")

    def test_obtener_producto(self):
        producto = obtener_producto(1)
        self.assertIsInstance(producto, Producto)

    def test_producto_calcular_precio(self):
        producto = Producto("Pan", 2000, 10, "Pan tajado", "Alimento")
        self.assertEqual(producto.calcular_precio(5), 10000)

    def test_producto_calcular_inventario_precio(self):
        producto = Producto("Pan", 2000, 10, "Pan tajado", "Alimento")
        self.assertEqual(producto.calcular_inventario_precio(), 20000)

if __name__ == "__main__":
    unittest.main()

