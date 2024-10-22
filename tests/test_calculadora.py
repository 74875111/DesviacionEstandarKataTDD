import unittest
from src.logic.calculadora import Media
from src.logic.exceptions import NoSePuedeCalcular

class TestCalculadora(unittest.TestCase):
    def test_media_lista_vacia(self):
        media=Media()
        with self.assertRaises(NoSePuedeCalcular):
            media.calcularMedia()
if __name__ == '__main__':
    unittest.main() 