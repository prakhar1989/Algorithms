import unittest
import lcs

class TestLCS(unittest.TestCase):
    def test_lcs(self):
        self.assertEqual(lcs.longest_common_subsequence("ABCD", "BBDABXYDCCAD"), (4, "ABCD"))
        self.assertEqual(lcs.longest_common_subsequence("BANANA", "ATANA"), (4, "AANA"))
        self.assertEqual(lcs.longest_common_subsequence("ABCDEFG", "BDGK"), (3, "BDG"))

if __name__ == "__main__":
    unittest.main()
