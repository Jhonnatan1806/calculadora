class decimal_octal:

    def __init__(self):
        pass

    def algoritmo(self, decimal):
        octal = ''
        while decimal >= 1:
            a = int(decimal) % 8
            decimal = decimal/8
            octal = str(a) + octal
        return octal