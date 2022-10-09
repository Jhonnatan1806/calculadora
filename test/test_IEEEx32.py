from modulos.IEEE754x32 import IEEE754x32
import unittest

class Test_IEEE754x32(unittest.TestCase):

    def setUp(self):
        self.tmp = IEEE754x32()
    
    def tearDown(self):
        del self.tmp

    def test_dec_bin_entero(self):
        self.assertEquals('01000001100100000000000000000000', self.tmp.dec_bin(18))
    
    def test_dec_bin_entero_frac(self):
        self.assertEquals('01000001001010000000000000000000', self.tmp.dec_bin(10.5))
    
    def test_dec_bin_frac(self):
        self.assertEquals('00111110100000000000000000000000', self.tmp.dec_bin(0.25))   

if __name__ == '__main__':
    unittest.main()
