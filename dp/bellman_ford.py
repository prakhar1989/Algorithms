""" The bellman ford algorithm for calculating single source shortest
paths - CLRS style """
graph = { 
    's' : {'t':6, 'y':7},
    't' : {'x':5, 'z':-4, 'y':8 },
    'y' : {'z':9, 'x':-3},
    'z' : {'x':7, 's': 2},
    'x' : {'t':-2}
}

INF = float('inf')

dist = {}
predecessor = {}

def initialize_single_source(graph, s):
    for v in graph:
        dist[v] = INF
        predecessor[v] = None
    dist[s] = 0
    
def relax(graph, u, v):
    if dist[v] > dist[u] + graph[u][v]:
        dist[v] = dist[u] + graph[u][v]
        predecessor[v] = u

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

def get_distances(graph, s):
    if bellman_ford(graph, s):
        return dist
    return "Graph contains a negative cycle"

print get_distances(graph, 's')
