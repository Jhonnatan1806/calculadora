class Decimal:

    def __init__(self,numero,base):
        self.__numero = numero
        self.__base = base
    
    # Algoritmo de base 10 a base n
    def __algoritmo(self):
        N = int (self.__numero)
        b = int(self.__base)
        palabra = '' 
        # Algoritmo para cambio de base 2, 8, 16 ...
        while N >= 1:
            a = int(N) % b
            N = N/b
            palabra = str(a) + palabra
        return palabra
    
    # Retorna el resultado del algoritmo
    def get(self):
        return self.__algoritmo()
