from paquetes.binario import Binario
from paquetes.fraccionario import Fraccionario

class IEEE754x32:

    def __init__(self):
        pass

    def __algoritmo(self,numero):
        # P1 Identificar el Signo
        # 0 = positivo & 1 = negativo
        signo = '0' if numero >= 0 else '1'
        # P2 Convertir en Numero en binario Fraccionario
        # binario[0] = parte entera binario[1] = parte fraccionaria
        b_fracionado = Fraccionario().get(abs(numero),23)
        binario = b_fracionado.split(',')
        # P3 Identificar el Exponente y el tipo de numero
        # Se le suma 126 + exponentes y se empaqueta en 8 bits
        exp_bin = Binario.get(len(binario[0]) + 126)
        exponente = '0'*(8-len(exp_bin)) + exp_bin
        # P4 Identificar la Mantisa
        # Normalizamos quitando el primer 1
        
        # P5 Unir las tres partes
        return numero

    def get(self,numero):
        return self.__algoritmo(numero)