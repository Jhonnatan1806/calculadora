from paquetes.binario import Binario

class Fraccionario:
    
    def __init__(self):
        pass

    def __algoritmo(self,numero,precision):
        # P1 separamos la parte entera de la decimal
        p_entera = int(numero)
        p_decimal = numero - p_entera
        # P2 pasamos la parte entera a binario
        b_entero = Binario().get(p_entera)
        # P3 pasamos la parte decimal a binario
        b_decimal = self.__decimal(p_decimal,4)
        return b_entero + ',' + b_decimal
    
    def __decimal(self, numero, precision):
        binario = ''
        for i in range(precision):
            numero *= 2
            binario += str(int(numero))
            if numero >= 1:
                numero -= 1
        return binario

    def get(self,numero,precision):
        return self.__algoritmo(numero,precision)

