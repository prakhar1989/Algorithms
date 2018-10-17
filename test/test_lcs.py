import pytest
from dp import lcs

def test_lcs():
	assert lcs.longest_common_subsequence("ABCD", "BBDABXYDCCAD") == (4, "ABCD")
	assert lcs.longest_common_subsequence("BANANA", "ATANA") == (4, "AANA")
	assert lcs.longest_common_subsequence("ABCDEFG", "BDGK") == (3, "BDG")
