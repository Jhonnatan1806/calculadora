from paquetes.decimal import Decimal

class Octal:

    def __init__(self):
        pass

    def __algoritmo(self, numero):
        # Reutilizamos el algoritmo decimal pero con base=8
        return Decimal(self.__numero,8).get()
    
    def get(self):
        return self.__algoritmo()