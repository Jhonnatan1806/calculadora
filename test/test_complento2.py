from paquetes.complemento2 import Complemento2
import unittest

class Test_Complemento2(unittest.TestCase):

    def setUp(self):
        self.dec_binc2 = Complemento2()
    
    def tearDown(self):
        del self.dec_binc2

    def test_complemento1(self):
        self.assertEquals('11111100',self.dec_binc2.get(-4))

if __name__ == '__main__':
    unittest.main()