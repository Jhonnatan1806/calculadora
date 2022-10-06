class Decimal:

    def __init__(self):
        pass
    
    # Algoritmo de base 10 a base n
    def __algoritmo(self,numero,base):
        palabra = '' 
        # Algoritmo para cambio de base 2, 8, 16 ...
        while numero >= 1:
            a = int(numero) % base
            numero = numero/base
            palabra = str(a) + palabra
        return palabra
    
    # Retorna el resultado del algoritmo
    def get(self,numero,base):
        return self.__algoritmo(numero,base)
