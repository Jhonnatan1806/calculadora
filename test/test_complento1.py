from modulos.complemento1 import Complemento1
import unittest

class Test_Complemento1(unittest.TestCase):

    def setUp(self):
        self.tmp = Complemento1()
    
    def tearDown(self):
        del self.tmp

    def test_dec_bin(self):
        self.assertEquals('11101101', self.tmp.dec_bin(-18))
    
    def test_dec_bin_error(self):
        self.assertEquals('11101101', self.tmp.dec_bin(18))
    
    def test_bin_dec(self):
        self.assertEquals(-18, self.tmp.bin_dec('11101101'))

if __name__ == '__main__':
    unittest.main()