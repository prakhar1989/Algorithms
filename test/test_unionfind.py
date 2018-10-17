import pytest
import unittest
from union_find.unionfind import UnionFind

@pytest.fixture
def setup_uf():
	uf = UnionFind()
	uf.insert("a", "b")
	uf.insert("b", "c")
	uf.insert("i", "j")
	return uf

def test_get_parent_method(setup_uf):
	uf = setup_uf
	assert "a" == uf.get_leader("a")
	assert "a" == uf.get_leader("b")
	assert "a" == uf.get_leader("c")
	assert "i" == uf.get_leader("j")
	assert "i" == uf.get_leader("i")
	assert uf.get_leader("a") != uf.get_leader("i")

def test_insert_method(setup_uf):
	uf = setup_uf
	uf.insert("c", "d")
	assert uf.get_leader("c") == uf.get_leader("d")
	assert uf.get_leader("a") == uf.get_leader("d")

def test_insert_one_node(setup_uf):
	uf = setup_uf
	uf.insert('z')
	assert uf.get_leader('z') == 'z'
	assert uf.count_groups() == 3

def test_make_union_method(setup_uf):
	uf = setup_uf
	uf.make_union(uf.get_leader("a"), uf.get_leader("i"))
	assert uf.get_leader("a") == uf.get_leader("i")

def test_make_union_with_invalid_leader_raises_exception(setup_uf):
	uf = setup_uf
	with pytest.raises(Exception):
		assert uf.make_union("a", "z")

def test_get_count(setup_uf):
	uf = setup_uf
	uf.insert("z", "y")
	assert uf.count_groups() == 3
