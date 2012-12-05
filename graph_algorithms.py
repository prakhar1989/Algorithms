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

def shortest_hops(gr, s):
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

def directed_connected_components(digr):
    """ Returns a list of strongly connected components
    in a directed graph using Kosaraju's two pass algorithm """
    if not digr.DIRECTED:
        raise Exception("%s is not a directed graph" % digr)
    finishing_times = DFS_loop(digr.get_transpose())
    # use finishing_times in descending order
    nodes_explored, connected_components = [], []
    for node in finishing_times[::-1]:
        component = []
        outer_dfs(digr, node, nodes_explored, component)
        if component:
            nodes_explored += component
            connected_components.append(component)
    return connected_components

def outer_dfs(digr, node, nodes_explored, path):
    if node in path or node in nodes_explored: 
        return False
    path.append(node)
    for each in digr.neighbors(node):
        if each not in path or each not in nodes_explored:
            outer_dfs(digr, each, nodes_explored, path)

def DFS_loop(digr):
    """ Core DFS loop used to find strongly connected components
    in a directed graph """
    node_explored = [] # list for keeping track of nodes explored
    finishing_times = [] # list for adding nodes based on their finishing times
    for node in digr.nodes():
        if node not in node_explored:
            leader_node = node
            inner_DFS(digr, node, node_explored, finishing_times)
    return finishing_times 

def inner_DFS(digr, node, node_explored, finishing_times):
    """ Inner DFS used in DFS loop method """
    node_explored.append(node) # mark explored
    for each in digr.neighbors(node):
        if each not in node_explored:
            inner_DFS(digr, each, node_explored, finishing_times)
    global finishing_counter
    # adds nodes based on increasing order of finishing times
    finishing_times.append(node) 

def shortest_path(digr, s):
    """ Finds the shortest path from s to every other vertex findable
    from s using Dijkstra's algorithm in O(mn) time """
    nodes_explored = [s]
    nodes_unexplored = DFS(digr, s) # all accessible nodes from s
    dist = {s:0}
    nodes_unexplored.remove(s)
    while len(nodes_unexplored) > 0:
        edge_frontier = [(u, v) for (u, v) in digr.edges() if u in nodes_explored 
                        and v in nodes_unexplored]
        min_dist = min([(dist[u] + digr.get_edge_weight((u, v)), v) for (u, v) in edge_frontier])
        nodes_explored.append(min_dist[1])
        nodes_unexplored.remove(min_dist[1])
        dist[min_dist[1]] = min_dist[0]
    return dist
