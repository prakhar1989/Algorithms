#Topological sort is for "Directed and Acyclic Graphs"
#Time complexity O(V+E)
#Topological ordering is an ordering from node u -> v such that,
#node u is always placed befor node v in the ordering
# you can modify this code for any implementation
g = {  0:[1],
       1:[2],
       2:[3],
       3:[4],
       4:[5],
       5:[6],
       6:[7],
       7:[8],
       8:[9],
       9:[10],
       10:[11],
       11:[]}
N = len(g)
V = [False for i in range(N)]
def dfs(at,visitedNodes):
    V[at] = True
    
    # print("Neighbours of {} are {}".format(at,g[at]))
    
    for next in g[at]: 
        if V[next] == False:
            # print("Visited:",V)
            dfs(next,visitedNodes)
    
    # print('Visited nodes list:',visitedNodes)
    
    visitedNodes.append(at)

def topsort():
    ordering = [0 for i in range(N)]
    i = N-1  #Index for ordering array

    for at in range(N):  #For each node in the graph run DFS on it if unvisited
        
        # print("Calling DFS for:",at)
        
        if V[at] == False:
            visitedNodes = []
            dfs(at,visitedNodes)
            for nodeId in visitedNodes:
                ordering[i] = nodeId
                i -= 1
    
    # print(ordering)
    
    return ordering
print(topsort())
