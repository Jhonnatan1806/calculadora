class decimal_complemento1:
    
    def __init__(self):
        pass

    def algoritmo(self,decimal):
        # P1 pasamos el numero a binario
        decimal = abs(decimal)
        binario = self.__dec_bin(decimal)
        # P2 empaquetamos el numero
        bits = self.__bits(decimal) - len(binario)
        binario = '0'*bits + binario
        # P3 Invertimos el numero
        binario = self.__invertir(binario)
        return binario
    
    def __dec_bin(self,decimal):
        binario = ''
        while decimal >= 1:
            a = int(decimal) % 2
            decimal = decimal/2
            binario = str(a) + binario
        return binario

    def __bits(self, decimal):
        # verificamos si el decimal sera 
        # empaquetado en 8,16,32,64 bits
        if decimal < 127:
            return 8
        elif decimal < 32768:
            return 16
        elif decimal < 2147483648:
            return 32
        else:
            return 64
    
    def __invertir(self, binario):
        bin_invertido = ''
        for i in range(len(binario)):
            if binario[i]=='0':
                bin_invertido += '1'
            else:
                bin_invertido += '0'
        return bin_invertido