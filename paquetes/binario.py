from paquetes.decimal import Decimal

class Binario():

    def __init__(self,numero):
        self.__numero = numero
    
    # Algoritmo de base 10 a base 2
    def __algoritmo(self):
        # Reutilizamos el algoritmo decimal pero con base=2
        return Decimal(self.__numero,2).get()

    # Retorna el resultado del algoritmo
    def get(self):
        return self.__algoritmo()
