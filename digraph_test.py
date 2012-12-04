import unittest
from digraph import digraph

class test_graph(unittest.TestCase):

    def setUp(self):
        self.gr = digraph()
        self.gr.add_nodes(["a", "b", "c", "d", "e", "f"])
        self.gr.add_edges([("a","b"), ("b", "c"), ("a", "d"), ("d", "e"), ("d", "f")])
        self.gr.add_edge(("f", "b"))

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
        self.assertEqual(len(self.gr.edges()), 4)

    def test_has_edge_method(self):
        self.assertTrue(self.gr.has_edge(("a", "b")))
        self.assertFalse(self.gr.has_edge(("b", "a")))

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
        self.assertEqual(len(self.gr.edges()), 6)

    def test_node_orders_method(self):
        self.assertEqual(self.gr.node_order("d"), 2)

    def test_del_edge_method(self):
        self.gr.del_edge(("b", "c"))
        self.assertFalse(self.gr.has_edge(("b", "c")))

    def test_deleting_non_existing_edge_raises_exception(self):
        self.assertRaises(Exception, self.gr.del_edge, ("a", "z"))

    def test_get_default_weight(self):
        self.assertEqual(self.gr.get_edge_weight(("a", "b")), 1)

    def test_set_weight_on_existing_edge(self):
        self.gr.set_edge_weight(("a", "b"), 10)
        self.assertEqual(self.gr.get_edge_weight(("a", "b")), 10)

    def test_weight_for_nonexisting_edge(self):
        self.assertRaises(Exception, self.gr.get_edge_weight, ("a", "c"))

    def test_set_edge_properties(self):
        self.gr.set_edge_properties(('a', 'b'), label="label")
        self.assertEqual(self.gr.get_edge_properties(('a', 'b'))["label"], "label")

    def test_add_node_properties_of_existing_node(self):
        self.gr.add_node_attribute("a", "expensive")
        self.assertEqual(self.gr.node_attributes("a"), "expensive")

    def test_get_node_properties_of_blank_node(self):
        self.assertEqual(self.gr.node_attributes("a"), [])

    def test_add_node_attribute_of_non_existing_node(self):
        self.assertRaises(Exception, self.gr.add_node_attribute, "z")

    def test_clear_node_attributes_method(self):
        self.gr.add_node_attribute("a", "expensive")
        self.gr.clear_node_attributes()
        self.assertEqual(self.gr.node_attributes("a"), [])

if __name__ == "__main__":
    unittest.main()
