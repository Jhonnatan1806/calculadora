from paquetes.decimal import decimal

class binario():

    def __init__(self,numero):
        self.__numero = numero
    
    def __algoritmo(self):
        # Reutilizamos el algoritmo decimal pero con base=2
        return decimal(self.__numero,2).get()

    def get(self):
        return self.__algoritmo()
