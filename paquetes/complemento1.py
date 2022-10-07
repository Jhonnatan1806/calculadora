from paquetes.binario import Binario

class Complemento1:
    
    def __init__(self):
        pass

    # Algoritmo de base 10 a complemento 1
    def dec_bin(self,numero):
        # P1 Pasamos el numero a binario
        numero = abs(numero)
        binario = Binario().dec_bin(numero)
        # P3 Invertimos el numero
        binario = self.__invertir(binario)
        return binario

    # Funcion que invierte le numero binario
    def __invertir(self, binario):
        bin_invertido = ''
        for i in range(len(binario)):
            if binario[i]=='0':
                bin_invertido += '1'
            else:
                bin_invertido += '0'
        return bin_invertido
