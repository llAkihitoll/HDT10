import unittest
from grafo import Grafo
from clima import Clima

class TestGrafo(unittest.TestCase):

    def setUp(self):
        self.grafo = Grafo()
        self.grafo.leer_archivo("logistica.txt")

    def test_ruta_mas_corta(self):
        ruta = self.grafo.ruta_mas_corta("BuenosAires", "Quito")
        self.assertIsNotNone(ruta)
        self.assertTrue(ruta.distancia < float('inf'))

    def test_centro_del_grafo(self):
        centro = self.grafo.calcular_centro()
        self.assertIn(centro, self.grafo.ciudades)

    def test_cambio_clima(self):
        self.grafo.cambiar_clima(Clima.TORMENTA)
        ruta = self.grafo.ruta_mas_corta("BuenosAires", "Quito")
        self.assertGreater(ruta.distancia, 0)

    def test_modificar_trafico(self):
        self.grafo.modificar_trafico("BuenosAires", "Lima")
        ruta = self.grafo.ruta_mas_corta("BuenosAires", "Lima")
        self.assertEqual(ruta.distancia, float('inf'))

    def test_añadir_conexion(self):
        nueva = ["SantaCruz", "LaPaz", [10, 12, 14, 20]]
        self.grafo.añadir_conexion(nueva[0], nueva[1], nueva[2])
        ruta = self.grafo.ruta_mas_corta("SantaCruz", "LaPaz")
        self.assertEqual(ruta.distancia, 10)

if __name__ == '__main__':
    unittest.main()
