import sys, time
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]

    def mst(self, parent):
        print "Edge \tWeight"
        for i in range(1,self.V):
            print parent[i],"-",i,"\t",self.graph[i][ parent[i] ]
    def minKey(self, key, mstSet):
        min = sys.maxint
 
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index
    
    def prims(self):
        key = [sys.maxint] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1 
 
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
 
        self.mst(parent)


g  = Graph(5)
g.graph = [ [0, 4, 0, 5, 0],
             [4, 0, 7, 9, 3],
             [0, 2, 0, 0, 7],
             [4, 8, 0, 0, 10],
             [0, 7, 9, 8, 0],
           ]
a=time.clock()
g.prims()
print "Time taken is "+str(time.clock()-a)
