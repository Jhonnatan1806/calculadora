class Hexadecimal:

    def __init__(self):
        pass
    
    # Algoritmo de base 10 a base 16
    def __algoritmo(self, numero):
        palabra = '' 
        while numero >= 1:
            a = int(numero) % 16
            numero = numero/16
            if a >= 10:
                palabra = chr(a+55) + palabra
            else:
                palabra = str(a) + palabra
        return palabra
    
    # Retorna el resultado del algoritmo
    def get(self,numero):
        return self.__algoritmo(numero)