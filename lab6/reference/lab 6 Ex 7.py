from collections import defaultdict

class Graph: 
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    def addEdge(self, u, v): 
        self.graph[u].append(v) 

    def DFSUtil(self, v, visited, array): 
        # Mark the current node as visited  
        # and print it 
        visited[v] = True
        array.append(v)  
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited, array) 
        return array

    def DFS(self, v, N): 
        array = [] # keep the vertex that vertexA can go to 
        visited = [False] * (N+1) # create list for check whether vertex is visited or not
        self.DFSUtil(v, visited, array)
        return array    

file = open("lab6/test_case/Extra6.5.txt","r")
chk = True
inputData = file.readline().split() 
while inputData[0] != "0" and inputData[1] != "0":
    g = Graph()
    if len(inputData) == 2:
        N = int(inputData[0])
        M = int(inputData[1])
    inputData = file.readline().split()    
    for i in range(M):
        vertexA = int(inputData[0])
        vertexB = int(inputData[1])
        g.addEdge(vertexA, vertexB)
        g.addEdge(vertexB, vertexA)
        inputData = file.readline().split()
    for i in list(g.graph): # check that can vertexA go back and forth to vertexB or not.
        tmp = g.DFS(i,N)
        print(tmp)
        if len(tmp) == N:
            chk = True
            break
        else:
            chk = False
            break    
    if chk == False:
        print(0)  
    else:
        print(1)          
file.close()