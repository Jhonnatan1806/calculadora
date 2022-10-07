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
        # Se identifica si tiene parte entera o no
        if int(binario[1]) > 0:
            # Se le suma exponentes + 126
            exp_dec = len(binario[0]) + 126
            exp_bin = Binario().get(exp_dec)
        else:
            # Se le resta 128 - exponentes [VERIFICAR]
            exp_dec = binario[1].index('1') + 1
            exp_bin = Binario().get(128 - exp_dec)
        # Se empaqueta en 8 bits
        exponente = '0'*(8-len(exp_bin)) + exp_bin
        # P4 Identificar la Mantisa
        if int(binario[1]) > 0:
            pos = binario[0].index('1')
            mantisa = binario[0][pos+1:] + binario[1]
        else:
            mantisa = binario[1][exp_dec:]
        bits = len(mantisa)
        if bits<23:
            mantisa = mantisa + '0'*(23-bits)
        else:
            mantisa = mantisa[:23]
        # P5 Unir las tres partes
        return signo + exponente + mantisa

    def get(self,numero):
        return self.__algoritmo(numero)