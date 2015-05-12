from collections import deque
from copy import deepcopy
from union_find.unionfind import UnionFind
import heapq

def BFS(gr, s):
    """ Breadth first search 
    Returns a list of nodes that are "findable" from s """
    if not gr.has_node(s):
        raise Exception("Node %s not in graph" % s)
    nodes_explored = set([s])
    q = deque([s])
    while len(q)!=0:
        node = q.popleft()
        for each in gr.neighbors(node):
            if each not in nodes_explored:
                nodes_explored.add(each)
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
        nodes_explored = set([s])
        for n in gr.nodes():
            if n == s: dist[n] = 0
            else: dist[n] = float('inf')
        while len(q) != 0:
            node = q.popleft()
            for each in gr.neighbors(node):
                if each not in nodes_explored:
                    nodes_explored.add(each)
                    q.append(each)
                    dist[each] = dist[node] + 1
        return dist

def undirected_connected_components(gr):
    """ Returns a list of connected components
    in an undirected graph """
    if gr.DIRECTED:
        raise Exception("This method works only with a undirected graph")
    explored = set([])
    con_components = []
    for node in gr.nodes():
        if node not in explored:
            reachable_nodes = BFS(gr, node)
            con_components.append(reachable_nodes)
            explored |= reachable_nodes
    return con_components

def DFS(gr, s):
    """ Depth first search wrapper """
    path = set([])
    depth_first_search(gr, s, path)
    return path

def depth_first_search(gr, s, path):
    """ Depth first search 
    Returns a list of nodes "findable" from s """
    if s in path: return False
    path.add(s)
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
    node_explored = set([]) # list for keeping track of nodes explored
    finishing_times = [] # list for adding nodes based on their finishing times
    for node in digr.nodes():
        if node not in node_explored:
            leader_node = node
            inner_DFS(digr, node, node_explored, finishing_times)
    return finishing_times 

def inner_DFS(digr, node, node_explored, finishing_times):
    """ Inner DFS used in DFS loop method """
    node_explored.add(node) # mark explored
    for each in digr.neighbors(node):
        if each not in node_explored:
            inner_DFS(digr, each, node_explored, finishing_times)
    global finishing_counter
    # adds nodes based on increasing order of finishing times
    finishing_times.append(node) 

def shortest_path(digr, s):
    """ Finds the shortest path from s to every other vertex findable
    from s using Dijkstra's algorithm in O(mlogn) time. Uses heaps
    for super fast implementation """
    nodes_explored = set([s])
    nodes_unexplored = DFS(digr, s) # all accessible nodes from s
    nodes_unexplored.remove(s)
    dist = {s:0}
    node_heap = []

    for n in nodes_unexplored:
        min = compute_min_dist(digr, n, nodes_explored, dist)
        heapq.heappush(node_heap, (min, n))

    while len(node_heap) > 0:
        min_dist, nearest_node = heapq.heappop(node_heap)
        dist[nearest_node] = min_dist
        nodes_explored.add(nearest_node)
        nodes_unexplored.remove(nearest_node)

        # recompute keys for just popped node
        for v in digr.neighbors(nearest_node):
            if v in nodes_unexplored:
                for i in range(len(node_heap)):
                    if node_heap[i][1] == v:
                        node_heap[i] = (compute_min_dist(digr, v, nodes_explored, dist), v)
                        heapq.heapify(node_heap)

    return dist

def compute_min_dist(digr, n, nodes_explored, dist):
    """ Computes the min dist of node n from a set of
    nodes explored in digr, using dist dict. Used in shortest path """
    min = float('inf')
    for v in nodes_explored:
        if digr.has_edge((v, n)):
            d = dist[v] + digr.get_edge_weight((v, n))
            if d < min: min = d
    return min

def minimum_spanning_tree(gr):
    """ Uses prim's algorithm to return the minimum 
    cost spanning tree in a undirected connected graph.
    Works only with undirected and connected graphs """
    s = gr.nodes()[0] 
    nodes_explored = set([s])
    nodes_unexplored = gr.nodes()
    nodes_unexplored.remove(s)
    min_cost, node_heap = 0, []

    #computes the key for each vertex in unexplored
    for n in nodes_unexplored:
        min = compute_key(gr, n, nodes_explored)
        heapq.heappush(node_heap, (min, n))

    while len(nodes_unexplored) > 0:
        # adds the cheapest to "explored"
        node_cost, min_node = heapq.heappop(node_heap)
        min_cost += node_cost
        nodes_explored.add(min_node)
        nodes_unexplored.remove(min_node)

        # recompute keys for neighbors of deleted node
        for v in gr.neighbors(min_node):
            if v in nodes_unexplored:
                for i in range(len(node_heap)):
                    if node_heap[i][1] == v:
                        node_heap[i] = (compute_key(gr, v, nodes_explored), v)
                        heapq.heapify(node_heap)
    return min_cost

def compute_key(gr, n, nodes_explored):
    """ computes minimum key for node n from a set of nodes_explored
    in graph gr. Used in Prim's implementation """
    min = float('inf')
    for v in gr.neighbors(n):
        if v in nodes_explored:
            w = gr.get_edge_weight((n, v))
            if w < min: min = w
    return min

def kruskal_MST(gr):
    """ computes minimum cost spanning tree in a undirected, 
    connected graph using Kruskal's MST. Uses union-find data structure
    for running times of O(mlogn) """
    sorted_edges = sorted(gr.get_edge_weights())
    uf = UnionFind()
    min_cost = 0
    for (w, (u, v)) in sorted_edges:
        if (not uf.get_leader(u) and not uf.get_leader(v)) \
                or (uf.get_leader(u) != uf.get_leader(v)):
            uf.insert(u, v)
            min_cost += w
    return min_cost

def max_k_clustering(gr, k):
    sorted_edges = sorted(gr.get_edge_weights())
    uf = UnionFind()
    #initialize each node as its cluster
    for n in gr.nodes(): 
        uf.insert(n)
    for (w, (u, v)) in sorted_edges:
        if uf.count_groups() <= k: 
            return uf.get_sets()
        if uf.get_leader(u) != uf.get_leader(v):
            uf.make_union(uf.get_leader(u), uf.get_leader(v))
    
def compute_spacing(c1, c2):
    min = float('inf')
    for n in c1:
        for v in c2:
            cost = gr.get_edge_weight((n, v))
            if cost < min:
                min = cost
    return min

def get_max_spacing(clusters):
    min = float('inf')
    for u in clusters:
        for v in clusters:
            if u!= v:
                spacing = compute_spacing(u,v)
                if spacing < min:
                    min = spacing
    return min
