import os, sys
import unittest
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from misc import modular_exponentiation as me

class TestLCS(unittest.TestCase):
    def test_modular_exponentiation(self):
    	self.assertEqual(me.modular_exponentiation(2, 10, 100), 24)
    	self.assertEqual(me.modular_exponentiation(2, 200, 10), 6)
    	self.assertEqual(me.modular_exponentiation(5, 20, 1), 0)
    	#self.assertEqual(me.modular_exponentiation(8, 1, 10), 8)
    	self.assertRaises(ValueError, me.modular_exponentiation, 12, -1, 10)
    	self.assertRaises(ValueError, me.modular_exponentiation, 12, 5, 0)

if __name__ == "__main__":
    unittest.main()