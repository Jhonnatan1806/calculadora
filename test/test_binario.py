from paquetes.binario import Binario
import unittest

class Test_Binario(unittest.TestCase):

    def setUp(self):
        self.tmp = Binario()
    
    def tearDown(self):
        del self.tmp

    def test_dec_bin(self):
        self.assertEquals('00010010', self.tmp.dec_bin(18))
    
    def test_dec_bin_error(self):
        self.assertEquals('-1', self.tmp.dec_bin(-1))
    
    def test_bin_dec(self):
        self.assertEquals(18, self.tmp.bin_dec('00010010'))

if __name__ == '__main__':
    unittest.main()