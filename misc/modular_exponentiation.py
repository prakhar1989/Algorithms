"""
Problem: https://en.wikipedia.org/wiki/Modular_exponentiation
"""

def modular_exponentiation(base, exp, mod):
	if exp < 1:
		raise ValueError("Exponentiation should be ve+ int")
	if mod == 1:
		return 0
	elif mod < 1:
		raise ValueError("Modulus should be ve+ int")
	#Initialize result to 1
	result = 1
	base %= mod
	while exp > 0:
		#multiply base to result if exp is odd
		if exp % 2 == 1:
			result = (result * base) % mod
		#Double base and half exp
		exp = exp >> 1
		base = (base ** 2) % mod
	return result