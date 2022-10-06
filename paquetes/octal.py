from paquetes.decimal import Decimal

class Octal:

    def __init__(self):
        pass

    def __algoritmo(self, numero):
        # Reutilizamos el algoritmo decimal pero con base=8
        return Decimal().get(numero,8)
    
    def get(self, numero):
        return self.__algoritmo(numero)