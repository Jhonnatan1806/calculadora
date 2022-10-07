class Binario:

    def __init__(self):
        pass
    
    # =======================================================
    # Algoritmo de base 10 a base 2
    # =======================================================
    def dec_bin(self,numero):
        # P1 Pasamos el numero a binario
        binario = '' 
        while numero >= 1:
            a = int(numero) % 2
            numero = numero/2
            binario = str(a) + binario
        # P2 empaquetamos el numero
        bits = self.__bits(numero) - len(binario)
        binario = '0'*bits + binario
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

    # =======================================================
    # Algoritmo de base 2 a base 10
    # =======================================================
    def bin_dec(self,numero):
        pass