import os, sys
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
import unittest
from dp.edit_dist import edit_distance

class TestEditDist(unittest.TestCase):

    def test_edit_dist(self):
        self.assertEqual(edit_distance("ABCD", "BBDABXYDCCAD"), 8)
        self.assertEqual(edit_distance("", "AKADA"), 5)
        self.assertEqual(edit_distance("ABCDEFG", "BDGK"), 5)
	self.assertEqual(edit_distance("ABDVKGALE", "ADKKKBALE"), 4)

if __name__ == "__main__":
    unittest.main()
