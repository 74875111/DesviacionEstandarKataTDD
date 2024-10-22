import math
from src.logic.exceptions import NoSePuedeCalcular
class Media():
    def __init__(self, numeros=[]):
        self.numeros = numeros
    def calcularMedia(self):
        if (len(self.numeros)==0):
            raise NoSePuedeCalcular("No se puede calcular la media: la lista está vacía")
        elif (len(self.numeros)==1):
            return self.numeros[0]
        else:
            return sum(self.numeros)/len(self.numeros)

class DesviacionEstandar():
    def __init__(self, numeros=[]):
        self.numeros = numeros
    def calcular(self):
        if(len(self.numeros)==0):
            raise NoSePuedeCalcular("No se puede calcular la desviación estandar ya que la lista esta vacia")
        elif(len(self.numeros)==1):
            return 0
        else:
            media=Media(self.numeros).calcularMedia()
            suma_cuadrados = sum((x - media) ** 2 for x in self.numeros)
            varianza=suma_cuadrados/(len(self.numeros)-1)
            return math.sqrt(varianza)

