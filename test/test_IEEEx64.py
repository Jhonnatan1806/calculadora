from modulos.IEEE754x64 import IEEE754x64
import unittest

class Test_IEEE754x64(unittest.TestCase):

    def setUp(self):
        self.tmp = IEEE754x64()
    
    def tearDown(self):
        del self.tmp

    def test_dec_bin_entero(self):
        self.assertEquals('0100000000110010000000000000000000000000000000000000000000000000', self.tmp.dec_bin(18))
    
    def test_dec_bin_entero_frac(self):
        self.assertEquals('0100000000100101000000000000000000000000000000000000000000000000', self.tmp.dec_bin(10.5))
    
    def test_dec_bin_frac(self):
        self.assertEquals('0011111111010000000000000000000000000000000000000000000000000000', self.tmp.dec_bin(0.25))

    def test_bin_dec_infinito(self):
        self.assertEquals('infinito', self.tmp.bin_dec('01111111111110000000000000000000000000000000000000000000000000000'))   

    def test_bin_dec_infinito_neg(self):
        self.assertEquals('-infinito', self.tmp.bin_dec('11111111111110000000000000000000000000000000000000000000000000000'))

    def test_bin_dec_cero(self):
        self.assertEquals(0, self.tmp.bin_dec('1000000000001000000000000000000000000000000000000000000000000000'))

    def test_bin_dec_entero(self):
        self.assertEquals(-24, self.tmp.bin_dec('1100000000111000000000000000000000000000000000000000000000000000'))
    
    def test_bin_dec_entero_frac(self):
        self.assertEquals(18.5, self.tmp.bin_dec('0100000000110010100000000000000000000000000000000000000000000000'))
    
    def test_bin_dec_frac(self):
        self.assertEquals(0.65, self.tmp.bin_dec('0011111111100100110011001100110011001100110011001100110011001100'))

if __name__ == '__main__':
    unittest.main()
