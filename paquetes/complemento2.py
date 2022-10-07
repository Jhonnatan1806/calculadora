from paquetes.complemento1 import Complemento1

class Complemento2:
    
    def __init__(self):
        pass

    # Algoritmo de base 10 a complemento 2
    def __algoritmo(self,numero):
        # P1 Pasamos el numero a binario
        # P2 Empaquetamos el numero
        # P3 Invertimos el numero
        # Para esto utilizamos la clase complemento1
        binario = Complemento1().get(numero)
        # P4 Sumamos 1 bit
        binario = self.__agregar_bit(binario)
        return binario
    
    # Funcion que suma un bit al binario
    def __agregar_bit(self, binario):
        lista = list(binario)
        suma = ''
        sumando = 1
        for i in reversed(lista):
            if sumando == 1:
                if i == '0':
                    suma = '1' + suma
                    sumando = 0
                else:
                    suma = '0' + suma
            else:
                suma = i + suma
        return suma

    # Retorna el resultado del algoritmo
    def get(self,numero):
        return self.__algoritmo(numero)
    