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

    def test_bin_dec_infinito(self):
        self.assertEquals('infinito', self.tmp.bin_dec('011111111100000000000000000'))   

    def test_bin_dec_infinito_neg(self):
        self.assertEquals('-infinito', self.tmp.bin_dec('111111111100000000000000000'))

    def test_bin_dec_cero(self):
        self.assertEquals(0, self.tmp.bin_dec('100000000100000000000000000'))

    def test_bin_dec_entero(self):
        self.assertEquals(-24, self.tmp.bin_dec('110000011100000000000000000'))
    
    def test_bin_dec_entero_frac(self):
        self.assertEquals(18.5, self.tmp.bin_dec('01000001100101000000000000000000'))
    
    def test_bin_dec_frac(self):
        self.assertEquals(0.65, self.tmp.bin_dec('00111111001001100110011001100100'))

if __name__ == '__main__':
    unittest.main()
