import unittest
from src.logic.calculadora import Media
from src.logic.exceptions import NoSePuedeCalcular

class TestCalculadora(unittest.TestCase):
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
if __name__ == '__main__':
    unittest.main() 