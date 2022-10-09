class Binario:

    def __init__(self):
        pass
    
    # =======================================================
    # Algoritmo de base 10 a base 2
    # =======================================================

    def dec_bin(self, n_base10):
        # Verificamos que el numero sea positivo
        if n_base10 >= 0:
            # Incializamos las variables
            n_base2 = '' 
            # Ingresamos al algoritmo
            while n_base10 >= 1:
                a = int(n_base10) % 2
                n_base10 = n_base10/2
                n_base2 = str(a) + n_base2
            # Empaquetamos el numero
            bits = self.__bits(n_base10) - len(n_base2)
            n_base2 = '0'*bits + n_base2 
        else:
            # Error numero negativo
            n_base2 = '-1'
        return n_base2

    # Funcion que retorna la cantidad de bits a usar
    def __bits(self, n_base10):
        # verificamos si el decimal sera 
        # empaquetado en 8,16,32,64 bits
        if n_base10 < 127:
            return 8
        elif n_base10 < 2048:
            return 12
        elif n_base10 < 32768:
            return 16
        elif n_base10 < 2147483648:
            return 32
        else:
            return 64

    # =======================================================
    # Algoritmo de base 2 a base 10
    # =======================================================
    
    def bin_dec(self, n_base2):
        # Iniciamos la variable que retorna el resultado
        n_base10 = 0 
        # Ingresamos al algoritmo
        # Usamos a_{n} = b_{n} + 2*a_{n-1}
        for i in range(len(n_base2)) :
            n_base10 = int(n_base2[i]) + 2*n_base10
        return n_base10 