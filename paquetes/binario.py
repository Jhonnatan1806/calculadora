from paquetes.decimal import Decimal

class Binario():

    def __init__(self):
        pass
    
    # Algoritmo de base 10 a base 2
    def __algoritmo(self,numero):
        # Reutilizamos el algoritmo decimal pero con base=2
        return Decimal().get(numero,2)

    # Retorna el resultado del algoritmo
    def get(self,numero):
        return self.__algoritmo(numero)
