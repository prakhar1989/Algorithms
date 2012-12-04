import unittest
from digraph import digraph
from graph import graph
from graph_algorithms import *

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

    def test_shortest_path_undirected_graph(self):
        self.assertEqual(shortest_path(self.gr, "s")["c"], 2)
        self.assertEqual(shortest_path(self.gr, "c")["s"], 2)
        self.assertEqual(shortest_path(self.gr, "s")["s"], 0)
        self.assertEqual(shortest_path(self.gr, "c")["j"], float('inf'))

    def test_shortest_path_directed_graph(self):
        self.assertEqual(shortest_path(self.digr, "s")["f"], 3)
        self.assertEqual(shortest_path(self.digr, "f")["s"], float('inf'))
        self.assertEqual(shortest_path(self.digr, "s")["s"], 0)
        self.assertEqual(shortest_path(self.digr, "s")["c"], float('inf'))

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

if __name__ == "__main__":
    unittest.main()
