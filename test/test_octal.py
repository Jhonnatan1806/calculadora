from paquetes.octal import Octal
import unittest

class Test_Octal(unittest.TestCase):

    def setUp(self):
        self.tmp = Octal()
    
    def tearDown(self):
        del self.tmp

    def test_dec_oct(self):
        self.assertEquals('22', self.tmp.dec_oct(18))
    
    def test_oct_dec(self):
        self.assertEquals(18, self.tmp.oct_dec('22'))

if __name__ == '__main__':
    unittest.main()