import os, sys
import unittest
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from misc import modular_multiplicative_inverse as mmi

class TestLCS(unittest.TestCase):
    def test_modular_multiplicative_inverse(self):
    	self.assertEqual(mmi.modular_multiplicative_inv(10, 7), 5)
    	self.assertEqual(mmi.modular_multiplicative_inv(45, 13), 11)
    	self.assertEqual(mmi.modular_multiplicative_inv(52, 1), 0)
 
    	self.assertRaises(ValueError, mmi.modular_multiplicative_inv, 12, -1)
    	self.assertRaises(ValueError, mmi.modular_multiplicative_inv, 12, 2)

if __name__ == "__main__":
    unittest.main()