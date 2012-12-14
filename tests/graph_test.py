import os, sys
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
import unittest
from graphs.graph import graph


class test_graph(unittest.TestCase):

    def setUp(self):
        self.gr = graph()
        self.gr.add_nodes(["a", "b", "c", "d", "e", "f"])
        self.gr.add_edge(("a","b"))
        self.gr.add_edge(("a","f"))
        self.gr.add_edge(("b","c"))
        self.gr.add_edge(("c","e"))
        self.gr.add_edge(("c","d"))
        self.gr.add_edge(("d","f"))

    def test_nodes_method(self):
        self.assertEqual(len(self.gr.nodes()), 6)

    def test_add_node_method(self):
        self.gr.add_node("g")
        self.assertEqual(len(self.gr.nodes()), 7)

    def test_has_node_method(self):
        self.assertTrue(self.gr.has_node("a"))

    def test_neighbors_method(self):
        self.assertEqual(len(self.gr.neighbors("a")), 2)

    def test_del_node_method(self):
        self.gr.del_node("a")
        self.assertFalse(self.gr.has_node("a"))
        self.assertEqual(len(self.gr.edges()), 8)

    def test_has_edge_method(self):
        self.assertTrue(self.gr.has_edge(("a", "b")))
        self.assertFalse(self.gr.has_edge(("a", "d")))

    def test_add_duplicate_node_method_throws_exception(self):
        self.assertRaises(Exception, self.gr.add_node, "a")

    def test_del_nonexistent_node_throws_exception(self):
        self.assertRaises(Exception, self.gr.del_node, "z")

    def test_add_duplicate_edge_throws_exception(self):
        self.assertRaises(Exception, self.gr.add_edge, ("a", "b"))

    def test_add_edge_from_non_existing_node(self):
        self.assertRaises(Exception, self.gr.add_edge, ("b", "z"))

    def test_adding_self_loop(self):
        self.gr.add_edge(("a", "a"))
        self.assertTrue(self.gr.has_edge(("a", "a")))

    def test_remove_self_loop(self):
        self.gr.add_edge(("a", "a"))
        self.gr.del_edge(("a", "a"))
        self.assertFalse(self.gr.has_edge(("a", "a")))

    def test_edges_method(self):
        self.assertEqual(len(self.gr.edges()), 2*6)

    def test_add_edges_method(self):
        self.gr.add_edges([("a", "c"), ("c", "f"), ("d", "e")])
        self.assertTrue(self.gr.has_edge(("a", "c")))
        self.assertTrue(self.gr.has_edge(("c", "f")))
        self.assertTrue(self.gr.has_edge(("d", "e")))

    def test_node_orders_method(self):
        self.assertEqual(self.gr.node_order("c"), 3)

    def test_del_edge_method(self):
        self.gr.del_edge(("a", "f"))
        self.assertFalse(self.gr.has_edge(("a", "f")))

    def test_deleting_non_existing_edge_raises_exception(self):
        self.assertRaises(Exception, self.gr.del_edge, ("a", "z"))

    def test_get_default_weight(self):
        self.assertEqual(self.gr.get_edge_weight(("a", "b")), 1)

    def test_set_weight_on_existing_edge(self):
        self.gr.set_edge_weight(("a", "b"), 10)
        self.assertEqual(self.gr.get_edge_weight(("a", "b")), 10)

    def test_weight_for_nonexisting_edge(self):
        self.assertRaises(Exception, self.gr.get_edge_weight, ("a", "c"))

if __name__ == "__main__":
    unittest.main()
