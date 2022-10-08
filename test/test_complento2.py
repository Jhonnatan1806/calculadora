from paquetes.complemento2 import Complemento2
import unittest

class Test_Complemento2(unittest.TestCase):

    def setUp(self):
        self.tmp = Complemento2()
    
    def tearDown(self):
        del self.tmp
    
    def test_bin_dec(self):
        self.assertEquals(-19, self.tmp.bin_dec('11101101'))

    def test_dec_bin(self):
        self.assertEquals('11101101', self.tmp.dec_bin(-19))

if __name__ == '__main__':
    unittest.main()