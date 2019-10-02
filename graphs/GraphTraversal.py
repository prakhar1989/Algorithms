from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)     #To create a dictionary of lists {u:[v,x,n]}

    def AddEdge(self , u ,v):
        self.graph[u].append(v)

    def BFS(self,s):
        visited = [False]*(len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s , end ='  ')
            for i in self.graph[s]:
                if visited[i]== False:
                    queue.append(i)
                    visited[i] = True

    def DFSUtil(self,s,visited):
        visited[s] = True
        print(s , end='  ')
        for i in self.graph[s]:
            if visited[i] == False:
                self.DFSUtil(i,visited)
            
    def DFS(self , s):
        visited = [False]*(len(self.graph))
        self.DFSUtil(s,visited)
        
        

if __name__ == '__main__':
    g = Graph()
    g.AddEdge(0,1)
    g.AddEdge(0,2)
    g.AddEdge(1,0)
    g.AddEdge(2,0)
    
    g.AddEdge(1,3)
    g.AddEdge(3,1)
    
    g.AddEdge(2,4)
    g.AddEdge(4,2)
    
    g.AddEdge(1,4)
    g.AddEdge(4,1)
    
    g.AddEdge(3,4)
    g.AddEdge(4,3)
    
    g.AddEdge(3,5)
    g.AddEdge(5,3)
    
    g.AddEdge(4,5)
    g.AddEdge(5,4)
    g.BFS(0)
    print('\n')
    g.DFS(0)
    
