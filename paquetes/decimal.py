class decimal:

    def __init__(self,numero,base):
        self.__numero = numero
        self.__base = base
        
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
    
    def get(self):
        return self.__algoritmo()
