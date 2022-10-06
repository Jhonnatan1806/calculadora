from paquetes.decimal import Decimal

class Hexadecimal:

    def __init__(self):
        pass
    
    # Algoritmo de base 10 a base 16
    def __algoritmo(self, numero):
        # Reutilizamos el algoritmo decimal pero con base=16
        return Decimal().get(numero,16)
    
    # Retorna el resultado del algoritmo
    def get(self,numero):
        return self.__algoritmo(numero)