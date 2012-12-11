import os, sys
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))

from graphs import digraph
from heaps import minheap

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
    temp_gr = {}
    min_cost = 0
    for (w, (u, v)) in sorted_edges:
        temp_gr[u] = v
