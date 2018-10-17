import pytest
import fractions
from misc import GCD

def test_gcd():
	assert fractions.gcd(30,50) == GCD.greatest_common_divisor(30,50)
	assert fractions.gcd(55555,123450) == GCD.greatest_common_divisor(55555,123450)
	assert fractions.gcd(-30,-50) == GCD.greatest_common_divisor(-30,-50)
	assert fractions.gcd(-1234,1234) == GCD.greatest_common_divisor(-1234,1234)
