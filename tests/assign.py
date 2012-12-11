import os, sys
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from graphs.graph import graph
from union_find.unionfind import UnionFind

lines = [l for l in open("edges.txt").readlines()]
lines = lines[1:]
edges = [l.split() for l in lines]
gr = graph()

for (u, v, w) in edges:
    if u not in gr.nodes():
        gr.add_node(u)
    if v not in gr.nodes():
        gr.add_node(v)
    gr.add_edge((u, v), int(w))

def kruskal_MST(gr):
    sorted_edges = sorted(gr.get_edge_weights())
    uf = UnionFind()
    min_cost = 0
    for (w, (u, v)) in sorted_edges:
        if (not uf.get_leader(u) and not uf.get_leader(v)) \
                or (uf.get_leader(u) != uf.get_leader(v)):
            uf.insert(u, v)
            min_cost += w
    return min_cost

print kruskal_MST(gr)
