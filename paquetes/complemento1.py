from paquetes.binario import Binario

class Complemento1:
    
    def __init__(self):
        pass

    # =======================================================
    # Algoritmo de base 10 a base 2 complemento 1
    # =======================================================
    
    def dec_bin(self, n_base10):
        # P1 Pasamos el numero a binario
        n_base10 = abs(n_base10)
        n_base2 = Binario().dec_bin(n_base10)
        # P3 Invertimos el numero
        n_base2 = self.__invertir(n_base2)
        return n_base2

    # Funcion que invierte le numero binario
    def __invertir(self, n_base2):
        invertido = ''
        for i in range(len(n_base2)):
            if n_base2[i]=='0':
                invertido += '1'
            else:
                invertido += '0'
        return invertido

    # =======================================================
    # Algoritmo de base 2 complemento 1 a base 10
    # =======================================================
    
    def bin_dec(self, n_base2):
        n_base2 = self.__invertir(n_base2)
        n_base10 = Binario().bin_dec(n_base2)
        return n_base10