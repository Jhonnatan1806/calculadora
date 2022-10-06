from paquetes.decimal import Decimal

class Hexadecimal:

    def __init__(self):
        pass
    
    # Algoritmo de base 10 a base 16
    def __algoritmo(self, numero):
        # Reutilizamos el algoritmo decimal pero con base=8
        return Decimal(self.__numero,8).get()
    
    # Retorna el resultado del algoritmo
    def get(self):
        return self.__algoritmo()