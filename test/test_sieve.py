import pytest
from misc.sieve_of_eratosthenes import generate_primes

def test_primes():
	prime_list = [2,3,5,7,11,13,17,19]
	assert prime_list == generate_primes(20)
