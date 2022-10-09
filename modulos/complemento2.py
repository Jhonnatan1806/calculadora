from modulos.binario import Binario
from modulos.complemento1 import Complemento1

class Complemento2:
    
    def __init__(self):
        pass

    # =======================================================
    # Algoritmo de base 10 a base 2 complemento 2
    # =======================================================

    def dec_bin(self,n_base10):
        # P1 Pasamos el numero a binario
        # P2 Empaquetamos el numero
        # P3 Invertimos el numero
        # Para esto utilizamos la clase complemento1
        n_base2= Complemento1().dec_bin(n_base10)
        # P4 Sumamos 1 bit
        n_base2 = self.__agregar_bit(n_base2)
        return n_base2
    
    # Funcion que suma un bit al binario
    def __agregar_bit(self, n_base2):
        lista = list(n_base2)
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

    # =======================================================
    # Algoritmo de base 2 complemento 2 a base 10
    # =======================================================
    
    def bin_dec(self,n_base2):
        # P1 Pasamos el complemento a base 10
        complemento = Binario().bin_dec(n_base2)
        # P2 Obtenemos el tamaño de la palabra 8,16,32...
        lng = len(n_base2)
        # P3 Aplicamos C - 2^n = - x 
        n_base10 = complemento - pow(2,lng)
        return n_base10