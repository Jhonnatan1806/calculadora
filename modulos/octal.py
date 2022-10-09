class Octal:

    def __init__(self):
        pass

    # =======================================================
    # Algoritmo de base 10 a base 8
    # =======================================================

    def dec_oct(self, n_base10):
        n_base8 = '' 
        while n_base10 >= 1:
            a = int(n_base10) % 8
            n_base10 = n_base10/8
            n_base8 = str(a) + n_base8
        return n_base8

    # =======================================================
    # Algoritmo de base 10 a base 8
    # =======================================================

    def oct_dec(self,n_base8):
        n_base10 = 0 
        k = len(n_base8)
        for i in range(k):
            n_base10 += float(n_base8[i])*pow(8,k-1)
            k -=1 
        return n_base10