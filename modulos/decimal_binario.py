class decimal_binario:

    def __init__(self):
        pass

    def algoritmo(self, decimal):
        binario = ''
        while decimal >= 1:
            a = int(decimal) % 2
            decimal = decimal/2
            binario = str(a) + binario
        return binario