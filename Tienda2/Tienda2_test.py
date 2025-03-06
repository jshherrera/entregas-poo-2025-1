import unittest
from Tienda2 import Producto, obtener_producto

class TestPrograma(unittest.TestCase):
    def test_producto(self):
        """Verifica que la clase Producto se cree correctamente."""
        producto = Producto(
            nombre="Pan",
            precio=2000,
            cantidad=10,
            descripcion="Pan tajado",
            clasificacion="Alimentación"
        )
        self.assertEqual(producto.nombre, "Pan")
        self.assertEqual(producto.precio, 2000)
        self.assertEqual(producto.cantidad, 10)
        self.assertEqual(producto.descripcion, "Pan tajado")
        self.assertEqual(producto.clasificacion, "Alimentación")

    def test_obtener_producto(self):
        """Verifica que la función obtener_producto devuelva un objeto Producto con los datos correctos."""
        nombre = "Leche"
        precio = 5000
        cantidad = 15
        descripcion = "Bolsa de leche"
        clasificacion = "Alimentación"
        producto = obtener_producto(1)
        self.assertEqual(producto.nombre, nombre)
        self.assertEqual(producto.precio, precio)
        self.assertEqual(producto.cantidad, cantidad)
        self.assertEqual(producto.descripcion, descripcion)
        self.assertEqual(producto.clasificacion, clasificacion)

    def test_resumen(self):
        """Simula la entrada de datos y verifica que el programa se ejecute correctamente."""
        # Simula la entrada de datos
        input_values = [
            "Pan", "2000", "10", "Pan tajado", "Alimentación",
            "Leche", "5000", "15", "Bolsa de leche", "Alimentación"
        ]
        def input_mock(prompt):
            return input_values.pop(0)

        # Reemplaza la función input con la función mock
        import builtins
        builtins.input = input_mock

        # Llama a la función main
        from programa import main
        main()

        # Restablece la función input original
        builtins.input = __builtins__.input

if __name__ == "__main__":
    unittest.main()