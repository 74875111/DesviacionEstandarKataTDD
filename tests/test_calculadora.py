import unittest
from src.logic.calculadora import Media,DesviacionEstandar
from src.logic.exceptions import NoSePuedeCalcular

class TestCalculadora(unittest.TestCase):

    ##Test de la clase media
    def test_media_lista_vacia(self):
        media=Media([])
        with self.assertRaises(NoSePuedeCalcular):
            media.calcularMedia()
    def test_media_un_elemento(self):
        media=Media([5])
        self.assertEqual(media.calcularMedia(),5)
    def test_dos_elementos_lista(self):
        media=Media([5,7])
        self.assertEqual(media.calcularMedia(),6)
    def test_n_elementos_positivos(self):
        media=Media([4,8,5,1])
        self.assertEqual(media.calcularMedia(),4.5)
    def test_n_elementos_todos_cero(self):
        media=Media([0,0,0,0,0])
        self.assertEqual(media.calcularMedia(),0)
    def test_media_positivos_y_negativos(self):
        media=Media([-1, -2, 3, 4])
        self.assertEqual(media.calcularMedia(), 1)
    def test_media_elementos_no_numericos(self):
        media=Media([1, 'a', 3])
        with self.assertRaises(TypeError):
             media.calcularMedia()

    ## Test de la clase Desviación estandar
    def test_desviacion_lista_vacia(self):
        desviacionEstandar=DesviacionEstandar([])
        with self.assertRaises(NoSePuedeCalcular):
            desviacionEstandar.calcular()
    def test_desviacion_un_elemento(self):
        desviacionEstandar=DesviacionEstandar([5])
        self.assertEqual(desviacionEstandar.calcular(), 0)
    def test_desviacion_dos_elementos(self):
        desviacionEstandar=DesviacionEstandar([2, 4])
        self.assertAlmostEqual(desviacionEstandar.calcular(), 1.41, places=2)
if __name__ == '__main__':
    unittest.main() 