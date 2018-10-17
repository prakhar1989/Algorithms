import pytest
from graphs.digraph import digraph
from graphs.graph import graph
from graphs.graph_algorithms import *

@pytest.fixture
def setup_graph():
	gr = graph()
	gr.add_nodes(["s", "a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l"])
	gr.add_edges([("s", "a"), ("s", "b"), ("a", "c"), ("c", "e")])
	gr.add_edges([("e", "d"), ("d", "b"), ("a", "b"), ("c", "d")])
	gr.add_edges([("g", "h"), ("f", "g")])
	gr.add_edges([("j", "k"), ("j", "l")])
	return gr

@pytest.fixture
def setup_digraph():
	digr = digraph()
	digr.add_nodes(['s', 'a', 'b', 'c', 'd', 'e', 'f'])
	digr.add_edges([("s", "a"), ("a", "b"), ("b", "a"), ("c", "b")])
	digr.add_edges([("b", "s"), ("s", "d"), ("d", "e"), ("e", "d")])
	digr.add_edges([("b", "f"), ("e", "f")])
	return digr

def test_bfs_undirected_graph(setup_graph):
	gr = setup_graph
	assert len(BFS(gr, "s")) == 6
	assert len(BFS(gr, "j")) == 3
	assert len(BFS(gr, "g")) == 3

def test_bfs_directed_graph(setup_digraph):
	digr = setup_digraph
	assert len(BFS(digr, "s")) == 6
	assert len(BFS(digr, "c")) == 7
	assert len(BFS(digr, "f")) == 1

def test_dfs_undirected_graph(setup_graph):
	gr = setup_graph
	assert len(DFS(gr, "s")) == 6
	assert len(DFS(gr, "j")) == 3
	assert len(DFS(gr, "g")) == 3

def test_dfs_directed_graph(setup_digraph):
	digr = setup_digraph
	assert len(DFS(digr, "s")) == 6
	assert len(DFS(digr, "c")) == 7
	assert len(DFS(digr, "f")) == 1

def test_shortest_hops_undirected_graph(setup_graph):
	gr = setup_graph
	assert shortest_hops(gr, "s")["c"] == 2
	assert shortest_hops(gr, "c")["s"] == 2
	assert shortest_hops(gr, "s")["s"] == 0
	assert shortest_hops(gr, "c")["j"] == float('inf')

def test_shortest_hops_directed_graph(setup_digraph):
	digr = setup_digraph
	assert shortest_hops(digr, "s")["f"] == 3
	assert shortest_hops(digr, "f")["s"] == float('inf')
	assert shortest_hops(digr, "s")["s"] == 0
	assert shortest_hops(digr, "s")["c"] == float('inf')

def test_undirected_connected_component(setup_graph, setup_digraph):
	gr = setup_graph
	digr = setup_digraph
	assert len(undirected_connected_components(gr)) == 3
	with pytest.raises(Exception):
		assert undirected_connected_components(digr)

def test_topological_ordering(setup_graph):
	gr = setup_graph
	dag = digraph() # directed acyclic graph
	dag.add_nodes(["a", "b", "c", "d", "e", "f", "g", "h"])
	dag.add_edges([("a", "b"), ("a", "c"), ("a", "e"), ("d", "a")])
	dag.add_edges([("g", "b"), ("g", "f"), ("f", "e"), ("h", "f"), ("h", "a")])
	order = {o[0]: o[1] for o in topological_ordering(dag)}
	assert sum([order[u] < order[v] for (u, v) in dag.edges()]) == len(dag.edges()) # all comparisons are True

def test_directed_connected_components():
	digr = digraph()
	digr.add_nodes(["a", "b", "c", "d", "e", "f", "g", "h", "i"])
	digr.add_edges([("b", "a"), ("a", "c"), ("c", "b"), ("d", "b")])
	digr.add_edges([("d", "f"), ("f", "e"), ("e", "d"), ("g", "e")])
	digr.add_edges([("g", "h"), ("h", "i"), ("i", "g")])
	assert len(directed_connected_components(digr)) == 3
	digr2 = digraph()
	digr2.add_nodes(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])
	digr2.add_edges([("a", "b"), ("b", "c"), ("c", "a"), ("b", "d"), ("d", "e")])
	digr2.add_edges([("e", "f"), ("f", "g"), ("g", "e"), ("d", "g"), ("i", "f")])
	digr2.add_edges([("h", "g"), ("c", "h"), ("c", "k"), ("h", "i"), ("i", "j")])
	digr2.add_edges([("h", "j"), ("j", "k"), ("k", "h")])
	assert len(directed_connected_components(digr2)) == 4

def test_shortest_path_in_directed_graph():
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
	assert shortest_path(digr, "a")["a"] == 0
	assert shortest_path(digr, "a")["b"] == 7
	assert shortest_path(digr, "a")["c"] == 9
	assert shortest_path(digr, "a")["d"] == 20
	assert shortest_path(digr, "a")["e"] == 20
	assert shortest_path(digr, "a")["f"] == 11

def test_prims_minimum_spanning_tree(setup_graph):
	gr = setup_graph
	gr = graph()
	gr.add_nodes(["a", "b", "c", "d"])
	gr.add_edge(("a", "b"), 4)
	gr.add_edge(("b", "c"), 3)
	gr.add_edge(("a", "c"), 1)
	gr.add_edge(("c", "d"), 2)
	min_cost = minimum_spanning_tree(gr)
	assert min_cost == 6

def test_kruskals_minimum_spanning_tree(setup_graph):
	gr = setup_graph
	gr = graph()
	gr.add_nodes(["a", "b", "c", "d"])
	gr.add_edge(("a", "b"), 4)
	gr.add_edge(("b", "c"), 3)
	gr.add_edge(("a", "c"), 1)
	gr.add_edge(("c", "d"), 2)
	min_cost = kruskal_MST(gr)
	assert min_cost == 6
