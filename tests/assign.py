import os, sys
import operator
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from graphs.graph import graph
from itertools import *
from union_find.unionfind import UnionFind

def ham_dist(e1, e2):
    """ computes hamming distance between two strings e1 and e2 """
    ne = operator.ne
    return sum(imap(ne, e1, e2))

path = "clustering3.txt"
nodes = open(path).readlines()
uf = UnionFind()

# bitcount = {i: nodes[i].count('1') for i in range(len(nodes))}
# similar = [(bitcount[i]-9, ham_dist(nodes[i], nodes[0])) for i in range(1, len(nodes))]
# print nodes[1].count('1') - nodes[2].count('1')
# print hamdist(nodes[1], nodes[2])
for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        print i, j, ham_dist(nodes[i], nodes[j])
