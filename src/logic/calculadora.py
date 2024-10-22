from src.logic.exceptions import NoSePuedeCalcular
class Media(Exception):
    def __init__(self, numeros=[]):
        self.numeros = numeros
    def calcularMedia(self):
        raise NoSePuedeCalcular("No se puede calcular la media: la lista está vacía")
