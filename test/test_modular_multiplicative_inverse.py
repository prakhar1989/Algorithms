import pytest
from misc import modular_multiplicative_inverse as mmi

def test_modular_multiplicative_inverse():
	assert mmi.modular_multiplicative_inv(10, 7) == 5
	assert mmi.modular_multiplicative_inv(45, 13) == 11
	assert mmi.modular_multiplicative_inv(52, 1) == 0

def test_modular_multiplicative_inverse_valuerror():
	with pytest.raises(ValueError):
		assert mmi.modular_multiplicative_inv(12, -1)
		assert mmi.modular_multiplicative_inv(12, 2)
