from modulos.fraccionario import Fraccionario
import unittest

class Test_Fraccionario(unittest.TestCase):

    def setUp(self):
        self.tmp = Fraccionario()
    
    def tearDown(self):
        del self.tmp

    def test_dec_bin(self):
        self.assertEquals('00010010,0011', self.tmp.dec_bin(18.2,4))

    def test_bin_dec(self):
        self.assertEquals(18.5, self.tmp.bin_dec('00010010,1000'))

if __name__ == '__main__':
    unittest.main()