import pytest
from misc import modular_exponentiation as me

def test_modular_exponentiation():
	assert me.modular_exponentiation(2, 10, 100) == 24
	assert me.modular_exponentiation(2, 200, 10) == 6
	assert me.modular_exponentiation(5, 20, 1) == 0

def test_modular_exponentiation_valuerror():
	with pytest.raises(ValueError):
		assert me.modular_exponentiation(12, -1, 10)
		assert me.modular_exponentiation(12, 5, 0)