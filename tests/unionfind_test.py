import os, sys
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
import unittest
from union_find.unionfind import UnionFind

class test_unionfind(unittest.TestCase):

    def setUp(self):
        self.uf = UnionFind()
        self.uf.insert("a", "b")
        self.uf.insert("b", "c")
        self.uf.insert("i", "j")

    def test_get_parent_method(self):
        self.assertEqual("a", self.uf.get_leader("a"))
        self.assertEqual("a", self.uf.get_leader("b"))
        self.assertEqual("a", self.uf.get_leader("c"))
        self.assertEqual("i", self.uf.get_leader("j"))
        self.assertEqual("i", self.uf.get_leader("i"))
        self.assertNotEqual(self.uf.get_leader("a"), self.uf.get_leader("i"))

    def test_insert_method(self):
        self.uf.insert("c", "d")
        self.assertEqual(self.uf.get_leader("c"), self.uf.get_leader("d"))
        self.assertEqual(self.uf.get_leader("a"), self.uf.get_leader("d"))

    def test_insert_one_node(self):
        self.uf.insert('z')
        self.assertEqual(self.uf.get_leader('z'), 'z')
        self.assertEqual(self.uf.count_groups(), 3)

    def test_make_union_method(self):
        self.uf.make_union(self.uf.get_leader("a"), self.uf.get_leader("i"))
        self.assertEqual(self.uf.get_leader("a"), self.uf.get_leader("i"))

    def test_make_union_with_invalid_leader_raises_exception(self):
        self.assertRaises(Exception, self.uf.make_union, "a", "z")

    def test_get_count(self):
        self.uf.insert("z", "y")
        self.assertEqual(self.uf.count_groups(), 3)

if __name__ == "__main__":
    unittest.main()
