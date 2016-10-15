"""
Problem: https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
"""
import GCD as gcd

def modular_multiplicative_inv(a, m):
	if m == 1:
		return 0
	if m < 1:
		raise ValueError('Modulus should be ve+ int > 0')
	# check for co-prime condition
	if gcd.greatest_common_divisor(a, m) != 1:
		raise ValueError('a and m are not co-primes')

	# Make var "a" positive if it's negative
	if a < 0:
		a %= m

	# Initialise vars
	m0 = m
	x0 = 0
	x1 = 1

	while a > 1:
		# Calculate quotient q; store m into temp t
		q = a / m
		t = m

		# Calculate m as remainder(a, m); store temp t into a
		m = a % m
		a = t

		# Assign x0 into temp t; Calculate x0 and store temp t into x1
		t = x0
		x0 = x1 - q * x0
		x1 = t

	# If x1 is negative then add modulus m0
	if x1 < 0:
		x1 += m0

	return x1