""" Johnson's algorithm for all-pairs shortest path problem.
Reimplemented Bellman-Ford and Dijkstra's for clarity"""
from heapq import heappush, heappop
from datetime import datetime
from copy import deepcopy
graph = { 
    'a' : {'b':-2},
    'b' : {'c':-1},
    'c' : {'x':2, 'a':4, 'y':-3},
    'z' : {'x':1, 'y':-4},
    'x' : {},
    'y' : {},
}

inf = float('inf')
dist = {}

def read_graph(file,n):
    graph = dict()
    with open(file) as f:
        for l in f:
            (u, v, w) = l.split()
            if int(u) not in graph:
                graph[int(u)] = dict()
            graph[int(u)][int(v)] = int(w)
    for i in range(n):
        if i not in graph:
            graph[i] = dict()
    return graph

def dijkstra(graph, s):
    n = len(graph.keys())
    dist = dict()
    Q = list()
    
    for v in graph:
        dist[v] = inf
    dist[s] = 0
    
    heappush(Q, (dist[s], s))

    while Q:
        d, u = heappop(Q)
        if d < dist[u]:
            dist[u] = d
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                heappush(Q, (dist[v], v))
    return dist

def initialize_single_source(graph, s):
    for v in graph:
        dist[v] = inf
    dist[s] = 0
    
def relax(graph, u, v):
    if dist[v] > dist[u] + graph[u][v]:
        dist[v] = dist[u] + graph[u][v]

def bellman_ford(graph, s):
    initialize_single_source(graph, s)
    edges = [(u, v) for u in graph for v in graph[u].keys()]
    number_vertices = len(graph)
    for i in range(number_vertices-1):
        for (u, v) in edges:
            relax(graph, u, v)
    for (u, v) in edges:
        if dist[v] > dist[u] + graph[u][v]:
            return False # there exists a negative cycle
    return True

def add_extra_node(graph):
    graph[0] = dict()
    for v in graph.keys():
        if v != 0:
            graph[0][v] = 0

def reweighting(graph_new):
    add_extra_node(graph_new)
    if not bellman_ford(graph_new, 0):
        # graph contains negative cycles
        return False
    for u in graph_new:
        for v in graph_new[u]:
            if u != 0:
                graph_new[u][v] += dist[u] - dist[v]
    del graph_new[0]
    return graph_new

def johnsons(graph_new):
    graph = reweighting(graph_new)
    if not graph:
        return False
    final_distances = {}
    for u in graph:
        final_distances[u] = dijkstra(graph, u)

    for u in final_distances:
        for v in final_distances[u]:
            final_distances[u][v] += dist[v] - dist[u]
    return final_distances
            
def compute_min(final_distances):
    return min(final_distances[u][v] for u in final_distances for v in final_distances[u])

if __name__ == "__main__":
    # graph = read_graph("graph.txt", 1000)
    graph_new = deepcopy(graph)
    t1 = datetime.utcnow()
    final_distances =  johnsons(graph_new)
    if not final_distances:
        print "Negative cycle"
    else:
        print compute_min(final_distances)
    print datetime.utcnow() - t1
