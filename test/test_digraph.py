import pytest
from graphs.digraph import digraph

@pytest.fixture
def setup_graph():
	gr = digraph()
	gr.add_nodes(["a", "b", "c", "d", "e", "f"])
	gr.add_edges([("a","b"), ("b", "c"), ("a", "d"), ("d", "e"), ("d", "f")])
	gr.add_edge(("f", "b"))
	return gr

def test_nodes_method(setup_graph):
	gr = setup_graph
	assert len(gr.nodes()) == 6

def test_add_node_method(setup_graph):
	gr = setup_graph
	gr.add_node("g")
	assert len(gr.nodes()) == 7

def test_has_node_method(setup_graph):
	gr = setup_graph
	assert gr.has_node("a") == True

def test_neighbors_method(setup_graph):
	gr = setup_graph
	assert len(gr.neighbors("a")) == 2

def test_del_node_method(setup_graph):
	gr = setup_graph
	gr.del_node("a")
	assert gr.has_node("a") == False
	assert len(gr.edges()) == 4

def test_has_edge_method(setup_graph):
	gr = setup_graph
	print gr.edges()
	assert gr.has_edge(("a", "b")) == True
	assert gr.has_edge(("b", "a")) == False

def test_add_duplicate_node_method_throws_exception(setup_graph):
	gr = setup_graph
	with pytest.raises(Exception):
		assert gr.add_node("a")

def test_del_nonexistent_node_throws_exception(setup_graph):
	gr = setup_graph
	with pytest.raises(Exception):
		assert gr.del_node("z")

def test_add_duplicate_edge_throws_exception(setup_graph):
	gr = setup_graph
	with pytest.raises(Exception):
		assert gr.add_edge(("a", "b"))

def test_adding_self_loop(setup_graph):
	gr = setup_graph
	gr.add_edge(("a", "a"))
	assert gr.has_edge(("a", "a")) == True

def test_remove_self_loop(setup_graph):
	gr = setup_graph
	gr.add_edge(("a", "a"))
	gr.del_edge(("a", "a"))
	assert gr.has_edge(("a", "a")) == False

def test_edges_method(setup_graph):
	gr = setup_graph
	assert len(gr.edges()) == 6

def test_node_orders_method(setup_graph):
	gr = setup_graph
	assert gr.node_order("d") == 2

def test_del_edge_method(setup_graph):
	gr = setup_graph
	gr.del_edge(("b", "c"))
	assert gr.has_edge(("b", "c")) == False

def test_deleting_non_existing_edge_raises_exception(setup_graph):
	gr = setup_graph
	with pytest.raises(Exception):
		assert gr.del_edge(("a", "z"))

def test_get_default_weight(setup_graph):
	gr = setup_graph
	assert gr.get_edge_weight(("a", "b")) == 1

def test_set_weight_on_existing_edge(setup_graph):
	gr = setup_graph
	gr.set_edge_weight(("a", "b"), 10)
	assert gr.get_edge_weight(("a", "b")) == 10

def test_weight_for_nonexisting_edge(setup_graph):
	gr = setup_graph
	with pytest.raises(Exception):
		assert gr.get_edge_weight(("a", "c"))

def test_get_transpose_method(setup_graph):
	gr = setup_graph
	transpose = gr.get_transpose()
	assert len(transpose.nodes()) == len(gr.nodes())
	assert len(transpose.edges()) == len(gr.edges())
	assert gr.has_edge(("a", "b")) == True
	assert transpose.has_edge(("b", "a")) == True
	assert transpose.has_edge(("a", "b")) == False