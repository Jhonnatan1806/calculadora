from paquetes.binario import Binario
import unittest

class Test_Binario(unittest.TestCase):

    def setUp(self):
        self.dec_bin = Binario()
    
    def tearDown(self):
        del self.dec_bin

    def test_binario(self):
        self.assertEquals('101',self.dec_bin.get(5))
if __name__ == '__main__':
    unittest.main()