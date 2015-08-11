import unittest
import fractions
import GCD

class TestEuclideanGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(fractions.gcd(30,50),GCD.greatest_common_divisor(30,50))
        self.assertEqual(fractions.gcd(55555,123450),GCD.greatest_common_divisor(55555,123450))
        self.assertEqual(fractions.gcd(-30,-50),GCD.greatest_common_divisor(-30,-50))
        self.assertEqual(fractions.gcd(-1234,1234),GCD.greatest_common_divisor(-1234,1234))

if __name__ == "__main__":
    unittest.main()
