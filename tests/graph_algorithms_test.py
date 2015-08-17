import os, sys
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
import unittest
from graphs.digraph import digraph
from graphs.graph import graph
from graphs.graph_algorithms import *

class test_graph(unittest.TestCase):

    def setUp(self):
        self.gr = graph()
        self.gr.add_nodes(["s", "a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l"])
        self.gr.add_edges([("s", "a"), ("s", "b"), ("a", "c"), ("c", "e")])
        self.gr.add_edges([("e", "d"), ("d", "b"), ("a", "b"), ("c", "d")])
        self.gr.add_edges([("g", "h"), ("f", "g")])
        self.gr.add_edges([("j", "k"), ("j", "l")])

        self.digr = digraph()
        self.digr.add_nodes(['s', 'a', 'b', 'c', 'd', 'e', 'f'])
        self.digr.add_edges([("s", "a"), ("a", "b"), ("b", "a"), ("c", "b")])
        self.digr.add_edges([("b", "s"), ("s", "d"), ("d", "e"), ("e", "d")])
        self.digr.add_edges([("b", "f"), ("e", "f")])

    def test_bfs_undirected_graph(self):
        self.assertEqual(len(BFS(self.gr, "s")), 6)
        self.assertEqual(len(BFS(self.gr, "j")), 3)
        self.assertEqual(len(BFS(self.gr, "g")), 3)

    def test_bfs_directed_graph(self):
        self.assertEqual(len(BFS(self.digr, "s")), 6)
        self.assertEqual(len(BFS(self.digr, "c")), 7)
        self.assertEqual(len(BFS(self.digr, "f")), 1)

    def test_dfs_undirected_graph(self):
        self.assertEqual(len(DFS(self.gr, "s")), 6)
        self.assertEqual(len(DFS(self.gr, "j")), 3)
        self.assertEqual(len(DFS(self.gr, "g")), 3)

    def test_dfs_directed_graph(self):
        self.assertEqual(len(DFS(self.digr, "s")), 6)
        self.assertEqual(len(DFS(self.digr, "c")), 7)
        self.assertEqual(len(DFS(self.digr, "f")), 1)

    def test_shortest_hops_undirected_graph(self):
        self.assertEqual(shortest_hops(self.gr, "s")["c"], 2)
        self.assertEqual(shortest_hops(self.gr, "c")["s"], 2)
        self.assertEqual(shortest_hops(self.gr, "s")["s"], 0)
        self.assertEqual(shortest_hops(self.gr, "c")["j"], float('inf'))

    def test_shortest_hops_directed_graph(self):
        self.assertEqual(shortest_hops(self.digr, "s")["f"], 3)
        self.assertEqual(shortest_hops(self.digr, "f")["s"], float('inf'))
        self.assertEqual(shortest_hops(self.digr, "s")["s"], 0)
        self.assertEqual(shortest_hops(self.digr, "s")["c"], float('inf'))

    def test_undirected_connected_component(self):
        self.assertEqual(len(undirected_connected_components(self.gr)), 3)
        self.assertRaises(Exception, undirected_connected_components, self.digr)

    def test_topological_ordering(self):
        dag = digraph() # directed acyclic graph
        dag.add_nodes(["a", "b", "c", "d", "e", "f", "g", "h"])
        dag.add_edges([("a", "b"), ("a", "c"), ("a", "e"), ("d", "a")])
        dag.add_edges([("g", "b"), ("g", "f"), ("f", "e"), ("h", "f"), ("h", "a")])
        order = {o[0]: o[1] for o in topological_ordering(dag)}
        self.assertEqual(sum([order[u] < order[v] for (u, v) in
                         dag.edges()]), len(dag.edges())) # all comparisons are True

    def test_directed_connected_components(self):
        digr = digraph()
        digr.add_nodes(["a", "b", "c", "d", "e", "f", "g", "h", "i"])
        digr.add_edges([("b", "a"), ("a", "c"), ("c", "b"), ("d", "b")])
        digr.add_edges([("d", "f"), ("f", "e"), ("e", "d"), ("g", "e")])
        digr.add_edges([("g", "h"), ("h", "i"), ("i", "g")])
        self.assertEqual(len(directed_connected_components(digr)), 3)
        digr2 = digraph()
        digr2.add_nodes(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])
        digr2.add_edges([("a", "b"), ("b", "c"), ("c", "a"), ("b", "d"), ("d", "e")])
        digr2.add_edges([("e", "f"), ("f", "g"), ("g", "e"), ("d", "g"), ("i", "f")])
        digr2.add_edges([("h", "g"), ("c", "h"), ("c", "k"), ("h", "i"), ("i", "j")])
        digr2.add_edges([("h", "j"), ("j", "k"), ("k", "h")])
        self.assertEqual(len(directed_connected_components(digr2)), 4)

    def test_shortest_path_in_directed_graph(self):
        digr = digraph()
        digr.add_nodes(["a", "b", "c", "d", "e", "f"])
        digr.add_edge(("a", "b"), 7)
        digr.add_edge(("a", "c"), 9)
        digr.add_edge(("a", "f"), 14)
        digr.add_edge(("f", "e"), 9)
        digr.add_edge(("c", "f"), 2)
        digr.add_edge(("c", "d"), 11)
        digr.add_edge(("b", "c"), 10)
        digr.add_edge(("b", "d"), 15)
        digr.add_edge(("d", "e"), 6)
        self.assertEqual(shortest_path(digr, "a")["a"], 0)
        self.assertEqual(shortest_path(digr, "a")["b"], 7)
        self.assertEqual(shortest_path(digr, "a")["c"], 9)
        self.assertEqual(shortest_path(digr, "a")["d"], 20)
        self.assertEqual(shortest_path(digr, "a")["e"], 20)
        self.assertEqual(shortest_path(digr, "a")["f"], 11)

    def test_prims_minimum_spanning_tree(self):
        gr = graph()
        gr.add_nodes(["a", "b", "c", "d"])
        gr.add_edge(("a", "b"), 4)
        gr.add_edge(("b", "c"), 3)
        gr.add_edge(("a", "c"), 1)
        gr.add_edge(("c", "d"), 2)
        min_cost = minimum_spanning_tree(gr)
        self.assertEqual(min_cost, 6)

    def test_kruskals_minimum_spanning_tree(self):
        gr = graph()
        gr.add_nodes(["a", "b", "c", "d"])
        gr.add_edge(("a", "b"), 4)
        gr.add_edge(("b", "c"), 3)
        gr.add_edge(("a", "c"), 1)
        gr.add_edge(("c", "d"), 2)
        min_cost = kruskal_MST(gr)
        self.assertEqual(min_cost, 6)

if __name__ == "__main__":
    unittest.main()
