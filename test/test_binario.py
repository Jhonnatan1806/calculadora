from paquetes.binario import Binario
import unittest

class Test_Binario(unittest.TestCase):

    def setUp(self):
        self.tmp = Binario()
    
    def tearDown(self):
        del self.tmp

    def test_dec_bin_positivo(self):
        self.assertEquals('00010010', self.tmp.dec_bin(18))

if __name__ == '__main__':
    unittest.main()