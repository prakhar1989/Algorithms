import sys, time
inf=sys.maxint
def bm(G):
    lenv=len(G)
    l=[inf]*lenv
    l[0]=0
    for i in range(0,lenv-1):
        for j in range(0,lenv):
            for k in range(0,lenv):
                l[k] = min(l[k],l[j]+G[j][k])
    print "Vertex       Distance from source"
    for i in range(lenv):
        print str(i)+"                  "+str(l[i]),
        print

a=time.clock()
bm([ [inf, 4, inf, 5, inf],
     [4, inf, 7, 9, 3],
     [inf, 2, inf, inf, 7],
     [4, 8, inf, inf, inf],
     [inf, 7, 9, 8, inf],  ])
print "Time taken is "+str(time.clock()-a)        
            

