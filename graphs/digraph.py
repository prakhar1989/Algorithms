from graph import graph
from copy import deepcopy
class digraph(graph):
    """
    Directed Graph class - made of nodes and edges

    methods: add_edge, add_edges, add_node, add_nodes, has_node,
    has_edge, nodes, edges, neighbors, del_node, del_edge, node_order,
    set_edge_weight, get_edge_weight, 
    """

    DEFAULT_WEIGHT = 1
    DIRECTED = True

    def __init__(self):
        self.node_neighbors = {}

    def __str__(self):
        return "Directed Graph \nNodes: %s \nEdges: %s" % (self.nodes(), self.edges())

    def add_edge(self, edge, wt=DEFAULT_WEIGHT, label=""):
        """
        Add an edge to the graph connecting two nodes.
        An edge, here, is a pair of node like C(m, n) or a tuple
        with m as head and n as tail :  m -> n
        """
        u, v = edge
        if (v not in self.node_neighbors[u]):
            self.node_neighbors[u][v] = wt
        else:
            raise Exception("Edge (%s, %s) already added in the graph" % (u, v))

    def del_edge(self, edge):
        """
        Deletes an edge from a graph. An edge, here, is a pair like
        C(m,n) or a tuple
        """
        u, v = edge
        if not self.has_edge(edge):
            raise Exception("Edge (%s, %s) not an existing edge" % (u, v))
        del self.node_neighbors[u][v]

    def del_node(self, node):
        """
        Deletes a node from a graph
        """
        for each in list(self.neighbors(node)):
            if (each != node):
                self.del_edge((node, each))
        for n in self.nodes():
            if self.has_edge((n, node)):
                self.del_edge((n, node))
        del(self.node_neighbors[node])

    def get_transpose(self):
        """ Returns the transpose of the graph
        with edges reversed and nodes same """
        digr = deepcopy(self)
        for (u, v) in self.edges():
            digr.del_edge((u, v))
            digr.add_edge((v, u))
        return digr
