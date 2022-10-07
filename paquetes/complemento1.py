from paquetes.binario import Binario

class Complemento1:
    
    def __init__(self):
        pass

    # Algoritmo de base 10 a complemento 1
    def __algoritmo(self,numero):
        # P1 Pasamos el numero(+) a binario
        numero = abs(numero)
        binario = Binario().get(numero)
        # P2 empaquetamos el numero
        bits = self.__bits(numero) - len(binario)
        binario = '0'*bits + binario
        # P3 Invertimos el numero
        binario = self.__invertir(binario)
        return binario

    # Funcion que retorna la cantidad de bits a usar
    def __bits(self, numero):
        # verificamos si el decimal sera 
        # empaquetado en 8,16,32,64 bits
        if numero < 127:
            return 8
        elif numero < 32768:
            return 16
        elif numero < 2147483648:
            return 32
        else:
            return 64
    
    # Funcion que invierte le numero binario
    def __invertir(self, binario):
        bin_invertido = ''
        for i in range(len(binario)):
            if binario[i]=='0':
                bin_invertido += '1'
            else:
                bin_invertido += '0'
        return bin_invertido

    # Retorna el resultado del algoritmo
    def get(self,numero):
        return self.__algoritmo(numero)