import math
from src.logic.exceptions import NoSePuedeCalcular
class Media():
    def __init__(self, elementos=[]):
        self.elementos = elementos
    def calcularMedia(self):
        if (len(self.elementos)==0):
            raise NoSePuedeCalcular("No se puede calcular la media: la lista está vacía")
        elif (len(self.elementos)==1):
            return self.elementos[0]
        else:
            return sum(self.elementos)/len(self.elementos)

class DesviacionEstandar():
    def __init__(self, elementos=[]):
        self.elementos = elementos
    def calcular(self):
        if(len(self.elementos)==0):
            raise NoSePuedeCalcular("No se puede calcular la desviación estandar ya que la lista esta vacia")
        elif(len(self.elementos)==1):
            return 0
        else:
            media=Media(self.elementos).calcularMedia()
            suma_cuadrados = sum((x - media) ** 2 for x in self.elementos)
            varianza=suma_cuadrados/(len(self.elementos)-1)
            return math.sqrt(varianza)

