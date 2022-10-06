import unittest
from modulos.decimal_binario import decimal_binario as dec_bin
from modulos.decimal_complemento1 import decimal_complemento1 as dec_bin_c1
from modulos.decimal_complemento2 import decimal_complemento2 as dec_bin_c2
from modulos.decimal_octal import decimal_octal as dec_oct

class test_all(unittest.TestCase):
    
    def test_decimal_binario(self):
        tmp = dec_bin()
        self.assertEquals('10010',tmp.algoritmo(18))
    
    def test_decimal_complemento1(self):
        tmp = dec_bin_c1()
        self.assertEquals('11101101',tmp.algoritmo(18))
    
    def test_decimal_complemento2(self):
        tmp = dec_bin_c2()
        self.assertEquals('11101110',tmp.algoritmo(-18))
    
    def test_decimal_octal(self):
        tmp = dec_oct()
        self.assertEquals('22',tmp.algoritmo(18))

if __name__ == '__main__':
    unittest.main()
