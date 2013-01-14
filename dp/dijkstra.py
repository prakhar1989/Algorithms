from heapq import heappush, heappop
# graph = { 
#     's' : {'t':6, 'y':7},
#     't' : {'x':5, 'z':4, 'y':8 },
#     'y' : {'z':9, 'x':3},
#     'z' : {'x':7, 's': 2},
#     'x' : {'t':2}
# }

def read_graph(file):
    graph = dict()
    with open(file) as f:
        for l in f:
            (u, v, w) = l.split()
            if int(u) not in graph:
                graph[int(u)] = dict()
            graph[int(u)][int(v)] = int(w)
    return graph

inf = float('inf')
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

graph = read_graph("graph.txt")
print dijkstra(graph, 1)
