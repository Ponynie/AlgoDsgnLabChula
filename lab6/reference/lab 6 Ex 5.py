from collections import defaultdict

class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    # A function used by DFS 
    def DFSUtil(self,v,visited,p): 
        # Mark the current node as visited and print it 
        visited[v]= True
        if v==0:
            print ("-------")
        else :    
            p.append(v)
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.DFSUtil(i,visited,p) 

    def fillOrder(self,v,visited, stack): 
        # Mark the current node as visited  
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 
        stack = stack.append(v) 
      
  
    # Function that returns reverse (or transpose) of this graph 
    def getTranspose(self): 
        g = Graph(self.V) 
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph: 
            for j in self.graph[i]: 
                g.addEdge(j,i) 
        return g 
    
    def printSCCs(self): 
        print("Strongly connected component")
        p=[]
        
        stack = [] 
        # Mark all the vertices as not visited (For first DFS) 
        visited =[False]*(self.V) 
        # Fill vertices in stack according to their finishing 
        # times 
        for i in range(self.V): 
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 
  
        # Create a reversed graph 
        gr = self.getTranspose() 
           
         # Mark all the vertices as not visited (For second DFS) 
        visited =[False]*(self.V) 
  
         # Now process all vertices in order defined by Stack 
        while stack: 
            i = stack.pop() 
            if visited[i]==False: 
                gr.DFSUtil(i, visited, p) 
                if len(p)>1:
                    print(p)
                    p.clear()
                else:
                    p.clear()

file = open("lab6/test_case/6.1real.txt","r")
inputData = file.readline().split() 
while inputData[0] != "0" and inputData[1] != "0":
    g = Graph(int(inputData[0])+1)
    if len(inputData) == 2:
        N = int(inputData[0])
        M = int(inputData[1])
    inputData = file.readline().split()    
    for i in range(M):
        vertexA = int(inputData[0])
        vertexB = int(inputData[1])
        mode = int(inputData[2])
        if mode == 1:
            g.addEdge(vertexA, vertexB)
        if mode == 2:
            g.addEdge(vertexA, vertexB)
            g.addEdge(vertexB, vertexA)
        inputData = file.readline().split()
    g.printSCCs()
              
file.close()