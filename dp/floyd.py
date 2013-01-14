""" Floyd warshall in numpy and standard implementation """
from numpy import * 
inf = float('inf')
graph = [
    [0, 3, 8, inf, -4], 
    [inf, 0, inf, 1, 7], 
    [inf, 4, 0, inf, inf], 
    [2, inf, -5, 0, inf], 
    [inf, inf, inf, 6, 0]
]

def make_matrix(file, n):
    graph = [[inf for i in range(n)] for i in range(n)]
    with open(file) as f:
        for l in f:
           (i, j, w) = l.split() 
           graph[int(i)-1][int(j)-1] = int(w)
    return graph

def floyd_warshall(graph):
    n = len(graph)
    D = graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j:
                    D[i][j] = 0
                else:
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D

def fastfloyd(D):
	_,n = D.shape
	for k in xrange(n):
		i2k = reshape(D[k,:],(1,n))
		k2j = reshape(D[:,k],(n,1))
		D = minimum(D,i2k+k2j)
	return D.min() if not any(D.diagonal() < 0) else None

def get_min_dist(D):
    if negative_cost_cycle(D):
        return "Negative cost cycle"
    return min(i for d in D for i in d)

def negative_cost_cycle(D):
    n = len(D)
    for i in range(n):
        if D[i][i] < 0:
            return True
    return False

# print get_min_dist(floyd_warshall(graph))
n = 1000
gr = make_matrix("g1.txt", n)
#D = floyd_warshall(gr)
print fastfloyd(array(gr))
# print get_min_dist(D)
# print D
