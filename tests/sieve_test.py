import unittest
from sieve_of_eratosthenes import calculate_primes

class TestSieveOfEratosthenes(unittest.TestCase):
	def test_primes(self):
		self.prime_list = [2,3,5,7,11,13,17,19]
		self.assertEqual(self.prime_list,calculate_primes(20))

if __name__ == '__main__':
	unittest.main()
