class Octal:

    def __init__(self):
        pass

    def __algoritmo(self, numero):
        palabra = '' 
        while numero >= 1:
            a = int(numero) % 8
            numero = numero/8
            palabra = str(a) + palabra
        return palabra
    
    def get(self, numero):
        return self.__algoritmo(numero)