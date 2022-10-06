from paquetes.complemento1 import Complemento1
import unittest

class Test_Complemento1(unittest.TestCase):

    def setUp(self):
        self.dec_binc1 = Complemento1()
    
    def tearDown(self):
        del self.dec_binc1

    def test_complemento1(self):
        self.assertEquals('11111011',self.dec_binc1.get(-4))

if __name__ == '__main__':
    unittest.main()