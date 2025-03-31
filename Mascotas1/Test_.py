import unittest
from datetime import datetime
from Mascotas1 import Mascota, Perro, Gato


class TestMascotas(unittest.TestCase):
    def setUp(self):
        """Configura los datos de prueba antes de cada test."""
        self.perro = Perro("Rex", 5, "Labrador")
        self.gato = Gato("Misu", 3, "Siames")

    def test_instanciacion(self):
        """Verifica que las instancias de Perro y Gato sean correctas."""
        self.assertIsInstance(self.perro, Perro)
        self.assertIsInstance(self.gato, Gato)
        self.assertIsInstance(self.perro, Mascota)
        self.assertIsInstance(self.gato, Mascota)

    def test_atributos(self):
        """Verifica que los atributos se asignen correctamente."""
        self.assertEqual(self.perro.nombre, "Rex")
        self.assertEqual(self.perro.edad, 5)
        self.assertEqual(self.perro.raza, "Labrador")
        
        self.assertEqual(self.gato.nombre, "Misu")
        self.assertEqual(self.gato.edad, 3)
        self.assertEqual(self.gato.raza, "Siames")

    def test_fecha_ingreso(self):
        """Verifica que la fecha de ingreso se genere correctamente."""
        self.assertIsInstance(self.perro.fecha_ingreso, str)
        self.assertIsInstance(self.gato.fecha_ingreso, str)
        
        fecha_formateada = datetime.fromisoformat(self.perro.fecha_ingreso)
        self.assertIsInstance(fecha_formateada, datetime)

    def test_obtener_datos(self):
        """Verifica que el método obtener_datos retorne un diccionario válido."""
        datos_perro = self.perro.obtener_datos()
        datos_gato = self.gato.obtener_datos()

        self.assertEqual(datos_perro["Nombre"], "Rex")
        self.assertEqual(datos_perro["Edad"], "5 años")
        self.assertEqual(datos_perro["Raza"], "Labrador")
        self.assertEqual(datos_perro["Clase"], "Perro")

        self.assertEqual(datos_gato["Nombre"], "Misu")
        self.assertEqual(datos_gato["Edad"], "3 años")
        self.assertEqual(datos_gato["Raza"], "Siames")
        self.assertEqual(datos_gato["Clase"], "Gato")


if __name__ == "__main__":
    unittest.main()
