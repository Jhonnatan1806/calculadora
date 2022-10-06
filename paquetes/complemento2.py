from paquetes.complemento1 import Complemento_1

class Ccomplemento_2:
    
    def __init__(self):
        pass

    # Algoritmo de base 10 a complemento 2
    def __algoritmo(self,numero):
        # P1 Pasamos el numero a binario
        # P2 Empaquetamos el numero
        # P3 Invertimos el numero
        # Para esto utilizamos la clase complemento1
        binario = Complemento_1(numero).get()
        # P4 Sumamos 1 bit
        binario = self.__agregar_bit(binario)
        return binario
    
    # Funcion que suma un bit y retorna un string
    # con el resultado
    def __agregar_bit(self, binario):
        lista = list(binario)
        res = {'suma':'','op':0}
        for i in reversed(lista):
            if res['op'] == -1:
                if i == '0':
                    res['suma'] = '1' + res['suma']
                    res['op'] = 1
                else:
                    res['suma'] = '0' + res['suma']
            else:
                res['suma'] = i + res['suma']
        return res['suma']

    # Retorna el resultado del algoritmo
    def get(self):
        return self.__algoritmo(self.__numero)
    