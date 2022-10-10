class Hexadecimal:

    def __init__(self):
        pass
    
    # =======================================================
    # Algoritmo de base 10 a base 16
    # =======================================================

    def dec_hex(self, n_base10):
        n_base16 = '' 
        while n_base10 >= 1:
            a = int(n_base10) % 16
            n_base10 = n_base10/16
            # Utilizamos char para convertirlo el string en ASCII
            if a >= 10:
                n_base16 = chr(a+55) + n_base16
            # Caso contrario solo tomamos el valor numerico
            else:
                n_base16 = str(a) + n_base16
        return n_base16
    
    # =======================================================
    # Algoritmo de base 16 a base 10
    # =======================================================

    def hex_dec(self,n_base16):
        n_base10 = 0 
        k = len(n_base16)
        for i in range(k):
            # numeros de 1 - 9
            if ord(n_base16[i]) <= 57:
                n = int(n_base16[i])
            # numero de 10(A=65) - 15(F=70)
            else:
                n = int(ord(n_base16[i]))-55
            n_base10 += n*pow(16,k-1)
            k -=1 
        return n_base10