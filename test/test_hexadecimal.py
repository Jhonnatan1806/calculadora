from modulos.hexadecimal import Hexadecimal
import unittest

class Test_Hexadecimal(unittest.TestCase):

    def setUp(self):
        self.tmp = Hexadecimal()
    
    def tearDown(self):
        del self.tmp

    def test_dec_hex(self):
        self.assertEquals('1A', self.tmp.dec_hex(26))
    
    def test_hex_dec(self):
        self.assertEquals(26, self.tmp.hex_dec('1A'))

if __name__ == '__main__':
    unittest.main()