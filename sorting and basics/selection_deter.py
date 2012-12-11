# selection problem solved deterministically
from sorting import mergesort
def median_of_medians(a):
    n = len(a)
    p = range(0, n, 5) + [n]
    sublist = [a[p[i]:p[i+1]] for i in range(len(p)-1)]
    mergelist = [mergesort(s)[len(s)/2] for s in sublist]
    # TODO: make this call recursive
    return mergelist[len(mergelist)/2]

def select(a, i):
    """ returns the ith order statistic in array a 
    in linear time.""" 
    if i < 1 or i > len(a):
        return None
    if len(a) <= 1: return a
    # choose pivot
    p = median_of_medians(a)

    # partioning
    lesser = [x for x in a if x < p]
    greater = [x for x in a if x > p]
    j = len(lesser)

    if j == i:
        return p
    elif i < j:
        return select(lesser, i)
    else: # i > j
        return select(greater, i-j)

