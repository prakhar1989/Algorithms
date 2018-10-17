import pytest
from graphs.graph import graph

@pytest.fixture
def setup_graph():
	gr = graph()
	gr.add_nodes(["a", "b", "c", "d", "e", "f"])
	gr.add_edge(("a","b"))
	gr.add_edge(("a","f"))
	gr.add_edge(("b","c"))
	gr.add_edge(("c","e"))
	gr.add_edge(("c","d"))
	gr.add_edge(("d","f"))
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
	assert len(gr.edges()) == 8

def test_has_edge_method(setup_graph):
	gr = setup_graph
	assert gr.has_edge(("a", "b")) == True
	assert gr.has_edge(("a", "d")) == False

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

def test_add_edge_from_non_existing_node(setup_graph):
	gr = setup_graph
	with pytest.raises(Exception):
		assert gr.add_edge(("b", "z"))

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
	assert len(gr.edges()) == 2*6

def test_add_edges_method(setup_graph):
	gr = setup_graph
	gr.add_edges([("a", "c"), ("c", "f"), ("d", "e")])
	assert gr.has_edge(("a", "c")) == True
	assert gr.has_edge(("c", "f")) == True
	assert gr.has_edge(("d", "e")) == True

def test_node_orders_method(setup_graph):
	gr = setup_graph
	assert gr.node_order("c") == 3

def test_del_edge_method(setup_graph):
	gr = setup_graph
	gr.del_edge(("a", "f"))
	assert gr.has_edge(("a", "f")) == False

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
