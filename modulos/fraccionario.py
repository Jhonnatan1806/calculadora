from modulos.binario import Binario

class Fraccionario:
    
    def __init__(self):
        pass
    
    # =======================================================
    # Algoritmo de base 10 a Punto Fijo
    # =======================================================

    def dec_bin(self,n_base10,precision):
        # P1 separamos la parte entera de la decimal
        n_entero = int(n_base10)
        n_frac = n_base10 - n_entero
        # P2 pasamos la parte entera a binario
        b_entero = Binario().dec_bin(n_entero)
        # P3 pasamos la parte decimal a binario
        b_frac = self.__dec_bin_frac(n_frac,precision)
        return b_entero + '.' + b_frac
    
    # Algoritmo para pasar un decimal base 10 a base 2
    def __dec_bin_frac(self, n_base10, precision):
        n_base2 = ''
        for i in range(precision):
            n_base10 *= 2
            n_base2 += str(int(n_base10))
            if n_base10 >= 1:
                n_base10 -= 1
        return n_base2

    # =======================================================
    # Algoritmo de Punto Fijo a base 10
    # =======================================================

    def bin_dec(self,n_base2,precison):
        if n_base2.find('.')!=-1:
            numero = n_base2.split('.')
            n_entero = Binario().bin_dec(numero[0])
            n_frac = self.__bin_dec_frac(numero[1],precison)
            return n_entero + n_frac
        else:
            n_entero = Binario().bin_dec(n_base2)
            return n_entero

    # Algoritmo para pasar un decimal base 2 a base 10
    def __bin_dec_frac(self,n_base2,precison):
        n_base10 = 0 
        for i in range(len(n_base2)):
            n_base10 += float(n_base2[i])/pow(2,i+1)
        return round(n_base10,precison)