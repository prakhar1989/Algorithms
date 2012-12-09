class graph(object):
    """
    Graph class - made of nodes and edges

    methods: add_edge, add_edges, add_node, add_nodes, has_node,
    has_edge, nodes, edges, add_node_attribute, node_attributes
    neighbors, del_node, del_edge, node_order, set_edge_weight,
    get_edge_weight, set_edge_properties, get_edge_properties
    clear_node_attributes
    """

    DEFAULT_WEIGHT = 1
    DIRECTED = False

    def __init__(self):
        self.node_neighbors = {}

        # Metadata about edges
        self.edge_properties = {} # Edge -> dict mapping

        # Metadata about nodes
        self.node_attr = {} # Node -> dict mapping

    def __str__(self):
        return "Undirected Graph \nNodes: %s \nEdges: %s" % (self.nodes(), self.edges())

    def add_nodes(self, nodes):
        """
        Takes a list of nodes as input and adds these
        to a graph
        """
        for node in nodes:
            self.add_node(node)

    def add_node(self, node, attrs=None):
        """
        Adds a node to the graph
        """
        if node not in self.node_neighbors:
            if attrs is None: attrs = []
            self.node_neighbors[node] = []
            self.node_attr[node] = attrs
        else:
            raise Exception("Node %s is already in graph" % node)

    def has_node(self, node):
        """
        Returns boolean to indicate whether a node exists in the graph
        """
        return node in self.node_neighbors

    def add_edge(self, edge, wt=1, label=""):
        """
        Add an edge to the graph connecting two nodes.
        An edge, here, is a pair of node like C(m, n) or a tuple
        """
        u, v = edge
        if (v not in self.node_neighbors[u] and u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)
            if (u!=v):
                self.node_neighbors[v].append(u)
            self.set_edge_properties((u, v), label=label, weight=wt)
            self.set_edge_properties((v, u), label=label, weight=wt)
        else:
            raise Exception("Edge (%s, %s) already added in the graph" % (u, v))

    def add_edges(self, edges):
        """ Adds multiple edges in one go. Edges, here, is a list of
        tuples"""
        for edge in edges:
            self.add_edge(edge)

    def nodes(self):
        """
        Returns a list of nodes in the graph
        """
        return list(self.node_neighbors.keys())

    def has_edge(self, edge):
        """
        Returns a boolean to indicate whether an edge exists in the
        graph. An edge, here, is a pair of node like C(m, n) or a tuple
        """
        u, v = edge
        if v not in self.node_neighbors[u]:
            return False
        else:
            return True

    def neighbors(self, node):
        """
        Returns a list of neighbors for a node
        """
        if node not in self.node_neighbors:
            raise "Node %s not in graph" % node
        return self.node_neighbors[node]

    def del_node(self, node):
        """
        Deletes a node from a graph
        """
        for each in list(self.neighbors(node)):
            if (each != node):
                self.del_edge((each, node))
        del(self.node_neighbors[node])

    def del_edge(self, edge):
        """
        Deletes an edge from a graph. An edge, here, is a pair like
        C(m,n) or a tuple
        """
        u, v = edge
        if not self.has_edge(edge):
            raise Exception("Edge (%s, %s) not an existing edge" % (u, v))
        self.node_neighbors[u].remove(v)
        if (u!=v):
            self.node_neighbors[v].remove(u)

    def node_order(self, node):
        """
        Return the order or degree of a node
        """
        return len(self.neighbors(node))


    def edges(self):
        """
        Returns a list of edges in the graph
        """
        edge_list = []
        for node in self.nodes():
            for each in self.neighbors(node):
                edge_list.append((node, each))
        return edge_list

    # Methods for setting properties on nodes and edges

    def get_edge_properties(self, edge):
        """Returns the edge properties; {} if none exist """
        u, v = edge
        if not self.has_edge(edge):
            raise Exception("Edge (%s, %s) not an existing edge" % (u, v))
        return self.edge_properties.setdefault(edge, {})

    def set_edge_properties(self, edge, **properties):
        u, v = edge
        if not self.has_edge(edge):
            raise Exception("Edge (%s, %s) not an existing edge" % (u, v))
        self.edge_properties.setdefault(edge, {}).update(properties)

    def set_edge_weight(self, edge, wt):
        """Set the weight of the edge """
        self.set_edge_properties(edge, weight=wt)

    def get_edge_weight(self, edge):
        """Returns the weight of an edge """
        return self.get_edge_properties(edge).setdefault("weight", self.DEFAULT_WEIGHT)

    def add_node_attribute(self, node, attr):
        """ Adds attributes to a node"""
        if not self.has_node(node):
            raise Exception("Node %s does not exist in graph" % node)
        self.node_attr[node] = attr

    def node_attributes(self, node):
        """ Returns attributes of a node if it exists, none otherwise"""
        return self.node_attr[node]

    def clear_node_attributes(self):
        """ Clears the attributes set on nodes """
        for node in self.nodes():
            self.node_attr[node] = []
