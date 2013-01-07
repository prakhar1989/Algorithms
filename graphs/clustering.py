import os, sys
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from graph import graph
from union_find.unionfind import UnionFind

data = """1 2 6808
1 3 5250
1 4 74
1 5 3659
1 6 8931
1 7 1273
1 8 7545
1 9 879
1 10 7924
1 11 7710
1 12 4441
1 13 8166
1 14 4493
1 15 3043
1 16 7988
1 17 2504
1 18 2328
1 19 1730
1 20 8841
2 3 4902
2 4 812
2 5 6617
2 6 6892
2 7 8672
2 8 1729
2 9 6672
2 10 1662
2 11 7046
2 12 3121
2 13 241
2 14 7159
2 15 9454
2 16 9628
2 17 5351
2 18 3712
2 19 5564
2 20 9595
3 4 3782
3 5 1952
3 6 9231
3 7 3322
3 8 3214
3 9 5129
3 10 1951
3 11 8601
3 12 8960
3 13 9755
3 14 9993
3 15 5195
3 16 3331
3 17 8633
3 18 3560
3 19 8778
3 20 7780
4 5 5000
4 6 4521
4 7 4516
4 8 2578
4 9 9923
4 10 7143
4 11 3981
4 12 5882
4 13 6886
4 14 31
4 15 6326
4 16 2437
4 17 6995
4 18 3946
4 19 2603
4 20 3234
5 6 8696
5 7 6896
5 8 5665
5 9 5601
5 10 5119
5 11 5118
5 12 3724
5 13 1618
5 14 3755
5 15 9569
5 16 8588
5 17 4576
5 18 4914
5 19 8123
5 20 4158
6 7 2495
6 8 3894
6 9 3065
6 10 4564
6 11 5430
6 12 5502
6 13 6873
6 14 6941
6 15 8054
6 16 4330
6 17 2233
6 18 2281
6 19 9360
6 20 5475
7 8 2739
7 9 4442
7 10 4843
7 11 8503
7 12 5466
7 13 5370
7 14 8012
7 15 3909
7 16 3503
7 17 1844
7 18 5374
7 19 7081
7 20 9837
8 9 3060
8 10 5421
8 11 5098
8 12 4080
8 13 3019
8 14 8318
8 15 9158
8 16 2031
8 17 722
8 18 4052
8 19 1072
8 20 9529
9 10 7569
9 11 563
9 12 5705
9 13 9597
9 14 4813
9 15 6965
9 16 8810
9 17 5046
9 18 17
9 19 1710
9 20 2262
10 11 3444
10 12 370
10 13 8675
10 14 5780
10 15 6209
10 16 2586
10 17 9086
10 18 4323
10 19 1212
10 20 79
11 12 1975
11 13 1665
11 14 3396
11 15 9439
11 16 594
11 17 5821
11 18 6006
11 19 836
11 20 2450
12 13 6821
12 14 5835
12 15 8470
12 16 3141
12 17 9413
12 18 760
12 19 3568
12 20 7424
13 14 4357
13 15 6374
13 16 7456
13 17 6025
13 18 9458
13 19 3064
13 20 9874
14 15 9946
14 16 6500
14 17 2476
14 18 4187
14 19 6686
14 20 9103
15 16 8910
15 17 5182
15 18 4761
15 19 8506
15 20 4676
16 17 881
16 18 4769
16 19 2903
16 20 66
17 18 2747
17 19 7119
17 20 2874
18 19 6302
18 20 7382
19 20 1143
"""

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

if __name__ == "__main__":
    edges = [l.split() for l in data.splitlines()]
    gr = graph()

    for (u, v, w) in edges:
        if u not in gr.nodes():
            gr.add_node(u)
        if v not in gr.nodes():
            gr.add_node(v)
        gr.add_edge((u, v), int(w))

    print "Min Spacing - %s " % (get_max_spacing(max_k_clustering(gr, 4)))
