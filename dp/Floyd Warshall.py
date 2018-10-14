import time,sys
V=4
def floydWarshall(graph):
    dist=graph
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j] ,dist[i][k]+ dist[k][j])
    print "shortest distances between every pair of vertices"
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == inf):
                print "    %s" %("inf"),
            else:
                print "    %d\t" %(dist[i][j]),
            if j == V-1:
                print ""

    

inf=sys.maxint
graph = [[0,6,inf,3],
        [inf,0,9,inf],
        [inf, inf, 3, 5],
        [inf, inf, inf, 7]]

a=time.clock()
floydWarshall(graph)
print "Time taken is "+str(time.clock()-a)
