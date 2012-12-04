from collections import deque
from graph import graph
from digraph import digraph
from copy import deepcopy

def BFS(gr, s):
    """ Breadth first search 
    Returns a list of nodes that are "findable" from s """
    if not gr.has_node(s):
        raise Exception("Node %s not in graph" % s)
    nodes_explored = [s]
    q = deque([s])
    while len(q)!=0:
        node = q.popleft()
        for each in gr.neighbors(node):
            if each not in nodes_explored:
                nodes_explored.append(each)
                q.append(each)
    return nodes_explored

def shortest_path(gr, s):
    """ Finds the shortest number of hops required
    to reach a node from s. Returns a dict with mapping:
    destination node from s -> no. of hops
    """
    if not gr.has_node(s):
        raise Exception("Node %s is not in graph" % s)
    else:
        dist = {}
        q = deque([s])
        nodes_explored = [s]
        for n in gr.nodes():
            if n == s: dist[n] = 0
            else: dist[n] = float('inf')
        while len(q) != 0:
            node = q.popleft()
            for each in gr.neighbors(node):
                if each not in nodes_explored:
                    nodes_explored.append(each)
                    q.append(each)
                    dist[each] = dist[node] + 1
        return dist

def undirected_connected_components(gr):
    """ Returns a list of connected components
    in an undirected graph """
    if gr.DIRECTED:
        raise Exception("This method works only with a undirected graph")
    explored = []
    con_components = []
    for node in gr.nodes():
        if node not in explored:
            reachable_nodes = BFS(gr, node)
            con_components.append(reachable_nodes)
            explored += reachable_nodes
    return con_components

def DFS(gr, s):
    """ Depth first search wrapper """
    path = []
    depth_first_search(gr, s, path)
    return path

def depth_first_search(gr, s, path):
    """ Depth first search 
    Returns a list of nodes "findable" from s """
    if s in path: return False
    path.append(s)
    for each in gr.neighbors(s):
        if each not in path:
            depth_first_search(gr, each, path)

def topological_ordering(digr_ori):
    """ Returns a topological ordering for a 
    acyclic directed graph """
    if not digr_ori.DIRECTED:
        raise Exception("%s is not a directed graph" % digr)
    digr = deepcopy(digr_ori)
    ordering = []
    n = len(digr.nodes())
    while n > 0:
        sink_node = find_sink_node(digr)
        ordering.append((sink_node, n))
        digr.del_node(sink_node)
        n -= 1
    return ordering

def find_sink_node(digr):
    """ Finds a sink node (node with all incoming arcs) 
    in the directed graph. Valid for a acyclic graph only """
    # first node is taken as a default
    node = digr.nodes()[0]
    while digr.neighbors(node):
        node = digr.neighbors(node)[0]
    return node
